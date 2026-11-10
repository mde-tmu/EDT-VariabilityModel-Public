#!/usr/bin/env python3
"""Generate GitHub-friendly feature-model artifacts from FeatureIDE XML."""

from __future__ import annotations

from pathlib import Path
import textwrap
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "DT-Builder-VariabilityModel" / "FeatureModelDT_v2" / "model.xml"
OUT_DIR = ROOT / "feature-model"
MARKDOWN_PATH = OUT_DIR / "full-feature-model.md"
DOT_PATH = OUT_DIR / "full-feature-model.dot"

FEATURE_TAGS = {"and", "or", "alt", "feature"}

GROUP_LABELS = {
    "and": "and",
    "or": "or",
    "alt": "xor",
    "feature": "leaf",
}

COLORS = {
    "Digital_Twin_Builder_v2": "#f7f7f7",
    "Twinning_System": "#f7c6d0",
    "Cyber_Physical_System": "#bfe9f4",
    "Architecture_System": "#fff0b8",
    "Deployment_Runtime": "#d7dcff",
    "User_Interface": "#c9efbf",
    "Connectivity_System": "#ffd1a6",
    "Data_Integration_System": "#efc4ea",
    "Goal_and_Capability_System": "#d9c7ff",
    "Security_System": "#f2b8b8",
    "Standards_Compliance": "#e2e2e2",
}


def feature_children(element: ET.Element) -> list[ET.Element]:
    return [child for child in list(element) if child.tag in FEATURE_TAGS]


def edge_marker(element: ET.Element, is_root: bool = False) -> str:
    if is_root or element.attrib.get("mandatory") == "true":
        return "M"
    return "O"


def group_label(element: ET.Element) -> str:
    return GROUP_LABELS.get(element.tag, element.tag)


def markdown_hierarchy(element: ET.Element, depth: int = 0, is_root: bool = False) -> list[str]:
    name = element.attrib["name"]
    marker = edge_marker(element, is_root)
    suffixes = []
    if feature_children(element):
        suffixes.append(f"{group_label(element)} group")
    if element.attrib.get("abstract") == "true":
        suffixes.append("abstract")

    suffix = f" ({', '.join(suffixes)})" if suffixes else ""
    lines = [f"{'  ' * depth}- [{marker}] `{name}`{suffix}"]
    for child in feature_children(element):
        lines.extend(markdown_hierarchy(child, depth + 1))
    return lines


def flatten_conjunction(element: ET.Element) -> list[str]:
    values: list[str] = []
    if element.tag == "conj":
        for child in list(element):
            values.extend(flatten_conjunction(child))
    elif element.tag == "var":
        values.append(element.text or "")
    return values


def format_formula(element: ET.Element) -> str:
    if element.tag == "var":
        return f"`{element.text}`"
    if element.tag == "conj":
        values = [f"`{value}`" for value in flatten_conjunction(element)]
        if len(values) <= 1:
            return values[0] if values else ""
        if len(values) == 2:
            return f"{values[0]} and {values[1]}"
        return ", ".join(values[:-1]) + f", and {values[-1]}"
    if element.tag == "disj":
        values = [format_formula(child) for child in list(element)]
        if len(values) <= 1:
            return values[0] if values else ""
        if len(values) == 2:
            return f"{values[0]} or {values[1]}"
        return ", ".join(values[:-1]) + f", or {values[-1]}"
    if element.tag == "not":
        return f"not {format_formula(list(element)[0])}"
    return ""


def markdown_constraints(root: ET.Element) -> list[str]:
    constraints = root.find("constraints")
    if constraints is None:
        return ["No cross-tree constraints are defined in the source model."]

    lines: list[str] = []
    for rule in constraints.findall("rule"):
        implication = rule.find("imp")
        if implication is None or len(list(implication)) != 2:
            continue
        left, right = list(implication)
        lines.append(f"- {format_formula(left)} requires {format_formula(right)}.")
    return lines or ["No cross-tree constraints are defined in the source model."]


def wrap_label(name: str, max_width: int = 24) -> list[str]:
    parts = name.split("_")
    lines: list[str] = []
    current = ""
    for part in parts:
        candidate = f"{current}_{part}" if current else part
        if len(candidate) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = part
    if current:
        lines.append(current)
    return lines


def dot_escape_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def dot_label(lines: list[str]) -> str:
    return "\\n".join(dot_escape_text(line) for line in lines)


