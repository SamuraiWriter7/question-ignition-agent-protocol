# Question-Ignition Autonomous Engine

**問い発火型自律推論エンジン**

A controlled reasoning engine that treats a question as an ignition device, not as endless fuel.

問い発火型自律推論エンジンは、問いを無限燃料ではなく「発火装置」として扱い、反問・自問自答・派生問い・検証・圧縮・停止条件によって、推論を安全に循環させるためのエージェント構造です。

---

## Concept

Conventional agents usually start from a task.

```text
Goal → Plan → Execute → Complete
```

The Question-Ignition Autonomous Engine starts from a question.

```text
Question → Counter-Question → Self-Dialogue → Derived Questions → Verification → Conclude or Re-Ignite
```

The purpose of this engine is not to create an agent that thinks endlessly.

The purpose is to define a controlled reasoning cycle that starts from a question, tests its premises, develops hypotheses, verifies reasoning, compresses the result, and decides whether to stop, hold, request human review, or re-ignite.

---

## Core Idea

```text
Question = ignition plug
Counter-question = premise compression
Self-dialogue = hypothesis combustion
Derived questions = reasoning expansion
Verification = governor
Compression = cooling and summarization
Stop conditions = brake
Re-ignition = next cycle
```

A question is not fuel.

A question is an ignition event that activates a reasoning system.

---

## Reasoning Cycle

```text
Question
  ↓
Counter-Question
  ↓
Self-Dialogue
  ↓
Derived Questions
  ↓
Verification
  ↓
Conclude or Re-Ignite
```

This cycle treats a question not as a simple input, but as a structural event that starts controlled inquiry.

---

## Engine Layers

### 1. Ignition Layer

Receives the initial question.

This layer records the question, ignition context, purpose, and reasoning scope.

### 2. Decomposition Layer

Decomposes the question into smaller reasoning units.

This prevents the engine from trying to solve an oversized question in one uncontrolled step.

### 3. Counter-Question Layer

Generates structured counter-questions before deeper self-dialogue begins.

This layer tests hidden assumptions, definitions, scope, evidence conditions, reasoning risks, and human intent.

Examples:

```text
What hidden assumption does this question rely on?
Are the key terms clearly defined?
Is the reasoning scope narrow enough for one cycle?
What evidence would be required to answer this safely?
How would this look from another perspective?
What risk appears if this question is answered too quickly?
Is the user's intent clear enough to continue?
```

### 4. Self-Dialogue Loop

Develops hypotheses through structured internal question-and-answer turns.

This layer does not produce final conclusions.
It grows, tests, compares, and summarizes hypotheses so that later layers can verify them.

Examples:

```text
What is the first plausible hypothesis after counter-questioning?
Does this hypothesis depend on an untested assumption?
What contradiction could weaken the current hypothesis?
What alternative interpretation should be compared?
Which reasoning branch should be selected for downstream expansion?
What summary should be passed to the next layer?
```

### 5. Expansion Layer

Generates derived questions from the initial inquiry.

This layer identifies deeper branches, follow-up questions, and possible next-cycle ignition points.

### 6. Verification Layer

Checks evidence, contradictions, and reasoning leaps.

This layer prevents narrative drift, overconfidence, unsupported conclusions, and repeated loops.

### 7. Compression Layer

Compresses excessive question branches back into usable structure.

This layer turns expanded reasoning into a summary, decision, or refined question.

### 8. Stop / Re-Ignition Gate

Determines whether the engine should stop, hold, request human review, or re-ignite the reasoning cycle.

---

## v0.1 — Engine Configuration

v0.1 defines the minimum viable configuration of the Question-Ignition Autonomous Engine.

It includes:

* reasoning cycle
* engine layers
* control policy
* semantics
* multi-model responsibilities
* output contract
* naming metadata

### v0.1 Files

```text
schemas/question-ignition-engine-config.schema.json
examples/question-ignition-autonomous-engine.example.yaml
```

---

## v0.2 — Counter-Question Layer

v0.2 defines the **Counter-Question Layer** as an independent reasoning layer.

A counter-question is not a rejection of the original question.

