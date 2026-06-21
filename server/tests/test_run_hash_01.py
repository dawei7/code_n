"""End-to-end: ``POST /api/challenges/hash_01/run`` with the Two Sum optimal solution.

Verifies that the linear hash-map implementation is correctly classified as O(n)
using the reference-derived dynamic complexity limits and tolerance bands, and
that the response message includes the reference and user coefficients.
"""
from __future__ import annotations

from challenges.algorithms.hashing import HASH_01_SOURCE

from . import conftest


class RunHash01Test(conftest._Base):
    def test_optimal_two_sum_passes_as_o_n(self) -> None:
        r = self.client.post(
            "/api/challenges/hash_01/run",
            json={"source": HASH_01_SOURCE, "n": 16, "seed": 1},
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertTrue(body["passed"], f"expected passed=true, got: {body}")
        self.assertTrue(body["correct"])
        self.assertTrue(body["within_threshold"])
        self.assertEqual(body["actual_complexity"], "O(n)")
        self.assertEqual(body["required_complexity"], "O(n)")
        
        # Verify the message does not display coefficients in the result tab,
        # but reference_coefficient is returned in the response.
        self.assertIn("Passed!", body["message"])
        self.assertIn("complexity: O(n)", body["message"])
        self.assertNotIn("ref coeff:", body["message"])
        
        self.assertIsNotNone(body["reference_coefficient"])
        self.assertGreater(body["reference_coefficient"], 0.0)
        self.assertEqual(body["scaling_data"], [])
        
        # The AST op counts should be reported
        self.assertGreater(body["user_ast_ops"], 0)
        self.assertGreater(body["reference_ast_ops"], 0)
