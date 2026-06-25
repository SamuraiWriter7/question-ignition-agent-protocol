# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based versioning flow during early protocol development.

---

## [v0.5.0-candidate] - 2026-06-25

### Added

* Added the **Re-Ignition Policy** as the final decision layer of the first architecture arc.
* Added JSON Schema for the v0.5 layer:

```text
schemas/re-ignition-policy.schema.json
```

* Added example YAML configuration for the v0.5 layer:

```text
examples/re-ignition-policy.example.yaml
```

* Updated validation script to validate v0.1, v0.2, v0.3, v0.4, and v0.5 examples:

```text
scripts/validate_examples.py
```

* Updated `README.md` to describe:

  * v0.5 Re-Ignition Policy
  * re-ignition decision types
  * policy responsibilities
  * engine position
  * re-ignition output structure
  * first architecture arc completion
  * updated repository structure
  * updated design principle

### Re-Ignition Decision Types

v0.5 introduces the following decision types:

```text
conclude
hold
request_human_review
return_to_counter_question
return_to_self_dialogue
continue_to_compression
reignite_with_refined_question
stop_cycle
```

### Policy Responsibilities

The Re-Ignition Policy is responsible for:

* determining whether the current cycle has reached a conclusion
* detecting whether evidence is still missing
* detecting whether unresolved contradictions remain
* deciding whether to return to an earlier layer
* deciding whether human review is required
* generating a refined next question
* preventing endless re-ignition loops
* preserving traceability across cycles

### Output Structure

Each re-ignition decision may include:

* decision
* reason
* source_layer
* next_layer
* refined_question
* requires_human_review
* cycle_status
* trace_link

### Decision Policy

After running the Re-Ignition Policy, the engine may decide:

```text
conclude
hold
request_human_review
return_to_counter_question
return_to_self_dialogue
reignite_with_refined_question
stop_cycle
```

### First Architecture Arc

v0.5 completes the first architecture arc:

```text
v0.1 — Engine Configuration
v0.2 — Counter-Question Layer
v0.3 — Self-Dialogue Loop
v0.4 — Verification Governor
v0.5 — Re-Ignition Policy
```

This means the engine now has:

* ignition
* premise testing
* hypothesis development
* verification
* compression handoff
* final stop / hold / return / re-ignition control

### Purpose

v0.5 prevents the engine from continuing simply because continuation is possible.

Re-ignition is allowed only when the previous reasoning cycle has passed through verification, compression, trace preservation, and loop control.

### Design Principle

```text
The engine should not continue because it can.
It should continue only when the previous cycle produces a valid next ignition.
A reasoning engine is autonomous only if it can stop, hold, return, or re-ignite with control.
```

### Status

* Status: `v0.5.0-candidate`
* Stability: experimental
* Scope: Re-Ignition Policy / first architecture arc completion
* Validation: JSON Schema + YAML example validation

---

## [v0.4.0-candidate] - 2026-06-25

### Added

* Added the **Verification Governor** as an independent reasoning control layer.
* Added JSON Schema for the v0.4 layer:

```text
schemas/verification-governor.schema.json
```

* Added example YAML configuration for the v0.4 layer:

```text
examples/verification-governor.example.yaml
```

* Updated validation script to validate v0.1, v0.2, v0.3, and v0.4 examples:

```text
scripts/validate_examples.py
```

* Updated `README.md` to describe:

  * v0.4 Verification Governor
  * verification types
  * governor responsibilities
  * engine position
  * verification finding output structure
  * decision policy
  * updated repository structure
  * updated roadmap
  * updated design principle

### Verification Types

v0.4 introduces the following verification types:

```text
evidence_check
contradiction_check
scope_check
unsupported_inference_check
loop_check
confidence_check
human_review_check
```

### Governor Responsibilities

The Verification Governor is responsible for:

* checking whether hypotheses are supported by evidence
* detecting contradictions between reasoning branches
* detecting unsupported inference
* checking whether the reasoning scope has been exceeded
* detecting repeated loops
* reducing overconfidence
* determining whether human review is required
* preparing verified material for compression

### Purpose

v0.4 prevents hypotheses generated through self-dialogue from becoming overconfident conclusions before verification.

### Design Principle

```text
A hypothesis should not become a conclusion before verification.
The governor prevents reasoning combustion from becoming runaway certainty.
```

### Status

* Status: `v0.4.0-candidate`
* Stability: experimental
* Scope: Verification Governor
* Validation: JSON Schema + YAML example validation

---

## [v0.3.0-candidate] - 2026-06-25

