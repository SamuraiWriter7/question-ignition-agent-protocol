# Question-Ignition Autonomous Engine

**問い発火型自律推論エンジン**

A controlled reasoning engine that treats a question as an ignition device, not as endless fuel.

問い発火型自律推論エンジンは、問いを無限燃料ではなく「発火装置」として扱い、反問・自問自答・派生問い・検証・圧縮・停止条件によって、推論を安全に循環させるためのエージェント構造です。

---

## Concept

通常のエージェントは、タスクを起点に動きます。

```text
Goal → Plan → Execute → Complete
```

問い発火型自律推論エンジンは、問いを起点に動きます。

```text
Question → Counter-Question → Self-Dialogue → Derived Questions → Verification → Conclude or Re-Ignite
```

このエンジンの目的は、AIを「勝手に考え続ける存在」にすることではありません。

目的は、問いを発火点として推論を起動し、検証・圧縮・停止条件によって暴走を防ぎながら、必要に応じて再発火できる制御付き推論サイクルを定義することです。

---

## Core Idea

```text
問い = 点火プラグ
反問 = 前提の圧縮
自問自答 = 仮説の燃焼
派生問い = 推論の展開
検証 = 調速機
圧縮 = 冷却・要約
停止条件 = ブレーキ
再発火 = 次サイクル
```

問いは燃料ではありません。
問いは、眠っている推論系に火花を飛ばす点火装置です。

---

## Reasoning Cycle

```text
問い
  ↓
反問
  ↓
自問自答
  ↓
派生問い
  ↓
検証
  ↓
収束または再発火
```

この循環により、問いは単なる入力ではなく、推論を起動する構造的イベントとして扱われます。

---

## Layers

### 1. Ignition Layer

最初の問いを受け取る層です。

問いの内容、発火文脈、目的、スコープを記録します。

### 2. Decomposition Layer

問いを分解する層です。

複雑な問いを、扱いやすい小さな問いへ分割します。

### 3. Counter-Question Layer

反問を生成する層です。

問いの前提、定義、視点、隠れた条件を揺らします。

例：

```text
それは何を前提にしているのか？
その定義は妥当か？
別の角度ではどう見えるか？
```

### 4. Self-Dialogue Layer

自問自答によって仮説を育てる層です。

内部対話を通じて、可能性・反例・接続先を探索します。

例：

```text
仮にAならどうなる？
Bの場合は破綻するか？
Cと接続できるか？
```

### 5. Expansion Layer

派生問いを生成する層です。

最初の問いから生じた追加の問い、深掘りの方向、次の調査対象を整理します。

### 6. Verification Layer

根拠・矛盾・飛躍を検査する層です。

問いの展開が物語化・自己正当化・無限ループに陥っていないかを確認します。

### 7. Compression Layer

増えすぎた問いを圧縮する層です。

推論の枝を整理し、実用可能な構造へ戻します。

### 8. Stop / Re-Ignition Gate

停止・保留・再発火を判定する層です。

エンジンが止まるべきか、保留すべきか、人間確認を求めるべきか、次の問いとして再発火すべきかを決定します。

---

## Control Policy

問い発火型エンジンは、自律性と停止条件をセットで扱います。

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

自律型エージェントにおいて重要なのは、無限に動くことではありません。

**止まれること**です。

止まれないエージェントは、自律ではなく暴走です。

---

## Output Contract

各推論サイクルは、最低限以下の出力を持つべきです。

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

これにより、エンジンがどの問いを受け取り、どのように反問し、自問自答し、検証し、圧縮し、停止または再発火したかを追跡できます。

---

## Example Configuration

