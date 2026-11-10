# Definitions used in the revised model

Definitions are scoped author interpretations unless an external identity source
is stated. Complete paths/group cardinalities are in the generated
`feature-model/full-feature-model.md`; source candidates are in feature_mapping.json.
Selecting a capability records its inclusion/need, not a verified implementation.

| Term | Meaning within one complete configured solution |
|---|---|
| Twinning_System | Representation, coupling and associated data/reasoning capabilities. |
| Digital_Model | Representation capability; cumulative, not an exclusive no-coupling class. |
| Digital_Shadow | Automatic inward coupling from the asset to the representation. |
| Digital_Twin | Inward coupling plus a software command path back to the plant. |
| Feedback_Loop | Selected arrangements for outward command coupling. |
| Human_Actuated | Human initiation/authorization of a command transmitted through software. |
| Human_Supervised | Software commands subject to human supervision/override. |
| Autonomous | Software-originated commands without per-command human initiation. |
| Real_Time_Sync | Live incoming updates; no quantitative timing guarantee. |
| Data | Acquired, stored, synthetic or model data. |
| Data_Acquisition_and_Ingestion | Obtaining and ingesting data used for inward coupling. |
| Data_Streaming | A service delivering/handling a stream of data. |
| Real_Time_Processing | Processing incoming live updates as they arrive, without a specified deadline bound. |
| Reasoning_System | Data processing plus one or more selected reasoning models; inherited beneath the shadow capability. |
| Optimization | Objective-directed optimization, optional even when reasoning is present. |
| Simulation | Simulation capability; inherited placement limits offline-only use. |
| Cyber_Physical_System | Physical/embedded computation and asset interface choices. |
| High_Level | Connecting to an existing system through a supplied interface/protocol. |
| Low_Level | Directly integrated sensing, actuation or logic. |
| Connectivity_System | Infrastructure/platform integration, transport and storage choices. |
| Local_Storage | Local networking/server infrastructure (legacy group name retained). |
| Cloud_Integration | Cloud/platform integration choices; includes platforms that may be self-hosted. |
| Architecture_System | Selected architecture concepts/patterns for the solution. |
| Cloud_Stack_Architecture | An implemented cloud stack within the solution boundary. |
| Deployment_Runtime | Deployment sites and runtime/clock-service choices. |
| Hybrid_Edge_Fog_Cloud | The explicitly three-layer profile; other combinations use direct layer selections. |
| Kubernetes_Edge | Kubernetes-based runtime at an edge site. |
| Data_Integration_System | Patterns and representations used to make data usable. |
| Streaming_Integration | An integration pattern requiring a streaming service, without fixing transport. |
| API_Based_Integration | Integration through an API service, including an external supplied API. |
| API_Services | Software/API interfaces included or relied on by the solution. |
| Goal_and_Capability_System | Selected intentions/capabilities and quality/lifecycle concerns; no automatic goal mapping. |
| Command_Control | A software command capability for the physical system. |
| Interoperability | Explicit interoperability concern, not proof of successful interchange. |
| User_Interface | Selected dashboard, app or visualization responsibilities. |
| Wrapper_Code / Logic_Model_Code | Inherited dashboard integration/behavior code responsibilities; not code emitted by this artifact. |
| Security_System | Selected protection responsibilities; absence does not establish acceptable risk. |
| Standards_Compliance | Intended standard/technology use; not certified conformance. |
| Modeling_Standards | Intended modeling specifications, implying the named formalism in C8–C10. |

Remaining leaves generally retain their technology or domain names. Exact
standard identities are linked in the rule ledger. The glossary does not invent
precise semantics for unresolved source concepts; targeted review remains needed.
