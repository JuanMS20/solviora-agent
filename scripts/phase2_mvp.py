"""
Phase 2 — Simplify MVP surface.
- Disable model_catalog by default
- Filter setup_gateway() to show only Telegram, API Server, Webhook
- Hide voice/kanban from help prominence
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ========================================================================
# 1. config.py — disable model_catalog (points to Nous Research URL)
# ========================================================================
print('1. config.py — disabling model_catalog...')
f = 'hermes_cli/config.py'
t = open(f, encoding='utf-8').read()

t = t.replace(
    '"enabled": True,\n        "url": "https://hermes-agent.nousresearch.com/docs/api/model-catalog.json"',
    '"enabled": False,\n        "url": "",'
)

open(f, 'w', encoding='utf-8').write(t)
print(f'   {f}: done')

# ========================================================================
# 2. setup.py — filter setup_gateway() to MVP platforms only
# ========================================================================
print('2. setup.py — filtering gateway platforms...')
f = 'hermes_cli/setup.py'
t = open(f, encoding='utf-8').read()

# Replace the platform list builder in setup_gateway to filter to MVP only
# The function calls _all_platforms() and shows all of them.
# We add a filter after _all_platforms() to keep only MVP platforms.

old_block = '''    platforms = _all_platforms()

    # Build checklist, pre-selecting already-configured platforms.'''
new_block = '''    platforms = _all_platforms()

    # ── MVP filter: only show core platforms in setup ──
    _MVP_PLATFORMS = {"telegram", "webhook", "api_server"}
    _configured_non_mvp = [
        p for p in platforms
        if p["key"] not in _MVP_PLATFORMS and _platform_status(p) == "configured"
    ]
    if _configured_non_mvp:
        _MVP_PLATFORMS.update(p["key"] for p in _configured_non_mvp)
    platforms = [p for p in platforms if p["key"] in _MVP_PLATFORMS]

    # Build checklist, pre-selecting already-configured platforms.'''

assert old_block in t, f'Could not find platform list block in {f}'
t = t.replace(old_block, new_block)

open(f, 'w', encoding='utf-8').write(t)
print(f'   {f}: done')

# ========================================================================
# 3. commands.py — mark voice/kanban as less prominent
#    We don't remove them (still functional), just adjust descriptions
#    to indicate they're advanced/optional.
# ========================================================================
print('3. commands.py — adjusting voice/kanban descriptions...')
f = 'hermes_cli/commands.py'
t = open(f, encoding='utf-8').read()

t = t.replace(
    'CommandDef("voice", "Toggle voice mode", "Configuration",',
    'CommandDef("voice", "Toggle voice mode (advanced)", "Configuration",'
)
t = t.replace(
    'CommandDef("kanban", "Multi-profile collaboration board (tasks, links, comments)",',
    'CommandDef("kanban", "Multi-profile collaboration board (advanced, tasks, links, comments)",'
)

open(f, 'w', encoding='utf-8').write(t)
print(f'   {f}: done')

print('\nPhase 2 changes applied. Compiling...')
