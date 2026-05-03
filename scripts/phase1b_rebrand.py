"""Phase 1B — Replace visible Hermes branding strings with Solviora."""
import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

# --- cli.py ---
def process_cli():
    f = 'cli.py'
    t = open(f, encoding='utf-8').read()
    
    # Response labels
    t = t.replace('"⚕ Hermes"', '"Solviora"')
    t = t.replace('" ⚕ Hermes "', '" Solviora "')
    t = t.replace('"⚕ NOUS HERMES - AI Agent Framework"', '"SOLVIORA AGENT - AI Agent Framework"')
    t = t.replace('"⚕ NOUS HERMES"', '"Solviora"')
    
    # Welcome / identity
    t = t.replace('Welcome to Hermes Agent! Type your message or /help for commands.',
                  'Welcome to Solviora Agent! Type your message or /help for commands.')
    t = t.replace('"Hermes Agent"', '"Solviora Agent"')
    t = t.replace("'Hermes Agent'", "'Solviora Agent'")
    t = t.replace('"Hermes CLI Status"', '"Solviora Agent Status"')
    t = t.replace('"Hermes needs your input"', '"Solviora needs your input"')
    
    # Personality strings
    t = t.replace('Captain Hermes, the most tech-savvy pirate', 'Captain Solviora, the most tech-savvy pirate')
    t = t.replace('They call me Hermes - I solve problems', 'They call me Solviora - I solve problems')
    
    # Chat prefixes
    t = t.replace('"◆ Hermes: "', '"◆ Solviora: "')
    t = t.replace('"[Hermes #"', '"[Solviora #"')
    
    # Conversational
    t = t.replace('"Hermes keeps working until it is', '"Solviora keeps working until it is')
    t = t.replace('while Hermes is working.', 'while Solviora is working.')
    t = t.replace('while Hermes is busy.', 'while Solviora is busy.')
    t = t.replace('chat with Hermes!', 'chat with Solviora!')
    t = t.replace('"Starting Hermes Gateway', '"Starting Solviora Gateway')
    t = t.replace('"Hermes Agent CLI - Interactive AI Assistant"', '"Solviora Agent CLI - Interactive AI Assistant"')
    
    # Context length warning
    t = t.replace('"Hermes needs 16k', '"Solviora needs 16k')
    
    # File naming
    t = t.replace('"hermes_conversation_', '"solviora_conversation_')
    t = t.replace('"hermes_voice"', '"solviora_voice"')
    t = t.replace('"hermes_voice/', '"solviora_voice/')
    
    # Command references in user-visible strings
    t = t.replace('"hermes --resume', '"solviora --resume')
    t = t.replace('"hermes -c ', '"solviora -c ')
    t = t.replace('run hermes -w', 'run solviora -w')
    t = t.replace('"hermes sessions list', '"solviora sessions list')
    t = t.replace("'hermes sessions list'", "'solviora sessions list'")
    t = t.replace('"hermes --checkpoints', '"solviora --checkpoints')
    
    # "designed for use with Hermes Agent"
    t = t.replace('designed for use with Hermes Agent.', 'designed for use with Solviora Agent.')
    
    # Snapshot description
    t = t.replace('Hermes config/state', 'Solviora config/state')
    
    # Model fallback display
    t = t.replace("else 'Hermes'", "else 'Solviora'")
    
    # Checkpoint tip
    t = t.replace('hermes --checkpoints', 'solviora --checkpoints')
    
    open(f, 'w', encoding='utf-8').write(t)
    print(f'  {f}: done')

