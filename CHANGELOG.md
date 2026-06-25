# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based versioning flow during early protocol development.

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
