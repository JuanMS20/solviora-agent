"""
Backward-compatibility shim — DO NOT USE FOR NEW CODE.

STATUS (Phase 3B): dual-module transition period.

This file exists so existing imports continue to work during the
migration from ``hermes_*`` to ``solviora_*`` names.

New code MUST import from the ``solviora_*`` module directly.
Old imports still load the real file content via this re-export.

The two copies are currently identical and will remain in sync
until the shim is removed (tracked in Phase 3C).

TODO(solviora): remove this shim after one release cycle.
"""

from solviora_state import *  # noqa: F401,F403