# --- hermes_cli/main.py ---
def process_main():
    f = 'hermes_cli/main.py'
    t = open(f, encoding='utf-8').read()
    
    # General identity replacements
    t = t.replace('Hermes Agent', 'Solviora Agent')
    t = t.replace('Hermes CLI', 'Solviora CLI')
    t = t.replace("Authenticate Hermes", "Authenticate Solviora")
    t = t.replace('Hermes home directory', 'Solviora home directory')
    t = t.replace('Hermes log files', 'Solviora log files')
    t = t.replace('Hermes repository', 'Solviora repository')
    
    # "hermes" command in user-visible strings (argparse help, print statements)
    # Be careful: only in string literals, not in code references
    t = t.replace("'hermes {command_name}'", "'solviora {command_name}'")
    t = t.replace('"hermes --tui', '"solviora --tui')
    t = t.replace('"hermes sessions list"', '"solviora sessions list"')
    t = t.replace("'hermes sessions list'", "'solviora sessions list'")
    
    # Bare hermes command in help strings
    t = t.replace('    hermes ', '    solviora ')
    t = t.replace('   hermes ', '   solviora ')
    t = t.replace('  hermes ', '  solviora ')
    t = t.replace('"hermes ', '"solviora ')
    t = t.replace("'hermes ", "'solviora ")
    t = t.replace('exec hermes ', 'exec solviora ')
    t = t.replace('sudo hermes ', 'sudo solviora ')
    t = t.replace('command -v hermes', 'command -v solviora')
    t = t.replace('/usr/local/bin/hermes', '/usr/local/bin/solviora')
    t = t.replace('~/hermes-backup-', '~/solviora-backup-')
    t = t.replace('prefix="hermes-', 'prefix="solviora-')
    t = t.replace('"Hermes Agent — ensure', '"Solviora Agent — ensure')
    t = t.replace('Hermes behaves unexpectedly', 'Solviora behaves unexpectedly')
    
    # Specific user-facing strings
    t = t.replace('"⚕ Updating Hermes Agent..."', '"Updating Solviora Agent..."')
    t = t.replace('update Hermes Agent', 'update Solviora Agent')
    t = t.replace('"⚕ Hermes Setup"', '"Solviora Setup"')
    
    # Bot name default
    t = t.replace('"Hermes")', '"Solviora")')
    t = t.replace('"Hermes\')"', '"Solviora\')"')  
    
    # Dashboard
    t = t.replace('"hermes dashboard"', '"solviora dashboard"')
    t = t.replace('"No hermes dashboard', '"No solviora dashboard')
    t = t.replace('hermes dashboard process', 'solviora dashboard process')
    t = t.replace('hermes dashboard"', 'solviora dashboard"')
    
    # Debug
    t = t.replace('"hermes debug', '"solviora debug')
    t = t.replace("'hermes debug", "'solviora debug")
    
    # Config / managed
    t = t.replace('hermes web will not', 'solviora web will not')
    t = t.replace('"hermes --resume', '"solviora --resume')
    t = t.replace('"hermes -c ', '"solviora -c ')
    t = t.replace("'hermes -c ", "'solviora -c ")
    
    # Logs command help
    t = t.replace('    hermes logs', '    solviora logs')
    
    # Description strings
    t = t.replace('delegates Hermes turns', 'delegates Solviora turns')
    t = t.replace('Hermes currently starts', 'Solviora currently starts')
    t = t.replace('Hermes uses your selected', 'Solviora uses your selected')
    t = t.replace('Hermes typically makes', 'Solviora typically makes')
    t = t.replace('To use Gemini with Hermes', 'To use Gemini with Solviora')
    t = t.replace('Hermes will use Claude', 'Solviora will use Claude')
    t = t.replace('Hermes will probe', 'Solviora will probe')
    t = t.replace('Hermes will still save', 'Solviora will still save')
    t = t.replace('Hermes isn\'t configured', 'Solviora isn\'t configured')
    t = t.replace('WhatsApp with Hermes?', 'WhatsApp with Solviora?')
    t = t.replace('Hermes only falls back', 'Solviora only falls back')
    t = t.replace('multiple isolated Hermes instances', 'multiple isolated Hermes instances')  # keep
    t = t.replace('multiple isolated Hermes instances', 'multiple isolated Solviora instances')
    t = t.replace('hermes --tui', 'solviora --tui')
    t = t.replace('hermes -p ', 'solviora -p ')
    t = t.replace('"hermes slack', '"solviora slack')
    t = t.replace("'hermes slack", "'solviora slack")
    t = t.replace('"hermes mcp', '"solviora mcp')
    t = t.replace("'hermes mcp", "'solviora mcp")
    t = t.replace('"hermes profile', '"solviora profile')
    t = t.replace('"hermes claw', '"solviora claw')
    t = t.replace('"hermes gateway', '"solviora gateway')
    t = t.replace('"hermes auth', '"solviora auth')
    t = t.replace('"hermes config', '"solviora config')
    t = t.replace('"hermes tools', '"solviora tools')
    t = t.replace('"hermes model', '"solviora model')
    t = t.replace('"hermes setup', '"solviora setup')
    t = t.replace('"hermes status', '"solviora status')
    t = t.replace('"hermes doctor', '"solviora doctor')
    t = t.replace('"hermes cron', '"solviora cron')
    t = t.replace('"hermes update', '"solviora update')
    t = t.replace('"hermes version', '"solviora version')
    t = t.replace('"hermes uninstall', '"solviora uninstall')
    t = t.replace('"hermes acp', '"solviora acp')
    t = t.replace('"hermes logs', '"solviora logs')
    t = t.replace('"hermes sessions', '"solviora sessions')
    t = t.replace('"hermes dashboard', '"solviora dashboard')
    t = t.replace('"hermes backup', '"solviora backup')
    t = t.replace('hermes gateway run', 'solviora gateway run')
    
    # hermes-ink package references (keep these - they're npm package names)
    # Don't change hermes_cli, hermes_constants etc.
    
    open(f, 'w', encoding='utf-8').write(t)
    print(f'  {f}: done')

