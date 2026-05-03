# Migración editorial: Hermes Agent → Solviora Agent

> Fecha: 2026-05-03
> Objetivo: Inventariar el contenido de la web pública y documentación de Hermes Agent para planificar la ampliación de la documentación de Solviora.
> Fuentes: https://hermes-agent.nousresearch.com/ + /docs
> Método: migración editorial, no copia literal.

---

## 1. Inventario completo de secciones detectadas en la home de Hermes

| # | Sección | Descripción |
|---|---------|-------------|
| 1.1 | **Hero / Tagline** | "An agent that grows with you." Open source · MIT. No es un copilot atado a un IDE ni un wrapper de chat. |
| 1.2 | **Install CTA** | `curl -fsSL https://hermes-agent.../install.sh \| bash` — install en 60s. Luego `hermes setup`. Menciona WSL2. |
| 1.3 | **See it in action** | GIF/video demo del terminal |
| 1.4 | **Feature: Lives where you do** | Multi-plataforma: Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI. Crece lista. |
| 1.5 | **Feature: Grows the longer it runs** | Memoria persistente + skills auto-generados. Aprende proyectos, no olvida soluciones. |
| 1.6 | **Feature: Scheduled automations** | Cron en lenguaje natural para informes, backups, briefings. Corre desatendido via gateway. |
| 1.7 | **Feature: Delegates & parallelizes** | Subagentes aislados con sus propias conversaciones, terminales y scripts Python RPC. |
| 1.8 | **Feature: Real sandboxing** | 5 backends: local, Docker, SSH, Singularity, Modal. Hardening de contenedores. |
| 1.9 | **Feature: Full web & browser control** | Web search, browser automation, vision, image gen, TTS, multi-model reasoning. |
| 1.10 | **Footer** | v0.12.0 · Nous Research · MIT License · 2026 |

---

## 2. Inventario completo de secciones/páginas detectadas en la docs de Hermes

### 2.1 Getting Started

| Página | Descripción |
|--------|-------------|
| Installation | Linux, macOS, WSL2, Termux (Android) |
| Quickstart | De instalación a primer chat en <5 min |
| Learning Path | Rutas por nivel de experiencia y caso de uso |
| Updating | Actualización y desinstalación |
| Termux (Android) | Ejecución en Android |
| Nix Setup | Instalación y deploy con Nix |

### 2.2 User Guide — Using Hermes

| Página | Descripción |
|--------|-------------|
| CLI | Interface de terminal: comandos, keybindings, personalidades |
| TUI (Ink) | Terminal UI moderno con ratón, overlays, input no bloqueante |
| Configuration | config.yaml, providers, models, API keys |
| Configuring Models | Selección y configuración de modelos |
| Sessions | Persistencia, resume, búsqueda, gestión multi-plataforma |
| Profiles | Múltiples instancias aisladas |
| Git Worktrees | Múltiples agentes en mismo repo con worktrees |
| Docker Backend | Hermes en Docker y Docker como backend terminal |
| Security | Modelo de seguridad: aprobación de comandos, autorización, aislamiento |
| Checkpoints & Rollback | Snapshots automáticos y shadow git repos |

### 2.3 User Guide — Core Features

| Página | Descripción |
|--------|-------------|
| Features Overview | Mapa general de funcionalidades |
| Tools | 68 herramientas, toolsets, backends de terminal |
| Skills System | Progressive disclosure, agent-managed skills, Skills Hub |
| Curator | Mantenimiento background de skills (uso, obsolescencia, archivo) |
| Memory | MEMORY.md, USER.md, búsqueda entre sesiones (FTS5) |
| Memory Providers | Honcho, OpenViking, Mem0, Hindsight, Holographic, RetainDB, ByteRover, Supermemory |
| Context Files | .hermes.md, AGENTS.md, CLAUDE.md, SOUL.md, .cursorrules |
| Context References | Sintaxis @ para adjuntar archivos, carpetas, git diffs, URLs |
| Personality & SOUL.md | Voz por defecto del agente, personalidades, personas personalizadas |
| Plugins | Extensión via plugins con tools, hooks, integraciones |
| Built-in Plugins | Plugins shipped: disk-cleanup y otros |

### 2.4 User Guide — Automation

| Página | Descripción |
|--------|-------------|
| Cron Jobs | Tareas automatizadas con lenguaje natural, skills adjuntos |
| Delegation | Subagentes hijos aislados con delegate_task |
| Kanban Multi-Agent | Tablero SQLite para coordinar múltiples perfiles Hermes |
| Kanban Tutorial | Tutorial del sistema Kanban |
| Persistent Goals | Goal tipo "Ralph loop" — el agente sigue trabajando hasta completar |
| Code Execution | Ejecución programática Python con acceso RPC a tools |
| Hooks | Código custom en puntos del ciclo de vida |
| Batch Processing | Generación de trayectorias a escala |

### 2.5 User Guide — Media & Web

