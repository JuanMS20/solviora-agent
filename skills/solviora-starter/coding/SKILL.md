---
name: coding
description: "Coding workflow — write, execute, debug, and iterate on code from the terminal."
version: 0.1.0
metadata:
  hermes:
    tags: [coding, development, starter]
    category: solviora-starter
---

# Coding Starter

## When to use

Use this skill when the user wants to write, modify, debug, or understand code.

## Workflow

1. **Understand** — read relevant files with `read_file` or `search_files` before writing anything.
2. **Write** — use `write_file` for new files, `patch` for modifications. Prefer patching over rewriting.
3. **Execute** — use `terminal` to run the code and verify it works.
4. **Iterate** — if there are errors, read the output, fix, and re-run. Max 3 iterations before asking the user for guidance.

## Conventions

- Match the existing code style in the project (indentation, naming, imports).
- Use the project's existing dependencies — don't introduce new libraries without asking.
- Write minimal, focused changes — don't refactor unrelated code.
- Include error handling for I/O operations (file reads, network calls, user input).

## Languages

Default to **Python** unless the user specifies another language. Use the terminal's current working directory as the project root.

## Tips

- Run `ls` or `search_files` to understand project structure before editing.
- For multi-file changes, plan the edits before executing any.
- Always verify: run the code, check the output, confirm it matches the request.