# --- hermes_cli/setup.py ---
def process_setup():
    f = 'hermes_cli/setup.py'
    t = open(f, encoding='utf-8').read()
    
    t = t.replace('Interactive setup wizard for Hermes Agent.', 'Interactive setup wizard for Solviora Agent.')
    t = t.replace('⚕ Hermes Setup — Non-interactive mode', 'Solviora Setup — Non-interactive mode')
    t = t.replace('Configure Hermes using environment variables', 'Configure Solviora using environment variables')
    t = t.replace('Hermes can keep multiple credentials', 'Solviora can keep multiple credentials')
    t = t.replace('one Hermes can auto-use', 'one Solviora can auto-use')
    t = t.replace('where Hermes runs shell commands', 'where Solviora runs shell commands')
    t = t.replace('using Hermes via Telegram', 'using Solviora via Telegram')
    t = t.replace('where Hermes delivers cron job results', 'where Solviora delivers cron job results')
    t = t.replace('where Hermes delivers cron', 'where Solviora delivers cron')
    t = t.replace('Your Hermes agent on Slack', 'Your Solviora agent on Slack')
    t = t.replace('Hermes adds new commands', 'Solviora adds new commands')
    t = t.replace('Connects Hermes to iMessage', 'Connects Solviora to iMessage')
    t = t.replace('Connect Hermes to messaging', 'Connect Solviora to messaging')
    t = t.replace('chat with Hermes from anywhere', 'chat with Solviora from anywhere')
    t = t.replace('Hermes configured', 'Solviora configured')
    t = t.replace('set up Hermes?', 'set up Solviora?')
    t = t.replace('Launch hermes chat now?', 'Launch solviora chat now?')
    t = t.replace('Hermes Agent Setup Wizard', 'Solviora Agent Setup Wizard')
    t = t.replace('Hermes Agent installation', 'Solviora Agent installation')
    t = t.replace('⚕ Hermes Agent Setup Wizard', 'Solviora Agent Setup Wizard')
    t = t.replace('Hermes can preview', 'Solviora can preview')
    t = t.replace('configure Hermes to use', 'configure Solviora to use')
    t = t.replace('point Hermes at your', 'point Solviora at your')
    t = t.replace('Hermes equivalents', 'Solviora equivalents')
    t = t.replace('existing Hermes config', 'existing Solviora config')
    t = t.replace('semantics in Hermes', 'semantics in Solviora')
    t = t.replace("Hermes's yolo mode", "Solviora's yolo mode")
    t = t.replace('Hermes Setup —', 'Solviora Setup —')
    t = t.replace('bot_name="Hermes"', 'bot_name="Solviora"')
    
    # Command references
    t = t.replace("hermes slack manifest", "solviora slack manifest")
    t = t.replace("hermes claw migrate", "solviora claw migrate")
    t = t.replace('    hermes ', '    solviora ')
    t = t.replace('  hermes ', '  solviora ')
    t = t.replace('"hermes ', '"solviora ')
    t = t.replace("'hermes ", "'solviora ")
    t = t.replace("Re-run `hermes", "Re-run `solviora")
    
    open(f, 'w', encoding='utf-8').write(t)
    print(f'  {f}: done')

# --- agent/display.py ---
def process_display():
    f = 'agent/display.py'
    t = open(f, encoding='utf-8').read()
    t = t.replace("in Hermes' inline transcript style.", "in Solviora's inline transcript style.")
    open(f, 'w', encoding='utf-8').write(t)
    print(f'  {f}: done')

if __name__ == '__main__':
    print('Phase 1B: Replacing visible Hermes branding...')
    process_cli()
    process_main()
    process_setup()
    process_display()
    print('Done. Verify with smoke tests.')