| Página | Descripción |
|--------|-------------|
| Voice Mode | Voz en tiempo real: CLI, Telegram, Discord (DMs, canales, VC) |
| Browser | Automatización de navegador |
| Vision | Procesamiento de imágenes |
| Image Generation | Generación de imágenes |
| Text-to-Speech (TTS) | TTS y transcripción de mensajes de voz |

### 2.6 User Guide — Messaging Platforms

| Página | Descripción |
|--------|-------------|
| Overview | Arquitectura del gateway, 15+ plataformas |
| Telegram | Setup como bot de Telegram |
| Discord | Setup como bot de Discord |
| Slack | Setup como bot Slack (Socket Mode) |
| WhatsApp | Bridge Baileys |
| Signal | Via signal-cli daemon |
| Email | Asistente IMAP/SMTP |
| SMS | Via Twilio |
| Matrix | Bot Matrix |
| Mattermost | Bot Mattermost |
| Home Assistant | Integración |
| Webhooks | Eventos GitHub, GitLab, etc. |

### 2.7 Integrations

| Página | Descripción |
|--------|-------------|
| Integrations Overview | Mapa de integraciones |
| Providers | Catálogo completo de proveedores LLM |
| MCP (Model Context Protocol) | Conexión a servidores MCP externos |
| ACP (Agent Context Protocol) | Integración con VS Code, Zed, JetBrains |
| API Server | API compatible OpenAI para cualquier frontend |
| Honcho Memory | Memoria persistente con dialectic reasoning |
| Provider Routing | Enrutamiento entre proveedores |
| Fallback Providers | Proveedores de respaldo |
| Credential Pools | Pool de credenciales rotables |

### 2.8 Guides & Tutorials

| Página | Descripción |
|--------|-------------|
| Tips & Best Practices | Atajos CLI, context files, memoria, costos, seguridad |
| Local LLMs on Mac | llama.cpp, MLX en Apple Silicon |
| Daily Briefing Bot | Bot de briefing diario automatizado |
| Team Telegram Assistant | Bot de Telegram para equipos |
| Use Hermes as a Python Library | AIAgent embebido en scripts propios |
| Use MCP with Hermes | Guía práctica de MCP |
| Use Voice Mode with Hermes | Setup y uso de voz |
| Use SOUL.md with Hermes | Personalidad del agente |
| Build a Hermes Plugin | Creación de plugins completa |
| Automate with Cron | Patrones reales de automatización |
| Work with Skills | Encontrar, instalar, usar y crear skills |
| Delegation Patterns | Cuándo y cómo usar subagentes |
| GitHub PR Review Agent | Revisor automático de PRs |

### 2.9 Developer Guide

| Página | Descripción |
|--------|-------------|
| Contributing | Dev setup, code style, PR process |
| Architecture | Subsistemas, flujos, dónde leer más |
| Agent Loop | AIAgent execution, API modes, tools, callbacks, fallbacks |
| Prompt Assembly | System prompt, cache stability, ephemeral layers |
| Context Compression & Caching | Compresión y caching |
| Gateway Internals | Boot, autorización, routing, delivery |
| Session Storage | SQLite, FTS5, session lineage |
| Provider Runtime | Resolución de providers, credenciales, API modes |
| Adding Tools | Cómo añadir un tool |
| Adding Providers | Cómo añadir un proveedor |
| Adding Platform Adapters | Cómo añadir una plataforma al gateway |
| Creating Skills | Formato SKILL.md y publicación |
| Extending the CLI | Widgets custom, keybindings, layout |
| Memory Provider Plugin | Plugin de memoria |
| Cron Internals | Implementación del scheduler |
| ACP Internals | Integración con editores |
| Environments, Benchmarks & Data Generation | RL training, trayectorias |
| Trajectory Format | Formato ShareGPT de trayectorias |
| Tool Gateway | API Gateway para tools (suscriptores Nous Portal) |
| Tools Runtime | Registry, dispatch, environments |
| LLMs.txt | Punto de entrada machine-readable |

### 2.10 Reference

| Página | Descripción |
|--------|-------------|
| CLI Commands | Referencia oficial de comandos de terminal |
| Slash Commands | Comandos interactivos CLI y messaging |
| Profile Commands | Comandos de perfiles |
| Environment Variables | Variables de entorno |
| Tools Reference | Tools agrupadas por toolset |
| Toolsets Reference | Toolsets core, composite, platform, dynamic |
| MCP Config Reference | Config keys, filtering, utility-tool policy |
| Model Catalog | Catálogo de modelos |
| Bundled Skills Catalog | ~90 skills incluidos |
| Optional Skills Catalog | ~60 skills instalables adicionales |
| FAQ & Troubleshooting | Preguntas frecuentes |

---

## 3. Mapa de equivalencias Hermes → Solviora

