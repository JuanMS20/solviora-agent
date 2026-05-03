import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

SKIP_PATTERNS = [
    'hermes_constants', 'hermes_cli', 'hermes_state', 'hermes_logging',
    'hermes_time', 'hermes_home', 'hermes_md', 'get_hermes', 'display_hermes',
    '_hermes_', 'load_hermes', 'ensure_hermes', 'from hermes', 'import hermes',
    'hermes-agent', 'hermes_agent', 'HERMES_', '.hermes/', '~/.hermes',
    'HermesCLI', 'hermes-ink', 'hermes_dist', 'hermes_web', 'hermes_update',
    'hermes.gateway', 'hermes.service', 'hermes_conversation', 'hermes_debug',
    'hermes_model', 'hermes_ipv4', '@hermes', 'node_modules',
    'packages/hermes', 'hermes_setup', 'hermes_subprocess', 'hermes.s',
    'hermes_cli/', 'hermes-revision',
]

CRITICAL_FILES = [
    ('cli.py', 'CLI main'),
    ('hermes_cli/setup.py', 'Setup wizard'),
    ('hermes_cli/banner.py', 'Startup banner'),
    ('hermes_cli/main.py', 'CLI entry point'),
    ('agent/prompt_builder.py', 'Agent identity'),
    ('hermes_cli/commands.py', 'Help/commands'),
    ('hermes_cli/config.py', 'Config messages'),
    ('hermes_cli/gateway.py', 'Gateway setup'),
    ('.env.example', 'Env template'),
    ('solviora_constants.py', 'Constants'),
]

# Focus on user-visible strings: print statements, f-strings, help text, descriptions
# Skip: variable names, function names, class names, import paths, file paths, comments only

total_visible = 0
by_file = {}

for filepath, label in CRITICAL_FILES:
    try:
        lines = open(filepath, encoding='utf-8', errors='replace').readlines()
    except FileNotFoundError:
        continue
    
    file_issues = []
    for i, line in enumerate(lines, 1):
        if 'Hermes' not in line and 'hermes' not in line.lower():
            continue
        
        skip = False
        for s in SKIP_PATTERNS:
            if s in line:
                skip = True
                break
        if skip:
            continue
        
        stripped = line.strip()
        is_comment_only = stripped.startswith('#') and '"' not in stripped and "'" not in stripped
        if is_comment_only:
            continue
        
        # Check if it's actually user-visible
        has_string = '"' in stripped or "'" in stripped
        if not has_string:
            continue
        
        file_issues.append((i, stripped[:140]))
    
    if file_issues:
        by_file[filepath] = file_issues
        total_visible += len(file_issues)

print(f'TOTAL user-visible Hermes strings in critical files: {total_visible}')
print()

for filepath, issues in by_file.items():
    label = dict(CRITICAL_FILES).get(filepath, '?')
    print(f'--- {filepath} ({label}): {len(issues)} strings ---')
    for lineno, text in issues[:10]:
        print(f'  L{lineno}: {text}')
    if len(issues) > 10:
        print(f'  ... +{len(issues) - 10} more')
    print()
