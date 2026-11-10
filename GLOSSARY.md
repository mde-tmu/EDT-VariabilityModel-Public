# Glossary and Feature Model Notation

This glossary explains the feature-model notation and the terms used in the DT variability model. Feature names follow the labels used in the public tree artifacts, usually with underscores.

## Feature Model Notation

**Feature Model:** A structured representation of common and variable features in a family of related systems.

**Feature:** A distinguishable characteristic, capability, design option, or implementation choice that may appear in a system configuration.

**Mandatory Feature:** A feature that must be selected when its parent feature is selected.

**Optional Feature:** A feature that may be selected when its parent feature is selected.

**M:** Edge label for a mandatory feature.

**O:** Edge label for an optional feature.

**AND Group:** A decomposition where mandatory children are required and optional children may be selected.

**OR Group:** A feature group where one or more child features may be selected.

**XOR Group / Alternative Group:** A feature group where exactly one child feature may be selected.

**Cross-Tree Constraint:** A rule that links features in different parts of the tree. For example, `Digital_Twin => Data` means that selecting `Digital_Twin` requires selecting `Data`.

**Configuration:** A selected subset of features that represents one possible DT design.

**Variability:** The ability of the model to represent multiple valid DT designs through selectable features.

## Core DT and CPS Concepts

**Digital Twin (DT):** A virtual representation of a physical system that mirrors relevant state, behavior, and interactions to support monitoring, analysis, simulation, or control.

**Cyber-Physical System (CPS):** A system where computation interacts with physical processes through sensors, actuators, controllers, and communication networks.

**Digital_Twin_Builder_v2:** The root feature of the model, representing the overall configurable DT design space.

**Synchronization:** The process of keeping physical and digital states consistent.

**Bidirectional Flow:** Data or control exchange that occurs in both directions between physical and digital systems.

**One-Directional Flow:** Data exchange from the physical system to the digital system only.

## Plain-Language Aliases from the Original Glossary

These entries preserve the wording from the original README glossary. Where the model uses underscore-based feature labels, these aliases point to the same concept.

**Digital Twin:** Same general concept as `Digital Twin (DT)`; when written as `Digital_Twin`, it refers to the feature-model node for the full twinning configuration.

**Twinning System:** Same as `Twinning_System`.

**Security System:** Same as `Security_System`.

**Connectivity System:** Same as `Connectivity_System`.

**User Interface (UI):** Same as `User_Interface`.

**Computation Model:** Same as `Computation_Model`.

**System Type:** Same as `System_Type`.

**High-Level System:** Same as `High_Level`.

**Low-Level System:** Same as `Low_Level`.

**Single Board Computer:** Same as `Single_Board_Computer`.

**Single Board Controller:** Same as `Single_Board_Controller`.

**Microprocessor:** Same as `Micro_Processor`.

**Industrial PLC:** Same as `Industrial_PLC`.

**Actuators:** Same concept as `Actuator`; devices that perform physical actions based on commands or control logic.

**Logic Model (CPS):** Same as `Logic_Model`.

**Manual Code:** Same as `Manual_Code`.

**Generated Code:** Same as `Generated_Code`.

**Code Generation (Model Level):** Same as `Code_Generation` when code is generated from models or model-level specifications.

**Modelling Language:** Same concept as `Modeling_Formalisms`.

**Modeling_Formalisms:** Same concept as `Modelling Language`.

**Real-Time Sync:** Same as `Real_Time_Sync`.

**Partial Data:** Same as `Partial_Data`.

**Reasoning System:** Same as `Reasoning_System`.

**Reasoning Model:** Same as `Reasoning_Model`.

**Data Processing:** Same as `Data_Processing`.

**Types of Reasoning:** Same as `Types_of_Reasoning`.

**Anomaly Detection:** Same as `Anomaly_Detection`.

**Predictive Maintenance:** Same as `Predictive_Maintenance`.

**Diagnostics:** Same concept as `Diagnosis`.

**What-If Analysis:** Same as `What_If_Analysis`.

**Feedback Loop:** Same as `Feedback_Loop`.

