import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Agent identity is terminal-first
from agent.prompt_builder import DEFAULT_AGENT_IDENTITY
assert 'terminal' in DEFAULT_AGENT_IDENTITY.lower(), "Identity should mention terminal"
assert 'executes real work' in DEFAULT_AGENT_IDENTITY
assert 'Solviora Agent' in DEFAULT_AGENT_IDENTITY
print('[PASS] agent identity = terminal-first')

# 2. Constants still work
from solviora_constants import get_hermes_home
from hermes_constants import get_hermes_home as g2
assert get_hermes_home() == g2()
print('[PASS] constants shim OK')

# 3. Version
from hermes_cli import __version__
assert __version__ == '0.1.0'
print('[PASS] version = 0.1.0')

# 4. Config still loads
from hermes_cli.config import DEFAULT_CONFIG
mc = DEFAULT_CONFIG.get('model_catalog', {})
assert mc.get('enabled') == False
print('[PASS] model_catalog disabled')

# 5. Commands still resolve
from hermes_cli.commands import resolve_command
for cmd in ['help', 'model', 'config', 'tools', 'skills', 'new', 'status']:
    c = resolve_command(cmd)
    assert c is not None, "Missing command: " + cmd
print('[PASS] all core commands resolve')

# 6. Starter skills exist
from pathlib import Path
skills_dir = Path('skills/solviora-starter')
assert (skills_dir / 'web-research' / 'SKILL.md').exists()
assert (skills_dir / 'coding' / 'SKILL.md').exists()
assert (skills_dir / 'automation' / 'SKILL.md').exists()
assert (skills_dir / 'DESCRIPTION.md').exists()
print('[PASS] starter skills exist')

# 7. Quickstart doc exists
assert Path('docs/quickstart.md').exists()
print('[PASS] docs/quickstart.md exists')

# 8. README is terminal-first
readme = Path('README.md').read_text(encoding='utf-8')
assert 'terminal' in readme.lower()
assert 'gateway' in readme.lower()
assert 'optional' in readme.lower()
assert 'Tu agente de IA que ejecuta trabajo real desde la terminal' in readme
print('[PASS] README is terminal-first')

# 9. Setup gateway is optional (default skip)
setup = Path('hermes_cli/setup.py').read_text(encoding='utf-8')
assert 'Skip' in setup
assert "solviora setup gateway" in setup
assert "remote channel" in setup.lower() or "remote access" in setup.lower()
print('[PASS] setup gateway is optional')

# 10. Welcome message has examples
cli = Path('cli.py').read_text(encoding='utf-8')
assert 'Describe what you need, or try' in cli
assert 'search for the latest news' in cli
assert 'summarize the architecture' in cli
print('[PASS] welcome message has examples')

print()
print('ALL PHASE 3 SMOKE TESTS PASSED')