| Hermes | Solviora (existente) | Observaciones |
|--------|---------------------|---------------|
| `hermes` CLI command | `solviora` CLI command | ✅ Confirmado |
| `~/.hermes/` config dir | `~/.solviora/` | ✅ Confirmado (backwards compat con `HERMES_HOME`) |
| `hermes setup` | `solviora setup` | ✅ Confirmado |
| `hermes model` | `solviora model` | ⏳ Pending verification |
| `hermes config` | `solviora config` | ⏳ Pending verification |
| `hermes --tui` | `solviora --tui` | ⏳ Pending verification |
| `hermes --continue` | `solviora --resume` | ✅ Confirmado (ver cli-basics.mdx) |
| `hermes --yolo` | `solviora --yolo` | ⏳ Pending verification |
| `hermes doctor` | `solviora doctor` | ⏳ Pending verification |
| `hermes gateway` | `solviora gateway` | ⏳ Pending verification |
| `hermes tools` | `solviora tools` | ⏳ Pending verification |
| `hermes skills` | `solviora skills` | ⏳ Pending verification |
| `hermes pairing` | `solviora pairing` | ⏳ Pending verification |
| `hermes chat` | `solviora` (sin subcomando) | ⏳ Pending verification |
| `hermes update` | `solviora update` | 🔮 Future |
| `hermes acp` | `solviora acp` | 🔮 Future |
| `hermes sessions list` | `solviora sessions` | ⏳ Pending verification |
| Nous Research branding | Solviora branding | ✅ Reescribir completamente |
| AIAgent class (run_agent.py) | Misma base, fork | ⚠️ Verificar diferencias del fork |
| Messaging Gateway | `gateway/` | ⚠️ Verificar si está operativo |
| Skills System | `skills/` + `skills.mdx` | ⚠️ Verificar cobertura |
| Memory System | No documentado aún | ❌ No existe en docs Solviora |
| Cron Jobs | No documentado aún | ❌ No existe en docs Solviora |
| Security model | No documentado aún | ❌ No existe en docs Solviora |
| MCP Integration | No documentado aún | ❌ No existe en docs Solviora |
| Voice Mode | No documentado aún | ❌ No existe en docs Solviora |
| Browser/Web tools | No documentado aún | ❌ No existe en docs Solviora |
| Plugins | No documentado aún | ❌ No existe en docs Solviora |
| Provider catalog | `providers.mdx` | ⚠️ Existe pero hay que verificar exhaustividad |

---

## 4. Lista de contenido que se puede adaptar de inmediato

Basado en el código existente en el repo (ver `AGENTS.md`, `cli.py`, `run_agent.py`, `tools/`, `gateway/`):

| Contenido | Origen Hermes | Confianza | Notas |
|-----------|--------------|-----------|-------|
| Home hero + tagline | home page | Alta | Reescribir con branding Solviora |
| Feature: terminal-native | home + docs | Alta | Confirmado en `solviora` CLI |
| Feature: provider-agnostic | home + docs | Alta | El código soporta múltiples providers |
| Feature: built-in tools | home + docs | Alta | `tools/` existe con registry |
| Quickstart (install + first chat) | docs/getting-started/quickstart | Alta | `pip install solviora-agent` + `solviora` |
| Installation guide | docs/getting-started/installation | Alta | pip install, extras, WSL |
| CLI basics | docs/user-guide/cli | Alta | Comandos slash, sesiones, --model |
| Configuration (config.yaml + .env) | docs/user-guide/configuration | Alta | `~/.solviora/config.yaml` |
| Provider listing | docs/integrations/providers | Alta | El código soporta OpenAI, Anthropic, Gemini, etc. |
| Tools reference | docs/user-guide/features/tools | Alta | `tools/` autodiscovery |
| Skills system (conceptos generales) | docs/user-guide/features/skills | Alta | El código lee skills de `~/.solviora/skills/` |
| Profiles | docs/user-guide/profiles | Alta | `solviora -p <name>` confirmado |
| Session management | docs/user-guide/sessions | Alta | `solviora_state.py` con SQLite+FTS5 |
| Security (conceptos generales) | docs/user-guide/security | Alta | Código en `tools/approval.py` |
| FAQ / Troubleshooting | docs/reference/faq | Alta | Mismos patrones de error |
| Architecture overview | docs/developer-guide/architecture | Alta | Misma estructura de código |
| Adding tools guide | docs/developer-guide/adding-tools | Alta | Mismo sistema de registry |
| Creating skills guide | docs/developer-guide/creating-skills | Alta | Mismo formato SKILL.md |
| CLI commands reference | docs/reference/cli-commands | Alta | Basado en `hermes_cli/main.py` |
| Learning path | docs/getting-started/learning-path | Alta | Adaptable con rutas Solviora |
| Skin/theme system | docs/user-guide/features/skin-engine | Alta | `solviora_cli/skin_engine.py` existe |
| Tips & Best Practices | docs/guides/tips | Alta | Consejos generales de uso |

---

## 5. Lista de contenido que requiere validación antes de publicar