**Human-Actuated Feedback:** Same as `Human_Actuated`.

**Human-Supervised Feedback:** Same as `Human_Supervised`.

**Autonomous Feedback:** Same as `Autonomous`.

**Android Platform:** Same as `Android`.

**iOS Platform:** Same as `IOS`.

**Web Platform:** Same as `Web`.

**Logic Model Code:** Same as `Logic_Model_Code`.

**Wrapper Code:** Same as `Wrapper_Code`.

**Network Storage:** Same as `NetworkStorage`.

**Local Storage:** Same as `Local_Storage`.

**Cloud Integration:** Same as `Cloud_Integration`.

**Local Network:** Same as `Local_Network`.

**In-House Server:** Same as `In_House_Server`.

**Data Storage:** Same as `DataStorage`.

**On-Board Storage:** Same as `On_Board`.

**Online Storage:** Same as `Online`.

**Communication Protocols:** Same as `Communication_Protocols`.

**Access Control:** Same as `Access_Control`.

**User Roles:** Same as `User_Roles`.

**Audit Logs:** Same as `Audit_Logs`.

**OR-Group (Non-exclusive Choice):** Same as `OR Group`.

**XOR-Group (Exclusive Choice):** Same as `XOR Group / Alternative Group`.

## Main Subsystems

**Twinning_System:** The subsystem that captures digital model, digital shadow, digital twin, and extended twinning choices.

**Cyber_Physical_System:** The physical and embedded side of the DT, including computation, system type, sensors, actuators, and control logic.

**Architecture_System:** Architectural frameworks and concepts used to structure the DT.

**Deployment_Runtime:** Runtime and infrastructure choices such as edge, fog, cloud, operating system, orchestration, and time synchronization.

**User_Interface:** User-facing interaction mechanisms, including dashboards, apps, supported platforms, and immersive visualization.

**Connectivity_System:** Communication, network storage, cloud integration, data storage, and communication protocols.

**Data_Integration_System:** Integration patterns and data representation choices used to move, transform, and encode data.

**Goal_and_Capability_System:** Design goals and capabilities such as analytics, validation, reporting, quality attributes, and lifecycle support.

**Security_System:** Security-related features including encryption, anomaly alerts, device security, data encryption, privacy protection, access control, user roles, and audit logs.

**Standards_Compliance:** Standards related to simulation, modeling, physical entities, services, and engineering processes.

## Twinning System

**Digital_Model:** A virtual representation of a physical system. In this feature model, it is the mandatory basis for twinning because other twinning levels require a model to attach data, synchronization, reasoning, or feedback.

**Modeling_Formalisms / Modelling Language:** Languages or formalisms used to represent system structure or behavior.

**CBD:** Component-based design, where systems are modeled as interacting components.

**Cellular_Automata:** A discrete model based on cells that update according to local rules.

**StateCharts:** State-machine formalism with hierarchy, events, and transitions.

**Simulink:** A block-diagram modeling environment commonly used for simulation and control systems.

**Petri_Nets:** A formalism for modeling concurrent, asynchronous, and discrete-event systems.

**Timed_Automata:** Automata extended with timing constraints and clocks.

**Event_Scheduling_Discrete_Event:** A discrete-event simulation style where events are scheduled over simulated time.

**DEVS:** Discrete Event System Specification, a formalism for discrete-event modeling and simulation.

**Three_Phase_Discrete_Event:** A discrete-event simulation method organized around time advance, event execution, and conditional activities.

**Finite_State_Machines:** Models that describe behavior as states and transitions.

**Hybrid_Automata:** Models combining discrete state transitions with continuous dynamics.

**Modelica:** A modeling language for physical and cyber-physical systems.

**SysML:** Systems Modeling Language, used for systems engineering models.

**UML:** Unified Modeling Language, used for software and system design models.

**BPMN:** Business Process Model and Notation, used for process models.

**Formal_Methods:** Mathematically rigorous specification, modeling, or verification techniques.

**Data:** Information collected from or associated with the physical system and used by the digital representation.

