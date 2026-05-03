# PRD — Solviora Documentation Website

> **Status:** Final · **Date:** 2026-05-02  
> **Product:** `docs.solviora.dev` — static documentation portal + future skills/plugins directory  
> **NOT:** dashboard, chat, operational console, or runtime-connected app

---

## 1 · Product Definition

A Docusaurus 3 static site that serves as the **official documentation** for Solviora Agent. In a future phase it will host a browsable **skills & plugins directory** powered by static JSON catalogs.

The site is **completely isolated** from the agent runtime. Deleting it has zero effect on CLI, gateway, or agent behavior.

### Target users

| Persona | Needs |
|---------|-------|
| New user | Install, configure, first run in < 5 min |
| CLI power user | Deep reference on tools, skills, providers |
| Platform integrator | Gateway setup, messaging adapter config |
| Skill/plugin author | Authoring guide, catalog submission process |
| Spanish-speaking user | Full ES documentation, not machine-translated afterthought |

---

## 2 · Closed Decisions (non-negotiable)

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | **Docusaurus 3.x** as framework (pinned in `package.json`) | MDX, built-in i18n, search plugin, static generation, mature ecosystem |
| 2 | **Bilingual ES/EN from day 1** | **Política pública de Solviora:** todas las URLs públicas deben existir bajo `/en/...` y `/es/...`. **Nota de implementación:** Docusaurus no prefija el locale por defecto, por lo que la implementación usará configuración adicional y/o reglas de hosting para cumplir esa política. Internamente: `docs/` para EN, `i18n/es/docusaurus-plugin-content-docs/current/` para ES — layout estándar Docusaurus sin hacks |
| 3 | **Separate folder `docs-site/`** | Own `package.json`, own build/deploy, no imports from agent code |
| 4 | **No runtime connection** | Zero access to `~/.solviora/`, `state.db`, CLI, gateway, or agent process |
| 5 | **No dashboard, no chat, no logs** | This is documentation only. Operational UIs live in `/web/` |
| 6 | **Color palette: "Teal & Ink"** | Solviora Teal `#2BA8A0` accent, Ink `#0F1117` background. No neon, no cyberpunk, no purple gradients |
| 7 | **Dark mode default** | Developer audience, respect `prefers-color-scheme` |
| 8 | **Typography: Inter + JetBrains Mono** | Inter for body/headings, JetBrains Mono for code blocks |
| 9 | **Static JSON for catalogs** | Skills and plugins catalogs are JSON files generated at build time from repo data |
| 10 | **Search: @easyops-cn/docusaurus-search-local** | Zero-cost, no external service, works offline |
| 11 | **Content governance** | No feature ships without EN + ES docs or an explicitly approved placeholder. Enforced by CI |

---

## 3 · Information Architecture

```
solviora.dev/
├── Home (landing)
├── /en/docs/ · /es/docs/
│   ├── getting-started/
│   │   ├── quickstart
│   │   ├── installation
│   │   └── first-steps
│   ├── guides/
│   │   ├── cli-basics
│   │   ├── configuration
│   │   ├── providers
│   │   ├── tools
│   │   ├── skills
│   │   └── plugins
│   ├── reference/
│   │   ├── cli-commands
│   │   ├── tools-reference
│   │   └── configuration-reference
│   ├── examples/
│   │   └── (real-world usage examples)
│   └── troubleshooting/
├── /en/skills/ · /es/skills/        ← Phase 2
│   └── (browsable skills directory)
├── /en/plugins/ · /es/plugins/      ← Phase 2
│   └── (browsable plugins directory)
├── /en/about/ · /es/about/
└── /en/faq/ · /es/faq/
```

### Navigation

**Navbar:** `Docs · Skills · Plugins · FAQ · About`  
Skills and Plugins nav items link to a "Coming soon" page in Phase 1.

**Sidebar (docs):** Two levels max. Flat within each section. Collapsed by default.

**Footer:** GitHub · Discord/Community · License · Privacy

---

## 4 · MVP Page Inventory (Phase 1)

Only pages that ship in the first release. Each page exists in both `/en/` and `/es/`.

