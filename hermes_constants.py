"""Backward-compatibility shim — re-exports from solviora_constants.

All new code should import from ``solviora_constants`` directly.
This module exists so that existing imports ``from hermes_constants import ...``
continue to work during the transition period.
"""

from solviora_constants import *  # noqa: F401,F403
from solviora_constants import (  # noqa: F401 — explicit re-exports for type checkers
    VALID_REASONING_EFFORTS,
    AI_GATEWAY_BASE_URL,
    OPENROUTER_BASE_URL,
    OPENROUTER_MODELS_URL,
    apply_ipv4_preference,
    display_hermes_home,
    get_config_path,
    get_default_hermes_root,
    get_env_path,
    get_hermes_dir,
    get_hermes_home,
    get_optional_skills_dir,
    get_skills_dir,
    get_subprocess_home,
    is_container,
    is_termux,
    is_wsl,
    parse_reasoning_effort,
)
