"""
Backward-compatibility shim — DO NOT USE FOR NEW CODE.

STATUS (Phase 3A.1): dual-tree transition period.

- ``solviora_cli/`` is the NEW canonical namespace. All new code MUST
  import from ``solviora_cli`` directly.
- ``hermes_cli/`` is the LEGACY tree.  This ``__init__.py`` re-exports
  the package-level symbols, but submodule imports like
  ``from hermes_cli._parser import ...`` still load the REAL file
  from the ``hermes_cli/`` directory — they are NOT redirected to
  ``solviora_cli/`` automatically.
- Both trees are currently identical (same 66 files, same content) and
  will remain in sync until Phase 3C when the legacy tree is removed.

TODO(solviora) Phase 3C: remove ``hermes_cli/`` and its shim after all
imports have been migrated to ``solviora_cli``.  Until then:

  1. IMPORT NEW CODE from ``solviora_cli``.
  2. If you edit a file in ``solviora_cli/``, apply the SAME change to
     the corresponding file in ``hermes_cli/`` (or delete the old file
     once all imports are migrated).
  3. Run tests/test_solviora_cli_compat.py to verify both namespaces.
"""
from solviora_cli import *  # noqa: F401,F403
from solviora_cli import (  # noqa: F401 — explicit exports for type checkers
    __version__,
    __release_date__,
)