| Page | Content | Priority |
|------|---------|----------|
| **Home** | Hero, tagline, 3 value props, CTA to quickstart, feature highlights | P0 |
| **Quickstart** | `pip install` → first chat in 3 commands | P0 |
| **Installation** | pip, Docker, Termux, Nix, from source. Prerequisites per OS | P0 |
| **CLI Basics** | Interactive loop, slash commands, input modes | P0 |
| **Configuration** | `config.yaml` structure, `.env` for secrets, profiles | P0 |
| **Providers** | Supported AI providers, model routing, credential setup | P0 |
| **Tools** | Concept overview, toolset system, enabling/disabling | P0 |
| **Skills** | What skills are, using built-in skills, installing optional skills | P0 |
| **CLI Commands Reference** | Auto-generated or curated table of all slash commands | P1 |
| **Tools Reference** | Per-tool schema + usage examples | P1 |
| **Configuration Reference** | Full `config.yaml` schema with defaults | P1 |
| **Examples** | 3–5 real-world usage scenarios with code | P1 |
| **Troubleshooting** | Common errors, FAQ-style, searchable | P1 |
| **FAQ** | Top 10–15 questions | P1 |
| **About** | What is Solviora, relationship to Hermes, license, credits | P1 |

### MVP exclusions (intentionally deferred)

These topics exist in the agent but are **not** documented in Phase 1:

- Gateway setup & messaging platforms
- Cron/scheduler
- Memory providers
- Context compression
- MCP server integration
- Browser automation deep-dive
- RL training environments
- Kanban multi-agent coordination
- Skills/Plugins browsable directory
- Plugin authoring guide
- API server mode
- ACP adapter (editor integration)
- TUI (terminal UI)

**Rule:** If a feature needs a dedicated guide longer than a paragraph in an existing page, it's Phase 2.

---

## 5 · Visual Identity

### Color palette: "Teal & Ink"

| Token | Dark mode | Light mode | Usage |
|-------|-----------|------------|-------|
| Background | `#0F1117` | `#FAFBFC` | Page background |
| Surface | `#161922` | `#FFFFFF` | Cards, sidebar |
| Text primary | `#E8E9ED` | `#1A1D27` | Body text |
| Text secondary | `#8B8FA3` | `#5C6078` | Muted text |
| Accent | `#2BA8A0` | `#238F88` | Links, CTAs, highlights |
| Accent hover | `#3BC0B8` | `#1D7A74` | Interactive states |
| Code background | `#1A1D27` | `#F0F2F5` | Code blocks |
| Success | `#34D399` | `#059669` | Status indicators |
| Error | `#F87171` | `#DC2626` | Error states |

### Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Body | Inter | 400 | 16px / 1.6 line-height |
| H1 | Inter | 700 | 40px |
| H2 | Inter | 600 | 28px |
| H3 | Inter | 600 | 22px |
| Code | JetBrains Mono | 400 | 14px |
| Nav | Inter | 500 | 14px |

### Component styling

- **Code blocks:** Dark with syntax highlighting (Prism, `oneDark` theme in dark mode, `oneLight` in light)
- **Callouts/Admonitions:** Teal left border, themed `info`/`warning`/`danger`/`tip`
- **Cards:** Subtle border `#2A2D3A`, rounded `8px`, no shadow or minimal `0 1px 3px rgba(0,0,0,.2)`
- **Links:** Accent color, underline on hover only
- **Buttons (CTA):** Teal background `#2BA8A0`, white text, rounded `6px`, hover darken to `#238F88`

### Prohibited

- No neon, no glow effects, no purple gradients
- No cyberpunk or retro-futuristic aesthetic
- No animated backgrounds or particle effects
- No hero illustrations of robots/AI (use abstract patterns or terminal screenshots)

---

## 6 · Technical Stack

