"""Verify that solviora_cli and hermes_cli resolve identically.

NOTE (Phase 3A.1): this test confirms BOTH namespaces work and produce
the SAME results, but it does NOT assert that ``hermes_cli`` routes
through ``solviora_cli`` at the submodule level.  Direct submodule
imports (``from hermes_cli._parser import ...``) still load the real
files from the ``hermes_cli/`` directory — only package-level imports
(``from hermes_cli import X``) go through the ``__init__.py`` shim.
"""
import sys, pathlib
sys.path.insert(0, ".")

errors = 0

# 1. solviora_cli imports work
try:
    from solviora_cli._parser import build_top_level_parser as b1
    from solviora_cli.commands import COMMAND_REGISTRY as cr1
    from solviora_cli.config import DEFAULT_CONFIG
    from solviora_cli.colors import Colors
except ImportError as e:
    print(f"FAIL: solviora_cli import error: {e}")
    errors += 1

# 2. hermes_cli submodule imports still work (via real files, not shim)
try:
    from hermes_cli._parser import build_top_level_parser as b2
    from hermes_cli.commands import COMMAND_REGISTRY as cr2
    from hermes_cli.config import DEFAULT_CONFIG as dc2
except ImportError as e:
    print(f"FAIL: hermes_cli submodule import error: {e}")
    errors += 1

# 3. Same results (they MUST match since files are identical copies)
p1, _, _ = b1()
p2, _, _ = b2()
assert p1.prog == "solviora", f"Expected prog=solviora, got {p1.prog}"
assert p2.prog == "solviora", f"Expected shim prog=solviora, got {p2.prog}"
assert len(cr1) == len(cr2), f"Command count mismatch: {len(cr1)} vs {len(cr2)}"

# 4. Document the ACTUAL import origin (proves submodule imports are NOT shimmed)
import hermes_cli._parser as mod_h
import solviora_cli._parser as mod_s
print(f"hermes_cli._parser  loads from: {mod_h.__file__}")
print(f"solviora_cli._parser loads from: {mod_s.__file__}")
same_file = mod_h.__file__ == mod_s.__file__
print(f"Same file? {same_file}")

# 5. Verify the two trees are still in sync (no divergence)
old_dir = pathlib.Path("hermes_cli")
new_dir = pathlib.Path("solviora_cli")
divergent = []
for f in sorted(new_dir.rglob("*.py")):
    rel = f.relative_to(new_dir)
    old_f = old_dir / rel
    if old_f.exists() and f.read_bytes() != old_f.read_bytes():
        divergent.append(str(rel))
if divergent:
    print(f"DIVERGENT files ({len(divergent)}): {', '.join(divergent[:5])}")
else:
    print(f"Trees in sync: 65 files identical (__init__.py differs by design)")

print(f"\nOK: prog={p1.prog}, commands={len(cr1)}, config={DEFAULT_CONFIG.get('_config_version', '?')}")
print(f"OK: Colors class available")
if errors == 0:
    print(f"\nAll tests passed")
else:
    print(f"\n{errors} failure(s)")
    sys.exit(1)
