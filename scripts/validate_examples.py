#!/usr/bin/env python3
"""
Validate example YAML files against their JSON Schemas.

This script currently validates:

* Question-Ignition Autonomous Engine configuration
  schema : schemas/question-ignition-engine-config.schema.json
  example: examples/question-ignition-autonomous-engine.example.yaml
"""

from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Question-Ignition Autonomous Engine Configuration",
        "schema": ROOT / "schemas" / "question-ignition-engine-config.schema.json",
        "example": ROOT / "examples" / "question-ignition-autonomous-engine.example.yaml",
    }
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


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

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))

    if errors:
        print(f"[error] {name} validation failed", file=sys.stderr)
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            print(f"  - path: {path}", file=sys.stderr)
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