| Layer | Choice | Version |
|-------|--------|---------|
| Framework | Docusaurus | 3.x (pinned in `package.json`) |
| Content | MDX | built-in |
| Styling | CSS custom properties (Infima overrides) | — |
| Search | @easyops-cn/docusaurus-search-local | latest |
| Diagrams | @docusaurus/theme-mermaid | built-in |
| i18n | Docusaurus built-in i18n | — |
| Build | Node.js + npm | Node ≥ 20 |
| Deploy | Static hosting (Vercel / Cloudflare Pages / Netlify / GitHub Pages) | — |
| Catalogs | Static JSON generated at build time | — |

### Dependency policy

- Zero runtime dependencies beyond Docusaurus and its plugins
- No database, no server-side rendering, no API calls at runtime
- All data embedded at build time

---

## 7 · i18n Architecture

### Route structure

**La política pública de Solviora exige URLs localizadas con prefijo `/en/` y `/es/`.**  
**Docusaurus no hace esto así por defecto para el locale principal**, por lo que la implementación usará configuración adicional y/o reglas de hosting para cumplir esa política.

**Internamente se seguirá el layout estándar de Docusaurus:** `docs/` para EN y `i18n/es/docusaurus-plugin-content-docs/current/` para ES, evitando hacks innecesarios en la organización del contenido.

```
docs-site/
├── docs/                    ← EN content (default locale, standard Docusaurus location)
│   ├── getting-started/
│   ├── guides/
│   └── ...
└── i18n/
    └── es/
        ├── docusaurus-plugin-content-docs/
        │   └── current/     ← ES MDX content (mirrors docs/ structure)
        │       ├── getting-started/
        │       ├── guides/
        │       └── ...
        └── code.json        ← ES UI chrome translations
```

### Enabling strict `/en/` prefixes

Docusaurus no prefija el locale por defecto. Build output por defecto: EN en `/docs/...`, ES en `/es/docs/...`. Para cumplir la política pública, el equipo de implementación elegirá una de estas estrategias:

1. **`routeLegacy` config** (Docusaurus 3.x): maps the unprefixed default locale to the prefixed path with a redirect.
2. **Hosting-level redirect**: configure the host (Vercel, Cloudflare, etc.) to redirect `/docs/*` → `/en/docs/*`.
3. **Custom plugin**: a minimal Docusaurus plugin that adds the prefix during build.

```js
// docusaurus.config.ts (minimum viable i18n config)
i18n: {
  defaultLocale: 'en',
  locales: ['en', 'es'],
},
```

El equipo de implementación elige la estrategia de prefijo que mejor se adapte al hosting provider.

### Principles

1. **EN is the source of truth** — write EN first, translate to ES
2. **Product policy: public URLs use `/en/...` and `/es/...`** — implementation achieves this via config or hosting redirects, not by reorganizing Docusaurus internals
3. **Shared slugs** — `/en/docs/getting-started/quickstart` and `/es/docs/getting-started/quickstart` use the same slug
4. **UI chrome in `code.json`** — navbar, footer, labels, button text (ES in `i18n/es/code.json`)
5. **Content in MDX** — full paragraphs, not sentence-by-sentence translation
6. **`hreflang` auto-generated** by Docusaurus for SEO
7. **Language switcher** in navbar, persisted in localStorage
8. **No fallback to EN for missing ES pages** — if ES is missing, the build fails or CI blocks the PR. Phase 1 ships EN+ES together

---

## 8 · Folder Structure

```
docs-site/
├── docusaurus.config.ts       # Site config, navbar, footer, plugins, i18n
├── sidebars.ts                # Doc sidebar definition
├── package.json               # Independent from root package.json
├── tsconfig.json
├── static/
│   ├── img/                   # Logo, og-image, favicon
│   └── robots.txt
├── src/
│   ├── css/
│   │   └── custom.css         # Infima overrides, Teal & Ink palette
│   ├── components/            # Shared MDX components
│   │   ├── ToolCard.tsx       # Tool reference card (Phase 1)
│   │   ├── Badge.tsx          # Status/category badges
│   │   └── TabCode.tsx        # Tabbed code blocks (pip/docker/nix)
│   └── pages/
│       ├── index.tsx          # Home/landing
│       ├── skills.tsx         # "Coming soon" placeholder (Phase 1)
│       ├── plugins.tsx        # "Coming soon" placeholder (Phase 1)
│       ├── about.tsx
│       └── faq.tsx
├── docs/                      # EN content (default locale, standard Docusaurus location)
│   ├── getting-started/
│   ├── guides/
│   ├── reference/
│   ├── examples/
│   └── troubleshooting/
├── data/
│   └── tools.json             # Tool metadata for reference pages
├── scripts/
│   └── generate-catalog.mjs   # Build-time script to generate JSON from repo
└── i18n/
    └── es/
        ├── docusaurus-plugin-content-docs/
        │   └── current/       # ES MDX content (mirrors docs/ structure)
        │       ├── getting-started/
        │       ├── guides/
        │       ├── reference/
        │       ├── examples/
        │       └── troubleshooting/
        └── code.json          # ES UI chrome
```