def collect_dot(element: ET.Element) -> tuple[list[str], list[str], list[str]]:
    nodes: list[str] = []
    edges: list[str] = []
    top_rank_nodes: list[str] = []
    counter = 0

    def walk(node: ET.Element, parent_id: str | None = None, depth: int = 0, top: str | None = None) -> str:
        nonlocal counter
        node_id = f"n{counter}"
        counter += 1

        name = node.attrib["name"]
        current_top = name if depth == 1 else top
        fill = COLORS.get(current_top or name, COLORS.get(name, "#ffffff"))
        label_parts = wrap_label(name)
        if feature_children(node):
            label_parts.append(f"({group_label(node)})")
        if node.attrib.get("abstract") == "true":
            label_parts.append("abstract")
        label = dot_label(label_parts)

        nodes.append(
            f'  {node_id} [label="{label}", fillcolor="{fill}"];'
        )
        if depth == 1:
            top_rank_nodes.append(node_id)

        if parent_id is not None:
            marker = edge_marker(node)
            style = "solid" if marker == "M" else "dashed"
            penwidth = "1.5" if marker == "M" else "1.0"
            edges.append(
                f'  {parent_id} -> {node_id} [label="{marker}", style="{style}", penwidth={penwidth}];'
            )

        for child in feature_children(node):
            walk(child, node_id, depth + 1, current_top)
        return node_id

    walk(element)
    return nodes, edges, top_rank_nodes


def write_markdown(root: ET.Element, model_root: ET.Element) -> None:
    lines = [
        "# Complete Digital Twin Feature Model",
        "",
        "This file is generated from the FeatureIDE source model:",
        "",
        f"- `{MODEL_PATH.relative_to(ROOT)}`",
        "",
        "Use this Markdown view when GitHub's XML preview is too hard to read. The FeatureIDE XML remains the editable source of truth.",
        "",
        "## Legend",
        "",
        "- `[M]` means the feature edge is mandatory when its parent is selected.",
        "- `[O]` means the feature edge is optional when its parent is selected.",
        "- `and group` means all mandatory children are required and optional children may be selected.",
        "- `or group` means one or more child features may be selected.",
        "- `xor group` means exactly one alternative child may be selected.",
        "",
        "## Feature Hierarchy",
        "",
    ]
    lines.extend(markdown_hierarchy(root, is_root=True))
    lines.extend(
        [
            "",
            "## Cross-Tree Constraints",
            "",
        ]
    )
    lines.extend(markdown_constraints(model_root))
    lines.append("")
    MARKDOWN_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_dot(root: ET.Element) -> None:
    nodes, edges, top_rank_nodes = collect_dot(root)
    lines = [
        "digraph FeatureModel {",
        '  graph [rankdir=TB, bgcolor="white", outputorder=edgesfirst, splines=polyline, nodesep=0.22, ranksep=0.55, margin=0.15, labelloc=t, label="Complete DT Feature Model", fontsize=28, fontname="Helvetica"];',
        '  node [shape=box, style="rounded,filled", color="#707070", fontname="Helvetica", fontsize=16, margin="0.08,0.05"];',
        '  edge [color="#777777", arrowsize=0.55, fontname="Helvetica", fontsize=11];',
        "",
    ]
    lines.extend(nodes)
    lines.append("")
    lines.extend(edges)
    if top_rank_nodes:
        lines.append("")
        lines.append("  { rank=same; " + " ".join(top_rank_nodes) + " }")
    lines.append("}")
    DOT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    model = ET.parse(MODEL_PATH).getroot()
    struct = model.find("struct")
    if struct is None:
        raise RuntimeError("FeatureIDE model has no <struct> element.")
    roots = feature_children(struct)
    if len(roots) != 1:
        raise RuntimeError(f"Expected exactly one feature-model root, found {len(roots)}.")
    root = roots[0]

    write_markdown(root, model)
    write_dot(root)
    print(f"Wrote {MARKDOWN_PATH.relative_to(ROOT)}")
    print(f"Wrote {DOT_PATH.relative_to(ROOT)}")
    print(
        textwrap.dedent(
            f"""\
            Next:
              dot -Tsvg {DOT_PATH.relative_to(ROOT)} -o {OUT_DIR.relative_to(ROOT) / "full-feature-model.svg"}
              dot -Tpng -Gdpi=220 {DOT_PATH.relative_to(ROOT)} -o {OUT_DIR.relative_to(ROOT) / "full-feature-model.png"}
            """
        ).strip()
    )


if __name__ == "__main__":
    main()
