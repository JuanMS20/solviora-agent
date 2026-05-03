---
name: web-research
description: "Web research workflow — search, extract, and synthesize information into structured outputs."
version: 0.1.0
metadata:
  hermes:
    tags: [research, web, starter]
    category: solviora-starter
---

# Web Research Starter

## When to use

Use this skill when the user wants to research a topic, compare options, find information, or get a summary of web content.

## Workflow

1. **Search** — use `web_search` with specific, targeted queries. Run 2-3 searches with different angles if the topic is broad.
2. **Extract** — use `web_extract` on the most relevant results to get full content.
3. **Synthesize** — combine findings into a structured output matching the user's request format.

## Output formats

Default to **markdown** unless the user specifies otherwise:

- **Comparison table** — for "compare X vs Y" requests
- **Numbered list with summaries** — for "top N" or "best" requests
- **Executive summary** — for "summarize" or "overview" requests
- **Bullet points** — for quick fact-finding

## Tips

- Prefer recent sources. Add year qualifiers to search queries when recency matters.
- Always cite sources with URLs.
- If search results are thin, try rephrasing the query or searching for specific subtopics.
- For technical topics, include both official docs and community perspectives.