### Isolation rules

| Rule | Enforcement |
|------|-------------|
| No imports from `../agent/`, `../tools/`, `../gateway/` | `tsconfig.json` `paths` scoped to `./src/**` |
| No imports from `../web/` | Same scoping |
| No runtime API calls to agent | No `fetch()` to localhost or `~/.solviora/` anywhere |
| No reading `state.db` or config files | Static JSON only |
| Own `package.json` | Separate dependency tree, separate CI |
| Build output: `docs-site/build/` | Deployed independently |

**Deletion test:** `rm -rf docs-site/` has zero impact on agent, CLI, gateway, or web dashboard.

---

## 9 · Home Page (Landing)

### Hero section

```
Solviora Agent
Terminal-first AI agent for developers.

[Get Started →]   [View on GitHub]
```

- **Tagline:** "Terminal-first AI agent for developers."
- **Sub-text:** Brief description, no inflated claims. Example:  
  "Autonomous AI agent that runs in your terminal. Browse the web, execute code, manage files, automate tasks — all from the command line."
- **Value props (3 cards):**
  1. **Terminal-native** — Runs in your CLI. No browser, no Electron.
  2. **Tool ecosystem** — Built-in tools for web, files, code, browser automation, and more.
  3. **Extensible** — Skills and plugins to adapt to your workflow.
- **No counts in hero.** No "60+ tools" or "15 platforms." Use qualitative language.
- **CTA:** Primary button to quickstart, secondary to GitHub repo

### Feature highlights (below fold)

4–6 feature cards with icon + short description. No screenshots of the agent running (too much setup context). Use terminal-style code snippets or abstract icons.

---

## 10 · Content Guidelines

### Voice & tone

- **Direct and technical.** No marketing fluff.
- **Second person ("you").** Not "the user" or "users."
- **Short paragraphs.** 3–4 sentences max before a code example or list.
- **Code first.** Show the command/output, then explain.
- **Honest about limitations.** If something requires an API key, say so upfront.

### Bilingual quality

- EN content is original, not machine-translated.
- ES content is reviewed for natural phrasing, not literal translation.
- Technical terms stay in English when that's the industry norm (e.g., "toolset," "plugin," "MCP server").
- Locale-specific examples allowed (e.g., ES page can reference Spanish-language APIs if relevant).

### Code examples

- Always show the exact CLI command and expected output.
- Use `TabCode` component for multi-install methods (pip / Docker / Nix).
- Mark optional steps with "Optional" callout.
- Never show real API keys or tokens — use `YOUR_API_KEY_HERE`.

---

## 11 · Phase Plan

### Phase 1 — MVP (ship first, iterate later)

**Goal:** Users can install, configure, and run Solviora from docs alone.

| Deliverable | Scope |
|-------------|-------|
| Docusaurus project scaffold | `docs-site/` with config, palette, fonts |
| Home page | Hero, value props, CTAs |
| 6 core guides (EN + ES) | Quickstart, Installation, CLI Basics, Configuration, Providers, Tools |
| Skills guide (EN + ES) | What skills are, how to use them |
| 3 reference pages (EN + ES) | CLI commands, tools reference, config reference |
| Examples (EN + ES) | 3 real-world scenarios |
| Troubleshooting + FAQ (EN + ES) | Common issues, top questions |
| About page (EN + ES) | Project identity, license |
| Skills/Plugins placeholders | "Coming soon" pages |
| Search | Local search indexed on build |
| Deploy config | Vercel/Cloudflare/GitHub Pages ready |

