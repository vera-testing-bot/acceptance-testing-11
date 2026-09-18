"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add, clamp


def test_add() -> None:
    assert add(2, 3) == 5


def test_clamp_in_range() -> None:
    assert clamp(5, 0, 10) == 5


def test_clamp_below_low() -> None:
    assert clamp(-1, 0, 10) == 0


def test_clamp_above_high() -> None:
    assert clamp(11, 0, 10) == 10
