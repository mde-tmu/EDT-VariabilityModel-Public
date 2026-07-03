# EDT Variability Model for Digital Twins of Cyber-Physical Systems

This repository provides public artifacts for a feature model that supports the design and configuration of digital twins (DTs) for cyber-physical systems (CPSs).

The model represents DT design as a set of configurable features. It captures common DT design concerns such as twinning level, physical assets, computation, sensors and actuators, deployment, connectivity, data integration, user interfaces, goals, security, and standards. It also includes cross-tree constraints that encode dependencies a valid DT configuration must satisfy.

## Why This Model Exists

Designing a DT requires many connected decisions. For example, selecting a full digital twin should also imply data, synchronization, reasoning support, and a lower twinning level. A flat checklist does not capture these dependencies well.

This feature model makes the design space explicit by using:

- mandatory and optional features;
- `and`, `or`, and `xor` feature groups;
- subsystem colors for navigation;
- cross-tree constraints for checking valid configurations.

## Quick View

- [Zoomable full-tree SVG](feature-model/full-feature-model.svg): best option for browsing and zooming in a browser.
- [High-resolution PNG](feature-model/full-feature-model.png): bitmap preview/export of the full tree.
- [Graphviz DOT source](feature-model/full-feature-model.dot): graph source used to generate the SVG and PNG.
- [Glossary and notation guide](GLOSSARY.md): explains feature-model notation and common DT/CPS terms used in the model.

The editable FeatureIDE XML source model and example configurations are not included in this public artifact yet.

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

The model includes constraints that capture dependencies across separate branches:

- `Digital_Shadow` requires `Digital_Model` and `Data`.
- `Digital_Twin` requires `Digital_Shadow`, `Reasoning_System`, `Data`, and `Real_Time_Sync`.
- `Federated_Twin` requires `Federated_Digital_Twin_Architecture`, `Interoperability`, and `API_Services`.
- `Cloud_Layer` requires `Cloud_Integration`.
- `Edge_AI_Intelligence` requires `Edge_Layer` and `Edge_AI_Accelerator`.
- `Formal_Methods` requires `Validation` and `Safety`.
- `IEC_62541` requires `OPC_UA`.

These constraints prevent incomplete configurations, such as selecting a full digital twin without synchronization or reasoning support.

## Regenerating Visuals

The included DOT file can be rendered with Graphviz:

```sh
dot -Tsvg feature-model/full-feature-model.dot -o feature-model/full-feature-model.svg
dot -Tpng -Gdpi=220 feature-model/full-feature-model.dot -o feature-model/full-feature-model.png
```

The SVG is the preferred artifact for inspection because it remains sharp when zoomed.
