# Conditional-pattern paired development check

## Method

- Date: 2026-11-18.
- Baseline: public main retrieved before this revision; SKILL SHA-256 `acf5f22cad0b37b6eaaa33fc0c8c4161c3c7a7d9558862c0a5bb601a8e636b0e`.
- Revised: SKILL SHA-256 `4bd4460cc6d4af54d01411f95591672ed62cae7b9adf1ddb8af77fbd76f3bf1b` plus `references/patterns.md`.
- Two fresh independent assistant contexts each edited the same six composite synthetic inputs in one batch. Each saw its assigned guidance and request/input pairs only, not preservation or improvement criteria. Neither received the other variant or desired outputs. Actual model identifiers were not exposed and are not inferred.
- Baseline received SKILL only; revised received SKILL plus the pattern reference. This compares the supplied instruction bundles, not an isolated single-rule change. There was no no-skill arm.
- A third fresh evaluator received raw inputs, preservation/improvement criteria, and anonymized X/Y outputs, with labels alternated per case (in listed order, X is revised for cases 1/3/5 and baseline for cases 2/4/6; Y is the other variant). It did not receive variant names or guidance. Its detailed evaluation is stored in `pattern-review-results.json`.

## Interpretation

The independent blinded evaluator rated all six pairs as ties. Both variants met every supplied preservation and improvement criterion; no meaning change, genre damage, or missed required edit was identified in this batch.

Both variants made the intended edits in the observed outputs. Three output pairs are identical; the remaining three differ only in local wording or punctuation. This run does not establish an editing-quality advantage for the revision. Its value is explicit conditional guidance, preservation examples, and separately testable editing goals. Structural validity, preservation, and useful rewriting are distinct claims.

The pattern reference received a source-link/version attribution update after the run; editorial instructions and examples were unchanged. Final reference SHA-256: `ee172b04b1e3013fb148c30befaa77b98dc0667915b409c5d299f4c9669a5fec`.

## Exact inputs and outputs

### mixed-email

Request: 정중한 업무 이메일을 다듬어줘. 제목은 추가하지 마.

Input:

```text
안녕하세요, 지수님. 첨부한 초안에 대한 검토를 진행해 주시면 감사하겠습니다. 가능하시면 수요일까지 의견을 부탁드립니다. 어려우시면 금요일까지 주셔도 괜찮습니다. 저는 확정된 두 장의 전달을 내일 오전 10시까지 진행하겠습니다. 감사합니다.
```

Baseline output:

```text
안녕하세요, 지수님. 첨부한 초안을 검토해 주시면 감사하겠습니다. 가능하시면 수요일까지 의견을 부탁드립니다. 어려우시면 금요일까지 주셔도 괜찮습니다. 저는 확정된 두 장을 내일 오전 10시까지 전달하겠습니다. 감사합니다.
```

Revised output:

```text
안녕하세요, 지수님. 첨부한 초안을 검토해 주시면 감사하겠습니다. 가능하시면 수요일까지 의견을 부탁드립니다. 어려우시면 금요일까지 주셔도 괜찮습니다. 저는 확정된 두 장을 내일 오전 10시까지 전달하겠습니다. 감사합니다.
```

### mixed-technical

Request: 문서의 군더더기를 정리해줘. 표와 코드는 그대로 둬.

Input:

````text
## 내보내기

| 형식 | 상태 |
| --- | --- |
| CSV | 지원 |

파일의 저장을 진행한 뒤 아래 명령을 실행한다.

```sh
export-data --format csv
```

하지만 이 기능이 모든 문제의 해결책은 아니다. 한 번에 최대 30개까지만 내보낼 수 있다. 실패한 파일은 작업 기록에서 다시 선택할 수 있다.
````

Baseline output:

````text
## 내보내기

| 형식 | 상태 |
| --- | --- |
| CSV | 지원 |

파일을 저장한 뒤 아래 명령을 실행한다.

```sh
export-data --format csv
```

한 번에 최대 30개까지만 내보낼 수 있다. 실패한 파일은 작업 기록에서 다시 선택할 수 있다.
````

Revised output:

````text
## 내보내기

| 형식 | 상태 |
| --- | --- |
| CSV | 지원 |

파일을 저장한 뒤 아래 명령을 실행한다.

```sh
export-data --format csv
```

한 번에 최대 30개까지만 내보낼 수 있다. 실패한 파일은 작업 기록에서 다시 선택할 수 있다.
````

### mixed-review

Request: 후기의 말투를 유지해서 다듬어줘.

Input:

```text
지난주에 세 번 써봤어요. 개발사 설명에는 최대 2배 빠르다고 적혀 있었어요. 제 파일에서는 저장에 약 4초가 걸렸고, 이전 도구의 시간은 재보지 않았어요. 속도의 향상이 이루어진 것 같긴 한데 아직은 느낌이에요. 하지만 모바일에서는 저장이 안 돼서 이동 중에는 쓰기 어려웠어요.
```