| Contenido | Riesgo | Razón |
|-----------|--------|-------|
| `solviora gateway setup` command | Medio | Verificar que el comando gateway existe con ese nombre exacto |
| `solviora model` interactive wizard | Medio | Verificar que el CLI tiene ese subcomando |
| `solviora doctor` diagnostic command | Medio | Verificar existencia |
| `solviora tools` tool config command | Medio | Verificar existencia |
| `solviora skills` hub commands | Medio | Verificar que skills hub está operativo |
| Messaging platform guides (Telegram, Discord, etc.) | Alto | Verificar qué plataformas están funcionales en el fork |
| Voice mode setup | Alto | Depende de dependencias extra (`faster-whisper`, etc.) |
| MCP integration | Alto | Verificar que `tools/mcp_tool.py` está operativo |
| Cron jobs system | Alto | Verificar `cron/` está funcional |
| Docker/SSH/Modal terminal backends | Alto | Verificar `tools/environments/` completo |
| Plugin system | Alto | Verificar `hermes_cli/plugins.py` adaptado |
| Memory providers (Honcho, Mem0, etc.) | Alto | Verificar `plugins/memory/` |
| ACP editor integration | Alto | Verificar `acp_adapter/` operativo |
| Batch processing | Medio | Verificar `batch_runner.py` |
| RL / Atropos environments | Alto | Nicho, verificar `environments/` |
| Kanban multi-agent system | Alto | Verificar si existe en el fork |
| Checkpoints & rollback | Medio | Verificar implementación |
| Context compression & caching | Medio | Verificar `agent/context_compressor.py` |
| Tool Gateway (Nous Portal) | Alto | Específico de Nous Portal, no aplica a Solviora |

---

## 6. Draft de copy nuevo para Solviora

### 6.1 Home Hero

> **Solviora Agent**
>
> Terminal-first AI agent for developers.
> One config, many providers, zero lock-in.
>
> Open source · MIT
>
> [Get Started] [Explore the CLI]

### 6.2 Value Proposition

**Propuesta de valor principal:**
> Un agente autónomo para terminal que vive en tu servidor, recuerda lo que aprende y se vuelve más capaz cuanto más lo usas. No es un copilot atado a un IDE ni un wrapper de chat alrededor de una sola API.

**Diferenciadores clave:**
- Terminal-native — corre donde trabajan los desarrolladores
- Provider-agnostic — cambia de LLM con un solo comando
- Persistent memory — aprende de tus proyectos y nunca olvida
- Extensible — tools, skills, plugins, MCP
- Privacy-first — tus datos se quedan en tu máquina

### 6.3 Feature Grid

| Feature | Descripción |
|---------|-------------|
| **Multi-provider** | OpenAI, Anthropic, Gemini, DeepSeek, Ollama, LM Studio, y más. Cambia con `solviora model`. |
| **Built-in tools** | 60+ herramientas: terminal, archivos, web, búsqueda, browser, código, y más. Descubrimiento automático. |
| **Persistent memory** | Memoria entre sesiones con búsqueda FTS5. Skills que el agente crea y mejora solo. |
| **Messaging gateway** | Telegram, Discord, Slack, WhatsApp, Signal, Email — 15+ plataformas desde un mismo gateway. |
| **Scheduled automations** | Cron en lenguaje natural para informes, backups y briefings. Corre desatendido. |
| **Subagent delegation** | Hijos aislados con sus propias conversaciones y terminales para pipelines paralelos. |
| **Sandboxing real** | Local, Docker, SSH, Modal, Daytona, Singularity — aislamiento por contenedor. |
| **Web & browser** | Búsqueda web, automatización de navegador, visión, generación de imágenes, TTS. |
| **MCP support** | Conecta servidores MCP externos para capacidades extendidas. |
| **Plugin system** | Plugins con tools, hooks y comandos CLI. Memoria y context engines intercambiables. |

### 6.4 Quickstart Draft

```markdown
# Quickstart

Instala Solviora Agent, configura tu proveedor y empieza a chatear.

## Prerrequisitos

- Python 3.11+
- Una API key de OpenAI, Anthropic, Google, o cualquier proveedor compatible

## Instalación

```bash
pip install solviora-agent
```

## Configura tu API key

```bash
# OpenAI
export OPENAI_API_KEY=sk-...

# Anthropic
export ANTHROPIC_API_KEY=sk-ant-...

# Google Gemini
export GOOGLE_API_KEY=...
```

## Primer chat

```bash
solviora
```

Verás el banner de bienvenida con tu modelo y proveedor. Escribe un mensaje y presiona Enter.

## Verificar que funciona

Pregunta algo concreto:

```
¿Cuál es mi uso de disco? Muestra los 5 directorios más grandes.
```

Si obtienes una respuesta sin errores, ya está listo.

## Siguientes pasos

- [Configuración avanzada](./configuration)
- [CLI básico](./cli-basics)
- [Tools disponibles](./tools)
- [Skills](./skills)
```

### 6.5 Docs Landing

