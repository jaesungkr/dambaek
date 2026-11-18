# Behavior review

`cases.json` contains 16 runnable review inputs. Each record supplies the complete request, text and invariants. They are original fixtures, not user manuscripts.

## Run a review

1. Give the model the complete `SKILL.md`, one record’s `request` and `input`. Keep `invariants` hidden until grading.
2. Capture the actual model identifier when available, date, exact instruction version and unedited output. Do not infer a model identifier.
3. Evaluate every invariant against the output. Equivalent wording is allowed. Score preservation and useful editing separately; an unchanged but awkward sentence is not evidence of successful polishing.
4. Record failures, make a narrow revision, and rerun affected and nearby cases.

Use a fresh context per case for benchmark-style evaluation. A batch run is a bounded development check and must be labeled as such. Record any changed instructions or extra hints.

`REVIEW.md` records an earlier five-case check. `DEVELOPMENT_REVIEW.md`, when present, records the current bounded check. Neither establishes cross-platform compatibility or performance versus a baseline.

## Structural check

From the repository root:

```sh
python3 tests/check_structure.py
```

This dependency-free check verifies skill metadata, fixture completeness and local Markdown links. It does not execute an AI model, assess Korean prose quality or call external services.