It is a controlled reasoning operation that tests whether the engine should proceed, hold, ask for human review, or re-ignite with a refined question.

### Counter-Question Types

```text
premise_check
definition_check
scope_check
evidence_check
perspective_shift
risk_check
human_intent_check
```

### Responsibilities

The Counter-Question Layer is responsible for:

* identifying hidden assumptions
* checking whether key terms are defined
* detecting scope ambiguity
* requesting missing evidence
* generating alternative viewpoints
* detecting reasoning risks
* determining whether human review is needed

### Position in the Engine

```text
Question
  ↓
Decomposition
  ↓
Counter-Question Layer
  ↓
Self-Dialogue Loop
  ↓
Derived Questions
  ↓
Verification
  ↓
Compression
  ↓
Stop / Re-Ignition
```

The layer sits before self-dialogue because the engine should not begin developing internal hypotheses before testing the premise of the initial question.

### Counter-Question Output

Each counter-question should include:

* question
* type
* target
* purpose
* priority
* requires_human_review

### Layer Decision

After generating counter-questions, the layer may decide:

```text
continue
hold
request_human_review
reignite_with_refined_question
```

### v0.2 Files

```text
schemas/counter-question-layer.schema.json
examples/counter-question-layer.example.yaml
```

---

## v0.3 — Self-Dialogue Loop

v0.3 defines the **Self-Dialogue Loop** as an independent reasoning layer.

Self-dialogue is not free-form monologue.
It is a controlled internal reasoning loop that develops hypotheses through structured question-and-answer turns after the original question has passed through counter-questioning.

### Self-Dialogue Modes

```text
hypothesis_generation
hypothesis_testing
alternative_comparison
contradiction_probe
assumption_review
branch_selection
summary_preparation
```

### Responsibilities

The Self-Dialogue Loop is responsible for:

* generating candidate hypotheses
* testing hypotheses through internal question-answer pairs
* comparing alternative interpretations
* probing for contradictions
* reviewing remaining assumptions
* selecting useful reasoning branches
* preparing a traceable summary for downstream verification

### Position in the Engine

```text
Question
  ↓
Decomposition
  ↓
Counter-Question Layer
  ↓
Self-Dialogue Loop
  ↓
Expansion
  ↓
Verification
  ↓
Compression
  ↓
Stop / Re-Ignition
```

The Self-Dialogue Loop begins only after the question has passed through counter-questioning.

This prevents the engine from developing hypotheses too early, before premises, definitions, scope, evidence conditions, and risks have been tested.

### Self-Dialogue Output

Each self-dialogue turn should include:

* prompt_question
* internal_answer
* mode
* hypothesis
* confidence
* contradiction_found
* next_action

### Layer Decision

After running the self-dialogue loop, the layer may decide:

```text
continue_to_expansion
hold_for_verification
request_human_review
return_to_counter_question
```

### v0.3 Files

```text
schemas/self-dialogue-loop.schema.json
examples/self-dialogue-loop.example.yaml
```

---

## Control Policy

The engine treats autonomy and stopping conditions as one design unit.

```yaml
control:
  max_depth: 5
  max_questions_per_cycle: 7
  evidence_required: true
  contradiction_check: true
  human_review_gate: true
  cost_budget: fixed
  stop_when:
    - conclusion_reached
    - contradiction_detected
    - evidence_missing
    - loop_repeated
    - scope_exceeded
```

The important point is not that an autonomous agent can move forever.

The important point is that it can stop.

An agent that cannot stop is not autonomous. It is runaway reasoning.

---

## Output Contract

Each reasoning cycle should produce a trace.

```yaml
output_contract:
  required_outputs:
    - initial_question
    - decomposed_questions
    - counter_questions
    - self_dialogue_trace
    - derived_questions
    - verification_result
    - compression_summary
    - decision

  decision_status:
    - conclude
    - hold
    - reignite
    - human_review_required

  trace_required: true
```

This makes it possible to audit how the engine received a question, decomposed it, generated counter-questions, developed self-dialogue, verified reasoning, compressed the result, and made a decision.

