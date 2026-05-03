"""Shared constants for Solviora Agent.

Import-safe module with no dependencies — can be imported from anywhere
without risk of circular imports.

Environment variable transition:
  SOLVIORA_HOME is preferred.  Falls back to HERMES_HOME for compatibility
  with existing deployments migrated from Hermes Agent.

Env var helper API (Phase 3C):
  Use ``resolve_env_str`` / ``resolve_env_bool`` / ``resolve_env_int`` /
  ``resolve_env_float`` in all NEW code.  They read ``SOLVIORA_*`` first,
  fall back to ``HERMES_*`` with a ``FutureWarning``, and return a typed
  default when neither is set.
"""

import os
from pathlib import Path
from warnings import warn


# ── Phase 3C: Dual env-var resolution ─────────────────────────────────
# Set of legacy env var names that have already triggered a deprecation
# warning once per process.
_warned_legacy_envs: set[str] = set()


def _resolve_env(name_new: str, name_old: str, default: str = "") -> str:
    """Resolve an env var preferring ``name_new`` over ``name_old``.

    Returns the **raw string** (or ``default``).  Typed wrappers
    (``resolve_env_bool`` etc.) are the stable public API.

    Rules:
      1. ``name_new`` (SOLVIORA_*) set → use it, no warning.
      2. Only ``name_old`` (HERMES_*) set → use it, once-per-process
         ``FutureWarning``.
      3. Both set → ``name_new`` wins, no warning.
      4. Neither set → ``default``.
      5. An empty string ``""`` in ``name_new`` is treated as an explicit
         value (does NOT fall through to ``name_old``).
    """
    val = os.environ.get(name_new)
    if val is not None:
        return val
    val = os.environ.get(name_old)
    if val is not None:
        if name_old not in _warned_legacy_envs:
            _warned_legacy_envs.add(name_old)
            warn(
                f"Environment variable {name_old} is deprecated. "
                f"Use {name_new} instead.",
                FutureWarning,
                stacklevel=2,
            )
        return val
    return default


def _warn_parse(raw: str, name_new: str, name_old: str, default: object) -> None:
    """Emit a one-time parse warning for an invalid env-var value."""
    warn(
        f"Invalid value {raw!r} for {name_new}/{name_old}. "
        f"Falling back to {default}.",
        FutureWarning,
        stacklevel=3,
    )


def resolve_env_str(name_new: str, name_old: str, default: str = "") -> str:
    """Resolve a string env var, preferring SOLVIORA_* over HERMES_*."""
    return _resolve_env(name_new, name_old, default)


def resolve_env_bool(name_new: str, name_old: str, default: bool = False) -> bool:
    """Resolve a boolean env var.

    Truthy (case-insensitive): ``1``, ``true``, ``yes``, ``on``.
    Falsy: ``0``, ``false``, ``no``, ``off``, ``""``.
    Invalid → warning + ``default``.
    """
    raw = _resolve_env(name_new, name_old)
    if raw == "":
        # Unset → default; empty string (explicit) → False
        if os.environ.get(name_new) is None and os.environ.get(name_old) is None:
            return default
        return False
    low = raw.strip().lower()
    if low in ("1", "true", "yes", "on"):
        return True
    if low in ("0", "false", "no", "off"):
        return False
    _warn_parse(raw, name_new, name_old, default)
    return default


def resolve_env_int(name_new: str, name_old: str, default: int = 0) -> int:
    """Resolve an integer env var. Invalid → warning + ``default``."""
    raw = _resolve_env(name_new, name_old)
    if raw == "":
        return default
    try:
        return int(raw.strip())
    except ValueError:
        _warn_parse(raw, name_new, name_old, default)
        return default


def resolve_env_float(name_new: str, name_old: str, default: float = 0.0) -> float:
    """Resolve a float env var. Invalid → warning + ``default``."""
    raw = _resolve_env(name_new, name_old)
    if raw == "":
        return default
    try:
        return float(raw.strip())
    except ValueError:
        _warn_parse(raw, name_new, name_old, default)
        return default


# ── Home-directory helpers (Phase 3C-ready) ───────────────────────────

def _resolve_home_env() -> str:
    """Resolve the home directory env var, preferring SOLVIORA_HOME."""
    val = os.environ.get("SOLVIORA_HOME", "").strip()
    if val:
        return val
    return os.environ.get("HERMES_HOME", "").strip()


def get_hermes_home() -> Path:
    """Return the Solviora home directory (default: ~/.solviora).

    Reads SOLVIORA_HOME env var first, then HERMES_HOME for backward
    compatibility, falls back to ~/.solviora.
    """
    val = _resolve_home_env()
    if val:
        return Path(val)
    return Path.home() / ".solviora"


def get_default_hermes_root() -> Path:
    """Return the root Solviora directory for profile-level operations.

    In standard deployments this is ``~/.solviora``.

    In Docker or custom deployments where ``SOLVIORA_HOME`` points outside
    ``~/.solviora`` (e.g. ``/opt/data``), returns ``SOLVIORA_HOME`` directly.

    In profile mode where ``SOLVIORA_HOME`` is ``<root>/profiles/<name>``,
    returns ``<root>`` so that ``profile list`` can see all profiles.

    Import-safe — no dependencies beyond stdlib.
    """
    native_home = Path.home() / ".solviora"
    env_home = _resolve_home_env()
    if not env_home:
        return native_home
    env_path = Path(env_home)
    try:
        env_path.resolve().relative_to(native_home.resolve())
        return native_home
    except ValueError:
        pass

    if env_path.parent.name == "profiles":
        return env_path.parent.parent

    return env_path


