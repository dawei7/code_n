"""Tests for ``POST /api/challenges/{challenge_id}/analyze``."""
from __future__ import annotations

from unittest.mock import patch, MagicMock
from . import conftest


class AnalyzeRouteTest(conftest._Base):
    def test_missing_api_key_returns_400(self) -> None:
        # Load progress with empty API key
        self.client.put("/api/progress", json={"gemini_api_key": ""})

        r = self.client.post(
            "/api/challenges/sort_01/analyze",
            json={
                "source": "def solve(data, n):\n    return data",
                "n": 8,
                "seed": 1,
                "returned": "[3, 1, 2]",
                "expected": "[1, 2, 3]",
                "inputs": {"data": "[3, 1, 2]"}
            },
        )
        self.assertEqual(r.status_code, 400)
        self.assertIn("Please configure your Gemini API Key", r.text)

    def test_unknown_challenge_returns_404(self) -> None:
        # Load progress with an API key
        self.client.put("/api/progress", json={"gemini_api_key": "dummy_key"})

        r = self.client.post(
            "/api/challenges/does_not_exist/analyze",
            json={
                "source": "def solve(data, n):\n    return data",
                "n": 8,
                "seed": 1,
                "returned": "[3, 1, 2]",
                "expected": "[1, 2, 3]",
                "inputs": {"data": "[3, 1, 2]"}
            },
        )
        self.assertEqual(r.status_code, 404)
        self.assertIn("Challenge 'does_not_exist' not found", r.text)

    @patch("requests.post")
    def test_successful_analysis(self, mock_post: MagicMock) -> None:
        # Setup mock response from Gemini API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": "This is a mock AI analysis of the sorting bug."
                            }
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        # Load progress with an API key
        self.client.put("/api/progress", json={"gemini_api_key": "valid_mock_key"})

        r = self.client.post(
            "/api/challenges/sort_01/analyze",
            json={
                "source": "def solve(data, n):\n    return data",
                "n": 8,
                "seed": 1,
                "returned": "[3, 1, 2]",
                "expected": "[1, 2, 3]",
                "inputs": {"data": "[3, 1, 2]"}
            },
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertEqual(body["analysis"], "This is a mock AI analysis of the sorting bug.")

        # Verify that mock post was called with correct parameters
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertIn("gemma-4-31b-it", args[0])
        self.assertIn("key=valid_mock_key", args[0])
        payload = kwargs["json"]
        self.assertIn("contents", payload)
        prompt_text = payload["contents"][0]["parts"][0]["text"]
        self.assertIn("def solve(data, n):", prompt_text)
        self.assertIn("Input Variables:", prompt_text)
        self.assertIn("- data: [3, 1, 2]", prompt_text)
        self.assertIn("What User's Code Returned: [3, 1, 2]", prompt_text)
        self.assertIn("What was Expected (Correct Return Value): [1, 2, 3]", prompt_text)

    @patch("requests.post")
    def test_model_fallback_on_429(self, mock_post: MagicMock) -> None:
        # Setup mock responses: first returns 429, second returns 200
        mock_response_429 = MagicMock()
        mock_response_429.status_code = 429
        mock_response_429.json.return_value = {"error": {"message": "Resource exhausted"}}

        mock_response_200 = MagicMock()
        mock_response_200.status_code = 200
        mock_response_200.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": "Analysis from fallback model."
                            }
                        ]
                    }
                }
            ]
        }
        # Side effect: first call gets 429, second gets 200
        mock_post.side_effect = [mock_response_429, mock_response_200]

        # Load progress with an API key
        self.client.put("/api/progress", json={"gemini_api_key": "fallback_mock_key"})

        r = self.client.post(
            "/api/challenges/sort_01/analyze",
            json={
                "source": "def solve(data, n):\n    return data",
                "n": 8,
                "seed": 1,
                "returned": "[3, 1, 2]",
                "expected": "[1, 2, 3]",
                "inputs": {"data": "[3, 1, 2]"}
            },
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertEqual(body["analysis"], "Analysis from fallback model.")

        # Verified that requests.post was called twice (first model, then second)
        self.assertEqual(mock_post.call_count, 2)
        call_args_list = mock_post.call_args_list
        # First call should target gemma-4-31b-it
        self.assertIn("gemma-4-31b-it", call_args_list[0][0][0])
        # Second call should target gemma-4-26b-a4b-it
        self.assertIn("gemma-4-26b-a4b-it", call_args_list[1][0][0])

    @patch("requests.post")
    def test_thinking_content_filtered(self, mock_post: MagicMock) -> None:
        # Setup mock response with thinking block followed by the final answer
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": "This is a thinking step.",
                                "thought": True
                            },
                            {
                                "text": "This is the final answer."
                            }
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        # Load progress with an API key
        self.client.put("/api/progress", json={"gemini_api_key": "valid_mock_key"})

        r = self.client.post(
            "/api/challenges/sort_01/analyze",
            json={
                "source": "def solve(data, n):\n    return data",
                "n": 8,
                "seed": 1,
                "returned": "[3, 1, 2]",
                "expected": "[1, 2, 3]",
                "inputs": {"data": "[3, 1, 2]"}
            },
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        # Assert that thinking text was excluded
        self.assertEqual(body["analysis"], "This is the final answer.")