> # Solviora Agent Docs
>
> ## What is Solviora Agent?
>
> Es un agente de IA autónomo para terminal. Corre donde sea — un VPS de $5, un clúster de GPUs, o infraestructura serverless. Habla con él desde Telegram mientras trabaja en una VM en la nube sin necesidad de hacer SSH.
>
> ## Quick Links
>
> | | |
> |---|---|
> | 🚀 Installation | Instala en 60 segundos en Linux, macOS o WSL2 |
> | 📖 Quickstart | Tu primera conversación en <5 minutos |
> | 🗺️ Learning Path | Encuentra la ruta adecuada para tu nivel |
> | ⚙️ Configuration | Config file, providers, modelos y opciones |
> | 💬 Messaging Gateway | Telegram, Discord, Slack, WhatsApp |
> | 🔧 Tools & Toolsets | 60+ herramientas integradas |
> | 🧠 Memory System | Memoria persistente entre sesiones |
> | 📚 Skills System | Conocimiento procedural que el agente crea y reusa |
> | 🔌 MCP Integration | Conecta servidores MCP externos |

### 6.6 Sidebar / Sitemap Sugerido

```
Getting Started
├── Quickstart
├── Installation
├── Learning Path
└── Updating

Using Solviora
├── CLI Basics
├── TUI (Terminal UI)
├── Configuration
├── Sessions
├── Profiles
└── Security

Core Features
├── Tools
├── Skills System
├── Memory
├── Context Files
├── Personality & SOUL.md
├── Plugins
└── Voice Mode

Automation
├── Cron Jobs
├── Delegation & Subagents
├── Code Execution
└── Hooks

Messaging Gateway
├── Overview
├── Telegram
├── Discord
├── Slack
├── WhatsApp
├── Signal
├── Email
└── Webhooks

Integrations
├── AI Providers
├── MCP (Model Context Protocol)
├── ACP (Editor Integration)
├── API Server
├── Provider Routing
└── Fallback Providers

Guides
├── Tips & Best Practices
├── Local LLMs
├── Daily Briefing Bot
├── Use as Python Library
├── Use MCP with Solviora
├── Automate with Cron
├── Work with Skills
└── Delegation Patterns

Developer Guide
├── Architecture
├── Agent Loop
├── Prompt Assembly
├── Adding Tools
├── Creating Skills
├── Adding Providers
├── Plugin Development
└── Contributing

Reference
├── CLI Commands
├── Slash Commands
├── Environment Variables
├── Tools Reference
├── Toolsets Reference
├── Model Catalog
├── Skills Catalog
└── FAQ
```

---

## 7. Propuesta de estructura MDX/Docusaurus para docs-site

### Árbol de archivos propuesto

```
docs-site/docs/
├── index.mdx                          # Docs landing page
├── quickstart.mdx                     # ✅ Existe, ampliar
├── installation.mdx                   # ✅ Existe, ampliar
├── learning-path.mdx                  # ✨ Nueva
├── updating.mdx                       # ✨ Nueva
│
├── cli-basics.mdx                     # ✅ Existe, ampliar
├── tui.mdx                            # ✨ Nueva
├── configuration.mdx                  # ✅ Existe, ampliar
├── sessions.mdx                       # ✨ Nueva
├── profiles.mdx                       # ✨ Nueva
├── security.mdx                       # ✨ Nueva
│
├── features/                          # ✨ Nuevo directorio
│   ├── overview.mdx                   # ✨ Nueva
│   ├── tools.mdx                      # ✨ Nueva (ampliar tools.mdx existente)
│   ├── skills.mdx                     # ✅ Existe, ampliar
│   ├── memory.mdx                     # ✨ Nueva
│   ├── context-files.mdx              # ✨ Nueva
│   ├── personality.mdx                # ✨ Nueva
│   ├── plugins.mdx                    # ✨ Nueva
│   ├── voice-mode.mdx                 # ✨ Nueva
│   ├── cron.mdx                       # ✨ Nueva
│   ├── delegation.mdx                 # ✨ Nueva
│   ├── code-execution.mdx             # ✨ Nueva
│   ├── browser.mdx                    # ✨ Nueva
│   └── vision.mdx                     # ✨ Nueva
│
├── messaging/                         # ✨ Nuevo directorio
│   ├── index.mdx                      # ✨ Nueva
│   ├── telegram.mdx                   # ✨ Nueva
│   ├── discord.mdx                    # ✨ Nueva
│   ├── slack.mdx                      # ✨ Nueva
│   ├── whatsapp.mdx                   # ✨ Nueva
│   ├── signal.mdx                     # ✨ Nueva
│   ├── email.mdx                      # ✨ Nueva
│   └── webhooks.mdx                   # ✨ Nueva
│
├── integrations/                      # ✨ Nuevo directorio
│   ├── providers.mdx                  # ✅ Existe, ampliar masivamente
│   ├── mcp.mdx                        # ✨ Nueva
│   ├── acp.mdx                        # ✨ Nueva
│   └── api-server.mdx                 # ✨ Nueva
│
├── guides/                            # ✨ Nuevo directorio
│   ├── tips.mdx                       # ✨ Nueva
│   ├── local-llm.mdx                  # ✨ Nueva
│   ├── daily-briefing-bot.mdx         # ✨ Nueva
│   ├── use-as-python-library.mdx      # ✨ Nueva
│   ├── use-mcp.mdx                    # ✨ Nueva
│   ├── automate-with-cron.mdx         # ✨ Nueva
│   ├── work-with-skills.mdx           # ✨ Nueva
│   └── delegation-patterns.mdx        # ✨ Nueva
│
├── developer-guide/                   # ✨ Nuevo directorio
│   ├── architecture.mdx               # ✨ Nueva
│   ├── agent-loop.mdx                 # ✨ Nueva
│   ├── prompt-assembly.mdx            # ✨ Nueva
│   ├── adding-tools.mdx               # ✨ Nueva
│   ├── creating-skills.mdx            # ✨ Nueva
│   ├── adding-providers.mdx           # ✨ Nueva
│   ├── plugin-development.mdx         # ✨ Nueva
│   └── contributing.mdx               # ✨ Nueva
│
├── reference/                         # ✨ Nuevo directorio
│   ├── cli-commands.mdx               # ✅ Existe, ampliar
│   ├── slash-commands.mdx             # ✨ Nueva
│   ├── environment-variables.mdx      # ✨ Nueva
│   ├── tools-reference.mdx            # ✅ Existe, ampliar
│   ├── toolsets-reference.mdx         # ✨ Nueva
│   ├── model-catalog.mdx              # ✨ Nueva
│   ├── skills-catalog.mdx             # ✨ Nueva
│   └── faq.mdx                        # ✅ Existe, ampliar
│
├── examples.mdx                       # ✅ Existe
├── troubleshooting.mdx                # ✅ Existe
├── wsl-smoke-test.mdx                 # ✅ Existe
└── about.mdx                          # ✅ Existe
```