**Estimated pages:** ~25 unique pages × 2 locales = ~50 pages total

### Phase 2 — Directory & Advanced Docs

**Goal:** Browsable ecosystem + documentation for power users.

| Deliverable | Scope |
|-------------|-------|
| Skills directory | Browsable catalog with `SkillCard` components, filter by category |
| Plugins directory | Browsable catalog with `PluginCard` components |
| Plugin authoring guide | How to create and submit a plugin |
| Gateway docs | Platform setup, messaging adapters |
| Advanced guides | Cron, memory providers, context compression, MCP, browser automation |
| API server docs | OpenAI-compatible endpoint setup |
| TUI docs | Terminal UI features and customization |
| Build-time catalog generator | Script to auto-generate `skills.json` and `plugins.json` from repo |

### Phase 3 — Community & Contributions

| Deliverable | Scope |
|-------------|-------|
| Contribution guide | How to write docs, submit PRs |
| Changelog / Release notes | Per-version highlights |
| Versioned docs | Docusaurus versioning for major releases |
| Community pages | Discord/Community links, governance |

---

## 12 · Success Metrics

| Metric | Target (3 months post-launch) |
|--------|-------------------------------|
| Quickstart completion rate | > 60% of visitors reach Configuration page |
| Bounce rate on Home | < 50% |
| Search usage | > 30% of sessions use search |
| ES traffic share | > 15% of total pageviews |
| Time to first successful run | < 5 minutes from landing to first agent response |
| Zero runtime coupling | CI test: delete `docs-site/` → all agent tests pass |

---

## 13 · Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Content drift from code | Docs show wrong flags/config | Build-time script extracts CLI `--help` and config schema into reference pages |
| i18n debt accumulates | ES pages fall behind EN | Require EN+ES in same PR for content changes; CI check for missing ES files |
| Missing bilingual content | Feature ships without ES docs | Content governance rule (§2, decision #11): no feature enters the site without EN+ES docs or an explicitly approved placeholder. CI enforces |
| Scope creep (Phase 2 in Phase 1) | Delayed launch | Strict page inventory in §4; new pages require explicit scope change |
| Inherited Hermes numbers | Misleading claims | Use qualitative language; never publish exact counts without build-time validation |
| Deploy coupling | Docs break when agent changes | Separate CI pipelines; docs deploy independently |
| Docusaurus upgrade friction | Security patches blocked | Pin Docusaurus minor version; upgrade in dedicated PR each quarter |

---

## 14 · Build & Deploy

### Local development

```bash
cd docs-site
npm install
npm start          # Dev server at localhost:3000
npm run build      # Static output in build/
npm run serve      # Preview production build
```

### CI/CD

```yaml
# .github/workflows/docs.yml (or equivalent)
on:
  push:
    paths: [docs-site/**]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: cd docs-site && npm ci && npm run build
      - # Deploy build/ to hosting provider
```

### Deployment targets (pick one)

- **Vercel:** Zero-config for Docusaurus, preview deploys on PRs
- **Cloudflare Pages:** Fast global CDN, free tier generous
- **GitHub Pages:** Free for public repos, direct from `gh-pages` branch
- **Netlify:** Similar to Vercel, good form-handling if needed later

---

## 15 · Open Questions (to resolve before Phase 1 implementation)

| # | Question | Default if unresolved |
|---|----------|-----------------------|
| 1 | Domain: `docs.solviora.dev` or `solviora.dev/docs`? | `docs.solviora.dev` (subdomain) |
| 2 | Hosting provider preference? | Vercel (fastest setup) |
| 3 | Logo and wordmark ready? | Use text-only "Solviora" until logo delivered |
| 4 | Should tools reference be auto-generated or hand-written? | Hand-written with build-time validation |
| 5 | Community platform: Discord, Discussions, or other? | Link placeholder until decided |

---

*End of PRD. This document replaces all previous website design drafts for Solviora.*
