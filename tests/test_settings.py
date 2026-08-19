"""Verify the pinned settings defaults in `.vera/settings.yaml` apply cleanly.

The acceptance shard repo pins the documented product default
(`auto_manage_issues: false`) so acceptance runs are deterministic. It also
seeds a disallowed project-layer override (`escalation_timeout_hours`) which
Vera must ignore at the project layer; this test documents that the override
is expected to be ignored, not removed.
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def test_settings_defaults_apply_cleanly() -> None:
    settings_path = Path(__file__).resolve().parents[1] / ".vera" / "settings.yaml"
    parsed = yaml.safe_load(settings_path.read_text())

    assert parsed["auto_manage_issues"] is False
    assert "escalation_timeout_hours" in parsed
