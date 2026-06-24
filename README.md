# Feature Model Glossary (Digital Twin System)

**Digital Twin:** A virtual representation of a physical system that mirrors its behavior, state, and interactions, enabling monitoring, simulation, and control.

**Cyber-Physical System (CPS):** The physical hardware layer of the system that interacts with the digital twin through sensors, actuators, and computational units.

**Twinning System:** The virtual modelling and reasoning layer of the digital twin responsible for representing, simulating, and analyzing the CPS.

**Feature Model:** A structured representation of system variability that defines common and configurable features in a software product line.

**Feature:** A distinguishable characteristic or functionality of a system that can be included, excluded, or configured.

**Mandatory Feature:** A feature that must be included in every valid system configuration.

**Optional Feature:** A feature that may or may not be included depending on system requirements.

**OR-Group (Non-exclusive Choice):** A feature grouping where one or more features can be selected simultaneously.

**XOR-Group (Exclusive Choice):** A feature grouping where exactly one feature must be selected.

**Variability:** The ability of a system to support multiple configurations through selectable features.

---

**Security System:** A subsystem responsible for protecting data, users, and system operations within the digital twin environment.

**Encryption:** A method of securing data by converting it into an unreadable format without proper authorization.

**Anomaly Alerts:** A mechanism that detects and reports unusual or suspicious system behavior.

**Access Control:** A security mechanism that defines and enforces user permissions within the system.

**User Roles:** Defined categories of users with specific permissions based on responsibilities.

**Audit Logs:** A record of system and user activities used for traceability and forensic analysis.

---

**Connectivity System:** A subsystem that manages communication, data exchange, and integration between CPS and digital twin components.

**Network Storage:** The deployment environment that defines where the system is hosted and operated.

**Local Storage:** A deployment option where data and services are hosted within local infrastructure.

**Cloud Integration:** A deployment option using cloud platforms for scalability and remote access.

**Local Network:** A closed communication environment that may operate independently of the internet.

**In-House Server:** A locally managed server that can optionally be connected to external networks.

**Data Storage:** A mechanism for storing CPS or system data for processing and analysis.

**On-Board Storage:** Storage located directly on CPS hardware devices.

**Online Storage:** Cloud-based or external storage services used for data management.

**Communication Protocols:** Rules and standards that define how system components exchange data.

**HTTP:** A request-response protocol used for standard web communication.

**WebSocket:** A protocol enabling persistent, real-time bidirectional communication.

---

**User Interface (UI):** The layer that allows users to interact with the digital twin system.

**App:** A simplified interface designed for non-expert users for monitoring and control.

**Dashboard:** An advanced interface designed for experts with analytics, configuration, and control features.

**Android Platform:** A mobile operating system used for deploying applications.

**iOS Platform:** A mobile operating system used for deploying applications on Apple devices.

**Web Platform:** A browser-based platform for accessing the digital twin system.

**Logic Model Code:** Generated or manually written code derived from system models to implement behavior.

**Wrapper Code:** Supporting integration code required to deploy and connect system components.

---

**Computation Model:** The processing hardware architecture used within the CPS.

**Single Board Computer:** A compact computing system capable of running full operating systems.

**Single Board Controller:** A microcontroller-based system designed for simple control tasks.

**Microprocessor:** A processing unit used in custom embedded hardware systems.

**Emulator:** A virtual environment that simulates CPS hardware behavior.

**Industrial PLC:** A programmable logic controller used in industrial automation systems.

**System Type:** The architectural abstraction level of a CPS system (high-level or low-level design).

**High-Level System:** A black-box system accessed through APIs or protocols with limited hardware access.

**Low-Level System:** A system providing direct control over hardware components such as sensors and actuators.

**Sensors:** Devices that collect real-world physical data from the environment.

**Actuators:** Devices that perform physical actions based on system commands.

**Logic Model (CPS):** The control logic that governs CPS behavior and system interactions.

**Manual Code:** Handwritten software implementation of system logic.

**Generated Code:** Automatically generated code derived from models or AI systems.

**Model-to-Code Transformation:** A process in model-driven engineering that converts models into executable code.

**AI Models (LLMs):** Machine learning models used to generate or assist in software development tasks.

---

**Modelling Language:** A formal language used to represent system structure and behavior.

**Data (Model Level):** Datasets used to enhance the accuracy and realism of models.

**Code Generation (Model Level):** Automatic generation of executable artifacts from system models.

**Real-Time Sync:** Continuous synchronization between the CPS and its digital representation.

**Partial Data:** Selective exchange of data between physical and digital systems.

**Reasoning System:** A subsystem that analyzes CPS data to generate insights and decisions.

**Reasoning Model:** The algorithmic approach used for reasoning such as rule-based or AI-based methods.

**Data Processing:** The transformation and preparation of data for analysis.

**Optimization:** Techniques used to improve system performance and decision quality.

**Types of Reasoning:** Categories of analytical tasks such as anomaly detection, diagnostics, and predictive maintenance.

**Anomaly Detection:** The process of identifying abnormal behavior in system data.

**Predictive Maintenance:** A method for predicting failures before they occur.

**Diagnostics:** The process of identifying the cause of system issues.

**Simulation:** Virtual execution of system behavior without physical hardware.

**What-If Analysis:** Simulation of hypothetical scenarios to evaluate potential outcomes.

---

**Feedback Loop:** A mechanism where insights from the digital twin influence the physical system.

**Human-Actuated Feedback:** Feedback applied manually by human operators.

**Human-Supervised Feedback:** Automated feedback applied under human supervision.

**Autonomous Feedback:** Fully automated feedback applied without human intervention.

**Synchronization:** The process of keeping physical and digital states consistent.

**Bidirectional Flow:** Data exchange occurring in both directions between systems.

**One-Directional Flow:** Data flow from physical system to digital system only.
