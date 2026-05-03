# Solviora Agent

**Terminal-native AI agent that gets real work done.**

Search the web, write and run code, read and write files, research, automate — and deliver results. All from your terminal, no browser needed.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://python.org)
[![Docs](https://img.shields.io/badge/docs-solviora.dev-2BA8A0)](https://docs.solviora.dev)

> **Attribution:** Solviora Agent is built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com), used under the [MIT License](LICENSE).

---

## Quick Start

```bash
# Install from source
git clone https://github.com/JuanMS20/solviora-agent.git
cd solviora-agent
./setup-solviora.sh
```

Configure your provider and start:

```bash
solviora setup          # 3-step setup: provider → model → go
solviora "search for the latest AI frameworks and compare features"
```

Your first result in minutes. No browser, no IDE, no friction.

## What it does

- **Web research** — search, extract, summarize any topic
- **Code** — write, execute, debug in any language
- **Files** — read, write, patch, search across your project
- **Memory** — persistent memory across sessions
- **Automation** — delegate subtasks, schedule cron jobs
- **Skills** — install specialized skill packs for your workflow

## Connect remotely (optional)

Solviora works fully in your terminal. If you need remote access:

```bash
solviora setup gateway  # Connect Telegram, webhook, or API server
```

Gateways are optional extensions — not required for any core feature.

## CLI Commands

```
solviora "your task"     # Run a task directly
solviora                 # Interactive CLI session
solviora model           # Choose LLM provider and model
solviora tools           # Configure enabled tools
solviora setup           # Run setup wizard
solviora setup gateway   # Configure remote access
solviora status          # Show system status
solviora doctor          # Diagnose issues
```

## Configuration

- Config file: `~/.solviora/config.yaml`
- API keys: `~/.solviora/.env`
- Sessions: `~/.solviora/sessions/`
- Skills: `~/.solviora/skills/`

## Documentation

Visit [docs.solviora.dev](https://docs.solviora.dev) for the full documentation:

- [Quickstart](https://docs.solviora.dev/docs/quickstart)
- [Installation Guide](https://docs.solviora.dev/docs/installation)
- [CLI Reference](https://docs.solviora.dev/docs/cli-commands)
- [Providers](https://docs.solviora.dev/docs/providers)

### Run docs locally

```bash
cd docs-site
npm install
npm run start
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE).

This project includes code originally developed by Nous Research (Hermes Agent), also under the MIT License. See [NOTICE](NOTICE) for details.
