#!/bin/bash
# Test script for Solviora Agent Installer — run inside WSL/Linux
set -e

echo "=== 1. Environment ==="
echo "HOME=$HOME"
echo "SHELL=$SHELL"
echo "git: $(command -v git || echo 'NOT FOUND')"
echo "python3: $(command -v python3 || echo 'NOT FOUND')"
echo "uv: $(command -v uv || echo 'NOT FOUND')"
echo "node: $(command -v node || echo 'NOT FOUND')"

echo ""
echo "=== 2. Run installer (non-interactive, skip setup) ==="
cd /tmp
rm -rf /tmp/solviora-test
mkdir -p /tmp/solviora-test
cd /tmp/solviora-test

# Copy the installer from the repo mount
cp /mnt/c/Users/ASUS/Downloads/Solviora_Agent/scripts/install.sh ./install.sh
chmod +x install.sh

# Run in non-interactive mode with skip-setup
export CI=1
bash install.sh --skip-setup 2>&1 || echo "INSTALLER EXIT CODE: $?"

echo ""
echo "=== 3. Verify repo clone ==="
if [ -d "$HOME/.solviora/solviora-agent/.git" ]; then
    cd "$HOME/.solviora/solviora-agent"
    echo "REPO URL: $(git remote get-url origin 2>&1)"
    echo "BRANCH: $(git rev-parse --abbrev-ref HEAD 2>&1)"
    echo "✓ Repo cloned correctly"
else
    echo "✗ Repo NOT found at ~/.solviora/solviora-agent/"
fi

echo ""
echo "=== 4. Verify symlinks ==="
for cmd in solviora hermes; do
    if [ -L "$HOME/.local/bin/$cmd" ]; then
        target=$(readlink -f "$HOME/.local/bin/$cmd")
        echo "✓ ~/.local/bin/$cmd → $target"
    elif [ -x "$HOME/.local/bin/$cmd" ]; then
        echo "✓ ~/.local/bin/$cmd (regular file, executable)"
    else
        echo "✗ ~/.local/bin/$cmd NOT FOUND"
    fi
done

echo ""
echo "=== 5. Verify data dirs ==="
for d in config.yaml .env cron sessions logs skills; do
    if [ -e "$HOME/.solviora/$d" ] || [ -d "$HOME/.solviora/$d" ]; then
        echo "✓ ~/.solviora/$d exists"
    else
        echo "✗ ~/.solviora/$d NOT FOUND"
    fi
done

echo ""
echo "=== 6. Command: solviora --help ==="
if [ -x "$HOME/.local/bin/solviora" ]; then
    "$HOME/.local/bin/solviora" --help 2>&1 | head -20 || echo "(expected error if no venv)"
else
    echo "solviora not found — checking venv..."
fi

echo ""
echo "=== 7. Command: hermes --help ==="
if [ -x "$HOME/.local/bin/hermes" ]; then
    "$HOME/.local/bin/hermes" --help 2>&1 | head -20 || echo "(expected error if no venv)"
else
    echo "hermes not found"
fi

echo ""
echo "=== 8. Verify install dir ==="
if [ -d "$HOME/.solviora/solviora-agent/venv" ]; then
    echo "✓ venv exists"
    "$HOME/.solviora/solviora-agent/venv/bin/python" --version 2>&1 || true
else
    echo "✗ venv NOT FOUND"
fi

echo ""
echo "=== DONE ==="
