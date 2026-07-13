"""Tests for profiles and LeetCode verification routes."""
from __future__ import annotations

from . import conftest


class ProfilesTest(conftest._Base):
    def test_list_profiles_default(self) -> None:
        r = self.client.get("/api/profiles")
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertEqual(body["active_profile"], "Default")
        self.assertEqual(len(body["profiles"]), 1)
        self.assertEqual(body["profiles"][0]["name"], "Default")
        self.assertFalse(body["profiles"][0]["career_mode"])

    def test_create_and_select_profile(self) -> None:
        # Create a new profile
        r = self.client.post(
            "/api/profiles",
            json={"name": "CareerPrep", "career_mode": True, "leetcode_username": "test_user"},
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertEqual(body["active_profile"], "CareerPrep")
        self.assertEqual(len(body["profiles"]), 2)
        
        # Verify get_progress reflects active profile settings
        r_prog = self.client.get("/api/progress")
        self.assertEqual(r_prog.status_code, 200)
        prog_body = r_prog.json()
        self.assertTrue(prog_body["career_mode"])
        self.assertEqual(prog_body["leetcode_username"], "test_user")

        # Switch back to Default
        r_sel = self.client.post("/api/profiles/Default/select", json={})
        self.assertEqual(r_sel.status_code, 200)
        self.assertEqual(r_sel.json()["active_profile"], "Default")

    def test_delete_profile(self) -> None:
        # Create profile to delete
        self.client.post(
            "/api/profiles",
            json={"name": "DeleteMe"},
        )
        # Delete profile
        r = self.client.delete("/api/profiles/DeleteMe")
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertEqual(body["active_profile"], "Default")
        self.assertNotIn("DeleteMe", [p["name"] for p in body["profiles"]])

    def test_leetcode_mock_verification(self) -> None:
        # Update settings to enable simulate mode
        self.client.put(
            "/api/progress",
            json={"leetcode_username": "simulate"},
        )
        # Try to verify a mapped challenge
        r = self.client.post(
            "/api/progress/verify-leetcode",
            json={"challenge_id": "lc_1"},
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertTrue(body["success"])
        self.assertIn("lc_1", body["unlocked_leetcode"])
