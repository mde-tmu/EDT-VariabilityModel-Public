# Warehouse requirements and architectural decisions

The saved example (W-A) and its read-only alternative share a conveyor-zone boundary, a single-board edge controller,
MQTT messaging, direct sensors (temperature, humidity, proximity, RFID), warehouse
software interface, live ingestion, rule-based anomaly detection, local networking,
cloud history, dashboard and web app. They are constructed examples, not deployed
systems. No experiment measures response time, safety, performance or operator use.

| ID | Requirement/decision | Read-only alternative (scenario S3, not exported) | W-A: supervised automatic control |
|---|---|---|---|
| D1 | Required intervention | Notify an operator, who acts at a separate control console. | Deliver software commands to the edge controller under supervision. |
| D2 | Coupling choice | Digital_Shadow, Real_Time_Sync; Digital_Twin and Command_Control deselected. | Digital_Twin, Human_Supervised, Command_Control. |
| D3 | Command ownership | Existing plant controls and the operator own physical intervention. | An engineered command service owns requests; the edge controller owns final actuation/interlocks. |
| D4 | Asset interfaces | High_Level and Low_Level permit the software interface plus direct sensors. | Same interfaces; DC_Motor, Servo_Motor, Relay and Alarm describe the controlled equipment. |
| D5 | Data flow | Sensors -> MQTT -> edge ingestion -> rule service -> dashboard/cloud history. | Same observation flow; supervisor/controller -> command service -> edge controller -> actuator. |
| D6 | Runtime | Edge_Layer plus Cloud_Layer; Local_Network and GCP. | Same placement; numerical timing and fail-safe behavior require separate design. |
| D7 | Interfaces | Dashboard, Interactive_Dashboard and App/Platform/Web are present. | Same interfaces; authorization and override behavior must be implemented. |
| D8 | Security | Access_Control, User_Roles, Audit_Logs and Encryption. | Same selections; neither configuration certifies protection. |
| D9 | Standards | SysML used as a chosen modeling formalism. | Also selects intended ISO_IEC_19514_SysML use; C8 requires SysML. |

Start with S0-root from `scenarios.json`, then S1-control-propagation. Compare
`implied_selected`: requesting Digital_Twin adds Digital_Shadow, Command_Control,
Data and acquisition, while group alternatives remain manual decisions. The
scenario requirements then choose specific architecture, protocol, hardware and
interface options. The solver does not map a prose goal to these choices.

Conflict S2-read-only-conflict selects Digital_Twin and explicitly rejects
Command_Control. Repair S3-read-only-repair selects a shadow with live observation
and no software command path. Alternatively, change the requirements to permit a
command service and select W-A. This change does not preserve the original
read-only requirement.

W-A exports `smart_warehouse.xml` (90 selected nodes), the only saved warehouse
configuration. The read-only alternative is checked as scenario S3 and is not
exported. Every one of the 339 entries has an explicit manual selected/unselected
state. The file is written and re-imported using
FeatureIDE XMLConfFormat 3.12.0 and checked with ConfigurationAnalyzer.isValid().
The supplied scenario selections are the requirements record. The deterministic
completion prefers deselection for unresolved entries; any completion choices are
not recommendations or additional requirements. The old configuration had 231
entries with neither manual nor automatic state and was only a partial selection.

Remaining engineering decisions include rates, data schemas, model fidelity,
allocation of services, broker/API contracts, authorization, controller stability,
controller interlocks, loss-of-network behavior and runtime validation. These are recorded
responsibilities, not implemented outputs of the feature model.