### Sidebar actualizado (sidebars.ts)

```typescript
const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      type: "category",
      label: "Getting Started",
      collapsed: false,
      items: ["quickstart", "installation", "learning-path", "updating"],
    },
    {
      type: "category",
      label: "Using Solviora",
      collapsed: false,
      items: [
        "cli-basics",
        "tui",
        "configuration",
        "sessions",
        "profiles",
        "security",
      ],
    },
    {
      type: "category",
      label: "Core Features",
      collapsed: true,
      items: [
        "features/overview",
        "features/tools",
        "features/skills",
        "features/memory",
        "features/context-files",
        "features/personality",
        "features/plugins",
        "features/voice-mode",
      ],
    },
    {
      type: "category",
      label: "Automation",
      collapsed: true,
      items: [
        "features/cron",
        "features/delegation",
        "features/code-execution",
      ],
    },
    {
      type: "category",
      label: "Messaging Gateway",
      collapsed: true,
      items: [
        "messaging/index",
        "messaging/telegram",
        "messaging/discord",
        "messaging/slack",
        "messaging/whatsapp",
        "messaging/signal",
        "messaging/email",
        "messaging/webhooks",
      ],
    },
    {
      type: "category",
      label: "Integrations",
      collapsed: true,
      items: [
        "integrations/providers",
        "integrations/mcp",
        "integrations/acp",
        "integrations/api-server",
      ],
    },
    {
      type: "category",
      label: "Guides",
      collapsed: true,
      items: [
        "guides/tips",
        "guides/local-llm",
        "guides/daily-briefing-bot",
        "guides/use-as-python-library",
        "guides/use-mcp",
        "guides/automate-with-cron",
        "guides/work-with-skills",
        "guides/delegation-patterns",
      ],
    },
    {
      type: "category",
      label: "Developer Guide",
      collapsed: true,
      items: [
        "developer-guide/architecture",
        "developer-guide/agent-loop",
        "developer-guide/prompt-assembly",
        "developer-guide/adding-tools",
        "developer-guide/creating-skills",
        "developer-guide/adding-providers",
        "developer-guide/plugin-development",
        "developer-guide/contributing",
      ],
    },
    {
      type: "category",
      label: "Reference",
      collapsed: true,
      items: [
        "reference/cli-commands",
        "reference/slash-commands",
        "reference/environment-variables",
        "reference/tools-reference",
        "reference/toolsets-reference",
        "reference/model-catalog",
        "reference/skills-catalog",
        "reference/faq",
      ],
    },
    {
      type: "category",
      label: "Help",
      collapsed: true,
      items: [
        "examples",
        "troubleshooting",
        "wsl-smoke-test",
        "about",
      ],
    },
  ],
};
```

### Consideraciones técnicas

1. **i18n**: La estructura de archivos debe duplicarse en `i18n/es/docusaurus-plugin-content-docs/current/`. Los nuevos archivos deben tener su versión en español.

2. **Enrutamiento**: Usar slugs tipo `features/tools` en lugar de carpetas anidadas con `index.mdx` para consistencia con la estructura actual.

3. **Sidebar**: El archivo `sidebars.ts` se puede mantener plano (las categorías como objeto plano) o usar autogeneración por directorio. Para el volumen actual, plano es más explícito.

