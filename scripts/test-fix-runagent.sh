#!/bin/bash
set -e
cd ~/.solviora/solviora-agent
source venv/bin/activate

echo "=== 1. Reinstall editable ==="
uv pip install -e . 2>&1 | tail -3

echo ""
echo "=== 2. Verify import ==="
python3 -c "
from solviora_constants import resolve_env_float
print('resolve_env_float importable:', resolve_env_float)
from run_agent import AIAgent
print('AIAgent import OK')
"

echo ""
echo "=== 3. Oneshot test ==="
solviora --oneshot "Say exactly: HELLO_WORLD_OK" 2>&1 || true

echo ""
echo "=== 4. hermes oneshot test ==="
hermes --oneshot "Say exactly: HELLO_WORLD_OK" 2>&1 || true

echo ""
echo "=== 5. doctor test ==="
solviora doctor 2>&1 | head -5 || true

echo ""
echo "=== DONE ==="
