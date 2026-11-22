# 담백 · Dambaek

**English** | [한국어](README.ko.md)

Dambaek is a set of instructions for editing Korean prose with AI while preserving the writer’s meaning and tone.

## Installation

### Claude Code

Enter these commands in Claude Code. No Node.js update is required.

```text
/plugin marketplace add jaesungkr/dambaek
/plugin install dambaek@dambaek
```

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

**File preview in Codex and Claude Code**

In either agent, you can also ask naturally, “draft.md의 도입부를 자연스러운 한국어로 다듬어 줘.” Review the preview in chat. To write the change, say “방금 제안한 도입부만 파일에 반영해 줘.”

**Before**

> 모임 장소는 2층 강의실입니다. 다만 토요일에는 2층 강의실을 쓸 수 없어서 토요일 모임은 1층 도서실에서 엽니다.

**After**

> 모임 장소는 2층 강의실입니다. 토요일에는 강의실을 쓸 수 없어 1층 도서실에서 모입니다.

The edit mentions Saturday only once and keeps the reason for the change of venue.

## Try it on a draft

Paste the contents of [SKILL.md](SKILL.md) and your draft into the same conversation. For the example above, ask:

> 이 문단에서 반복되는 설명을 줄여 줘. 장소가 바뀌는 이유와 원래 말투는 그대로 살려 줘.

## Reuse the instructions

| Tool | Setup |
| --- | --- |
| ChatGPT | Add the file to a project and ask ChatGPT in the project instructions to use Dambaek when editing Korean. |
| Notion AI | Save the instructions on a page and mention it in your editing request. If the editor cannot read the page, paste the instructions with the draft. |

See the [platform guide](docs/platforms.md) for account requirements, official setup instructions, and the status of product testing.

## What survives an edit?

- **Counts.** Seeing an otter in the morning and again in the afternoon gives you two sightings. It could be the same otter.
- **Scope.** In “민지가 사진만 보냈다,” Minji sent only photos. In “민지만 사진을 보냈다,” only Minji sent photos.
- **Evidence.** A notice that omits the event date tells you what was published. The organizers may already have set a date.

Keep names, figures, quotations, uncertainty, and the strength of a request or promise. Edit within the requested scope and preserve the draft’s headings, tables, links, and code.

## Examples and review

- [Everyday writing](references/everyday-writing.md) covers emails, introductions, and personal messages.
- [Paired examples](references/patterns.md) show when a repeated expression can go and when it carries meaning.
- [Blog editing](references/blog-editing.md) looks at openings, transitions, and how to distinguish reported evidence from firsthand experience.
- [Editing examples](references/examples.md) and [review cases](tests/README.md) show how to check structure, meaning, and the quality of an edit.

## Contributing

Share a short before-and-after example or suggest a clearer instruction. Use text you can share and remove private information. See the [contribution guide](CONTRIBUTING.md).

## License

[MIT](LICENSE) © 2026 Jaesung Park.
