"""Phase 1B part 2 — remaining user-visible Hermes → Solviora replacements."""
import re
sys = __import__('sys')
sys.stdout.reconfigure(encoding='utf-8')

def replace_in_file(f, pairs):
    t = open(f, encoding='utf-8').read()
    for old, new in pairs:
        before = t
        t = t.replace(old, new)
        if t == before:
            # try to find partial match for debugging
            pass
    open(f, 'w', encoding='utf-8').write(t)
    print(f'  {f}: done')

# --- cli.py remaining user-visible ---
cli_pairs = [
    # Error/setup messages
    ('"Set OPENROUTER_API_KEY or run: hermes setup"', '"Set OPENROUTER_API_KEY or run: solviora setup"'),
    ('"Check your provider config or run: hermes setup"', '"Check your provider config or run: solviora setup"'),
    ('Use a session ID from a previous CLI run (hermes sessions list).', 'Use a session ID from a previous CLI run (solviora sessions list).'),
    ('(hermes sessions list).', '(solviora sessions list).'),
    ('run hermes chat -q --image', 'run solviora chat -q --image'),
    ("Run 'hermes setup' to configure", "Run 'solviora setup' to configure"),
    ('Resume the live session with: hermes --resume', 'Resume the live session with: solviora --resume'),
    ('hermes --resume {self.session_id}', 'solviora --resume {self.session_id}'),
    ('hermes -c "{session_title}"', 'solviora -c "{session_title}"'),
    ("re-run: hermes setup'", "re-run: solviora setup'"),
    ('Hermes Agent CLI - Interactive AI Assistant', 'Solviora Agent CLI - Interactive AI Assistant'),
    # Context warning
    ('Hermes needs 16k', 'Solviora needs 16k'),
    # Model warning — keep "Nous Research Hermes 3 & 4" as model name but update framing
    ('Nous Research Hermes 3 & 4 models are NOT agentic and are not ', 'Nous Research Hermes 3 & 4 models are NOT agentic and are not '),
    # These are model names, keep as-is
    # Clarify prompt
    ("'Hermes needs your input'", "'Solviora needs your input'"),
    # Worktree/branch prefixes — these are git identifiers, low priority but safe to rename
    ('f"hermes-{short_id}"', 'f"solviora-{short_id}"'),
    ('f"hermes/{wt_name}"', 'f"solviora/{wt_name}"'),
    ('``hermes/*``', '``solviora/*``'),
    ('.startswith("hermes-")', '.startswith("solviora-")'),
    ('``hermes/hermes-*``', '``solviora/solviora-*``'),
    ('``hermes -w``', '``solviora -w``'),
    ('.startswith("hermes/hermes-")', '.startswith("solviora/solviora-")'),
    ('or b.startswith("pr-")', 'or b.startswith("pr-")'),
    # Machine-readable note
    ('styled "Hermes" box', 'styled "Solviora" box'),
]
replace_in_file('cli.py', cli_pairs)

# --- hermes_cli/main.py remaining user-visible ---
main_pairs = [
    # Help text
    ('# Step-by-step migration guide: OpenClaw native → Hermes + Honcho', '# Step-by-step migration guide: OpenClaw native → Solviora + Honcho'),
    ('(hermes tools, hermes setup, hermes model)', '(solviora tools, solviora setup, solviora model)'),
    # User messages
    ('Start the gateway with: hermes gateway', 'Start the gateway with: solviora gateway'),
    # Comments referencing user-visible commands (keep as comments but update)
    ("'hermes'", "'solviora'"),  # This one is tricky — only in user-facing contexts
]
# main.py is tricky — many hermes refs are code identifiers. Be conservative.
# Only replace in print/help strings.
t = open('hermes_cli/main.py', encoding='utf-8').read()

# Specific targeted replacements for main.py
main_replacements = [
    # Print/error messages
    ('print("  Start the gateway with: hermes gateway")', 'print("  Start the gateway with: solviora gateway")'),
    ('"hermes gateway"', '"solviora gateway"'),
    ('"hermes model"', '"solviora model"'),
    ('"hermes tools"', '"solviora tools"'),
    ('"hermes setup"', '"solviora setup"'),
    ('"hermes update"', '"solviora update"'),
    ('"hermes auth"', '"solviora auth"'),
    ('"hermes config"', '"solviora config"'),
    ('"hermes doctor"', '"solviora doctor"'),
    ('"hermes cron"', '"solviora cron"'),
    ('"hermes sessions"', '"solviora sessions"'),
    ('"hermes dashboard"', '"solviora dashboard"'),
    ('"hermes logs"', '"solviora logs"'),
    ('"hermes status"', '"solviora status"'),
    ('"hermes profile"', '"solviora profile"'),
    ('"hermes backup"', '"solviora backup"'),
    ('"hermes version"', '"solviora version"'),
    ('"hermes uninstall"', '"solviora uninstall"'),
    ('"hermes acp"', '"solviora acp"'),
    ('"hermes web"', '"solviora web"'),
    ('"hermes claw"', '"solviora claw"'),
    ('"hermes slack"', '"solviora slack"'),
    ('"hermes mcp"', '"solviora mcp"'),
    
    # Migration guide comment
    ('→ Hermes + Honcho', '→ Solviora + Honcho'),
    
    # ArgumentParser prog names
    ("prog='hermes',", "prog='solviora',"),
    
    # Description strings with Hermes
    ('Hermes isn\'t configured', 'Solviora isn\'t configured'),
    ('Hermes behaves unexpectedly', 'Solviora behaves unexpectedly'),
    
    # "hermes" as bare command in user strings
    ('run `hermes', 'run `solviora'),
    ('Try `hermes', 'Try `solviora'),
    ('Use `hermes', 'Use `solviora'),
    ('See `hermes', 'See `solviora'),
    ('Run `hermes', 'Run `solviora'),
    
    # Dashboard
    ('hermes dashboard process', 'solviora dashboard process'),
    
    # Debug
    ('"hermes debug"', '"solviora debug"'),
    
    # the bare hermes command as prog
    ("'hermes {command_name}'", "'solviora {command_name}'"),
    
    # Slack manifest
    ('hermes slack manifest', 'solviora slack manifest'),
]

for old, new in main_replacements:
    t = t.replace(old, new)

open('hermes_cli/main.py', 'w', encoding='utf-8').write(t)
print('  hermes_cli/main.py: done')

# --- hermes_cli/setup.py remaining ---
setup_pairs = [
    ('hermes auth spotify', 'solviora auth spotify'),
    ('between `hermes tools` and `hermes setup tools`', 'between `solviora tools` and `solviora setup tools`'),
    ('used by ``hermes model``', 'used by ``solviora model``'),
    ('``hermes model``', '``solviora model``'),
    ('hermes model flow', 'solviora model flow'),
    ('hermes model"', 'solviora model"'),
    ("hermes model'", "solviora model'"),
    ('hermes setup agent', 'solviora setup agent'),
    ('after `hermes update`', 'after `solviora update`'),
]
replace_in_file('hermes_cli/setup.py', setup_pairs)

print('\nPhase 1B part 2 complete. Running smoke test...')
