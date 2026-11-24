# Use Dambaek with your AI / 도구별 사용 안내

[한국어 README](../README.md) · [English README](../README.en.md)

The same [SKILL.md](../SKILL.md) supplies the editing guidance. Start by pasting its contents with your draft. For recurring use, choose a documented setup below.

Official documentation checked: **2026-11-18**. These instructions describe supported ways to supply context. End-to-end Dambaek tests in each product remain pending. Availability and interface labels can depend on the account and workspace.

## ChatGPT

### One draft

1. Copy the contents of `SKILL.md` into a new chat.
2. Add your draft and the task: `담백 지침에 따라 원래 뜻과 말투를 유지하며 다듬어줘.`
3. Review the result against the source.

### Recurring editing

1. Create a ChatGPT Project.
2. Upload `SKILL.md` as a project source, or paste its text into the project's reference material.
3. Open the project's settings and add the instruction below.
4. Start an editing conversation inside that project and provide the draft.

```text
한국어 글을 다듬을 때 프로젝트 자료의 SKILL.md(담백)를 먼저 읽고 적용한다.
원래 의미, 사실, 조건, 수치, 인용, 말투를 유지한다.
지침 파일을 읽을 수 없으면 내용을 요청한다.
```

한국어: 프로젝트에 지침을 참고 자료로 넣고, 프로젝트 설정에서 편집 시 `SKILL.md`를 읽도록 지정한다. 원문은 해당 프로젝트 안의 대화에 제공한다. 한 번만 사용할 때는 지침과 원문을 함께 붙여넣으면 된다.

