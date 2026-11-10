# Semantic decisions for v2-serp4iot-v1

The configuration unit is one complete DT engineering solution. Features indicate
that a concern or capability occurs somewhere inside its stated boundary. The
Boolean model does not allocate features to individual components or count twins.

| Decision | Before | Revised meaning and rationale |
|---|---|---|
| Twinning names | Cumulative features described as exclusive classifications | `Digital_Model` means representation capability and remains mandatory. `Digital_Shadow` adds automatic inward data coupling; `Digital_Twin` adds automatic software-mediated outward commands. Classify a solution by its highest selected level. |
| Human intervention | Unspecified relationship with automatic feedback | `Human_Actuated` means human initiation/authorization followed by software command transmission. A person acting directly on the physical plant outside the DT command path belongs to a shadow-plus-operator design. Live observation can coexist with either intervention process. |
| C1 | Shadow requires Model and Data | Model is already mandatory; require Data and acquisition/ingestion. |
| C2 | Twin requires Shadow, Reasoning, Data, Real_Time_Sync | Require Shadow and Command_Control. Reasoning and live updates are scenario choices; scheduled command coupling is permitted. Data is transitively required by C1. |
| C3 | Federation requires architecture, interoperability, API services | Retain architecture and interoperability. API style is advisory; DDS or other interfaces can be used. |
| C5 | Edge AI requires an accelerator | Require Edge_Layer; CPU inference is permitted. Acceleration requires workload evidence. |
| C6 | Formal methods require Validation and Safety | Retire C6. Formal specification is possible before selecting validation and outside safety applications. The identifier is not reused. |
| Hybrid_Edge_Fog_Cloud | Undefined hybrid profile | Denotes all three named layers. Edge-plus-cloud uses those two explicit layers, without this profile. |
| System_Type | XOR High_Level/Low_Level | OR: black-box interfaces and directly integrated devices may coexist in a complete solution. |
| NetworkStorage | XOR local/cloud | OR: a complete solution may use both local infrastructure and cloud integration. |
| Local_Storage | XOR network/server | OR: a local network and in-house server can coexist. |
| DataStorage | XOR on-board/online | OR: buffering on-board and storing remotely can coexist. |
| Optimization | Mandatory beneath Reasoning_System | Optional: rule evaluation or anomaly detection need not optimize an objective. |
| Standards_Compliance | Could be read as certified compliance | An intended standard/technology choice. The model does not assess or certify compliance. |
| Data | Unspecified data | Acquired, stored, synthetic, or model data. Presence does not imply live physical coupling. |
| Real_Time_Sync | Could be read as a proved timing guarantee | Live incoming updates, requiring live processing. Numerical deadlines, clock error, jitter and scheduling remain outside this Boolean model. |
| API_Services | Ambiguous service location | An API interface used within the solution, including a supplied external endpoint. |
| Data_Streaming | Relation to integration unstated | A streaming service is required by Streaming_Integration; no transport is mandated. |

The new rules are explicit author integration definitions or standard/technology
identity relationships. They are not presented as rules validated by experts.
`constraint_rationale.json` is the rule ledger; XML rule order omits retired C6.

The public TwinCompass rule file is pinned in `source_inventory.json`. Its
Digital_Model exclusions are not imported because it uses different classification
semantics. Wireless/wired and topology exclusions are not whole-solution rules;
neither simulation/visualization exclusion nor continuous/real-time implication
is a universal requirement. Recommendations about sensors, actuators and transport
remain advice. A link between this rule-file commit and the published expert study
has not been verified.

Known remaining issue: `Simulation` is nested beneath `Reasoning_System` beneath
`Digital_Shadow`. Offline simulation therefore forces inward coupling even when
the documented use does not establish it. E1 exposes this semantic mismatch. The
case is reported as a limitation; satisfiability does not establish faithful fit.