4. **Home page**: La página principal (`src/pages/index.tsx`) necesita una ampliación significativa con más feature cards, call-to-action, y posiblemente una sección de "how it works".

5. **llms.txt**: Considerar generar un `/docs/llms.txt` y `/docs/llms-full.txt` para consumo por LLMs, siguiendo el patrón de Hermes.

---

## 8. Tabla final: source topic → proposed Solviora page → status

### Getting Started

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| Hero / Tagline | Home page `src/pages/index.tsx` | **ready** |
| Installation | `docs/installation.mdx` | **ready** (ampliar) |
| Quickstart | `docs/quickstart.mdx` | **ready** (ampliar) |
| Learning Path | `docs/learning-path.mdx` | **ready** |
| Updating | `docs/updating.mdx` | **ready** |
| Termux (Android) | `docs/installation.mdx` (sección) | **needs validation** |
| Nix Setup | `docs/installation.mdx` (sección) | **needs validation** |

### Using Solviora

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| CLI | `docs/cli-basics.mdx` | **ready** (ampliar) |
| TUI (Ink) | `docs/tui.mdx` | **ready** |
| Configuration | `docs/configuration.mdx` | **ready** (ampliar) |
| Configuring Models | `docs/configuration.mdx` (sección) | **ready** |
| Sessions | `docs/sessions.mdx` | **ready** |
| Profiles | `docs/profiles.mdx` | **ready** |
| Git Worktrees | `docs/guides/tips.mdx` (sección) | **needs validation** |
| Docker Backend | `docs/features/tools.mdx` (sección) | **needs validation** |
| Security | `docs/security.mdx` | **ready** |
| Checkpoints & Rollback | `docs/features/overview.mdx` (sección) | **needs validation** |

### Core Features

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| Features Overview | `docs/features/overview.mdx` | **ready** |
| Tools | `docs/features/tools.mdx` | **ready** |
| Skills System | `docs/features/skills.mdx` | **ready** (ampliar) |
| Curator | `docs/features/skills.mdx` (sección) | **needs validation** |
| Memory | `docs/features/memory.mdx` | **ready** |
| Memory Providers | `docs/features/memory.mdx` (sección) | **needs validation** |
| Context Files | `docs/features/context-files.mdx` | **ready** |
| Context References | `docs/features/context-files.mdx` (sección) | **ready** |
| Personality & SOUL.md | `docs/features/personality.mdx` | **ready** |
| Plugins | `docs/features/plugins.mdx` | **needs validation** |
| Built-in Plugins | `docs/features/plugins.mdx` (sección) | **needs validation** |
| Voice Mode | `docs/features/voice-mode.mdx` | **needs validation** |
| Browser | `docs/features/browser.mdx` | **needs validation** |
| Vision | `docs/features/vision.mdx` | **needs validation** |
| Image Generation | `docs/features/vision.mdx` (sección) | **needs validation** |
| TTS | `docs/features/voice-mode.mdx` (sección) | **needs validation** |

### Automation

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| Cron Jobs | `docs/features/cron.mdx` | **needs validation** |
| Delegation | `docs/features/delegation.mdx` | **needs validation** |
| Kanban Multi-Agent | `docs/guides/delegation-patterns.mdx` | **future** |
| Persistent Goals | `docs/features/overview.mdx` (sección) | **future** |
| Code Execution | `docs/features/code-execution.mdx` | **needs validation** |
| Hooks | `docs/features/hooks.mdx` | **needs validation** |
| Batch Processing | `docs/developer-guide/architecture.mdx` (sección) | **needs validation** |

### Messaging Gateway

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| Overview | `docs/messaging/index.mdx` | **needs validation** |
| Telegram | `docs/messaging/telegram.mdx` | **needs validation** |
| Discord | `docs/messaging/discord.mdx` | **needs validation** |
| Slack | `docs/messaging/slack.mdx` | **needs validation** |
| WhatsApp | `docs/messaging/whatsapp.mdx` | **needs validation** |
| Signal | `docs/messaging/signal.mdx` | **needs validation** |
| Email | `docs/messaging/email.mdx` | **needs validation** |
| SMS | `docs/messaging/sms.mdx` | **future** |
| Matrix | `docs/messaging/matrix.mdx` | **needs validation** |
| Mattermost | `docs/messaging/mattermost.mdx` | **needs validation** |
| Home Assistant | `docs/messaging/homeassistant.mdx` | **future** |
| Webhooks | `docs/messaging/webhooks.mdx` | **needs validation** |

### Integrations

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| Providers | `docs/integrations/providers.mdx` | **ready** (ampliar masivamente) |
| MCP | `docs/integrations/mcp.mdx` | **needs validation** |
| ACP (Editor) | `docs/integrations/acp.mdx` | **needs validation** |
| API Server | `docs/integrations/api-server.mdx` | **needs validation** |
| Provider Routing | `docs/integrations/providers.mdx` (sección) | **needs validation** |
| Fallback Providers | `docs/integrations/providers.mdx` (sección) | **needs validation** |
| Credential Pools | `docs/configuration.mdx` (sección) | **needs validation** |

