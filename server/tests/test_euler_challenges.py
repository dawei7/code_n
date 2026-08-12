"""Tests for Project Euler challenge integration."""

from challenges.registry import CHALLENGE_REGISTRY
from server.app.challenge_packages import euler_package_dir, is_euler_id


def test_euler_challenge_registered():
    assert "euler_1" in CHALLENGE_REGISTRY
    cls = CHALLENGE_REGISTRY.get("euler_1")
    assert cls is not None
    instance = cls()
    assert instance.info.id == "euler_1"
    assert "Multiples of 3 or 5" in instance.info.name


def test_euler_package_dir_resolution():
    assert is_euler_id("euler_1")
    package_dir = euler_package_dir("euler_1")
    assert package_dir is not None
    assert package_dir.name == "0001_multiples-of-3-or-5"
    assert (package_dir / "metadata.json").is_file()