**Data (Model Level):** Data used to improve, calibrate, validate, or operate a model.

**Code_Generation:** Generation of executable or deployable artifacts from models or model-related specifications.

**Data_Services:** Services that acquire, stream, transform, contextualize, store, or serve data for the DT.

**Data_Acquisition_and_Ingestion:** Collection and intake of data from physical systems, devices, files, services, or databases.

**Data_Streaming:** Continuous movement of data, often for near-real-time processing.

**Data_Transformation_Wrangling:** Cleaning, reshaping, joining, or converting data into usable forms.

**Data_Contextualization:** Adding semantic, asset, process, or operational context to raw data.

**Batch_Processing:** Processing data in bounded batches rather than continuously.

**Real_Time_Processing:** Processing data with low latency for operational monitoring or control.

**Data_Aggregation:** Combining multiple data points or streams into summaries or higher-level values.

**Synthetic_Data_Generation:** Producing artificial data for testing, simulation, training, or augmentation.

**Ontology_Management:** Managing formal vocabularies and relationships between concepts in a domain.

**Temporal_Data_Store:** Storage for time-indexed data such as time-series measurements.

**Data_Storage_Archive_Services:** Services for long-term storage, retrieval, and archival of DT data.

**Simulation_Model_Repository:** A repository that stores simulation models used by the DT.

**AI_Model_Repository:** A repository that stores machine-learning or AI models used by the DT.

**Digital_Shadow:** A digital model connected to data from the physical system, typically with one-way synchronization from the physical system to the digital representation.

**Real_Time_Sync:** Continuous or near-real-time synchronization between the physical system and its digital representation.

**Partial_Data:** Selective exchange of data between physical and digital systems.

**Reasoning_System:** A subsystem that processes data and produces insights, decisions, simulations, diagnoses, predictions, or optimizations.

**Data_Processing:** Transformation, preparation, filtering, or enrichment of data for analysis.

**Optimization:** Techniques used to improve system performance, resource use, control decisions, or design choices.

**Simulation:** Virtual execution of system behavior without requiring the physical system to run the scenario.

**What_If_Analysis:** Simulation or analysis of hypothetical scenarios.

**Discrete_Event_Simulation:** Simulation where state changes occur at discrete event times.

**Agent_Based_Simulation:** Simulation based on autonomous agents and their interactions.

**System_Dynamics_Simulation:** Simulation of feedback loops, accumulations, and flows over time.

**Continuous_Simulation:** Simulation of continuously changing system variables.

**Hybrid_Simulation:** Simulation combining continuous and discrete-event behavior.

**Physics_Based_Simulation:** Simulation based on physical laws or first-principles models.

**Monte_Carlo_Simulation:** Simulation using repeated random sampling to analyze uncertainty.

**Reasoning_Model:** The reasoning approach used by the DT.

**Logic_Based_Reasoning:** Reasoning based on formal logic.

**Rule_Based_Reasoning:** Reasoning based on explicit if-then rules.

**Ontological_Reasoning:** Reasoning over concepts, relations, and constraints defined in an ontology.

**Artificial_Intelligence_AI:** AI techniques used for prediction, reasoning, adaptation, or decision support.

**AI Models (LLMs):** Machine learning models, including large language models, that can assist analysis, generation, or automation tasks.

**Fuzzy_Logic_Reasoning:** Reasoning with degrees of truth rather than only binary true/false values.

**Probabilistic_Reasoning:** Reasoning under uncertainty using probability.

**ML_Based_Reasoning:** Reasoning or prediction using machine-learning models.

**Reinforcement_Learning_Reasoning:** Learning decisions through interaction, reward, and feedback.

**Types_of_Reasoning:** Categories of analytical or decision-support tasks performed by a DT.

**Anomaly_Detection:** Identifying abnormal behavior in system data.

**Predictive_Maintenance:** Predicting failures or maintenance needs before they occur.

**Diagnosis:** Identifying the cause of a system issue.

**Failure_Prediction:** Predicting likely failures or degradation events.

