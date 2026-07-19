from __future__ import annotations

from typing import Any

import pytest

from tools import fetch_leetcode_question


class _Response:
    def __init__(self, question: dict[str, Any]) -> None:
        self._question = question

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict[str, Any]:
        return {"data": {"question": self._question}}


class _Client:
    def __init__(self, question: dict[str, Any]) -> None:
        self._question = question
        self.request: dict[str, Any] | None = None

    def post(self, url: str, **kwargs: Any) -> _Response:
        self.request = {"url": url, **kwargs}
        return _Response(self._question)


def _question(**overrides: Any) -> dict[str, Any]:
    question = {
        "questionId": "2071",
        "questionFrontendId": "1902",
        "title": "Depth of BST Given Insertion Order",
        "titleSlug": "depth-of-bst-given-insertion-order",
        "isPaidOnly": True,
        "content": "<p>Return the tree&#39;s depth.</p><ul><li>Root depth is 1.</li></ul>",
        "codeSnippets": [
            {
                "lang": "Python3",
                "langSlug": "python3",
                "code": "class Solution:\n    def maxDepthBST(self, order):\n        pass",
            }
        ],
    }
    question.update(overrides)
    return question


@pytest.fixture(autouse=True)
def canonical_metadata(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        fetch_leetcode_question,
        "leetcode_metadata",
        lambda challenge_id: {
            "challenge_id": challenge_id,
            "frontend_id": "1902",
            "slug": "depth-of-bst-given-insertion-order",
        },
    )


def test_fetch_question_returns_authenticated_transient_evidence() -> None:
    client = _Client(_question())

    result = fetch_leetcode_question.fetch_question(client, "lc_1902")

    assert result["authenticated"] is True
    assert result["provider"] == "leetcode.com"
    assert result["paid_only"] is True
    assert result["content_text"] == "Return the tree's depth.\nRoot depth is 1."
    assert result["code_snippets"][0]["code"].startswith("class Solution:")
    assert client.request == {
        "url": "https://leetcode.com/graphql/",
        "json": {
            "query": fetch_leetcode_question.QUESTION_QUERY,
            "variables": {"titleSlug": "depth-of-bst-given-insertion-order"},
        },
        "headers": {
            "Referer": (
                "https://leetcode.com/problems/depth-of-bst-given-insertion-order/"
            )
        },
        "timeout": 60,
    }


@pytest.mark.parametrize(
    "overrides, message",
    [
        ({"questionFrontendId": "1903"}, "identity does not match"),
        ({"titleSlug": "wrong-slug"}, "slug does not match"),
        ({"content": None}, "no Premium statement content"),
    ],
)
def test_fetch_question_rejects_untrusted_or_inaccessible_payloads(
    overrides: dict[str, Any],
    message: str,
) -> None:
    with pytest.raises(RuntimeError, match=message):
        fetch_leetcode_question.fetch_question(_Client(_question(**overrides)), "lc_1902")
