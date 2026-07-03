# Glossary and Feature Model Notation

This glossary explains common terms used in the DT feature model and the notation used in the visual artifacts.

## Feature Model Notation

**Feature Model:** A structured representation of common and variable features in a family of related systems.

**Feature:** A distinguishable characteristic, capability, design option, or implementation choice that may appear in a system configuration.

**Mandatory Feature:** A feature that must be selected when its parent feature is selected.

**Optional Feature:** A feature that may be selected when its parent feature is selected.

**AND Group:** A decomposition where mandatory children are required and optional children may be selected.

**OR Group:** A feature group where one or more child features may be selected.

**XOR Group / Alternative Group:** A feature group where exactly one child feature may be selected.

**Cross-Tree Constraint:** A rule that links features in different parts of the tree. For example, `Digital_Twin => Data` means that selecting `Digital_Twin` requires selecting `Data`.

**Configuration:** A selected subset of features that represents one possible DT design.

**Variability:** The ability of the model to represent multiple valid DT designs through selectable features.

## Digital Twin Concepts

**Digital Twin (DT):** A virtual representation of a physical system that mirrors relevant state, behavior, and interactions to support monitoring, analysis, simulation, or control.

**Cyber-Physical System (CPS):** A system where computation interacts with physical processes through sensors, actuators, controllers, and communication networks.

**Digital Model:** A virtual representation of a physical system. In this feature model, it is the mandatory basis for twinning because other twinning levels require a model to attach data, synchronization, reasoning, or feedback.

**Digital Shadow:** A digital model connected to data from the physical system, typically with one-way synchronization from the physical system to the digital representation.

**Digital Twin:** A more advanced twinning configuration that includes data, synchronization, reasoning, and feedback-related capabilities.

**Extended Twinning Types:** Additional variants such as cognitive, hybrid, federated, minimal, or twined systems.

## Main Subsystems

**Twinning System:** The subsystem that captures digital model, digital shadow, digital twin, and extended twinning choices.

**Cyber-Physical System:** The physical and embedded side of the DT, including computation, system type, sensors, actuators, and control logic.

**Architecture System:** Architectural frameworks and concepts used to structure the DT.

**Deployment Runtime:** Runtime and infrastructure choices such as edge, fog, cloud, operating system, orchestration, and time synchronization.

**User Interface:** User-facing interaction mechanisms, including dashboards, apps, supported platforms, and immersive visualization.

**Connectivity System:** Communication, network storage, cloud integration, data storage, and communication protocols.

**Data Integration System:** Integration patterns and data representation choices used to move, transform, and encode data.

**Goal and Capability System:** Design goals and capabilities such as analytics, validation, reporting, quality attributes, and lifecycle support.

**Security System:** Security-related features including encryption, anomaly alerts, device security, data encryption, privacy protection, access control, user roles, and audit logs.

**Standards Compliance:** Standards related to simulation, modeling, physical entities, services, and engineering processes.

## Selected Feature Definitions

**Modeling Formalism:** A language or formalism used to represent system structure or behavior, such as StateCharts, SysML, UML, Modelica, Petri nets, or formal methods.

**Data:** Information collected from or associated with the physical system and used by the digital representation.

**Code Generation:** Generation of executable or deployable artifacts from models or model-related specifications.

**Real-Time Sync:** Continuous or near-real-time synchronization between the physical system and its digital representation.

**Reasoning System:** A subsystem that processes data and produces insights, decisions, simulations, diagnoses, predictions, or optimizations.

**Reasoning Model:** The reasoning approach used by the DT, such as logic-based reasoning, rule-based reasoning, ontological reasoning, artificial intelligence, fuzzy logic, probabilistic reasoning, machine learning, or reinforcement learning.

**Feedback Loop:** A mechanism where information from the digital side influences the physical system or human operator.

**Computation Model:** The computation platform used by the CPS, such as single-board computers, controllers, industrial PLCs, GPUs, or edge AI accelerators.

**System Type:** The abstraction level of the CPS model, such as high-level or low-level representation.

**Sensors:** Devices that collect physical or environmental data.

**Actuators:** Devices that perform physical actions based on commands or control logic.

**Logic Model:** The control logic that governs CPS behavior.

**Deployment Layers:** Runtime placement choices such as edge, fog, cloud, or hybrid edge/fog/cloud deployment.

**Runtime Orchestration:** Infrastructure for running and coordinating services, such as Docker, Kubernetes, Kubernetes Edge, Node-RED, or Home Assistant.

**Time Synchronization:** Mechanisms such as NTP, PTP, or TSN that align timing across distributed components.

**Dashboard:** A user interface for monitoring, analytics, configuration, or control.

**App Platform:** Supported application platforms such as Android, iOS, and Web. This is modeled as an OR group because a DT app may support more than one platform.

**Immersive Visualization:** Visualization approaches such as 3D rendering, augmented reality, virtual reality, gaming-engine visualization, or virtual prototyping.

**Cloud Integration:** Connectivity to cloud services or DT platforms such as AWS, Azure, GCP, AWS IoT TwinMaker, Azure Digital Twins, Eclipse Ditto, FIWARE, ThingWorx, MindSphere, or Predix.

**Communication Protocols:** Protocols and standards used for component communication, such as MQTT, Modbus, WebSocket, HTTP, OPC UA, AMQP, DDS, CoAP, CAN bus, EtherCAT, PROFINET, RS-485, I2C, SPI, UART, Bluetooth LE, Zigbee, LoRaWAN, or NB-IoT.

**Integration Patterns:** Data movement and integration styles such as streaming, batch, event-driven integration, API-based integration, file-based integration, message queues, webhooks, ETL pipelines, and change data capture.

**Data Representation:** Data formats and modeling representations such as JSON, XML, YAML, CSV, HDF5, Parquet, Protocol Buffers, Avro, JSON-LD, RDF, OWL, DTDL, and AutomationML.

**OPC UA:** Open Platform Communications Unified Architecture, an industrial interoperability standard.

**IEC 62541:** The IEC standard series for OPC UA. In the model, selecting `IEC_62541` requires selecting `OPC_UA`.
