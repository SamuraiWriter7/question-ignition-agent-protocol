#!/usr/bin/env python3
"""
Validate example YAML files against their JSON Schemas.

This script currently validates:

* v0.1 Question-Ignition Autonomous Engine Configuration
  schema : schemas/question-ignition-engine-config.schema.json
  example: examples/question-ignition-autonomous-engine.example.yaml

* v0.2 Counter-Question Layer
  schema : schemas/counter-question-layer.schema.json
  example: examples/counter-question-layer.example.yaml

* v0.3 Self-Dialogue Loop
  schema : schemas/self-dialogue-loop.schema.json
  example: examples/self-dialogue-loop.example.yaml

* v0.4 Verification Governor
  schema : schemas/verification-governor.schema.json
  example: examples/verification-governor.example.yaml
"""

from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "v0.1 Question-Ignition Autonomous Engine Configuration",
        "schema": ROOT / "schemas" / "question-ignition-engine-config.schema.json",
        "example": ROOT / "examples" / "question-ignition-autonomous-engine.example.yaml",
    },
    {
        "name": "v0.2 Counter-Question Layer",
        "schema": ROOT / "schemas" / "counter-question-layer.schema.json",
        "example": ROOT / "examples" / "counter-question-layer.example.yaml",
    },
    {
        "name": "v0.3 Self-Dialogue Loop",
        "schema": ROOT / "schemas" / "self-dialogue-loop.schema.json",
        "example": ROOT / "examples" / "self-dialogue-loop.example.yaml",
    },
    {
        "name": "v0.4 Verification Governor",
        "schema": ROOT / "schemas" / "verification-governor.schema.json",
        "example": ROOT / "examples" / "verification-governor.example.yaml",
    },
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if data is None:
        raise ValueError(f"YAML file is empty: {path}")

    if not isinstance(data, dict):
        raise TypeError(f"YAML root must be an object: {path}")

    return data


def format_error_path(error) -> str:
    path = ".".join(str(part) for part in error.path)
    return path if path else "<root>"


def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    if not schema_path.exists():
        print(f"[error] Schema file not found: {schema_path}", file=sys.stderr)
        return False

    if not example_path.exists():
        print(f"[error] Example file not found: {example_path}", file=sys.stderr)
        return False

    try:
        schema = load_json(schema_path)
        example = load_yaml(example_path)
    except Exception as exc:
        print(f"[error] Failed to load validation target: {name}", file=sys.stderr)
        print(f"  - {exc}", file=sys.stderr)
        return False

    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.path),
    )

    if errors:
        print(f"[error] {name} validation failed", file=sys.stderr)
        for error in errors:
            print(f"  - path: {format_error_path(error)}", file=sys.stderr)
            print(f"    message: {error.message}", file=sys.stderr)
        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    all_valid = True

    for target in VALIDATION_TARGETS:
        is_valid = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
        all_valid = all_valid and is_valid

    if not all_valid:
        return 1

    print("[done] all examples are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