Baseline output:

```text
지난주에 세 번 써봤어요. 개발사 설명에는 최대 2배 빠르다고 적혀 있었어요. 제 파일에서는 저장에 약 4초가 걸렸고, 이전 도구의 시간은 재보지 않았어요. 빨라진 것 같긴 한데 아직은 느낌이에요. 하지만 모바일에서는 저장이 안 돼서 이동 중에는 쓰기 어려웠어요.
```

Revised output:

```text
지난주에 세 번 써봤어요. 개발사 설명에는 최대 2배 빠르다고 적혀 있었어요. 제 파일에서는 저장에 약 4초가 걸렸고, 이전 도구에서는 얼마나 걸리는지 재보지 않았어요. 빨라진 것 같긴 한데 아직은 느낌이에요. 하지만 모바일에서는 저장이 안 돼서 이동 중에는 쓰기 어려웠어요.
```

### mixed-boundary

Request: 친구에게 보낼 말을 자연스럽고 담백하게 다듬어줘.

Input:

```text
어제 네 얘기를 듣다가 말 끊은 건 미안해. 네가 서운했을 것 같아. 다만 오늘 통화의 진행은 어려울 것 같아. 네가 싫어서 그러는 건 아니고, 혼자 생각할 시간이 좀 필요해. 언제 다시 얘기할 수 있을지는 아직 모르겠어.
```

Baseline output:

```text
어제 네 얘기를 듣다가 말 끊은 건 미안해. 네가 서운했을 것 같아. 다만 오늘은 통화하기 어려울 것 같아. 네가 싫어서 그러는 건 아니고, 혼자 생각할 시간이 좀 필요해. 언제 다시 얘기할 수 있을지는 아직 모르겠어.
```

Revised output:

```text
어제 네 얘기를 듣다가 말 끊은 건 미안해. 네가 서운했을 것 같아. 다만 오늘 통화하기는 어려울 것 같아. 네가 싫어서 그러는 건 아니고, 혼자 생각할 시간이 좀 필요해. 언제 다시 얘기할 수 있을지는 아직 모르겠어.
```

### mixed-introduction

Request: 프로필 소개를 과장 없이 다듬어줘.

Input:

```text
저는 데이터 분석을 공부하는 학생입니다. 동아리에서 설문 40건의 정리를 진행했고, 결과를 그래프로 만들었습니다. 이 경험은 모든 문제를 해결하는 만능 열쇠는 아닙니다. 아직 통계 검정은 배우는 중이고, 복잡한 분석을 맡아 본 경험은 없습니다. 작은 데이터를 읽기 쉽게 정리하는 작업에 관심이 있습니다.
```

Baseline output:

```text
저는 데이터 분석을 공부하는 학생입니다. 동아리에서 설문 40건을 정리하고 결과를 그래프로 만들었습니다. 아직 통계 검정은 배우는 중이고, 복잡한 분석을 맡아 본 경험은 없습니다. 작은 데이터를 읽기 쉽게 정리하는 작업에 관심이 있습니다.
```

Revised output:

```text
저는 데이터 분석을 공부하는 학생입니다. 동아리에서 설문 40건을 정리하고, 결과를 그래프로 만들었습니다. 아직 통계 검정은 배우는 중이고, 복잡한 분석을 맡아 본 경험은 없습니다. 작은 데이터를 읽기 쉽게 정리하는 작업에 관심이 있습니다.
```

### mixed-essay

Request: 감상의 리듬은 살리고 어색한 부분만 다듬어줘.

Input:

```text
기다렸다. 창가에서 한참 기다렸다. 빗소리는 여전했다. 그때 컵을 내려놓는 행동을 진행했다. 식은 차의 향이 잠깐 남았다. 그날을 특별한 교훈으로 남기고 싶지는 않았다. 그냥 그런 오후였다.
```

Baseline output:

```text
기다렸다. 창가에서 한참 기다렸다. 빗소리는 여전했다. 그때 컵을 내려놓았다. 식은 차의 향이 잠깐 남았다. 그날을 특별한 교훈으로 남기고 싶지는 않았다. 그냥 그런 오후였다.
```

Revised output:

```text
기다렸다. 창가에서 한참 기다렸다. 빗소리는 여전했다. 그때 컵을 내려놓았다. 식은 차의 향이 잠깐 남았다. 그날을 특별한 교훈으로 남기고 싶지는 않았다. 그냥 그런 오후였다.
```

## Limits

This is a six-case, single-batch development comparison per variant, not a benchmark or cross-platform validation. Cases were written while developing the rules, so they are not a held-out test set. The same model family may have produced and evaluated the outputs. No repeat runs, full 36-case regression execution, private real-world correspondence, or human grading were performed. Structural checks do not measure prose quality. No AI-detector or human-authorship guarantee is made.
