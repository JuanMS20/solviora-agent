"""Tests for Phase 3C dual env-var resolution helpers."""
import os
import warnings
import pytest

from solviora_constants import (
    resolve_env_str,
    resolve_env_bool,
    resolve_env_int,
    resolve_env_float,
    _resolve_env,
    _warned_legacy_envs,
)


# ── Fixtures ──────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def _clean_env_and_warnings():
    """Reset env vars and warning registry before each test."""
    _warned_legacy_envs.clear()
    for key in list(os.environ):
        if key.startswith("SOLVIORA_TEST_") or key.startswith("HERMES_TEST_"):
            del os.environ[key]
    # Collect warnings so we can assert on them
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        yield w


# ── _resolve_env: raw string resolver ─────────────────────────────────

class TestResolveEnvRaw:
    def test_new_wins(self):
        os.environ["SOLVIORA_TEST_FOO"] = "new"
        os.environ["HERMES_TEST_FOO"] = "old"
        assert _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO") == "new"

    def test_legacy_fallback(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_FOO"] = "old"
        assert _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO") == "old"

    def test_legacy_emits_warning(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_FOO"] = "old"
        _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO")
        assert any("HERMES_TEST_FOO" in str(w.message) for w in _clean_env_and_warnings)

    def test_warning_once(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_FOO"] = "old"
        _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO")
        _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO")
        legacy_warnings = [w for w in _clean_env_and_warnings if "HERMES_TEST_FOO" in str(w.message)]
        assert len(legacy_warnings) == 1

    def test_default(self, _clean_env_and_warnings):
        assert _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO", "def") == "def"

    def test_empty_new_is_explicit(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_FOO"] = ""
        os.environ["HERMES_TEST_FOO"] = "old"
        assert _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO") == ""

    def test_no_warning_when_new_set(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_FOO"] = "new"
        _resolve_env("SOLVIORA_TEST_FOO", "HERMES_TEST_FOO")
        assert len(_clean_env_and_warnings) == 0


# ── resolve_env_bool ──────────────────────────────────────────────────

class TestResolveBool:
    def test_true_values(self, _clean_env_and_warnings):
        for v in ("1", "true", "True", "yes", "on"):
            os.environ["SOLVIORA_TEST_BOOL"] = v
            assert resolve_env_bool("SOLVIORA_TEST_BOOL", "HERMES_TEST_BOOL") is True

    def test_false_values(self, _clean_env_and_warnings):
        for v in ("0", "false", "False", "no", "off", ""):
            os.environ["SOLVIORA_TEST_BOOL"] = v
            assert resolve_env_bool("SOLVIORA_TEST_BOOL", "HERMES_TEST_BOOL") is False

    def test_invalid(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_BOOL"] = "maybe"
        assert resolve_env_bool("SOLVIORA_TEST_BOOL", "HERMES_TEST_BOOL") is False

    def test_legacy_wins_with_warning(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_BOOL"] = "1"
        assert resolve_env_bool("SOLVIORA_TEST_BOOL", "HERMES_TEST_BOOL") is True

    def test_empty_hermes_not_set(self, _clean_env_and_warnings):
        """No env set at all → default."""
        assert resolve_env_bool("SOLVIORA_TEST_BOOL", "HERMES_TEST_BOOL", True) is True


# ── resolve_env_int ───────────────────────────────────────────────────

class TestResolveInt:
    def test_valid(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_INT"] = "42"
        assert resolve_env_int("SOLVIORA_TEST_INT", "HERMES_TEST_INT") == 42

    def test_invalid(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_INT"] = "notanint"
        assert resolve_env_int("SOLVIORA_TEST_INT", "HERMES_TEST_INT", 10) == 10

    def test_negative(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_INT"] = "-5"
        assert resolve_env_int("SOLVIORA_TEST_INT", "HERMES_TEST_INT") == -5

    def test_legacy_fallback(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_INT"] = "99"
        assert resolve_env_int("SOLVIORA_TEST_INT", "HERMES_TEST_INT") == 99


# ── resolve_env_float ─────────────────────────────────────────────────

class TestResolveFloat:
    def test_valid(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_FLOAT"] = "3.14"
        assert resolve_env_float("SOLVIORA_TEST_FLOAT", "HERMES_TEST_FLOAT") == 3.14

    def test_invalid(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_FLOAT"] = "abc"
        assert resolve_env_float("SOLVIORA_TEST_FLOAT", "HERMES_TEST_FLOAT", 1.5) == 1.5

    def test_legacy_fallback(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_FLOAT"] = "2.5"
        assert resolve_env_float("SOLVIORA_TEST_FLOAT", "HERMES_TEST_FLOAT") == 2.5


# ── Integration: precedence matrix ────────────────────────────────────

class TestPrecedenceMatrix:
    def test_a_only_new(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_A"] = "30"
        assert _resolve_env("SOLVIORA_TEST_A", "HERMES_TEST_A") == "30"
        assert len(_clean_env_and_warnings) == 0

    def test_b_only_old(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_A"] = "30"
        assert _resolve_env("SOLVIORA_TEST_A", "HERMES_TEST_A") == "30"
        assert any("HERMES_TEST_A" in str(w.message) for w in _clean_env_and_warnings)

    def test_c_both_new_wins(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_A"] = "60"
        os.environ["HERMES_TEST_A"] = "30"
        assert _resolve_env("SOLVIORA_TEST_A", "HERMES_TEST_A") == "60"
        assert len(_clean_env_and_warnings) == 0

    def test_d_neither(self, _clean_env_and_warnings):
        assert _resolve_env("SOLVIORA_TEST_A", "HERMES_TEST_A", "def") == "def"

    def test_e_empty_new(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_A"] = ""
        os.environ["HERMES_TEST_A"] = "30"
        assert _resolve_env("SOLVIORA_TEST_A", "HERMES_TEST_A") == ""

    def test_f_invalid_integer(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_INT"] = "abc"
        assert resolve_env_int("SOLVIORA_TEST_INT", "HERMES_TEST_INT", 1800) == 1800

    def test_g_invalid_bool(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_BOOL"] = "maybe"
        assert resolve_env_bool("SOLVIORA_TEST_BOOL", "HERMES_TEST_BOOL") is False

    def test_h_both_bool_new_wins(self, _clean_env_and_warnings):
        os.environ["SOLVIORA_TEST_BOOL"] = "1"
        os.environ["HERMES_TEST_BOOL"] = "0"
        assert resolve_env_bool("SOLVIORA_TEST_BOOL", "HERMES_TEST_BOOL") is True

    def test_i_warning_once_called_twice(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_I"] = "val"
        _resolve_env("SOLVIORA_TEST_I", "HERMES_TEST_I")
        _resolve_env("SOLVIORA_TEST_I", "HERMES_TEST_I")
        h_warnings = [w for w in _clean_env_and_warnings if "HERMES_TEST_I" in str(w.message)]
        assert len(h_warnings) == 1

    def test_j_legacy_home(self, _clean_env_and_warnings):
        os.environ["HERMES_TEST_J"] = "/custom"
        r = _resolve_env("SOLVIORA_TEST_J", "HERMES_TEST_J")
        assert r == "/custom"
        assert any("HERMES_TEST_J" in str(w.message) for w in _clean_env_and_warnings)
