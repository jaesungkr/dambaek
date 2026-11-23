# 담백 · Dambaek

**English** | [한국어](README.ko.md)

Dambaek helps you edit Korean drafts. It trims repetition and smooths awkward phrasing while keeping your meaning and tone.

**Before**

> 모임 장소는 2층 강의실입니다. 다만 토요일에는 2층 강의실을 쓸 수 없어서 토요일 모임은 1층 도서실에서 엽니다.

**After**

> 모임 장소는 2층 강의실입니다. 토요일에는 강의실을 쓸 수 없어 1층 도서실에서 모입니다.

The edit mentions Saturday only once and keeps the reason for the change of venue.

## Install Dambaek in your writing tool

### Claude Code

**CLI (v2.1.292 or later).** Run this in PowerShell or your system terminal, outside the Claude Code session. [Claude Code installation reference](https://code.claude.com/docs/en/discover-plugins#add-a-marketplace-and-install-in-one-command)

```sh
claude plugin install dambaek --marketplace https://github.com/jaesungkr/dambaek.git
```

**Interactive terminal fallback.** Inside a Claude Code session, enter these two commands in order. No Node.js update is required.

```text
/plugin marketplace add jaesungkr/dambaek
/plugin install dambaek@dambaek
```

**Claude Desktop on Windows.** In **Code**, open **Plugins**, choose **+ Add**, and add the [Dambaek GitHub repository](https://github.com/jaesungkr/dambaek) as a marketplace. Then install Dambaek from that marketplace.

Start a new session and type `/dambaek:dambaek draft.md의 도입부를 다듬어 줘`.

### Codex

With **Node.js 22.20.0 or later**, run this in your project terminal:

```sh
npx --yes skills@1.9.0 add jaesungkr/dambaek --skill dambaek -a codex -y
```

Start Codex in that project and type `$dambaek draft.md의 도입부를 다듬어 줘`.

### Claude.ai and Claude Desktop chat

Download [dambaek-chat.zip](https://github.com/jaesungkr/dambaek/releases/download/v0.1.0/dambaek-chat.zip). In **Customize → Skills → + → Create skill → Upload a skill**, upload the ZIP as-is and enable Dambaek. Ask Claude to polish a Korean draft in chat. This route requires code execution and file creation in Claude and works without a local Node.js update.

ZIP SHA-256: `2bb9709f93cb16ee5d055766ddb484334af9973d37a420cd6f13ab65820c7048`

### Preview a file edit

In Codex or Claude Code, you can ask in your own words, “draft.md의 도입부를 자연스러운 한국어로 다듬어 줘.” Review the preview in chat. To write the change, say “방금 제안한 도입부만 파일에 반영해 줘.”

## Use the instructions in chat

Paste the contents of [SKILL.md](SKILL.md) and your draft into the same conversation. For the example above, ask:

> 이 문단에서 반복되는 설명을 줄여 줘. 장소가 바뀌는 이유와 원래 말투는 그대로 살려 줘.

### Keep the instructions in ChatGPT or Notion

| Tool | Setup |
| --- | --- |
| ChatGPT | Add the file to a project and ask ChatGPT in the project instructions to use Dambaek when editing Korean. |
| Notion AI | Save the instructions on a page and mention it in your editing request. If the editor cannot read the page, paste the instructions with the draft. |

See the [platform guide](docs/platforms.md) for account requirements, official setup instructions, and the status of product testing.

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