Official reference: [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

## Claude

### One draft

Paste the guidance and draft together in a chat, using the request above.

### Custom skill

1. Put `SKILL.md` and its relative reference files in a folder named `dambaek`.
2. ZIP that folder using Claude's documented custom-skill structure.
3. Ensure the account permits skills and that code execution and file creation are enabled, as required by Claude's skill feature.
4. Open **Customize → Skills**, choose **Create skill → Upload a skill**, and upload the ZIP.
5. Enable the skill and explicitly ask Claude to use Dambaek on a short Korean draft. Inspect the actual output before relying on it for a longer article.

This is a documentation-based setup path. A successful upload and invocation must be recorded before claiming Dambaek has been tested in Claude. No executable script is needed by Dambaek's core instructions.

한국어: 한 번만 사용할 때는 지침을 원문과 함께 붙여넣는다. 반복해서 쓸 때는 `SKILL.md`와 참조 파일을 `dambaek` 폴더에 넣어 ZIP으로 묶고, Claude의 사용자 스킬 업로드 기능을 이용한다. 실제 활성화와 결과를 확인해야 하며 조직 정책에 따라 사용이 제한될 수 있다.

Official reference: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Notion AI

1. Create a page named **담백 지침** and paste the contents of `SKILL.md` into it.
2. Open the draft and select the text to revise.
3. Choose **Edit with AI**. Supply the request below and use an actual page @-mention to reference **담백 지침**, where that editing interface supports it.
4. If the reference is unavailable or unreadable, paste the guidance into the request with the selected text.
5. Review the suggested changes before accepting them.

```text
담백 지침 페이지를 참고해 선택한 글을 다듬어줘.
원래 의미와 말투를 유지하고, 수정본을 검토할 수 있게 보여줘.
```

한국어: 지침을 별도 페이지에 보관하고 편집 요청에서 실제 페이지 참조를 추가한다. 참조를 읽을 수 없는 경우 지침을 직접 붙여넣는다. 결과는 확인한 뒤 적용한다.

Official reference: [What is Notion AI?](https://www.notion.com/help/notion-ai-faqs).

## Other assistants

Copy the plain-text instructions and draft into the same context. If the assistant supports reference files, provide `SKILL.md` and ask it to read the file explicitly. Keep the instruction and source text clearly separated. A repository URL alone does not establish that the file was loaded.

다른 AI에서도 지침과 원문을 같은 맥락에 제공한다. 링크만 보내기보다 파일을 읽었는지 확인하거나 내용을 직접 붙여넣는 방식을 권장한다.

## Validation record

| Check | Current status |
| --- | --- |
| Official setup documentation reviewed | 2026-11-18 |
| ChatGPT Project instruction loading and editing | Pending |
| Claude ZIP upload, skill invocation, and editing | Pending |
| Notion page reference and editing | Pending |

When recording a product test, include the date, product/model, instruction version, actual input/output, and findings. Check facts, uncertainty, numbers, caveats, quotations, speech level, code, links, and Markdown against the original. See the [review cases](../tests/README.md).

## Draft handling

Your chosen AI service processes the text you provide. Before sending unpublished or confidential material, review the provider's data settings and your organization's rules. The instruction file adds no independent privacy guarantee.

작성한 글은 선택한 AI 서비스가 처리한다. 비공개 자료를 입력하기 전에 해당 서비스의 데이터 설정과 소속 조직의 규칙을 확인한다.

## Additional installation candidates / 추가 설치 후보

The following routes use the same root `SKILL.md` and four files under `references/`. The commands show how to review this candidate from a local checkout. Product installation and invocation still need testing.

아래 경로는 루트의 `SKILL.md`와 `references/`의 파일 네 개를 함께 사용합니다. 명령은 로컬 후보 작업트리에서 검토할 때 씁니다. 앱 설치와 호출은 각각 확인이 필요합니다.

| Tool / 도구 | Candidate / 후보 |
| --- | --- |
| Pi | From the candidate checkout run `pi install -l "$PWD"`, then try `/skill:dambaek`. The git-source form uses `pi install git:github.com/jaesungkr/dambaek` once the manifest is publicly available. / 후보 작업트리에서 프로젝트용으로 설치하고 명령을 확인합니다. 공개 원격 명령은 매니페스트가 배포된 뒤 사용합니다. [Pi Packages](https://docs.pi.dev/latest/packages) |
| Cursor | The manifests point at the root skill. For manual project use, copy the skill as directed below into `.cursor/skills/dambaek/`. Repository import expects a Cursor marketplace manifest and a repository the app can access. / 플러그인 매니페스트의 루트 스킬 로딩과 저장소 가져오기는 앱에서 검증해야 합니다. 로컬 검토에는 프로젝트 스킬 경로를 쓸 수 있습니다. [Cursor Agent Skills](https://cursor.com/docs/skills) · [Cursor schemas](https://github.com/cursor/plugins/tree/main/schemas) |
| Skills CLI | Inspect discovery with `npx --yes skills@1.9.0 add . --list`. For an intended agent, use `npx --yes skills@1.9.0 add . --skill dambaek -a AGENT` from the candidate checkout and replace `AGENT` with its CLI identifier, such as `gemini-cli`, `github-copilot`, or `windsurf`. Pass `-a '*'` only when targeting all agents intentionally. / 후보 작업트리에서 검색 목록을 확인하고, 필요한 에이전트만 선택해 설치합니다. [Skills CLI](https://github.com/vercel-labs/skills) |
| Manual / 수동 | Copy `SKILL.md` and the entire `references/` directory into a folder named `dambaek` in the agent’s documented skill root. For example, use `.agents/skills/dambaek/` for a Codex project. If the assistant takes instructions only as text, paste the guidance and any relevant reference with the draft. / 도구의 공식 스킬 경로에 담백 폴더를 만들고 파일과 참조의 상대 경로를 유지합니다. [Agent Skills](https://agentskills.io/specification) · [Codex Skills](https://developers.openai.com/codex/skills) |
| Codex metadata / 표시 정보 | `agents/openai.yaml` supplies a name, short description and starter prompt. For a manual Codex copy, include the `agents/` directory if you want this metadata. / 수동 설치에서도 표시 정보가 필요하면 `agents/`를 함께 복사합니다. [OpenAI metadata guide](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/references/openai_yaml.md) |

### Build a Claude Chat ZIP from a checkout / 작업트리에서 Claude 채팅 ZIP 만들기

```sh
python3 scripts/build_chat_zip.py /tmp/dambaek-chat.zip
```

Choose a new output path. The archive contains a single `dambaek/` folder with the skill and four references. Upload that archive using the Claude custom-skill flow above. The existing release download remains available in the READMEs.

새 출력 경로를 지정하세요. ZIP에는 스킬과 참조 네 개가 든 `dambaek/` 폴더 하나가 들어갑니다. 위 Claude 사용자 스킬 절차에서 이 ZIP을 업로드하세요. 기존 릴리스 ZIP 링크는 README에 있습니다.