```yaml
engine_id: question-ignition-autonomous-engine-v0.1
name: 問い発火型自律推論エンジン
description: >
  問いを発火装置とし、反問・自問自答・派生問い・検証・圧縮・停止条件によって
  推論を安全に循環させる制御付き推論エンジン。

cycle:
  phases:
    - 問い
    - 反問
    - 自問自答
    - 派生問い
    - 検証
    - 収束または再発火

layers:
  - id: ignition
    name: Ignition Layer
    role: 最初の問いを受け取る

  - id: decomposition
    name: Decomposition Layer
    role: 問いを分解する

  - id: counter_question
    name: Counter-Question Layer
    role: 反問を生成し、前提を揺らす

  - id: self_dialogue
    name: Self-Dialogue Layer
    role: 自問自答で仮説を育てる

  - id: expansion
    name: Expansion Layer
    role: 派生問いを生成する

  - id: verification
    name: Verification Layer
    role: 根拠・矛盾・飛躍を検査する

  - id: compression
    name: Compression Layer
    role: 増えすぎた問いを圧縮し、使える構造に戻す

  - id: stop_or_reignite
    name: Stop / Re-Ignition Gate
    role: 停止・保留・再発火を判定する

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

semantics:
  counter_question:
    description: 外部から来た問いの前提を問い返す
    examples:
      - "それは何を前提にしているのか？"
      - "その定義は妥当か？"
      - "別の角度ではどう見えるか？"

  self_dialogue:
    description: 内部で仮説を育てる
    examples:
      - "仮にAならどうなる？"
      - "Bの場合は破綻するか？"
      - "Cと接続できるか？"

  roles:
    - name: 反問
      function: 前提を揺らす
    - name: 自問自答
      function: 内部で展開する
    - name: 検証
      function: 暴走を止める
    - name: 圧縮
      function: 使える構造に戻す

multi_model_design:
  small_model:
    responsibilities:
      - 問いの分解
      - 派生問い生成
      - 反問
      - ループ検知
      - 圧縮

  medium_model:
    responsibilities:
      - 仮説整理
      - 矛盾検査
      - 構造化

  large_model:
    responsibilities:
      - 高難度統合
      - 最終判断
      - 重要局面のみ起動

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

naming:
  primary_name: 問い発火型自律推論エンジン
  english_name: Question-Ignition Autonomous Engine
  aliases:
    - Question Engine Protocol
    - Autonomous Inquiry Engine
    - Reasoning Combustion Engine
    - Kazene Question Ignition OS
```

---

## Multi-Model Design

このエンジンは、巨大モデルを常時起動する設計ではありません。

小型・中型・大型モデルを役割分担させることで、省エネ型の推論リレー構造を実現します。

### Small Model

```text
問いの分解
派生問い生成
反問
ループ検知
圧縮
```

### Medium Model

```text
仮説整理
矛盾検査
構造化
```

### Large Model

```text
高難度統合
最終判断
重要局面のみ起動
```

これは、空母と艦載機群のような構造です。

常に巨大な推論母艦を動かすのではなく、問いが発火したときだけ必要な翼を起動します。

---

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── configs/
│   └── question-ignition-autonomous-engine.v0.1.yaml
├── schemas/
│   └── question-ignition-engine-config.schema.json
├── examples/
│   └── question-ignition-autonomous-engine.example.yaml
├── scripts/
│   └── validate_examples.py
└── .github/
    └── workflows/
        └── validate.yml
```

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
* alternative viewpoint generation

### v0.3 — Self-Dialogue Loop

Define structured self-dialogue.

* internal question-answer pairs
* hypothesis growth
* contradiction discovery
* branch control

### v0.4 — Verification Governor

Define the verification and anti-runaway governor.

* contradiction checks
* evidence requirements
* scope checks
* loop detection
* hallucination risk control

### v0.5 — Re-Ignition Policy

Define when the engine should stop, hold, request human review, or re-ignite.

* stop rules
* hold conditions
* re-ignition criteria
* human review gate
* cost-aware reasoning control

---

## Position in the Larger Architecture

Question-Ignition Autonomous Engine can act as the starter system for a broader reasoning architecture.

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
Reasoning should circulate.
Circulation should be verified.
Verification should compress.
Compression should decide.
The engine should stop, hold, or re-ignite.
```

問いは推論を起動する。
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

This project is currently at **v0.1-candidate**.

The first milestone defines the engine configuration for a controlled, question-driven autonomous reasoning system.
