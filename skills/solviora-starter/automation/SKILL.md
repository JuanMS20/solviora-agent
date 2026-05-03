---
name: automation
description: "Automation workflow — delegate tasks, schedule jobs, and chain multi-step operations."
version: 0.1.0
metadata:
  hermes:
    tags: [automation, delegation, cron, starter]
    category: solviora-starter
---

# Automation Starter

## When to use

Use this skill when the user wants to automate a recurring task, schedule a job, or chain multiple operations together.

## Workflow

1. **Clarify** — confirm what the automation should do, when, and how often.
2. **Choose approach**:
   - **One-shot script** — for single complex tasks with multiple steps. Use `execute_code` or `write_file` + `terminal`.
   - **Cron job** — for recurring tasks. Use `cronjob` tool with a natural language schedule.
   - **Subagent delegation** — for parallel or isolated subtasks. Use `delegate_task`.
3. **Test** — run the automation once manually before scheduling.
4. **Schedule** — set up cron or save the script with clear instructions for re-running.

## Cron examples

- "every day at 9am" → `0 9 * * *`
- "every monday" → `0 9 * * 1`
- "every 6 hours" → `0 */6 * * *`

## Tips

- Always include error handling and logging in automation scripts.
- Save outputs to files, not just stdout — cron jobs have no terminal to read.
- For long-running automations, suggest running in background with `notify_on_complete=true`.
- Keep automation scripts self-contained — they may run in fresh sessions.