---

## Multi-Model Design

The engine does not require a large model to run continuously.

It can distribute reasoning across small, medium, and large models.

### Small Model

```text
question_decomposition
derived_question_generation
counter_questioning
loop_detection
compression
```

### Medium Model

```text
hypothesis_organization
contradiction_checking
structural_formatting
```

### Large Model

```text
high_complexity_integration
final_judgment
activation_only_for_critical_reasoning
```

This creates an energy-efficient reasoning relay.

The small model handles lightweight branching and checks, the medium model organizes structure, and the large model is activated only when high-complexity integration is required.

---

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── schemas/
│   ├── question-ignition-engine-config.schema.json
│   ├── counter-question-layer.schema.json
│   └── self-dialogue-loop.schema.json
├── examples/
│   ├── question-ignition-autonomous-engine.example.yaml
│   ├── counter-question-layer.example.yaml
│   └── self-dialogue-loop.example.yaml
├── scripts/
│   └── validate_examples.py
└── .github/
    └── workflows/
        └── validate.yml
```

---

## Validation

Install dependencies:

```bash
pip install pyyaml jsonschema
```

Run validation:

```bash
python scripts/validate_examples.py
```

The validation script checks:

```text
v0.1 — Question-Ignition Autonomous Engine Configuration
v0.2 — Counter-Question Layer
v0.3 — Self-Dialogue Loop
```

GitHub Actions also runs validation on push, pull request, and manual workflow dispatch.

---

## Version Roadmap

### v0.1 — Engine Configuration

Define the basic configuration of the Question-Ignition Autonomous Engine.

* reasoning cycle
* layer structure
* control policy
* semantics
* multi-model responsibilities
* output contract

### v0.2 — Counter-Question Layer

Define counter-question generation as an independent layer.

* premise checking
* definition testing
* hidden assumption detection
* scope checks
* evidence checks
* risk checks
* human intent checks

### v0.3 — Self-Dialogue Loop

Define structured self-dialogue.

* internal question-answer pairs
* hypothesis growth
* contradiction discovery
* alternative comparison
* branch control
* traceable self-dialogue records

### v0.4 — Verification Governor

Define verification and anti-runaway controls.

* contradiction checks
* evidence requirements
* scope checks
* loop detection
* hallucination risk control
* unsupported inference detection

### v0.5 — Re-Ignition Policy

Define when the engine should stop, hold, request human review, or re-ignite.

* stop rules
* hold conditions
* re-ignition criteria
* human review gate
* cost-aware reasoning control

---

## Position in the Larger Architecture

The Question-Ignition Autonomous Engine can act as the starter system for a broader reasoning architecture.

```text
Question-Ignition Autonomous Engine
  ↓
Structural Rumination Layer
  ↓
Kazene Memory Breathing Protocol
  ↓
AI Search Trace Receipt Standard
  ↓
Synchronization Audit Protocol
  ↓
Carrier-Swarm / Energy-Efficient Reasoning Relay OS
```

In this architecture, the question is the ignition event.

The engine starts the reasoning cycle, the rumination layer digests errors, memory breathing manages retention and forgetting, trace receipts record references, synchronization audit checks origin and similarity, and the carrier-swarm structure activates only the necessary reasoning wings.

---

## Design Principle

```text
A question should ignite reasoning.
A premise should be tested before acceleration.
Self-dialogue should grow hypotheses without becoming self-hypnosis.
Reasoning should circulate.
Circulation should be verified.
Verification should compress.
Compression should decide.
The engine should stop, hold, or re-ignite.
```

問いは推論を起動する。
前提は加速前に検査される。
自問自答は仮説を育てるが、自己催眠になってはならない。
推論は循環する。
循環は検証される。
検証は圧縮される。
圧縮は判断を生む。
エンジンは停止・保留・再発火を選ぶ。

---

## License

TBD.

---

## Status

This project is currently at **v0.3.0-candidate**.

The current milestone defines the Self-Dialogue Loop as an independent reasoning layer for generating, testing, comparing, and summarizing hypotheses after counter-questioning and before downstream expansion and verification.
