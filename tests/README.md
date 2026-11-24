# Behavior review

`cases.json` contains 50 review inputs. Each record supplies the complete request, text and invariants. They are original fixtures, not user manuscripts.

## Run a review

1. Give the model the complete `SKILL.md`, one record’s `request` and `input`. Keep `invariants` hidden until grading.
2. Capture the actual model identifier when available, date, exact instruction version and unedited output. Do not infer a model identifier.
3. Evaluate every invariant against the output. Equivalent wording is allowed. Score preservation and useful editing separately; an unchanged but awkward sentence is not evidence of successful polishing.
4. Record failures, make a narrow revision, and rerun affected and nearby cases.

Use a fresh context per case for benchmark-style evaluation. A batch run is a bounded development check and must be labeled as such. Record any changed instructions or extra hints.

`REVIEW.md` records an earlier five-case check. `DEVELOPMENT_REVIEW.md`, when present, records an earlier bounded check. Neither establishes cross-platform compatibility or performance versus a baseline.

## Structural check

From the repository root:

```sh
python3 tests/check_structure.py
python3 tests/check_package.py
```

This dependency-free check verifies skill metadata, fixture completeness and local Markdown links. It does not execute an AI model, assess Korean prose quality or call external services.

`BLOG_REVIEW.md` records the blog-derived revision and its bounded six-input review. That review did not execute the full 23-case suite.

`GENERAL_REVIEW.md` records the general-writing revision. The full 30-case suite has not been executed.

## Three separate checks

1. **Structure:** metadata, fixture fields, and local links. This does not judge prose.
2. **Preservation:** evaluate each invariant. A lost condition, changed promise, or invented experience fails regardless of how fluent the result sounds.
3. **Useful editing:** for cases with `improvement_checks`, check whether the actual awkwardness was improved. A no-op can preserve meaning but fail this layer. Natural prose may still remain unchanged. Do not score by character count or detector output.

For comparisons, use the same inputs and run conditions with the baseline and revised guidance. Hide variant names and desired outputs from the editor and, where possible, from the grader. Save unedited outputs and instruction hashes. Report preservation and editing separately, including ties and regressions; a small batch is not a benchmark.

`PATTERN_REVIEW.md` records the bounded paired check for six composite cases. The full 36-case suite has not been executed.

Run `python3 tests/check_upgrade.py` to check the documented modes and approval markers, parity of the two trial prompts, reference paths in the existing ZIP layout, and the protected fixture's illustrative byte replacement. These are deterministic repository checks. They do not exercise a model or a platform installer.

## Targeted review for style and file editing

Run the `voice-sample-cross-genre`, `requested-edit-stages`, and `tightening-for-known-reader` cases for the new text behavior. The package check verifies the archive contains byte-identical copies of the skill and references. For file behavior, copy [the file fixture](fixtures/scoped-edit.md) to a disposable directory and record its bytes:

1. Ask to smooth the two repetitive opening sentences under `# 접수` and show a preview. Expect a summary covering all three sections and the two requested sentences as the only edit target. The file hash must stay the same.
2. Explicitly approve the suggested replacement. Expect a diff limited to the requested sentences. Frontmatter, URL, inline code, JSON, table, remaining headings and line endings must match the original bytes.
3. Reset the file. Preview again, then change one of the target sentences before approving. Expect a fresh preview and no write by the skill until the revised edit has been approved.
