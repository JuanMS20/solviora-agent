import sys
sys.stdout.reconfigure(encoding='utf-8')

files = ['cli.py', 'hermes_cli/main.py', 'hermes_cli/setup.py']
skip_internal = [
    'hermes_constants','hermes_cli','hermes_state','hermes_logging','hermes_time',
    'hermes_home','hermes_md','get_hermes','display_hermes','_hermes_home',
    'load_hermes','ensure_hermes','from hermes','import hermes',
    'hermes-agent','hermes_agent','HERMES_','hermes_ipv4',
    'hermes_model','hermes-revision','.hermes/','~/.hermes',
    'HermesCLI','hermes-ink','openclaw_to_hermes','hermes.service',
    'hermes_voice','hermes-backup','packages/hermes',
    'hermes_conversation','hermes_debug','@hermes','hermes_dist',
    'hermes_web','hermes_update','hermes.gateway','prefix=',
    'hermes_setup','hermes_subprocess','Hermes_','_hermes_now',
    'hermes.s','node_modules','hermes-ink','hermes_cli/',
]

user_visible = []
code_only = []

for f in files:
    try:
        lines = open(f, encoding='utf-8', errors='replace').readlines()
    except:
        continue
    for i, line in enumerate(lines, 1):
        if 'Hermes' not in line and 'hermes' not in line.lower():
            continue
        skip = False
        for s in skip_internal:
            if s in line:
                skip = True
                break
        if not skip:
            stripped = line.strip()
            is_comment = stripped.startswith('#')
            has_string = '"' in stripped or "'" in stripped
            if is_comment and not has_string:
                code_only.append((f, i, stripped[:140]))
            else:
                user_visible.append((f, i, stripped[:140]))

print(f'USER-VISIBLE: {len(user_visible)}')
for f, i, l in user_visible[:40]:
    print(f'  {f}:{i}: {l}')
if len(user_visible) > 40:
    print(f'  ... +{len(user_visible)-40} more')
print()
print(f'CODE-ONLY (comments): {len(code_only)}')