### Guides

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| Tips & Best Practices | `docs/guides/tips.mdx` | **ready** |
| Local LLMs on Mac | `docs/guides/local-llm.mdx` | **ready** |
| Daily Briefing Bot | `docs/guides/daily-briefing-bot.mdx` | **ready** |
| Team Telegram Assistant | `docs/guides/team-telegram.mdx` | **needs validation** |
| Use as Python Library | `docs/guides/use-as-python-library.mdx` | **ready** |
| Use MCP with Solviora | `docs/guides/use-mcp.mdx` | **needs validation** |
| Use Voice Mode | `docs/guides/use-voice-mode.mdx` | **needs validation** |
| Use SOUL.md | `docs/guides/use-soul.mdx` | **ready** |
| Build a Plugin | `docs/guides/plugin-development.mdx` | **needs validation** |
| Automate with Cron | `docs/guides/automate-with-cron.mdx` | **needs validation** |
| Work with Skills | `docs/guides/work-with-skills.mdx` | **ready** |
| Delegation Patterns | `docs/guides/delegation-patterns.mdx` | **needs validation** |
| GitHub PR Review Agent | `docs/guides/github-pr-review.mdx` | **future** |

### Developer Guide

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| Architecture | `docs/developer-guide/architecture.mdx` | **ready** |
| Agent Loop | `docs/developer-guide/agent-loop.mdx` | **ready** |
| Prompt Assembly | `docs/developer-guide/prompt-assembly.mdx` | **ready** |
| Context Compression & Caching | `docs/developer-guide/prompt-assembly.mdx` (sección) | **needs validation** |
| Gateway Internals | `docs/developer-guide/architecture.mdx` (sección) | **needs validation** |
| Session Storage | `docs/developer-guide/architecture.mdx` (sección) | **ready** |
| Provider Runtime | `docs/developer-guide/architecture.mdx` (sección) | **needs validation** |
| Adding Tools | `docs/developer-guide/adding-tools.mdx` | **ready** |
| Adding Providers | `docs/developer-guide/adding-providers.mdx` | **ready** |
| Adding Platform Adapters | `docs/developer-guide/architecture.mdx` (sección) | **future** |
| Creating Skills | `docs/developer-guide/creating-skills.mdx` | **ready** |
| Extending the CLI | `docs/developer-guide/extending-cli.mdx` | **future** |
| Contributing | `docs/developer-guide/contributing.mdx` | **ready** |
| RL / Environments / Trajectories | `docs/developer-guide/rl-training.mdx` | **future** |

### Reference

| Source Topic (Hermes) | Proposed Solviora Page | Status |
|-----------------------|----------------------|--------|
| CLI Commands | `docs/reference/cli-commands.mdx` | **ready** (ampliar) |
| Slash Commands | `docs/reference/slash-commands.mdx` | **ready** |
| Profile Commands | `docs/reference/cli-commands.mdx` (sección) | **ready** |
| Environment Variables | `docs/reference/environment-variables.mdx` | **ready** |
| Tools Reference | `docs/reference/tools-reference.mdx` | **ready** (ampliar) |
| Toolsets Reference | `docs/reference/toolsets-reference.mdx` | **ready** |
| MCP Config Reference | `docs/reference/mcp-config.mdx` | **needs validation** |
| Model Catalog | `docs/reference/model-catalog.mdx` | **ready** |
| Bundled Skills Catalog | `docs/reference/skills-catalog.mdx` | **ready** |
| Optional Skills Catalog | `docs/reference/optional-skills-catalog.mdx` | **needs validation** |
| FAQ & Troubleshooting | `docs/reference/faq.mdx` | **ready** (ampliar) |

---

## Resumen cuantitativo

| Estado | Cantidad | Acción |
|--------|----------|--------|
| **ready** | ~45 páginas/secciones | Se puede adaptar de inmediato con branding Solviora |
| **needs validation** | ~35 páginas/secciones | Requiere verificar el código del fork antes de publicar |
| **future** | ~8 páginas/secciones | Funcionalidad no confirmada o nicho, posponer |
| **Total inventariado** | ~88 páginas/secciones | Cobertura completa de la docs de Hermes |

### Prioridad recomendada para implementación

1. **Fase 1 (ready)** — Home hero, Quickstart, Installation, CLI Basics, Configuration, Providers, Tools, Skills, Sessions, Profiles, Security, FAQ
2. **Fase 2 (ready)** — Learning Path, Architecture, Adding Tools, Creating Skills, Tips, Context Files, Personality, Memory, CLI Commands, Reference pages restantes
3. **Fase 3 (needs validation)** — Messaging platforms, MCP, Voice, Cron, Plugins, Docker backend, Gateway guides
4. **Fase 4 (needs validation)** — ACP, Batch processing, Hooks, Memory providers, TTS, Browser, Vision, Image gen
5. **Fase 5 (future)** — Kanban, RL/Atropos, Platform adapters, GitHub PR agent, SMS, Home Assistant
