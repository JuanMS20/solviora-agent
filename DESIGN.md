---
version: "1.0"
name: "Solviora Design System"
description: "Single source of truth for ALL web surfaces — landing, docs, and future properties."
inspired-by: "HOSHI ONE"
---

# Solviora Design System

## Brand Personality

- **Professional** — This is infrastructure software for developers. Not a toy, not a demo.
- **Editorial** — Typography-led. Generous whitespace. Magazine-grade hierarchy.
- **Sober** — Restrained palette. No neon, no gradients, no decorative clutter.
- **Technical** — Code is a first-class citizen. Terminal mockups, monospace surfaces, CLI references.
- **Premium** — Tight letter-spacing, high-contrast choices, intentional negative space.

---

## Visual Tone

| Attribute | Direction |
|-----------|-----------|
| Energy | Controlled, deliberate |
| Temperature | Warm (canvas) + cold (ink) contrast |
| Density | Generous spacing, low density |
| Depth | Flat with hairline borders (Vercel method) |
| Motion | 150ms transitions, subtle |
| Voice | Direct, technical, confident |

---

## Design Principles

1. **One system, every surface.** No page gets its own private style. If you change a token, you change it everywhere.
2. **Typography is the interface.** Hierarchy comes from type scale and letter-spacing, not color or decoration.
3. **Borders, not shadows.** Surface separation comes from hairline borders (`0px 0px 0px 1px`), not drop shadows.
4. **Accent is scarce.** The red accent (#D81A1D) is used for emphasis, active states, and select highlights only. Most of the UI lives in neutral tones.
5. **Dark mode is not an afterthought.** Every token has a dark pair. Night mode is the default for code-focused surfaces.
6. **Radius has intent.** Buttons at 0px (sharp, editorial). Cards at 2px (subtle softening). Badges at 9999px (pills). No random rounding.
7. **Consistency over novelty.** If it works for landing, it works for docs. No section-level style experiments.

---

## Anti-Patterns (Forbidden)

| Anti-pattern | Why |
|--------------|-----|
| Purple/blue gradient hero sections | Generic AI startup aesthetic |
| Neon glow effects | Clashes with sober editorial direction |
| Three clone feature columns | Lazy layout without information hierarchy |
| Icons inside colored circles | Creates visual noise without meaning |
| Template-feeling sections | Each section must feel part of the same product |
| Landing and docs look different | They're the SAME brand |
| Drop shadows on everything | Use hairline borders instead |
| Random radius values | All radii come from the scale |
| Hardcoded colors in page CSS | Every color comes from a token |

---

## Typography

### Font Stack

| Role | Font | Weights | Fallback |
|------|------|---------|----------|
| Display / Headings | Oswald | 400, 500, 600, 700 | system-ui, sans-serif |
| Body text | Inter | 400, 500, 600 | system-ui, sans-serif |
| Code surfaces | JetBrains Mono | 400, 500 | 'Fira Code', monospace |

### Type Scale

```css
/* Oswald — Uppercase for hero, sentence case for docs headings */
--solv-font-display: 'Oswald', system-ui, sans-serif;

/* Inter — All body copy, labels, UI text */
--solv-font-body: 'Inter', system-ui, sans-serif;

/* JetBrains Mono — Code blocks, inline code, terminal */
--solv-font-code: 'JetBrains Mono', 'Fira Code', monospace;
```

| Token | Size | Weight | Line-Height | Letter-Spacing | Case |
|-------|------|--------|-------------|----------------|------|
| `--solv-text-hero` | clamp(3rem, 6vw, 5rem) | 700 | 1.05 | -0.0036em | uppercase |
| `--solv-text-h1` | clamp(2rem, 4vw, 3rem) | 600 | 1.1 | -0.003em | uppercase¹ |
| `--solv-text-h2` | clamp(1.5rem, 2.5vw, 2rem) | 600 | 1.2 | -0.002em | normal |
| `--solv-text-h3` | 1.25rem | 600 | 1.3 | -0.001em | normal |
| `--solv-text-h4` | 1rem | 600 | 1.4 | -0.001em | normal |
| `--solv-text-body` | 1rem | 400 | 1.65 | 0 | normal |
| `--solv-text-body-lg` | 1.125rem | 400 | 1.7 | 0 | normal |
| `--solv-text-label` | 0.75rem | 600 | 1 | 0.06em | uppercase |
| `--solv-text-small` | 0.875rem | 400 | 1.5 | 0 | normal |
| `--solv-text-code` | 0.875em | 400 | 1.6 | 0 | normal |
| `--solv-text-code-block` | 0.8125em | 400 | 1.7 | 0 | normal |

¹ Docs H1 uses sentence case (normal); Landing hero uses uppercase.

### Type Usage Rules

- **Headings use Oswald**, body text uses Inter. Never mix within the same line.
- **Hero titles** are always uppercase Oswald 700.
- **Doc page H1** is Oswald 600, sentence case (NOT uppercase) — reading comfort.
- **Body paragraphs** use Inter 400 at 1rem with 1.65 line-height.
- **Labels and badges** are Inter 600, uppercase, 0.06em letter-spacing.
- **Code** is always JetBrains Mono at 0.875em (inline) or 0.8125em (blocks).
- **Landing hero** may use the full display scale. Docs should be more restrained.

---

## Color Palette

### Light Mode

| Token | Value | Usage |
|-------|-------|-------|
| `--solv-canvas` | `#F3F1ED` | Page background — warm editorial cream |
| `--solv-canvas-soft` | `#F7F5F2` | Secondary background |
| `--solv-surface` | `#FFFFFF` | Cards, panels, code blocks |
| `--solv-surface-dim` | `#E8E5E0` | Code inline bg, disabled surfaces |
| `--solv-ink` | `#111111` | Headings, primary text |
| `--solv-body` | `#5A5852` | Body text |
| `--solv-muted` | `#8A8780` | Secondary text, metadata |
| `--solv-muted-soft` | `#B0ADA5` | Placeholder text |
| `--solv-primary` | `#D81A1D` | Accent — editorial red |
| `--solv-primary-hover` | `#B01517` | Accent hover state |
| `--solv-primary-light` | `rgba(216, 26, 29, 0.08)` | Subtle accent bg (badges, highlights) |
| `--solv-tertiary` | `#E9A514` | Gold — support accent |
| `--solv-hairline` | `#D4D1CB` | Borders, dividers |
| `--solv-hairline-strong` | `#B8B4AC` | Strong borders |
| `--solv-hairline-soft` | `#E2DFDA` | Subtle hairline |

### Dark Mode

| Token | Value | Usage |
|-------|-------|-------|
| `--solv-canvas` | `#0D0D0D` | Page background — near-black |
| `--solv-canvas-soft` | `#141414` | Secondary background |
| `--solv-surface` | `#1A1A1A` | Cards, panels |
| `--solv-surface-dim` | `#222222` | Code inline bg |
| `--solv-ink` | `#F0EFE8` | Headings, primary text (warm off-white) |
| `--solv-body` | `#A8A69E` | Body text |
| `--solv-muted` | `#706E68` | Secondary text |
| `--solv-muted-soft` | `#585650` | Placeholder |
| `--solv-primary` | `#E03535` | Accent — lighter red for dark bg |
| `--solv-primary-hover` | `#D81A1D` | Hover state |
| `--solv-primary-light` | `rgba(224, 53, 53, 0.12)` | Subtle accent bg |
| `--solv-tertiary` | `#F0B830` | Gold accent |
| `--solv-hairline` | `rgba(255, 255, 255, 0.08)` | Borders |
| `--solv-hairline-strong` | `rgba(255, 255, 255, 0.15)` | Strong borders |
| `--solv-hairline-soft` | `rgba(255, 255, 255, 0.04)` | Subtle divider |

### Color Usage Rules

- **Primary red (#D81A1D):** Use for active links, buttons (primary), active sidebar items, in-code highlights, badges. Do NOT use as page background or large surface color.
- **Tertiary gold (#E9A514):** Use sparingly — version badges, premium/enterprise markers, complementary accent. Do NOT use for primary actions.
- **Ink (#111111 / #F0EFE8):** Use for all headings and primary text. Never use pure black (#000) for text — it creates visual vibration on screens.
- **Canvas (#F3F1ED / #0D0D0D):** The page background. Warm cream editorial feel light, deep charcoal dark.
- **Surface (#FFFFFF / #1A1A1A):** Cards, panels, code blocks. Clean contrast vs canvas.

---

## Spacing Scale

Base unit: **4px**

| Token | Value | px |
|-------|-------|-----|
| `--solv-space-05` | 0.125rem | 2px |
| `--solv-space-1` | 0.25rem | 4px |
| `--solv-space-2` | 0.5rem | 8px |
| `--solv-space-3` | 0.75rem | 12px |
| `--solv-space-4` | 1rem | 16px |
| `--solv-space-5` | 1.25rem | 20px |
| `--solv-space-6` | 1.5rem | 24px |
| `--solv-space-8` | 2rem | 32px |
| `--solv-space-10` | 2.5rem | 40px |
| `--solv-space-12` | 3rem | 48px |
| `--solv-space-16` | 4rem | 64px |
| `--solv-space-20` | 5rem | 80px |
| `--solv-space-24` | 6rem | 96px |

### Spacing Rules

- Section padding: `--solv-space-24` (6rem) on landing, `--solv-space-16` (4rem) on docs
- Card padding: `--solv-space-6` (1.5rem)
- Button padding: `--solv-space-3` vertical (0.75rem), `--solv-space-6` horizontal (1.5rem)
- Grid gaps: `--solv-space-4` (1rem) to `--solv-space-8` (2rem)
- Content max-width: 72rem (1152px) full width, 48rem (768px) narrow reading width

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--solv-radius-none` | 0px | Buttons, inputs, search bar |
| `--solv-radius-sm` | 2px | Cards, code blocks, images, sections |
| `--solv-radius-pill` | 9999px | Badges, tags, theme toggle |

### Radius Rules

- **Buttons are 0px radius.** Sharp, editorial, intentional. Primary and secondary.
- **Cards are 2px radius** (`--solv-radius-sm`). Subtle softening without losing editorial edge.
- **Code blocks are 2px radius.** Same as cards — consistent material system.
- **Badges are pill (9999px).** Differentiate decorative elements from structural ones.
- **Images in docs are 2px radius.**
- **No 8px or 12px radii** in the new system. These were from the previous Vercel-inspired system.

---

## Shadows & Depth

The system uses **Vercel-style border-as-shadow** — surface separation comes from hairline borders, not drop shadows.

| Token | Value | Usage |
|-------|-------|-------|
| `--solv-shadow-border` | `0px 0px 0px 1px` | Default surface border |
| `--solv-shadow-card` | `0px 0px 0px 1px var(--solv-hairline)` | Card separation |
| `--solv-shadow-elevated` | `0px 0px 0px 1px var(--solv-hairline-strong)` | Hover/focused state |
| `--solv-shadow-inner-ring` | `inset 0px 0px 0px 1px var(--solv-hairline-soft)` | Inner surface ring |

Cards use a single hairline border (`--solv-shadow-border`). On hover, the border becomes stronger (`--solv-shadow-elevated`). No traditional box shadows (no Y-offset blur).

---

## Components

### Buttons

| Property | Primary | Secondary |
|----------|---------|-----------|
| Background | `var(--solv-ink)` | `transparent` |
| Text color | `var(--solv-canvas)` | `var(--solv-body)` |
| Border | `none` | `1px solid var(--solv-hairline)` |
| Radius | `var(--solv-radius-none)` = 0px | `var(--solv-radius-none)` = 0px |
| Padding | `0.75rem 1.5rem` | `0.75rem 1.5rem` |
| Font | `var(--solv-font-body)` 500 weight | `var(--solv-font-body)` 500 weight |
| Hover | `opacity: 0.85` (no color shift) | `border-color: var(--solv-hairline-strong)`; `color: var(--solv-ink)` |
| Transition | 150ms opacity | 150ms color, border |

No border-radius on buttons. No box-shadow on buttons. Sharp, intentional edges.

### Cards

| Property | Value |
|----------|-------|
| Background | `var(--solv-surface)` |
| Radius | `var(--solv-radius-sm)` = 2px |
| Border/shadow | `var(--solv-shadow-card)` |
| Padding | `1.5rem` |
| Hover | `var(--solv-shadow-elevated)`, `translateY(-1px)` |
| Transition | 150ms box-shadow, transform |

### Code Blocks

| Property | Value |
|----------|-------|
| Background | `var(--solv-surface)` |
| Radius | `var(--solv-radius-sm)` = 2px |
| Shadow | `var(--solv-shadow-card)` + `var(--solv-shadow-inner-ring)` |
| Font | `var(--solv-font-code)` at 0.8125em |
| Line-height | 1.7 |
| Padding | 1.25rem 1.5rem |
| Border | none |

Inline code: background `var(--solv-surface-dim)`, radius 2px, font-size 0.875em.

### Navbar

| Property | Value |
|----------|-------|
| Position | Fixed top |
| Background | `rgba(var(--solv-canvas-rgb), 0.85)` with backdrop blur 12px |
| Shadow/divider | `var(--solv-shadow-border)` on bottom |
| Height | 3.5rem |
| Logo | `var(--solv-font-display)` Oswald 700, `var(--solv-ink)` |
| Nav links | `var(--solv-font-body)` Inter 500, 0.875rem, `var(--solv-body)` color |
| Active link | `var(--solv-primary)` color |
| Theme toggle | Border-only button, `var(--solv-radius-none)` |

### Footer

| Property | Value |
|----------|-------|
| Background | `var(--solv-ink)` (#111111 light, #F0EFE8 inverted... wait, that's wrong) |

Actually, let me reconsider the footer. Having a dark footer in light mode is a common pattern and looks premium. Let me define:

Light mode footer:
- Background: `#111111` (ink/black, always dark regardless of theme)
- Text: `#FFFFFF` (white on dark)

Dark mode footer:
- Background: `#080808` (even darker than canvas)
- Text: `#A8A69E` (body color)

### Footer (revised)

| Property | Value |
|----------|-------|
| Background | `#111111` light, `#080808` dark |
| Text | `#FFFFFF` light, `#A8A69E` dark |
| Link color | muted on dark bg |
| Title | uppercase Inter 600, 0.06em tracking |
| Layout | 4-column grid, responsive collapse |
| Border-top | none (different from section borders) |

### Admonitions (Docs)

| Property | Value |
|----------|-------|
| Radius | `var(--solv-radius-sm)` = 2px |
| Shadow | `var(--solv-shadow-card)` |
| Left border | 3px solid accent color |
| Note border | `var(--solv-primary)` |
| Tip border | green complement |
| Warning border | amber complement |
| Danger border | red darker |

### Badges

| Property | Value |
|----------|-------|
| Background | `var(--solv-primary-light)` |
| Text color | `var(--solv-primary)` |
| Radius | `var(--solv-radius-pill)` = 9999px |
| Font | Inter 600, 0.6875rem, uppercase, 0.06em tracking |
| Padding | 0.25rem 0.75rem |

---

## Layout

| Property | Landing | Docs |
|----------|---------|------|
| Layout type | Grid | Full-width responsive |
| Content max-width | 72rem (1152px) | 72rem (1152px) |
| Reading width | 48rem (768px) hero | 48rem (768px) article |
| Section padding | 6rem vertical | 4rem vertical |
| Content padding | 0 1.5rem | 0 1.5rem |
| Section separator | `border-top: 1px solid var(--solv-hairline)` | Docusaurus default |

---

## Dark / Light Mode

- **Detection:** `prefers-color-scheme` with manual override
- **Storage:** `localStorage` key for landing, Docusaurus built-in for docs
- **Attribute:** `html[data-theme="dark"]` (Docusaurus) / `html.dark` (landing)
- **Token switching:** CSS custom properties rebind in `html[data-theme="dark"]` block

Both surfaces must re-bind ALL palette tokens in the dark block — never mix light and dark token values.

---

## Consistent Documentation Surface

### Docs vs Landing Rules

| Aspect | Landing | Docs |
|--------|---------|------|
| Page background | `var(--solv-canvas)` | `var(--solv-canvas)` |
| Typography | Oswald uppercase for hero heading | Oswald sentence case for H1 |
| Button styles | Primary + secondary (same tokens) | Primary + secondary (same tokens) |
| Cards | 2px radius, surface bg | 2px radius, surface bg |
| Code blocks | 2px radius, surface bg | 2px radius, surface bg |
| Navbar | Oswald logo, Inter links | Oswald logo, Inter links |
| Footer | Ink bg, white text | Ink bg, white text |
| Section separators | Hairline border-top | Docusaurus default layout |
| Dark mode | Same tokens | Same tokens |

Every reusable component MUST look identical across both surfaces. No per-page style drift.

---

## Motion

| Property | Value |
|----------|-------|
| Duration | 150ms |
| Easing | `ease` or `cubic-bezier(0.4, 0, 0.2, 1)` |
| Hover effects | Opacity, color, border transitions |
| Card hover | `translateY(-1px)` + shadow upgrade |
| Link hover | Color transition only |
| Scroll behavior | `smooth` on html |
| Reduced motion | `@media(prefers-reduced-motion:reduce)` disables animation |

---

## Responsive Breakpoints

| Name | Width | Notes |
|------|-------|-------|
| Mobile | < 576px | Single column, collapsed nav |
| Tablet | 576px - 996px | 2-column grids |
| Desktop | > 996px | Full layout |

---

## Accessibility

- All color combinations meet WCAG AA contrast ratios
- Interactive elements use `:focus-visible` ring: `2px solid var(--solv-primary)`
- Theme toggle has `aria-label`
- Announcement bar is closeable and does not trap focus
- Code blocks are navigable via keyboard

---

## Implementation Architecture

```
DESIGN.md                                 ← THIS FILE (source of truth)
    │
    ├── landing/design-tokens.css          ← Canonical CSS custom properties
    │       @imported by landing/index.html
    │       Overrides for page-specific components
    │
    └── docs-site/src/css/custom.css       ← Duplicated tokens (same values)
            Docusaurus cannot @import from outside src/
            Must maintain 1:1 token parity with design-tokens.css
```

### Token Maintenance Rule

Whenever a design token changes in DESIGN.md:
1. Update `landing/design-tokens.css`
2. Update `docs-site/src/css/custom.css`
3. Verify both surfaces render identically

There is ONE source of truth (DESIGN.md), TWO implementations (landing tokens, docs tokens). They MUST remain in sync.

---

## What Was Unified (v1.0 Migration)

| Aspect | Before | After |
|--------|--------|-------|
| Color palette | Teal (#2BA8A0) accent, warm cream canvas | Red (#D81A1D) accent, warm editorial canvas |
| Display font | DM Sans | Oswald |
| Button radius | 8px | 0px |
| Card radius | 12px | 2px |
| Code block radius | 12px | 2px |
| Dark canvas | #1a1917 | #0D0D0D |
| Light canvas | #f7f7f4 | #F3F1ED |
| Accent usage | Liberal (teal badges, borders) | Scarce (red only for emphasis) |
| Footer (docs) | `style: "dark"` Docusaurus default | Custom ink bg, same as landing |
| Tokens | Duplicated across 2 files | DESIGN.md as source + synchronized CSS |
| DM Sans in docs | Missing — docs used Inter for everything | Oswald added to docs fonts |
| Shadow system | rgba-based layer shadows | Clean border-only shadows |
