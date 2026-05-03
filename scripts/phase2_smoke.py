import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Config loads and model_catalog is disabled
from hermes_cli.config import DEFAULT_CONFIG
mc = DEFAULT_CONFIG.get('model_catalog', {})
assert mc.get('enabled') == False, "model_catalog.enabled should be False"
assert mc.get('url') == '', "model_catalog.url should be empty"
print('[PASS] model_catalog disabled')

# 2. Default toolset is hermes-cli
assert DEFAULT_CONFIG.get('toolsets') == ['hermes-cli']
print('[PASS] default toolset = hermes-cli')

# 3. Voice is off by default
voice = DEFAULT_CONFIG.get('voice', {})
assert voice.get('auto_tts') == False
print('[PASS] voice auto_tts = False')

# 4. Commands still load
from hermes_cli.commands import COMMAND_REGISTRY, resolve_command
voice_cmd = resolve_command('voice')
assert voice_cmd is not None
assert 'advanced' in voice_cmd.description.lower()
print('[PASS] voice command marked advanced')

kanban_cmd = resolve_command('kanban')
assert kanban_cmd is not None
assert 'advanced' in kanban_cmd.description.lower()
print('[PASS] kanban command marked advanced')

# 5. Core commands still work
for cmd_name in ['help', 'model', 'config', 'tools', 'skills', 'new', 'save', 'status']:
    c = resolve_command(cmd_name)
    assert c is not None, "Command /" + cmd_name + " not found"
print('[PASS] all core commands resolve')

# 6. Constants still work
from solviora_constants import get_hermes_home, display_hermes_home
from hermes_constants import get_hermes_home as g2
assert get_hermes_home() == g2()
print('[PASS] constants shim OK')

# 7. Identity
from agent.prompt_builder import DEFAULT_AGENT_IDENTITY
assert 'Solviora' in DEFAULT_AGENT_IDENTITY
print('[PASS] agent identity = Solviora')

# 8. Version
from hermes_cli import __version__
assert __version__ == '0.1.0'
print('[PASS] version = 0.1.0')

print()
print('ALL PHASE 2 SMOKE TESTS PASSED')
