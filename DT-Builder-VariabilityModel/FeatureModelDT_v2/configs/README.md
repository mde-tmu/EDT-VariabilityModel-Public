# Complete FeatureIDE configuration

This configuration targets `FeatureModelDT_v2/model.xml`.

- `smart_warehouse.xml`: 90 selected features; supervised software command
  coupling to the edge controller, including `Digital_Twin`, `Command_Control` and
  `Human_Supervised`.

It uses a single-board edge computer, MQTT as the only communication protocol,
mixed high-/low-level interfaces, local networking plus cloud history,
streaming/API integration, and dashboard/web-app choices. It is a constructed
engineering example, not an implemented system or evidence of usefulness/safety.

All 339 feature states are explicit manual selected/unselected values. FeatureIDE
3.12.0 XMLConfFormat writes and re-imports the file, and ConfigurationAnalyzer
checks completeness and validity. Entries that the requirements leave open use
deterministic deselection-preferred completion, not ranking.
