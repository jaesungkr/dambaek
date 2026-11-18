# Bounded development review

Date: 2026-11-18. A fresh assistant context received the current `SKILL.md` and six requests together, without expected outputs or invariants. The assistant's explicit model identifier was unavailable. This is a batched qualitative check, not a platform test, blinded comparative trial or claim of general success.

## Actual requests and outputs

### 1. Register and no-op

Request: 다듬어줘.

Input: 이번에는 설정이 꽤 간단했어요. 파일을 넣고 버튼만 누르면 됐거든요.

Output: 이번에는 설정이 꽤 간단했어요. 파일을 넣고 버튼만 누르면 됐거든요.

### 2. Empty and necessary contrasts

Request: 군더더기 정리.

Input: 표의 열 너비를 드래그해서 조절할 수 있습니다. 하지만 모바일에서는 지원하지 않습니다. 하지만 모든 문제를 해결하는 만능 도구는 아닙니다.

Output: 표의 열 너비를 드래그해서 조절할 수 있습니다. 모바일에서는 지원하지 않습니다.

### 3. Limited evidence and uncertainty

Request: 자연스럽게.

Input: 표본 8개에서는 약 5% 빨랐다. 캐시를 늘리면 응답 시간이 줄어들 수 있다.

Output: 표본 8개에서는 약 5% 빨랐다. 캐시를 늘리면 응답 시간이 줄어들 수 있다.

### 4. Protected typography

Request: 긴 대시만 -로.

Input: 완료 — 저장됨. 인용은 “읽기 — 쓰기”. 범위는 2–4. 코드는 `x—y`.

Output: 완료 - 저장됨. 인용은 “읽기 — 쓰기”. 범위는 2–4. 코드는 `x—y`.

### 5. Diagnosis only

Request: 문장을 수정하지 말고 어색한 표현만 짚어줘.

Input: 설정의 변경을 진행하는 것이 가능합니다.

Output: “설정의 변경”은 명사형이 겹쳐 딱딱하게 읽힙니다. “진행하는 것이 가능합니다”는 간단한 가능 여부를 길게 풀어 쓴 표현입니다.

### 6. Unknown actor and useful detail

Request: 사람처럼 다듬어줘.

Input: 배포 뒤 설정 파일이 삭제됐다. 원인은 아직 확인하지 못했다. 오류가 나면 로그 폴더를 확인한다. 날짜별로 파일이 나뉘어 있어서 실패한 시각의 파일을 찾으면 된다.

Output: 배포 뒤 설정 파일이 삭제됐다. 원인은 아직 확인하지 못했다. 오류가 나면 로그 폴더를 확인한다. 날짜별로 파일이 나뉘어 있어서 실패한 시각의 파일을 찾으면 된다.

## Observations

All six outputs kept the checked information and edit scope. Case 2 removed the empty qualification and retained the mobile restriction. Case 4 changed only the prose em dash. Case 5 obeyed the diagnosis-only request. The remaining no-op results demonstrate preservation in those examples, not improved writing quality.

The complete 16-fixture suite has not been executed against any named model or product. ChatGPT, Claude and Notion UI loading and persistence have not been tested. `check_structure.py` passed after the final file edits; it checks metadata, fixture completeness and links only.