**Asset_Health_Estimation:** Estimating the condition or remaining useful state of an asset.

**Pattern_Recognition:** Identifying recurring structures or behaviors in data.

**Analysis:** General analytical capability for interpreting DT data and behavior.

**Digital_Twin:** A more advanced twinning configuration that includes data, synchronization, reasoning, and feedback-related capabilities.

**Feedback_Loop:** A mechanism where information from the digital side influences the physical system or human operator.

**Human_Actuated:** Feedback applied manually by a human operator.

**Autonomous:** Feedback or control applied automatically without human intervention.

**Human_Supervised:** Automated feedback or control applied under human supervision.

**Extended_Twinning_Types:** Additional twinning variants beyond the basic digital model, digital shadow, and digital twin distinction.

**Cognitive_Twin:** A twin with advanced reasoning, learning, or cognitive capabilities.

**Hybrid_Twin:** A twin that combines multiple modeling, data, or synchronization approaches.

**Federated_Twin:** A twin formed by coordinating multiple twins or twin components.

**Minimal_Twin:** A reduced twin configuration that includes only the essential features needed for a purpose.

**Twined_System:** A system designed or operated together with its digital twin representation.

## Cyber-Physical System

**Computation_Model:** The computation platform used by the CPS.

**Single_Board_Computer:** A compact computing system capable of running a full operating system.

**Single_Board_Controller:** A microcontroller-based system designed for simpler control tasks.

**Micro_Processor:** A processing unit used in custom embedded hardware systems.

**Emulator:** A virtual environment that simulates CPS hardware behavior.

**Industrial_PLC:** A programmable logic controller used in industrial automation systems.

**FPGA:** Field-programmable gate array, configurable hardware for parallel or specialized computation.

**DSP:** Digital signal processor, optimized for real-time signal processing.

**GPU:** Graphics processing unit, often used for parallel computation or AI workloads.

**Edge_AI_Accelerator:** Specialized edge hardware for running AI inference near the physical system.

**System_Type:** The architectural abstraction level of a CPS system, such as high-level or low-level design.

**High_Level:** A black-box or higher-abstraction system accessed through APIs, protocols, or component interfaces.

**Protocols:** Communication or interaction rules exposed by a high-level system.

**Hardware_Components:** Physical or logical hardware units exposed or represented by the system.

**Low_Level:** A system providing direct control over hardware components such as sensors, actuators, and control logic.

**Actuator:** A device that performs a physical action based on a command.

**LED:** A light-emitting diode used as an output or indicator.

**Alarm:** An alerting actuator used to signal abnormal or important events.

**Buzzer:** An audible signaling actuator.

**Servo_Motor:** A motor that provides controlled angular or linear position.

**DC_Motor:** A direct-current motor.

**AC_Motor:** An alternating-current motor.

**Stepper_Motor:** A motor that moves in discrete steps.

**Linear_Motor:** A motor that produces linear motion.

**Pneumatic_Actuator:** An actuator driven by compressed air.

**Hydraulic_Actuator:** An actuator driven by pressurized fluid.

**Solenoid_Valve:** An electromechanical valve used to control fluid or air flow.

**Relay:** An electrically controlled switch.

**Piezoelectric_Actuator:** An actuator using piezoelectric material deformation.

**Sensors:** Devices that collect physical or environmental data.

**Flame_Sensor:** A sensor for detecting flame or fire.

**Heat_Sensor:** A sensor for detecting heat levels or heat changes.

**Ultrasonic_Sensor:** A distance or presence sensor using ultrasonic sound.

**PIR_Sensor:** Passive infrared sensor commonly used for motion detection.

**LDR_Sensor:** Light-dependent resistor used for measuring light intensity.

**Vibration_Sensor:** A sensor for detecting vibration or oscillation.

**Temperature_Sensor:** A sensor for measuring temperature.

**Proximity_Sensor:** A sensor for detecting nearby objects.

**Humidity_Sensor:** A sensor for measuring humidity.

**Gas_Sensor:** A sensor for detecting gases or gas concentration.

