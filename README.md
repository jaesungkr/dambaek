![담백 심볼](docs/images/dambaek.svg)

# 담백 · Dambaek

뜻과 말투를 살리면서 한국어 초안의 반복과 어색한 표현을 다듬습니다.

[30초 체험](#30초-체험) · [채팅에서 사용](#채팅에-지침을-붙여-넣어-쓰기) · [도구에 설치](#사용하는-도구에-설치하기) · [English](README.en.md)

**원문**

> 목요일에는 책을 반납할 수 있습니다. 목요일 반납은 안내실에서만 가능합니다.

**다듬은 뒤**

> 목요일에는 안내실에서만 책을 반납할 수 있습니다.

‘목요일’을 한 번만 쓰고, 반납 장소가 안내실로 한정된다는 뜻을 살렸습니다.

## 30초 체험

아래 블록을 통째로 복사해 평소 쓰는 ChatGPT, Claude, Notion AI 등의 채팅에 붙여 넣으세요. 짧은 체험용 요청입니다. 담백의 전체 지침은 아래에서 볼 수 있습니다.

```text
아래 문단을 자연스러운 한국어로 다듬어 줘. 반복되는 설명을 합치고, 원문에 있는 이유는 관련 안내와 이어 줘. 뜻, 조건, 말투를 유지하고 수정문만 보여 줘.

수요일에는 1층에서 신청을 받습니다. 수요일 신청은 1층에서만 가능합니다. 2층은 그날 전기 점검으로 신청을 받지 않습니다.
```

<a name="use-the-instructions-in-chat"></a>

## 채팅에 지침을 붙여 넣어 쓰기

ChatGPT와 Notion AI에서는 지침을 복사하고, Claude 일반 채팅에서는 ZIP을 업로드하세요. 파일을 다루는 [Claude Code](#claude-code)와 [Codex](#codex)는 아래에 별도로 안내합니다.

- **ChatGPT 또는 Notion AI.** [SKILL.md](SKILL.md)의 내용을 복사해 다듬을 글과 함께 같은 대화에 붙여 넣으세요.
- **Claude 웹 또는 데스크톱 일반 채팅.** [dambaek-chat.zip](https://github.com/jaesungkr/dambaek/releases/download/v0.2.0/dambaek-chat.zip)을 내려받으세요. 사이드바의 **Plugins**를 열고 압축을 풀지 않은 채 스킬로 업로드하세요. 담백을 켠 뒤 채팅에 초안을 붙여 넣으세요. Claude의 코드 실행·파일 생성 기능이 필요합니다. [Claude Plugins 안내](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

이렇게 요청해 보세요.

> 담백으로 이 글을 다듬어 줘. 뜻과 말투는 그대로 살려 줘.

<details>
<summary>Claude 이전 메뉴에서 업로드하기와 ZIP 체크섬</summary>

사이드바에 **Customize**가 보이면 **Customize → Skills → + → Create skill → Upload a skill**에서 업로드하세요. [Claude 사용자 스킬 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

ZIP SHA-256: `8f534c2eb09ea5416221c983f0a51dec9d4980fa64213fd4831185c5e51cde96`

</details>

### ChatGPT와 Notion에 지침 저장하기

| 도구 | 지침을 다시 쓰는 방법 |
| --- | --- |
| ChatGPT | 프로젝트 자료에 지침 파일을 올리고, 프로젝트 지침에 “한국어 글을 다듬을 때 담백을 참고해 줘”라고 적으세요. |
| Notion AI | 지침을 페이지에 저장한 뒤 편집을 요청할 때 그 페이지를 지정하세요. AI가 페이지를 읽을 수 없으면 지침을 직접 붙여 넣으세요. |

**단락 편집.** 글 전체나 지정한 범위의 문장과 문단을 이어 달라고 요청하세요. [단락 편집 예시](references/examples.md#단락-편집-예시)

**문체 카드.** 내 글로 짧은 문체 카드를 만들고 필요할 때 다시 제공하세요. [문체 카드 안내](references/everyday-writing.md#문체-카드)

## 사용하는 도구에 설치하기

<a name="claude-code"></a>

<details>
<summary>Claude Code · 터미널 또는 Windows 데스크톱 Code</summary>

**터미널에서 Claude Code v2.1.292 이상 사용 시.** Claude Code를 시작하기 전에 PowerShell이나 시스템 터미널에서 실행하세요. [Claude Code 설치 안내](https://code.claude.com/docs/en/discover-plugins#add-a-marketplace-and-install-in-one-command)

```sh
claude plugin install dambaek --marketplace https://github.com/jaesungkr/dambaek.git
```

**Windows 데스크톱 Code.** **Plugins**에서 **+ Add**를 선택해 [담백 GitHub 주소](https://github.com/jaesungkr/dambaek)를 마켓플레이스로 추가하세요. 추가한 마켓플레이스에서 담백을 설치하세요.

새 세션에서 `/dambaek:dambaek draft.md의 도입부를 다듬어 줘`를 입력하세요.

<details>
<summary>이전 Claude Code 버전에서 설치하기</summary>

터미널에서 Claude Code 세션을 열고 아래 명령을 차례대로 입력하세요.

```text
/plugin marketplace add jaesungkr/dambaek
/plugin install dambaek@dambaek
```

</details>
</details>

<a name="codex"></a>

<details>
<summary>Codex · Node.js 22.20.0 이상에서 프로젝트에 설치</summary>

프로젝트 터미널에서 실행하세요.

```sh
npx --yes skills@1.9.0 add jaesungkr/dambaek --skill dambaek -a codex -y
```

같은 프로젝트에서 Codex를 열고 `$dambaek draft.md의 도입부를 다듬어 줘`를 입력하세요.

</details>

**파일을 다듬을 때.** 대화에서 수정안을 확인한 뒤 파일에 반영할 부분을 지정해 승인하세요.

**Pi, Cursor와 다른 에이전트**는 [추가 설치 후보](docs/platforms.md#additional-installation-candidates--추가-설치-후보)를 참고하세요.

[도구별 사용 안내](docs/platforms.md)에서 이용 조건, 설정 방법, 제품별 검증 범위를 확인할 수 있습니다.

## 다듬을 때 지키는 것

- **관찰 횟수.** “오전과 오후에 수달을 봤다”는 두 번 봤다는 뜻입니다. 같은 수달을 두 번 봤을 수도 있습니다.
- **‘만’의 위치.** “민지가 사진만 보냈다”는 민지가 보낸 게 사진뿐이라는 뜻입니다. “민지만 사진을 보냈다”는 사진을 보낸 사람이 민지뿐이라는 뜻입니다.
- **자료로 확인한 사실.** 공지에 날짜가 없다고 해서 행사 날짜가 아직 정해지지 않았다고 쓸 수는 없습니다.

이름과 수치, 인용, 글쓴이의 의견과 망설임도 원문에 맞게 남깁니다. 별도 요청이 없으면 제목과 표, 링크, 코드를 그대로 두고, 짧은 메시지에 서론이나 결론을 덧붙이지 않습니다.

## 글 종류별 예시와 검토 방법

- [일상 글 편집 예시](references/everyday-writing.md)는 부탁이나 약속을 다듬으면서 상대와의 거리와 감정의 강도를 유지한 사례입니다.
- [표현을 덜어낼 때와 남길 때](references/patterns.md)는 비슷한 표현을 문맥에 따라 다르게 고친 사례를 나란히 보여 줍니다.
- [블로그 글 편집 사례](references/blog-editing.md)에서는 실제 발행한 글을 바탕으로 도입부와 문단을 잇는 법, 표를 설명하는 법, 발표 자료와 직접 경험을 구분하는 법을 살펴봅니다. 원문은 출처 링크에서 읽을 수 있습니다. 한다체를 쓰거나 1인칭을 줄이는 방식은 기술 블로그에서 택할 수 있는 문체입니다.
- [편집 전후 예시](references/examples.md)와 [검토 방법](tests/README.md)에서는 형식이 온전한지, 원래 뜻을 지켰는지, 표현이 실제로 나아졌는지를 각각 살핍니다. 담백은 아직 개발 초기이며, 검토 사례는 편집할 때 기대하는 결과를 보여 줍니다.

## 기여하기

다듬고 나서 뜻이 달라진 문장이나 더 알기 쉬운 사용법이 있다면 알려 주세요. 수정 전후를 짧게 보여 주시면 도움이 됩니다. 직접 썼거나 공유할 수 있는 글에서 개인정보를 지운 뒤 [기여 안내](CONTRIBUTING.md)에 따라 제안해 주세요.

## 라이선스

[MIT](LICENSE) © 2026 Jaesung Park.
