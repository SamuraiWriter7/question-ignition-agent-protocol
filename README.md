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
Question → Counter-Question → Self-Dialogue → Derived Questions → Verification → Compression → Stop or Re-Ignite
```

The purpose of this engine is not to create an agent that thinks endlessly.

The purpose is to define a controlled reasoning cycle that starts from a question, tests its premises, develops hypotheses, verifies reasoning, compresses the result, and decides whether to stop, hold, request human review, return to an earlier layer, or re-ignite with a refined question.

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
Re-ignition = next controlled cycle
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
Compression
  ↓
Stop / Hold / Return / Re-Ignite
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

### 6. Verification Governor

Verifies hypotheses, checks evidence, detects contradictions, identifies unsupported inference, and prevents self-dialogue from becoming overconfident conclusion.

The Verification Governor is not a simple fact-checking layer.

It is a reasoning control mechanism that asks:

```text
Is this hypothesis supported?
What evidence is missing?
Does this contradict another branch?
Is the reasoning scope still valid?
Has the loop repeated itself?
Is the engine becoming overconfident?
Should the cycle continue, hold, compress, return, or request human review?
```

### 7. Compression Layer

Compresses excessive question branches back into usable structure.

This layer turns expanded and verified reasoning into a summary, decision, or refined question.

### 8. Re-Ignition Policy

Determines whether the engine should conclude, hold, request human review, return to an earlier layer, stop, or re-ignite as a refined question.

Re-ignition is not endless continuation.

It is a controlled decision that allows the engine to start a new reasoning cycle only when the previous cycle has produced a valid reason to continue.

The Re-Ignition Policy asks:

```text
Has the current question been answered sufficiently?
Is evidence still missing?
Did verification detect unresolved contradiction?
Should the engine return to counter-questioning?
Should the engine return to self-dialogue?
Should human review be requested?
Can the result be compressed into a refined next question?
Should the cycle stop?
```

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

### v0.3 Files

```text
schemas/self-dialogue-loop.schema.json
examples/self-dialogue-loop.example.yaml
```

---

## v0.4 — Verification Governor

v0.4 defines the **Verification Governor** as an independent control layer.

The Verification Governor checks whether hypotheses generated through self-dialogue and expansion are supported, internally consistent, scoped correctly, and safe to compress into a usable result.

A hypothesis should not become a conclusion before verification.

### Verification Types

```text
evidence_check
contradiction_check
scope_check
unsupported_inference_check
loop_check
confidence_check
human_review_check
```

### v0.4 Files

```text
schemas/verification-governor.schema.json
examples/verification-governor.example.yaml
```

---

## v0.5 — Re-Ignition Policy

v0.5 defines the **Re-Ignition Policy** as the final decision layer of the first architecture arc.

This layer decides whether a reasoning cycle should conclude, hold, request human review, return to an earlier layer, stop, or re-ignite as a refined question.

Re-ignition is allowed only after verification, compression, trace preservation, and loop control.

### Re-Ignition Decision Types

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

### Responsibilities

The Re-Ignition Policy is responsible for:

* determining whether the current cycle has reached a conclusion
* detecting whether evidence is still missing
* detecting whether unresolved contradictions remain
* deciding whether to return to an earlier layer
* deciding whether human review is required
* generating a refined next question
* preventing endless re-ignition loops
* preserving traceability across cycles

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
Verification Governor
  ↓
Compression
  ↓
Re-Ignition Policy
```

Only verified and compressed reasoning should be allowed to become the next ignition point.

### Re-Ignition Output

Each re-ignition decision should include:

* decision
* reason
* source_layer
* next_layer
* refined_question
* requires_human_review
* cycle_status
* trace_link

### v0.5 Files

```text
schemas/re-ignition-policy.schema.json
examples/re-ignition-policy.example.yaml
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
│   ├── self-dialogue-loop.schema.json
│   ├── verification-governor.schema.json
│   └── re-ignition-policy.schema.json
├── examples/
│   ├── question-ignition-autonomous-engine.example.yaml
│   ├── counter-question-layer.example.yaml
│   ├── self-dialogue-loop.example.yaml
│   ├── verification-governor.example.yaml
│   └── re-ignition-policy.example.yaml
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
v0.4 — Verification Governor
v0.5 — Re-Ignition Policy
```

GitHub Actions also runs validation on push, pull request, and manual workflow dispatch.

---

## First Architecture Arc

The first architecture arc is complete at v0.5.

```text
v0.1 — Engine Configuration
  Question ignition engine configuration

v0.2 — Counter-Question Layer
  Premise-testing clutch

v0.3 — Self-Dialogue Loop
  Hypothesis combustion chamber

v0.4 — Verification Governor
  Anti-runaway reasoning governor

v0.5 — Re-Ignition Policy
  Final stop / hold / return / re-ignition gate
```

---

## Version Roadmap

### v0.1 — Engine Configuration

Define the basic configuration of the Question-Ignition Autonomous Engine.

### v0.2 — Counter-Question Layer

Define counter-question generation as an independent premise-testing layer.

### v0.3 — Self-Dialogue Loop

Define structured self-dialogue for hypothesis development.

### v0.4 — Verification Governor

Define verification and anti-runaway controls.

### v0.5 — Re-Ignition Policy

Define when the engine should stop, hold, request human review, return, or re-ignite.

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
A hypothesis should not become a conclusion before verification.
The engine should not continue because it can.
It should continue only when the previous cycle produces a valid next ignition.
Reasoning should circulate.
Circulation should be verified.
Verification should compress.
Compression should decide.
The engine should stop, hold, return, or re-ignite.
```

問いは推論を起動する。
前提は加速前に検査される。
自問自答は仮説を育てるが、自己催眠になってはならない。
仮説は検証される前に結論になってはならない。
エンジンは「続けられるから続ける」のではない。
前のサイクルが有効な次の発火点を生んだときだけ続ける。
推論は循環する。
循環は検証される。
検証は圧縮される。
圧縮は判断を生む。
エンジンは停止・保留・戻り・再発火を選ぶ。

---

## License

TBD.

---

## Status

This project is currently at **v0.5.0-candidate**.

The current milestone completes the first architecture arc of the Question-Ignition Autonomous Engine by defining the Re-Ignition Policy as the final stop, hold, return, human-review, and controlled re-ignition gate.