**Pressure_Sensor:** A sensor for measuring pressure.

**IMU_Sensor:** Inertial measurement unit for acceleration, rotation, or orientation.

**LiDAR:** Light detection and ranging sensor for distance or spatial mapping.

**Radar:** Radio-based sensing technology for object detection, distance, or motion.

**RFID:** Radio-frequency identification technology for identifying tagged objects.

**Camera_Sensor:** An image or video sensor.

**Logic_Model:** The control logic that governs CPS behavior and system interactions.

**Manual_Code:** Handwritten software implementation of system logic.

**Generated_Code:** Automatically generated code derived from models, transformations, or AI systems.

**Model_To_Code:** Model-driven transformation from models into executable code or software artifacts.

**Model-to-Code Transformation:** A process in model-driven engineering that converts models into executable code.

**AI_Enabled_Code_Generation:** Code generation assisted by AI techniques.

## Architecture System

**Architecture_Concepts:** Architectural patterns, frameworks, or reference models used to structure DT systems.

**Platform_Stack_Architectural_Framework:** An architecture organized around platform layers and technology stack concerns.

**RAMI_4_0:** Reference Architectural Model Industrie 4.0.

**IIRA:** Industrial Internet Reference Architecture.

**Unified_Architecture_Framework:** A framework for describing enterprise and system architectures.

**OPC_UA_Reference_Architecture:** Architecture based on OPC UA concepts for industrial interoperability.

**AAS_Reference_Architecture:** Architecture based on the Asset Administration Shell.

**TOGAF:** The Open Group Architecture Framework.

**NIST_Framework:** Architecture or security guidance associated with NIST frameworks.

**ISO_23247_Framework:** Framework for digital twins in manufacturing based on ISO 23247.

**Digital_Twin_as_a_Service:** A service-based delivery model for DT capabilities.

**Five_Dimension_DT_Model:** A DT architecture concept organized around five dimensions.

**Eight_Dimension_DT_Model:** A DT architecture concept organized around eight dimensions.

**Layered_Architecture:** An architecture organized into layers with distinct responsibilities.

**Modular_Service_Oriented_Architecture:** An architecture built from modular services.

**Federated_Digital_Twin_Architecture:** An architecture where multiple twins or DT components interoperate.

**Standard_Based_Architecture:** An architecture structured around recognized standards.

**Platform_Architecture:** Architecture centered on a reusable DT platform.

**Cloud_Stack_Architecture:** Architecture organized around cloud infrastructure and services.

**IoT_Based_Architecture:** Architecture centered on IoT devices, gateways, and connectivity.

## Deployment Runtime

**Deployment_Layers:** Runtime placement choices for DT components.

**Edge_Layer:** Execution near the physical system or data source.

**Fog_Layer:** Intermediate distributed computing layer between edge and cloud.

**Cloud_Layer:** Cloud-hosted execution or storage.

**Hybrid_Edge_Fog_Cloud:** Deployment combining edge, fog, and cloud resources.

**Operating_System:** Runtime operating system used by DT or CPS components.

**General_Purpose_OS:** General operating systems such as desktop or server OSs.

**Real_Time_OS:** Operating system designed for deterministic timing behavior.

**Linux_Embedded:** Embedded Linux deployment.

**Windows_IoT:** Microsoft Windows-based IoT deployment.

**ROS:** Robot Operating System middleware and tooling.

**Hypervisor_OS:** Virtualization layer for running isolated operating systems or components.

**Runtime_Orchestration:** Infrastructure for running and coordinating services or components.

**Docker:** Containerization technology.

**Kubernetes:** Container orchestration platform.

**Kubernetes_Edge:** Kubernetes-based orchestration adapted for edge environments.

**Node_RED:** Flow-based development and integration tool.

**Home_Assistant:** Home automation platform that can orchestrate smart devices.

**Time_Synchronization:** Mechanisms that align timing across distributed components.

**NTP:** Network Time Protocol.

**PTP:** Precision Time Protocol.

**TSN:** Time-Sensitive Networking.

## User Interface

