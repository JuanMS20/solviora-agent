import sys
sys.stdout.reconfigure(encoding='utf-8')
import tomllib

# 1. Dead deps removed
with open('pyproject.toml', 'rb') as f:
    d = tomllib.load(f)
deps = d['project']['dependencies']
dep_names = [d.split('>')[0].split('<')[0].split('[')[0].strip().lower() for d in deps]
assert 'tenacity' not in dep_names, "tenacity should be removed"
assert 'jinja2' not in dep_names, "jinja2 should be removed"
print('[PASS] tenacity and jinja2 removed from deps')

# 2. Update command says solviora
from hermes_cli.config import recommended_update_command
cmd = recommended_update_command()
assert 'solviora' in cmd, f"Expected solviora in update command, got: {cmd}"
assert 'hermes' not in cmd.lower(), f"Should not have hermes in update command, got: {cmd}"
print('[PASS] update command = solviora')

# 3. Prompt builder help guidance
t = open('agent/prompt_builder.py', encoding='utf-8').read()
assert 'solviora config set' in t, "Should reference solviora config set"
assert 'solviora setup' in t, "Should reference solviora setup"
assert 'solviora status' in t, "Should reference solviora status"
assert 'hermes setup' not in t.split('first. It has')[1].split('so you don')[0], "Should not have hermes setup in help guidance"
print('[PASS] prompt_builder guidance = solviora commands')

# 4. .env.example uses solviora
env = open('.env.example', encoding='utf-8').read()
assert '~/.solviora/config.yaml' in env, "Should reference solviora config path"
assert 'solviora model' in env, "Should reference solviora model"
assert 'solviora setup' in env, "Should reference solviora setup"
print('[PASS] .env.example uses solviora commands')

# 5. soundfile guard
tts = open('tools/tts_tool.py', encoding='utf-8').read()
assert 'try:' in tts.split('import soundfile')[0][-50:], "soundfile import should be guarded"
assert 'pip install soundfile' in tts, "should have install hint"
print('[PASS] soundfile import guarded')

# 6. Core still works
from solviora_constants import get_hermes_home
from agent.prompt_builder import DEFAULT_AGENT_IDENTITY
from hermes_cli import __version__
assert __version__ == '0.1.0'
assert 'Solviora' in DEFAULT_AGENT_IDENTITY
assert get_hermes_home().name == '.solviora'
print('[PASS] core constants/identity/version OK')

# 7. Commands still resolve
from hermes_cli.commands import resolve_command
for c in ['help', 'model', 'config', 'tools', 'skills', 'new', 'status']:
    assert resolve_command(c) is not None
print('[PASS] all core commands resolve')

print()
print('ALL RELEASE CANDIDATE SMOKE TESTS PASSED')
