# 담백 · Dambaek

**English** | [한국어](README.ko.md)

Dambaek helps edit Korean drafts for natural phrasing while preserving the writer’s meaning and tone. When editing a paragraph, it joins sentences whose relationship is clear from the draft and keeps the details readers need to follow it.

## Context-sensitive editing

A phrase is a cue to inspect, not a word to ban. [Paired examples](references/patterns.md) show when to trim a pattern and when to preserve its meaning or social role. Review separates structural validity, meaning preservation, and useful editing; see [review instructions](tests/README.md).

## Beyond blog posts

Dambaek also works as editing guidance for emails, everyday messages, introductions, and personal writing. Preserve the relationship, register, emotional tone, and strength of a request or commitment. It does not turn every draft into a blog post or add headings, tables, or conclusions by default. See [everyday writing examples](references/everyday-writing.md).

## What it helps with

| Pattern | Editing approach |
| --- | --- |
| Repeated em dashes | Use a hyphen, comma, or sentence break to suit the sentence. |
| An explanation followed by an unnecessary “but it is not…” | Remove empty qualification; retain distinctions that change the reader's understanding. |
| Stock introductions and inflated claims | Start with the actual subject and use specific language. |
| Repetitive connectors and endings | Make the flow natural without forcing variety into every sentence. |
| Excessive bold text and decorative structure | Keep emphasis where it helps the reader. |
| Translation-like Korean | Rewrite awkward phrasing while keeping facts, scope, and tone. |

## A small example

**Before**

> 이번 글에서는 새롭게 출시된 모델의 문서 작성 기능에 대해 자세히 알아보겠습니다. 하지만 모든 문제를 해결하는 만능 도구는 아닙니다.

**After**

> 새 모델의 문서 작성 기능을 살펴보겠습니다.

This example trims a generic opening and an empty caveat while keeping the polite ending. A concrete limitation such as “PDF export is unavailable” stays in the draft. The writer's preferred register takes priority.

## Start with your preferred AI

1. Open [SKILL.md](SKILL.md) and copy its contents.
2. Paste the guidance and your draft into your preferred AI using the prompt below.
3. Review the edited text, especially facts, qualifications, and quotations.

The core is a readable instruction file. It requires no application install or API key of its own. Your chosen AI service handles the editing. Provide the actual text when the assistant cannot read a link.

```text
아래 글을 담백 지침에 따라 자연스러운 한국어로 다듬어줘.
원래 의미, 사실, 수치, 인용과 글쓴이의 관점을 유지해줘.
불필요한 표현만 덜어내고, 수정본과 주요 변경 이유를 보여줘.

[담백 지침]
여기에 SKILL.md 내용을 붙여넣기

[원문]
여기에 다듬을 글을 붙여넣기
```

| Tool | How to supply the guidance |
| --- | --- |
| ChatGPT | Paste it with the draft, or keep it as project reference material and add a project instruction to use it. |
| Claude | Paste it with the draft. To install a custom skill, zip the `dambaek` folder containing `SKILL.md` and `references/`, then upload it to Claude. |
| Notion AI | Paste the guidance into your editing request, or keep it on a page and explicitly reference that page with your draft. |
| Other assistants | Provide the plain-text guidance and draft in the same context. |

See [platform notes](docs/platforms.md) for official setup references and validation status.

## Editorial principles

- Preserve facts, uncertainty, numbers, names, quotations, and the author's position.
- Count sightings separately from individuals. “오전과 오후에 수달을 봤다” records two sightings. Both could be of the same otter.
- Keep `만` (only) attached to what it limits. “민지가 사진만 보냈다” limits what Minji sent. “민지만 사진을 보냈다” limits who sent photos.
- State what the source establishes. “공지에는 날짜가 없다” tells us the notice omits the date. The event date could already be set.
- Keep useful caveats and genuine contrasts. Evaluate their purpose before cutting them.
- Preserve Korean speech level and the requested document format.
- Protect code, links, tables, and quoted material from incidental rewrites.
- Show meaningful changes so the writer can review them.
- Follow the writer's preferences rather than flattening every draft into one style.

## Learning from finished posts

Dambaek also draws on finished blog posts, not only lists of unwanted expressions. The [blog-editing reference](references/blog-editing.md) separates observations from reusable editing rules: concrete openings, useful transitions, table commentary, and the boundary between reported evidence and personal experience. The source posts are linked, not bundled as a corpus.

Technical-blog conventions such as declarative endings, tables and limited first-person narration are optional. A personal essay or polite email keeps its own voice.

## Examples and review

Explore the [editing examples](references/examples.md) and [behavioral review cases](tests/README.md). They cover both useful edits and information that must survive a rewrite.

The project is in early development. Platform setup guidance is based on official documentation; actual Dambaek runs in those products still need verification. The review cases describe expected behavior, not measured improvement.

## Contributing

Help improve Dambaek with Korean before-and-after examples, meaning-preservation failures, or better usage instructions. Small, specific examples are especially useful.

See [CONTRIBUTING.md](CONTRIBUTING.md) for a submission template and review checklist. Use original or shareable text and remove private information before posting.

## License

[MIT](LICENSE) © 2026 Jaesung Park.