**Dashboard:** A user interface for monitoring, analytics, configuration, or control.

**Static_Dashboard:** A dashboard that mainly displays fixed or non-interactive information.

**Interactive_Dashboard:** A dashboard that supports interaction, filtering, exploration, configuration, or control.

**Wrapper_Code:** Supporting integration code required to deploy and connect system components.

**Logic_Model_Code:** Generated or manually written code derived from system models to implement behavior.

**App:** A simplified interface designed for monitoring, control, or interaction by end users.

**Platform:** Supported application platforms.

**Android:** Mobile platform for Android devices.

**IOS:** Mobile platform for Apple iOS devices.

**Web:** Browser-based platform for accessing the DT system.

**App Platform:** Supported application platforms such as Android, iOS, and Web. This is modeled as an OR group because a DT app may support more than one platform.

**Immersive_Visualization:** Visualization approaches that provide spatial, 3D, or immersive interaction.

**Three_D_Rendering:** 3D rendering of assets, environments, or simulation states.

**Augmented_Reality_AR:** Overlaying digital information on the physical environment.

**Virtual_Reality_VR:** Immersive virtual environment for DT interaction or visualization.

**Gaming_Engine_Visualization:** Visualization built with game-engine technology.

**Virtual_Prototyping:** Using a virtual representation to explore or test a system before physical deployment.

## Connectivity System

**NetworkStorage:** Deployment or storage options related to local or cloud network environments.

**Network Storage:** The deployment environment that defines where the system is hosted and operated.

**Local_Storage:** A local infrastructure option for storage or hosting.

**Local Storage:** A deployment option where data and services are hosted within local infrastructure.

**Local_Network:** A closed or local communication environment that may operate independently of the internet.

**In_House_Server:** A locally managed server that can optionally connect to external networks.

**Cloud_Integration:** Connectivity to cloud services or DT platforms.

**AWS:** Amazon Web Services cloud platform.

**Azure:** Microsoft Azure cloud platform.

**GCP:** Google Cloud Platform.

**Custom_Cloud:** A custom cloud environment or provider-specific deployment.

**AWS_IoT_TwinMaker:** AWS service for building digital twin applications.

**Azure_Digital_Twins:** Azure service for modeling and building digital twin environments.

**Eclipse_Ditto:** Open-source framework for managing digital twin state.

**FIWARE:** Open-source platform components for smart applications and digital services.

**PTC_ThingWorx:** Industrial IoT and digital transformation platform.

**Siemens_MindSphere:** Siemens industrial IoT platform.

**GE_Predix:** Industrial IoT platform associated with GE.

**DataStorage:** Storage options for CPS or DT data.

**Data Storage:** A mechanism for storing CPS or system data for processing and analysis.

**On_Board:** Storage located directly on CPS hardware devices.

**On-Board Storage:** Storage located directly on CPS hardware devices.

**Online:** Cloud-based or external storage services used for data management.

**Online Storage:** Cloud-based or external storage services used for data management.

**Communication_Protocols:** Protocols and standards used for component communication.

**Communication Protocols:** Rules and standards that define how system components exchange data.

**MQTT:** Lightweight publish-subscribe messaging protocol often used in IoT.

**Modbus:** Industrial communication protocol.

**WebSocket:** Protocol enabling persistent, real-time bidirectional communication.

**HTTP:** Request-response protocol used for standard web communication.

**CustomProtocol:** Project-specific or domain-specific communication protocol.

**OPC_UA:** Open Platform Communications Unified Architecture, an industrial interoperability standard.

**AAS:** Asset Administration Shell, a standardized digital representation concept for Industry 4.0 assets.

**AMQP:** Advanced Message Queuing Protocol.

**DDS:** Data Distribution Service middleware standard.

**CoAP:** Constrained Application Protocol for constrained IoT devices.

**CAN_Bus:** Controller Area Network bus, commonly used in embedded and vehicle systems.

**EtherCAT:** Ethernet-based industrial fieldbus protocol.

**PROFINET:** Industrial Ethernet communication standard.

**RS_485:** Serial communication standard used in industrial systems.

