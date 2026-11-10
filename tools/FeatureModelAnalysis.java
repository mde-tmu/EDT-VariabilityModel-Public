import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.*;
import java.util.stream.Collectors;
import de.ovgu.featureide.fm.core.FeatureModelAnalyzer;
import de.ovgu.featureide.fm.core.base.*;
import de.ovgu.featureide.fm.core.init.FMCoreLibrary;
import de.ovgu.featureide.fm.core.io.manager.FeatureModelManager;
import de.ovgu.featureide.fm.core.job.monitor.NullMonitor;
import de.ovgu.featureide.fm.core.editing.AdvancedNodeCreator;
import de.ovgu.featureide.fm.core.analysis.cnf.formula.FeatureModelFormula;
import de.ovgu.featureide.fm.core.configuration.*;
import org.prop4j.*;

/** Headless analysis using the installed FeatureIDE library and its SAT4J backend.
 * Usage: FeatureModelAnalysis MODEL SCENARIOS.tsv OUTPUT.json CONFIG_OUTPUT_DIR
 * TSV: id, expected SAT/UNSAT, comma-separated signed feature literals, export name.
 * No missing configuration entry is interpreted as deselected.
 */
public class FeatureModelAnalysis {
    static String q(String s) {
        return "\"" + s.replace("\\", "\\\\").replace("\"", "\\\"")
            .replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t") + "\"";
    }
    static String arr(Collection<String> s) {
        return s.stream().map(FeatureModelAnalysis::q).collect(Collectors.joining(",", "[", "]"));
    }
    static List<String> names(Collection<IFeature> fs) {
        return fs.stream().map(IFeature::getName).sorted().collect(Collectors.toList());
    }
    static List<Node> parse(IFeatureModel fm, String text) {
        List<Node> a = new ArrayList<>();
        if (!text.isEmpty()) for (String s : text.split(",")) {
            if (!(s.startsWith("+") || s.startsWith("-"))) throw new IllegalArgumentException(s);
            if (fm.getFeature(s.substring(1)) == null) throw new IllegalArgumentException("Unknown feature: " + s);
            a.add(new Literal(s.substring(1), s.charAt(0) == '+'));
        }
        return a;
    }
    public static void main(String[] args) throws Exception {
        FMCoreLibrary.getInstance().install();
        Path modelPath = Path.of(args[0]);
        IFeatureModel fm = FeatureModelManager.load(modelPath);
        if (fm == null) throw new IllegalStateException("FeatureIDE could not load " + modelPath);
        var analyzer = new FeatureModelAnalyzer(fm);
        boolean valid = analyzer.isValid(new NullMonitor<>());
        if (!valid) throw new IllegalStateException("Void feature model");
        List<String> dead = names(analyzer.getDeadFeatures(new NullMonitor<>()));
        List<String> core = names(analyzer.getCoreFeatures(new NullMonitor<>()));
        List<String> falseOptional = names(analyzer.getFalseOptionalFeatures(new NullMonitor<>()));
        List<String> redundant = analyzer.getRedundantConstraints(new NullMonitor<>()).stream()
            .map(c -> Integer.toString(fm.getConstraintIndex(c) + 1)).collect(Collectors.toList());
        var solver = new SatSolver(AdvancedNodeCreator.createRegularCNF(fm), 30000);
        List<String> scenarioResults = new ArrayList<>();
        int failures = 0;
        Files.createDirectories(Path.of(args[3]));
        for (String line : Files.readAllLines(Path.of(args[1]))) {
            if (line.isBlank() || line.startsWith("#")) continue;
            String[] fields = line.split("\t", -1);
            var assumptions = parse(fm, fields[2]);
            boolean sat = solver.isSatisfiable(assumptions);
            boolean expected = fields[1].equals("SAT");
            if (sat != expected) failures++;
            List<String> implied = new ArrayList<>();
            Set<String> seeded = assumptions.stream().map(n -> ((Literal)n).var.toString()).collect(Collectors.toSet());
            if (sat) for (IFeature f : fm.getFeatures()) {
                if (seeded.contains(f.getName())) continue;
                var test = new ArrayList<>(assumptions);
                test.add(new Literal(f.getName(), false));
                if (!solver.isSatisfiable(test)) implied.add(f.getName());
            }
            Collections.sort(implied);
            String extra = "";
            if (sat && fields.length > 3 && !fields[3].isEmpty()) {
                // Deterministic inclusion-minimal completion: prefer deselection in model order.
                // The completion choices are not requirements inferred from the scenario.
                var complete = new ArrayList<>(assumptions);
                for (IFeature f : fm.getFeatures()) if (!seeded.contains(f.getName())) {
                    var test = new ArrayList<>(complete);
                    test.add(new Literal(f.getName(), false));
                    complete.add(new Literal(f.getName(), !solver.isSatisfiable(test)));
                }
                if (!solver.isSatisfiable(complete)) throw new IllegalStateException("Invalid completion");
                var formula = new FeatureModelFormula(fm);
                var config = new Configuration(formula);
                List<String> selected = new ArrayList<>();
                for (Node n : complete) {
                    Literal l = (Literal)n;
                    config.setManual(l.var.toString(), l.positive ? Selection.SELECTED : Selection.UNSELECTED);
                    if (l.positive) selected.add(l.var.toString());
                }
                if (!new ConfigurationAnalyzer(formula, config).isValid()) throw new IllegalStateException("Incomplete/invalid export");
                Path path = Path.of(args[3], fields[3] + ".xml");
                Files.writeString(path, new XMLConfFormat().write(config));
                var reloaded = new Configuration(formula);
                var problems = new XMLConfFormat().read(reloaded, Files.readString(path));
                if (problems.containsError() || !reloaded.getUndefinedFeatureNames().isEmpty()
                    || !new ConfigurationAnalyzer(formula, reloaded).isValid())
                    throw new IllegalStateException("Round-trip configuration failed: " + path);
                Collections.sort(selected);
                extra = ",\"complete_export\":" + q(fields[3] + ".xml")
                    + ",\"selected_count\":" + selected.size() + ",\"selected_features\":" + arr(selected);
            }
            scenarioResults.add("{\"id\":" + q(fields[0]) + ",\"expected\":" + q(fields[1])
                + ",\"observed\":" + q(sat ? "SAT" : "UNSAT") + ",\"assumptions\":" + q(fields[2])
                + ",\"implied_selected\":" + arr(implied) + extra + "}");
        }
        String hash = HexFormat.of().formatHex(MessageDigest.getInstance("SHA-256").digest(Files.readAllBytes(modelPath)));
        String result = "{\n\"featureide_version\":\"3.12.0.202603112104\","
            + "\n\"java_version\":" + q(System.getProperty("java.version"))
            + ",\n\"model_sha256\":" + q(hash) + ",\n\"feature_nodes\":" + fm.getNumberOfFeatures()
            + ",\n\"leaves\":" + analyzer.countTerminalFeatures() + ",\n\"constraints\":" + fm.getConstraintCount()
            + ",\n\"satisfiable\":" + valid + ",\n\"dead_features\":" + arr(dead)
            + ",\n\"core_features\":" + arr(core) + ",\n\"false_optional_features\":" + arr(falseOptional)
            + ",\n\"redundant_constraint_positions\":" + arr(redundant)
            + ",\n\"scenario_failures\":" + failures + ",\n\"scenarios\":[\n" + String.join(",\n", scenarioResults) + "\n]}\n";
        Files.writeString(Path.of(args[2]), result, StandardCharsets.UTF_8);
        System.out.println("FeatureIDE: " + fm.getNumberOfFeatures() + " features, " + fm.getConstraintCount()
            + " constraints, " + dead.size() + " dead, " + falseOptional.size() + " false-optional, "
            + redundant.size() + " redundant; " + scenarioResults.size() + " scenarios, " + failures + " mismatches.");
        if (failures != 0) throw new IllegalStateException("Scenario mismatches");
    }
}