### Added

* Added the **Self-Dialogue Loop** as an independent reasoning layer.
* Added JSON Schema for the v0.3 layer:

```text
schemas/self-dialogue-loop.schema.json
```

* Added example YAML configuration for the v0.3 layer:

```text
examples/self-dialogue-loop.example.yaml
```

* Updated validation script to validate v0.1, v0.2, and v0.3 examples:

```text
scripts/validate_examples.py
```

### Self-Dialogue Modes

v0.3 introduces the following self-dialogue modes:

```text
hypothesis_generation
hypothesis_testing
alternative_comparison
contradiction_probe
assumption_review
branch_selection
summary_preparation
```

### Purpose

v0.3 prevents internal reasoning from becoming uncontrolled monologue.

Self-dialogue is treated as a structured hypothesis-development loop, not as final confirmation.

### Design Principle

```text
A premise should be tested before internal reasoning begins.
Self-dialogue should grow hypotheses without becoming self-hypnosis.
```

### Status

* Status: `v0.3.0-candidate`
* Stability: experimental
* Scope: Self-Dialogue Loop
* Validation: JSON Schema + YAML example validation

---

## [v0.2.0-candidate] - 2026-06-25

### Added

* Added the **Counter-Question Layer** as an independent reasoning layer.
* Added JSON Schema for the v0.2 layer:

```text
schemas/counter-question-layer.schema.json
```

* Added example YAML configuration for the v0.2 layer:

```text
examples/counter-question-layer.example.yaml
```

* Updated validation script to validate both v0.1 and v0.2 examples:

```text
scripts/validate_examples.py
```

### Counter-Question Types

v0.2 introduces the following counter-question types:

```text
premise_check
definition_check
scope_check
evidence_check
perspective_shift
risk_check
human_intent_check
```

### Purpose

v0.2 prevents the engine from accelerating into self-dialogue before the premise of the question has been tested.

A counter-question is not a rejection of the original question.

It is the clutch between ignition and acceleration.

### Status

* Status: `v0.2.0-candidate`
* Stability: experimental
* Scope: Counter-Question Layer
* Validation: JSON Schema + YAML example validation

---

## [v0.1.0-candidate] - 2026-06-25

### Added

* Added initial `README.md` for the Question-Ignition Autonomous Engine.
* Defined the core concept of treating a question as an ignition device rather than endless fuel.
* Defined the controlled reasoning cycle:

```text
Question → Counter-Question → Self-Dialogue → Derived Questions → Verification → Conclude or Re-Ignite
```

* Added the initial engine layer structure:

  * Ignition Layer
  * Decomposition Layer
  * Counter-Question Layer
  * Self-Dialogue Layer
  * Expansion Layer
  * Verification Layer
  * Compression Layer
  * Stop / Re-Ignition Gate

* Added initial control policy:

  * maximum reasoning depth
  * maximum questions per cycle
  * evidence requirement
  * contradiction check
  * human review gate
  * fixed cost budget
  * stop conditions

* Added semantic definitions for:

  * counter-questioning
  * self-dialogue
  * verification
  * compression

* Added multi-model design for:

  * small model responsibilities
  * medium model responsibilities
  * large model responsibilities

* Added output contract for reasoning cycle traces:

  * initial question
  * decomposed questions
  * counter-questions
  * self-dialogue trace
  * derived questions
  * verification result
  * compression summary
  * final decision

* Added JSON Schema:

```text
schemas/question-ignition-engine-config.schema.json
```

* Added example YAML configuration:

```text
examples/question-ignition-autonomous-engine.example.yaml
```

* Added validation script:

```text
scripts/validate_examples.py
```

* Added GitHub Actions workflow:

```text
.github/workflows/validate.yml
```

### Purpose

This first candidate defines the minimum viable configuration for a controlled, question-driven autonomous reasoning engine.

The engine is designed to:

* ignite reasoning from an initial question
* destabilize assumptions through counter-questioning
* develop hypotheses through self-dialogue
* generate derived questions
* verify evidence, contradictions, and reasoning leaps
* compress expanded reasoning back into usable structure
* decide whether to conclude, hold, request human review, or re-ignite

### Design Principle

```text
A question should ignite reasoning.
Reasoning should circulate.
Circulation should be verified.
Verification should compress.
Compression should decide.
The engine should stop, hold, or re-ignite.
```

### Status

* Status: `v0.1.0-candidate`
* Stability: experimental
* Scope: initial engine configuration
* Validation: JSON Schema + YAML example validation
