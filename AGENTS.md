# 담백 작업 지침

편집 규칙은 루트의 `SKILL.md`에서 관리한다. 도구별 패키지는 같은 파일과 `references/`를 사용한다. 글을 고치는 규칙에는 공개 가능한 한국어 예시와 원문에서 지켜야 할 조건을 함께 남긴다.

배포 경로나 파일 구성을 바꾸면 한·영 README와 플랫폼 안내를 함께 확인한다. `python3 tests/check_structure.py`와 `python3 tests/check_package.py`, `python3 tests/check_upgrade.py`를 실행한다. 실제 앱에서 확인한 범위는 구조 검사와 구분해 기록한다.