**I2C:** Inter-Integrated Circuit serial communication bus.

**SPI:** Serial Peripheral Interface communication bus.

**UART:** Universal asynchronous receiver-transmitter serial communication.

**Bluetooth_LE:** Bluetooth Low Energy wireless communication.

**Zigbee:** Low-power wireless communication protocol.

**LoRaWAN:** Low-power wide-area network protocol.

**NB_IoT:** Narrowband IoT cellular communication technology.

## Data Integration System

**Integration_Patterns:** Styles for moving, connecting, or synchronizing data and services.

**Streaming_Integration:** Continuous data integration from streams.

**Batch_Integration:** Integration performed on batches of data.

**Event_Driven_Integration:** Integration triggered by events.

**Hybrid_Integration:** Integration combining multiple patterns such as batch and streaming.

**API_Based_Integration:** Integration through application programming interfaces.

**Database_Federation:** Querying or integrating data across multiple databases without physically merging all data.

**File_Based_Integration:** Integration through exchanged files.

**Message_Queue_Integration:** Integration through queues or message brokers.

**Webhook_Based_Integration:** Integration using HTTP callbacks triggered by events.

**ETL_Pipeline:** Extract, transform, and load pipeline for moving and preparing data.

**Change_Data_Capture:** Capturing and propagating changes from source data systems.

**Data_Representation:** Data formats and modeling representations used to encode DT data.

**JSON:** JavaScript Object Notation.

**XML:** Extensible Markup Language.

**YAML:** Human-readable data serialization format.

**CSV:** Comma-separated values tabular format.

**HDF5:** Hierarchical Data Format version 5.

**Parquet:** Columnar data storage format.

**Protocol_Buffers:** Binary serialization format by Google.

**Avro:** Data serialization system often used with streaming and big data systems.

**JSON_LD:** JSON for Linked Data.

**RDF:** Resource Description Framework.

**OWL:** Web Ontology Language.

**DTDL:** Digital Twins Definition Language.

**AutomationML:** XML-based data format for engineering and automation data exchange.

## Goal and Capability System

**Goal_Capabilities:** Functional and non-functional DT capabilities that support the system's goals.

**Enterprise_System_Integration:** Integration with enterprise systems such as ERP or business platforms.

**Engineering_System_Integration:** Integration with engineering tools, models, or lifecycle systems.

**OT_IoT_System_Integration:** Integration with operational technology and IoT systems.

**Digital_Twin_Integration:** Integration between DT components, twins, or DT platforms.

**API_Services:** Services exposed through APIs for access, integration, or automation.

**Edge_AI_Intelligence:** AI capability deployed near the physical system or data source.

**Command_Control:** Capability to issue commands or control actions.

**Machine_Learning_ML:** Machine-learning capability for prediction, classification, optimization, or analytics.

**Federated_Learning:** Machine learning across distributed data sources without centralizing all data.

**Orchestration_Workflow_Management:** Coordination of workflows, tasks, services, or processes.

**Alerts_Notifications:** User or system notifications triggered by events or conditions.

**Reporting:** Generation of reports from DT data or analysis.

**Descriptive_Analytics:** Analytics that summarize what happened.

**Diagnostic_Analytics:** Analytics that explain why something happened.

**Prescriptive_Analytics:** Analytics that recommend what action to take.

**Continuous_Intelligence:** Ongoing analytics over current data to support real-time or near-real-time decisions.

**Validation:** Checking whether models, configurations, or outputs satisfy requirements or expected behavior.

**Quality_Attributes:** Non-functional properties used to assess a DT design.

**Availability:** Degree to which the system is operational when needed.

**Reliability:** Degree to which the system performs correctly over time.

**Resilience:** Ability to recover from disruptions or continue operating under adverse conditions.

**Performance:** Efficiency, latency, throughput, or resource behavior of the system.

**Trustworthiness:** Degree to which the system can be relied on for correct, secure, and accountable behavior.

**Safety:** Avoidance of unacceptable harm to people, equipment, or environment.

