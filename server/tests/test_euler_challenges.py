from . import conftest
from challenges.registry import CHALLENGE_REGISTRY
from server.app.challenge_packages import euler_package_dir, is_euler_id


class EulerChallengesTest(conftest._Base):
    def test_euler_challenge_registered(self):
        assert "euler_1" in CHALLENGE_REGISTRY
        cls = CHALLENGE_REGISTRY.get("euler_1")
        assert cls is not None
        instance = cls()
        assert instance.info.id == "euler_1"
        assert "Multiples of 3 or 5" in instance.info.name

    def test_euler_package_dir_resolution(self):
        assert is_euler_id("euler_1")
        package_dir = euler_package_dir("euler_1")
        assert package_dir is not None
        assert package_dir.name == "0001_multiples-of-3-or-5"
        assert (package_dir / "metadata.json").is_file()

    def test_euler_starter_source_is_minimal(self):
        response = self.client.get("/api/challenges/euler_1")
        assert response.status_code == 200
        starter = response.json()["starter_source"]
        assert "# Description" not in starter
        assert "# Required Complexity" not in starter
        assert "def solve() -> int:" in starter
        assert "pass" in starter
