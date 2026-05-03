"""Phase 1B part 3 — final user-visible Hermes → Solviora pass."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def replace_in_file(f, pairs):
    t = open(f, encoding='utf-8').read()
    changed = 0
    for old, new in pairs:
        before = t
        t = t.replace(old, new)
        if t != before:
            changed += 1
    open(f, 'w', encoding='utf-8').write(t)
    print(f'  {f}: {changed} replacements')

# cli.py final
cli_pairs = [
    # Comments with hermes command references
    ('# without `hermes model`)', '# without `solviora model`)'),
    ('via ``hermes --resume <id>``', 'via ``solviora --resume <id>``'),
    ('then re-run: hermes setup"', 'then re-run: solviora setup"'),
]
replace_in_file('cli.py', cli_pairs)

# hermes_cli/main.py final
main_pairs = [
    # Print messages
    ('hermes gateway install"', 'solviora gateway install"'),
    ('``hermes model``', '``solviora model``'),
    ('"hermes model"', '"solviora model"'),
    ('"hermes slack <subcommand>"', '"solviora slack <subcommand>"'),
    ('"usage: hermes slack', '"usage: solviora slack'),
    ('Hermes backup from a zip', 'Solviora backup from a zip'),
    ('``hermes update --gateway``', '``solviora update --gateway``'),
    ('``hermes update``', '``solviora update``'),
    ('``hermes web``', '``solviora web``'),
    ('``hermes dashboard``', '``solviora dashboard``'),
    ('"hermes dashboard"', '"solviora dashboard"'),
    ('"hermes-update-autostash-', '"solviora-update-autostash-'),
    ("Hermes couldn't find the stash", "Solviora couldn't find the stash"),
    # Comments about commands
    ('Hermes uses lightweight', 'Solviora uses lightweight'),
    ('# Hermes uses lightweight', '# Solviora uses lightweight'),
    ('hermes tools, hermes setup, hermes model', 'solviora tools, solviora setup, solviora model'),
    # TUI reference
    ('hermes -p ', 'solviora -p '),
    # remaining bare command refs
    ('hermes model` to set', 'solviora model` to set'),
    ('after `hermes update`', 'after `solviora update`'),
    ('hermes dashboard --stop', 'solviora dashboard --stop'),
    ('pgrep -f "hermes.*dashboard"', 'pgrep -f "solviora.*dashboard"'),
    # Slack manifest command
    ('hermes slack manifest', 'solviora slack manifest'),
]
replace_in_file('hermes_cli/main.py', main_pairs)

# setup.py final
setup_pairs = [
    ('hermes auth spotify', 'solviora auth spotify'),
]
replace_in_file('hermes_cli/setup.py', setup_pairs)

print('\nDone. Running compile check...')
