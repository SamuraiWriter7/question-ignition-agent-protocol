# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based versioning flow during early protocol development.

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

### Output Structure

Each verification finding may include:

* finding
* type
* target
* severity
* evidence_status
* contradiction_detected
* recommended_action

### Decision Policy

After running the Verification Governor, the layer may decide:

```text
continue_to_compression
hold_for_evidence
return_to_self_dialogue
return_to_counter_question
request_human_review
stop_cycle
```

### Purpose

v0.4 prevents hypotheses generated through self-dialogue from becoming overconfident conclusions before verification.

The Verification Governor is not only a fact-checking layer.
It is a reasoning control mechanism that checks evidence, contradiction, scope, unsupported inference, repetition, confidence, and human review conditions.

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

* Updated `README.md` to describe:

  * v0.3 Self-Dialogue Loop
  * self-dialogue modes
  * loop responsibilities
  * engine position
  * dialogue turn output structure
  * decision policy
  * updated repository structure
  * updated roadmap
  * updated design principle

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

### Loop Responsibilities

The Self-Dialogue Loop is responsible for:

* generating candidate hypotheses
* testing hypotheses through internal question-answer pairs
* comparing alternative interpretations
* probing for contradictions
* reviewing remaining assumptions
* selecting useful reasoning branches
* preparing a traceable summary for downstream verification

### Output Structure

Each self-dialogue turn may include:

* prompt_question
* internal_answer
* mode
* hypothesis
* confidence
* contradiction_found
* next_action

### Decision Policy

After running the self-dialogue loop, the layer may decide:

```text
continue_to_expansion
hold_for_verification
request_human_review
return_to_counter_question
```

### Purpose

v0.3 prevents internal reasoning from becoming uncontrolled monologue.

Self-dialogue is treated as a structured hypothesis-development loop, not as final confirmation.

It allows the engine to grow hypotheses while preserving assumptions, contradiction findings, confidence levels, and next actions in a traceable form.

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

* Updated `README.md` to describe:

  * v0.2 Counter-Question Layer
  * counter-question types
  * layer responsibilities
  * engine position
  * output format
  * decision policy
  * updated repository structure
  * updated roadmap

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

### Layer Responsibilities

The Counter-Question Layer is responsible for:

* identifying hidden assumptions
* checking whether key terms are defined
* detecting scope ambiguity
* requesting missing evidence
* generating alternative viewpoints
* detecting reasoning risks
* determining whether human review is needed

### Output Structure

Each counter-question may include:

* question
* type
* target
* purpose
* priority
* requires_human_review

### Decision Policy

After generating counter-questions, the layer may decide:

```text
continue
hold
request_human_review
reignite_with_refined_question
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
