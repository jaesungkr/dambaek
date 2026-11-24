![Dambaek symbol](docs/images/dambaek.svg)

# 담백 · Dambaek

Edit repetition and awkward phrasing in Korean drafts while keeping the writer’s meaning and tone.

[30-second trial](#30-second-trial) · [Use in chat](#use-the-instructions-in-chat) · [Install](#install-dambaek-in-your-writing-tool) · [한국어](README.md)

**Before**

> 목요일에는 책을 반납할 수 있습니다. 목요일 반납은 안내실에서만 가능합니다.

**After**

> 목요일에는 안내실에서만 책을 반납할 수 있습니다.

The edit mentions Thursday once and keeps the restriction on where books can be returned.

## 30-second trial

Copy the whole block into a chat you already use, such as ChatGPT, Claude, or Notion AI. This quick trial uses a short prompt. The full Dambaek instructions are below.

```text
아래 문단을 자연스러운 한국어로 다듬어 줘. 반복되는 설명을 합치고, 원문에 있는 이유는 관련 안내와 이어 줘. 뜻, 조건, 말투를 유지하고 수정문만 보여 줘.

수요일에는 1층에서 신청을 받습니다. 수요일 신청은 1층에서만 가능합니다. 2층은 그날 전기 점검으로 신청을 받지 않습니다.
```

## Use the instructions in chat

Choose your chat app below. For editing project files, jump to [Claude Code](#claude-code) or [Codex](#codex).

- **ChatGPT or Notion AI.** Copy the contents of [SKILL.md](SKILL.md) and paste them with your draft into the same conversation.
- **Claude web or desktop chat.** Download [dambaek-chat.zip](https://github.com/jaesungkr/dambaek/releases/download/v0.2.0/dambaek-chat.zip). Open **Plugins** in the sidebar and upload the ZIP as a skill without unzipping it. Enable Dambaek, then paste your draft into chat. Claude requires code execution and file creation for custom skills. [Claude's Plugins guide](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

Then ask:

> 담백으로 이 글을 다듬어 줘. 뜻과 말투는 그대로 살려 줘.

<details>
<summary>Claude's older upload menu and ZIP checksum</summary>

If your sidebar still says **Customize**, use **Customize → Skills → + → Create skill → Upload a skill**. [Claude's custom skill guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

ZIP SHA-256: `8f534c2eb09ea5416221c983f0a51dec9d4980fa64213fd4831185c5e51cde96`

</details>

### Keep the instructions in ChatGPT or Notion

| Tool | Setup |
| --- | --- |
| ChatGPT | Add the file to a project and ask ChatGPT in the project instructions to use Dambaek when editing Korean. |
| Notion AI | Save the instructions on a page and mention it in your editing request. If the editor cannot read the page, paste the instructions with the draft. |

**Paragraph editing.** Ask Dambaek to connect and reorganize a selected passage or a full draft. See the [paragraph examples](references/examples.md#단락-편집-예시).

**Writing-style card.** Ask for a card from your own samples, then provide it when you want to reuse it. See the [card guide](references/everyday-writing.md#문체-카드).

## Install Dambaek in your writing tool

<a name="claude-code"></a>

<details>
<summary>Claude Code · Terminal or Windows desktop Code</summary>

**Terminal with Claude Code v2.1.292 or later.** Run this in PowerShell or your system terminal before starting Claude Code. [Claude Code installation guide](https://code.claude.com/docs/en/discover-plugins#add-a-marketplace-and-install-in-one-command)

```sh
claude plugin install dambaek --marketplace https://github.com/jaesungkr/dambaek.git
```

**Windows desktop Code.** Open **Plugins**, choose **+ Add**, and add [the Dambaek GitHub URL](https://github.com/jaesungkr/dambaek) as a marketplace. Install Dambaek from that marketplace.

Start a new session and type `/dambaek:dambaek draft.md의 도입부를 다듬어 줘`.

<details>
<summary>Fallback for older Claude Code versions</summary>

Inside a Claude Code terminal session, enter these commands in order:

```text
/plugin marketplace add jaesungkr/dambaek
/plugin install dambaek@dambaek
```

</details>
</details>

<a name="codex"></a>

<details>
<summary>Codex · Install in a project with Node.js 22.20.0 or later</summary>

Run this in your project terminal:

```sh
npx --yes skills@1.9.0 add jaesungkr/dambaek --skill dambaek -a codex -y
```

Start Codex in that project and type `$dambaek draft.md의 도입부를 다듬어 줘`.

</details>

**File edits.** Review the proposed edit in chat, then explicitly approve the portion you want written to the file.

For **Pi, Cursor, and other agents**, see [additional installation candidates](docs/platforms.md#additional-installation-candidates--추가-설치-후보).

See the [platform guide](docs/platforms.md) for account requirements, setup details, and product testing status.

## How Dambaek preserves meaning

- **Counts.** Seeing an otter in the morning and again in the afternoon gives you two sightings. It could be the same otter.
- **Scope.** In “민지가 사진만 보냈다,” Minji sent only photos. In “민지만 사진을 보냈다,” only Minji sent photos.
- **Evidence.** A notice that omits the event date tells you what was published. The organizers may already have set a date.

Keep names, figures, quotations, uncertainty, and the strength of a request or promise. Edit within the requested scope and preserve the draft’s headings, tables, links, and code.

## Editing examples

- [Everyday writing](references/everyday-writing.md) covers emails, introductions, and personal messages.
- [Paired examples](references/patterns.md) show when a repeated expression can go and when it carries meaning.
- [Blog editing](references/blog-editing.md) looks at openings, transitions, and how to distinguish reported evidence from firsthand experience.
- [Editing examples](references/examples.md) and [review cases](tests/README.md) show how to check structure, meaning, and the quality of an edit.

## Contributing

Share a short before-and-after example or suggest a clearer instruction. Use text you can share and remove private information. See the [contribution guide](CONTRIBUTING.md).

## License

[MIT](LICENSE) © 2026 Jaesung Park.