def get_optional_skills_dir(default: Path | None = None) -> Path:
    """Return the optional-skills directory, honoring package-manager wrappers."""
    override = os.getenv("SOLVIORA_OPTIONAL_SKILLS", "").strip()
    if not override:
        override = os.getenv("HERMES_OPTIONAL_SKILLS", "").strip()
    if override:
        return Path(override)
    if default is not None:
        return default
    return get_hermes_home() / "optional-skills"


def get_hermes_dir(new_subpath: str, old_name: str) -> Path:
    """Resolve a Solviora subdirectory with backward compatibility.

    New installs get the consolidated layout (e.g. ``cache/images``).
    Existing installs that already have the old path (e.g. ``image_cache``)
    keep using it — no migration required.
    """
    home = get_hermes_home()
    old_path = home / old_name
    if old_path.exists():
        return old_path
    return home / new_subpath


def display_hermes_home() -> str:
    """Return a user-friendly display string for the current home directory.

    Uses ``~/`` shorthand for readability::

        default:  ``~/.solviora``
        profile:  ``~/.solviora/profiles/coder``
        custom:   ``/opt/solviora-custom``

    Use this in **user-facing** print/log messages instead of hardcoding
    ``~/.solviora``.  For code that needs a real ``Path``, use
    :func:`get_hermes_home` instead.
    """
    home = get_hermes_home()
    try:
        return "~/" + str(home.relative_to(Path.home()))
    except ValueError:
        return str(home)


def get_subprocess_home() -> str | None:
    """Return a per-profile HOME directory for subprocesses, or None.

    When ``{HOME_DIR}/home/`` exists on disk, subprocesses should use it
    as ``HOME`` so system tools (git, ssh, gh, npm …) write their configs
    inside the Solviora data directory instead of the OS-level ``/root`` or
    ``~/``.
    """
    home_str = _resolve_home_env()
    if not home_str:
        return None
    profile_home = os.path.join(home_str, "home")
    if os.path.isdir(profile_home):
        return profile_home
    return None


VALID_REASONING_EFFORTS = ("minimal", "low", "medium", "high", "xhigh")


def parse_reasoning_effort(effort: str) -> dict | None:
    """Parse a reasoning effort level into a config dict.

    Valid levels: "none", "minimal", "low", "medium", "high", "xhigh".
    Returns None when the input is empty or unrecognized (caller uses default).
    Returns {"enabled": False} for "none".
    Returns {"enabled": True, "effort": <level>} for valid effort levels.
    """
    if not effort or not effort.strip():
        return None
    effort = effort.strip().lower()
    if effort == "none":
        return {"enabled": False}
    if effort in VALID_REASONING_EFFORTS:
        return {"enabled": True, "effort": effort}
    return None


def is_termux() -> bool:
    """Return True when running inside a Termux (Android) environment."""
    prefix = os.getenv("PREFIX", "")
    return bool(os.getenv("TERMUX_VERSION") or "com.termux/files/usr" in prefix)


_wsl_detected: bool | None = None


def is_wsl() -> bool:
    """Return True when running inside WSL (Windows Subsystem for Linux)."""
    global _wsl_detected
    if _wsl_detected is not None:
        return _wsl_detected
    try:
        with open("/proc/version", "r") as f:
            _wsl_detected = "microsoft" in f.read().lower()
    except Exception:
        _wsl_detected = False
    return _wsl_detected


_container_detected: bool | None = None


def is_container() -> bool:
    """Return True when running inside a Docker/Podman container."""
    global _container_detected
    if _container_detected is not None:
        return _container_detected
    if os.path.exists("/.dockerenv"):
        _container_detected = True
        return True
    if os.path.exists("/run/.containerenv"):
        _container_detected = True
        return True
    try:
        with open("/proc/1/cgroup", "r") as f:
            cgroup = f.read()
            if "docker" in cgroup or "podman" in cgroup or "/lxc/" in cgroup:
                _container_detected = True
                return True
    except OSError:
        pass
    _container_detected = False
    return False


# ─── Well-Known Paths ─────────────────────────────────────────────────────────


def get_config_path() -> Path:
    """Return the path to ``config.yaml`` under the home directory."""
    return get_hermes_home() / "config.yaml"


def get_skills_dir() -> Path:
    """Return the path to the skills directory under the home directory."""
    return get_hermes_home() / "skills"


def get_env_path() -> Path:
    """Return the path to the ``.env`` file under the home directory."""
    return get_hermes_home() / ".env"


# ─── Network Preferences ─────────────────────────────────────────────────────


def apply_ipv4_preference(force: bool = False) -> None:
    """Monkey-patch ``socket.getaddrinfo`` to prefer IPv4 connections.

    Safe to call multiple times — only patches once.
    Set ``network.force_ipv4: true`` in ``config.yaml`` to enable.
    """
    if not force:
        return

    import socket

    if getattr(socket.getaddrinfo, "_solviora_ipv4_patched", False):
        return

    _original_getaddrinfo = socket.getaddrinfo

    def _ipv4_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        if family == 0:
            try:
                return _original_getaddrinfo(
                    host, port, socket.AF_INET, type, proto, flags
                )
            except socket.gaierror:
                return _original_getaddrinfo(host, port, family, type, proto, flags)
        return _original_getaddrinfo(host, port, family, type, proto, flags)

    _ipv4_getaddrinfo._solviora_ipv4_patched = True  # type: ignore[attr-defined]
    _ipv4_getaddrinfo._hermes_ipv4_patched = True  # type: ignore[attr-defined]
    socket.getaddrinfo = _ipv4_getaddrinfo  # type: ignore[assignment]


OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODELS_URL = f"{OPENROUTER_BASE_URL}/models"

AI_GATEWAY_BASE_URL = "https://ai-gateway.vercel.sh/v1"
