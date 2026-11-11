# DT Variability Model for Digital Twins of Cyber-Physical Systems

This repository provides public artifacts for a feature model that supports the design and configuration of digital twins (DTs) for cyber-physical systems (CPSs).

The model represents DT design as a set of configurable features. It captures common DT design concerns such as twinning level, physical assets, computation, sensors and actuators, deployment, connectivity, data integration, user interfaces, goals, security, and standards. It also includes cross-tree constraints that encode dependencies a valid DT configuration must satisfy.

## Why This Model Exists

Designing a DT requires many connected decisions. For example, selecting a full digital twin should also imply the lower twinning level, data and its acquisition, and a command path back to the physical system. A flat checklist does not capture these dependencies well.

This feature model makes the design space explicit by using:

- mandatory and optional features;
- `and`, `or`, and `xor` feature groups;
- subsystem colors for navigation;
- cross-tree constraints for checking valid configurations.

## Quick View

- [Zoomable full-tree SVG](feature-model/full-feature-model.svg): best option for browsing and zooming in a browser.
- [High-resolution PNG](feature-model/full-feature-model.png): bitmap preview/export of the full tree.
- [Graphviz DOT source](feature-model/full-feature-model.dot): graph source used to generate the SVG and PNG.
- [Browsable Markdown hierarchy](feature-model/full-feature-model.md): full parent-child structure and cross-tree constraints in a GitHub-readable format.
- [Glossary and notation guide](GLOSSARY.md): explains feature-model notation and common DT/CPS terms used in the model.

## FeatureIDE Models and Example Configurations

The model is a FeatureIDE project. In Eclipse with FeatureIDE installed, use *File > Import > Existing Projects into Workspace* and select the `FeatureModelDT_v2` folder. Both example configurations are in its `configs/` folder.

| What | Path |
|---|---|
| DT feature model (339 features, 17 cross-tree constraints) | [`DT-Builder-VariabilityModel/FeatureModelDT_v2/model.xml`](DT-Builder-VariabilityModel/FeatureModelDT_v2/model.xml) |
| Smart warehouse example (90 selected features) | [`DT-Builder-VariabilityModel/FeatureModelDT_v2/configs/smart_warehouse.xml`](DT-Builder-VariabilityModel/FeatureModelDT_v2/configs/smart_warehouse.xml) |
| Smart home example (76 selected features) | [`DT-Builder-VariabilityModel/FeatureModelDT_v2/configs/smart_home.xml`](DT-Builder-VariabilityModel/FeatureModelDT_v2/configs/smart_home.xml) |

Both examples are configured on the same model. They are constructed engineering examples, not implemented systems.

Each example can also be viewed as a tree of its selected features, without installing FeatureIDE:

| Example | Zoomable SVG | High-resolution PNG | Graphviz DOT source |
|---|---|---|---|
| Smart warehouse | [SVG](feature-model/smart_warehouse-example.svg) | [PNG](feature-model/smart_warehouse-example.png) | [DOT](feature-model/smart_warehouse-example.dot) |
| Smart home | [SVG](feature-model/smart_home-example.svg) | [PNG](feature-model/smart_home-example.png) | [DOT](feature-model/smart_home-example.dot) |

## Model Structure

The root feature is `Digital_Twin_Builder_v2`. Its main subsystems are:

| Subsystem | Main concern |
|---|---|
| `Twinning_System` | Digital model, digital shadow, digital twin, and extended twin variants |
| `Cyber_Physical_System` | Computation, system type, sensors, actuators, and logic model |
| `Architecture_System` | Reference architectures and DT architectural concepts |
| `Deployment_Runtime` | Edge, fog, cloud, operating system, orchestration, and synchronization |
| `User_Interface` | Dashboards, apps, platforms, and immersive visualization |
| `Connectivity_System` | Storage, cloud integration, and communication protocols |
| `Data_Integration_System` | Integration patterns and data representations |
| `Goal_and_Capability_System` | DT goals, analytics, quality attributes, and lifecycle capabilities |
| `Security_System` | Encryption, alerts, device/data security, privacy, and access control |
| `Standards_Compliance` | Simulation, modeling, physical-entity, service, and engineering standards |

## How To Read The Feature Model

- `M` on an edge means the child feature is mandatory when its parent is selected.
- `O` on an edge means the child feature is optional.
- `and` means mandatory children are required and optional children may be added.
- `or` means one or more children may be selected.
- `xor` means exactly one child may be selected.

For example, `Digital_Model` is mandatory under `Twinning_System` because every DT configuration needs a virtual representation of the physical system. `Digital_Shadow`, `Digital_Twin`, and extended twinning variants are optional because a configuration may stop at a simpler twinning level or add more advanced capabilities.

## Cross-Tree Constraints

The model includes 17 constraints that capture dependencies across separate branches. Each one has the form "selecting the feature on the left requires the features on the right". C6 is retired, so the identifiers run from C1 to C18.

| ID | Selected feature | Required features |
|---|---|---|
| C1 | `Digital_Shadow` | `Data` and `Data_Acquisition_and_Ingestion` |
| C2 | `Digital_Twin` | `Digital_Shadow` and `Command_Control` |
| C3 | `Federated_Twin` | `Federated_Digital_Twin_Architecture` and `Interoperability` |
| C4 | `Cloud_Layer` | `Cloud_Integration` |
| C5 | `Edge_AI_Intelligence` | `Edge_Layer` |
| C7 | `IEC_62541` | `OPC_UA` |
| C8 | `ISO_IEC_19514_SysML` | `SysML` |
| C9 | `ISO_IEC_19505_UML` | `UML` |
| C10 | `ISO_IEC_19510_BPMN` | `BPMN` |
| C11 | `Hybrid_Edge_Fog_Cloud` | `Edge_Layer` and `Fog_Layer` and `Cloud_Layer` |
| C12 | `Streaming_Integration` | `Data_Streaming` |
| C13 | `API_Based_Integration` | `API_Services` |
| C14 | `Cloud_Stack_Architecture` | `Cloud_Layer` |
| C15 | `Kubernetes_Edge` | `Edge_Layer` |
| C16 | `OpenAPI` or `GraphQL` or `gRPC` | `API_Services` |
| C17 | `Data_Services` | `Data` |
| C18 | `Real_Time_Sync` | `Real_Time_Processing` |

The rationale for each constraint is in [`evidence/constraint_rationale.json`](evidence/constraint_rationale.json), and short feature definitions are in [`evidence/feature_glossary.md`](evidence/feature_glossary.md). The constraints are author-defined model rules; they are not expert-validated.

## Checking the Model

`python3 tools/run_feature_model_analysis.py` runs the model and the scenarios in [`evidence/scenarios.tsv`](evidence/scenarios.tsv) through the FeatureIDE 3.12 library (Java 21 and an Eclipse installation with FeatureIDE are required). The recorded result is in [`evidence/analysis.json`](evidence/analysis.json): the model is satisfiable, with no dead or false-optional features and no redundant constraints, and all 62 scenario records match their expected outcomes.

## Regenerating Visuals

The Markdown and DOT views are generated from the FeatureIDE XML and the two example configurations, and each DOT file is rendered with Graphviz:

```sh
python3 tools/generate_feature_model_artifacts.py
for name in full-feature-model smart_warehouse-example smart_home-example; do
  dot -Tsvg feature-model/$name.dot -o feature-model/$name.svg
  dot -Tpng -Gdpi=220 feature-model/$name.dot -o feature-model/$name.png
done
```

The SVG is the preferred artifact for inspection because it remains sharp when zoomed.