**Privacy:** Protection of personal, sensitive, or confidential information.

**Interoperability:** Ability of systems or components to exchange and use information.

**Traceability:** Ability to follow relationships among requirements, models, data, decisions, and artifacts.

**Evolution:** Ability of the DT to adapt as the physical system, requirements, or environment changes.

**Lifecycle_Capabilities:** Capabilities that support operation, governance, maintenance, or evolution across the system lifecycle.

**Device_Management:** Managing devices, identities, updates, monitoring, and operational status.

**Data_Governance:** Policies and processes for managing data quality, ownership, access, and compliance.

**Life_Cycle_Management:** Managing the system across design, deployment, operation, maintenance, and retirement.

**Product_Lifecycle_Management:** Managing product data and processes across the product lifecycle.

**Asset_Performance_Management:** Monitoring and improving the performance of physical assets.

**Digital_Product_Passport:** Digital record containing product information across the lifecycle.

**Digital_Continuity:** Maintaining consistent digital information across lifecycle stages, tools, and systems.

## Security System

**Encryption:** A method of securing data by converting it into an unreadable format without proper authorization.

**Anomaly_Alerts:** Mechanisms that detect and report unusual or suspicious behavior.

**Anomaly Alerts:** A mechanism that detects and reports unusual or suspicious system behavior.

**Device_Security:** Security mechanisms protecting devices, embedded systems, and endpoints.

**Data_Encryption:** Encryption applied to data at rest, in transit, or in use.

**Privacy_Protection:** Measures that protect private or sensitive information.

**Access_Control:** A security mechanism that defines and enforces user permissions within the system.

**User_Roles:** Defined categories of users with specific permissions based on responsibilities.

**Audit_Logs:** Records of system and user activities used for traceability and forensic analysis.

## Standards Compliance

**Simulation_Standards:** Standards related to simulation interoperability, execution, or model packaging.

**FMI:** Functional Mock-up Interface standard.

**HLA:** High Level Architecture standard for distributed simulation.

**DSEEP:** Distributed Simulation Engineering and Execution Process.

**DIS:** Distributed Interactive Simulation standard.

**SSP:** System Structure and Parameterization standard.

**Modeling_Standards:** Standards related to modeling languages and notations.

**ISO_IEC_19514_SysML:** ISO/IEC standard for SysML.

**ISO_IEC_19505_UML:** ISO/IEC standard for UML.

**ISO_IEC_19510_BPMN:** ISO/IEC standard for BPMN.

**ArchiMate_Standard:** Enterprise architecture modeling standard.

**Physical_Entity_Standards:** Standards related to physical assets, sensors, industrial automation, or DT manufacturing.

**IEEE_1451:** Standard family for smart transducer interfaces.

**ISO_23247_1:** ISO 23247 part 1 for digital twin framework in manufacturing.

**ISO_23247_2:** ISO 23247 part 2 for reference architecture in manufacturing digital twins.

**ISO_23247_3:** ISO 23247 part 3 for digital representation in manufacturing digital twins.

**ISO_23247_4:** ISO 23247 part 4 for information exchange in manufacturing digital twins.

**IEC_61131:** IEC standard family for programmable controllers.

**IEC_62541:** IEC standard series for OPC UA. In the model, selecting `IEC_62541` requires selecting `OPC_UA`.

**IEC_62443:** IEC standard family for industrial automation and control system security.

**Service_Standards:** Standards and interface styles for services and APIs.

**OpenAPI:** Specification for describing REST-style APIs.

**GraphQL:** Query language and API runtime for graph-shaped data access.

**AsyncAPI:** Specification for describing asynchronous/event-driven APIs.

**gRPC:** Remote procedure call framework using Protocol Buffers.

**Engineering_Standards:** Standards related to systems, software, functional safety, and process maturity.

**ISO_15288:** Systems and software engineering lifecycle process standard for systems.

**ISO_12207:** Systems and software engineering lifecycle process standard for software.

**ISO_26262:** Functional safety standard for road vehicles.

**CMMI:** Capability Maturity Model Integration.
