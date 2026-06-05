"""Tests for the per-challenge solution templates.

Every challenge's auto-generated starter file must:
  * have EXPLICIT parameter names (no `**kwargs`)
  * show the function signature as `def solve(arg1, arg2, ...):`
  * document the inputs and the return value in a docstring

These properties were added after the user reported the
`**kwargs` template was misleading. The check is purely textual
on the generated template; we don't write the file to disk.
"""
from __future__ import annotations

import re
import unittest

from code_n import solutions
from challenges.registry import get_challenge


class TemplateShapeTests(unittest.TestCase):
    """Every registered challenge's template must look like:

        def solve(arg1, arg2, ...):
            return None

    with the arg names spelled out (not **kwargs)."""

    def test_all_registered_challenges_have_explicit_templates(self):
        registered = set(__import__("challenges.registry", fromlist=["list_challenges"]).list_challenges())
        templated = set(solutions._CHALLENGE_TEMPLATES.keys())
        missing = registered - templated
        self.assertFalse(missing, msg=f"Missing explicit templates for: {sorted(missing)}")

    def test_no_template_uses_kwargs(self):
        for cid, info in solutions._CHALLENGE_TEMPLATES.items():
            params = info["params"]
            self.assertNotIn("**kwargs", params, msg=f"{cid} still uses **kwargs")
            self.assertTrue(all(re.match(r"^[a-z_][a-z0-9_]*$", p) for p in params),
                            msg=f"{cid} has invalid parameter names: {params}")

    def test_template_signature_matches_param_list(self):
        for cid, info in solutions._CHALLENGE_TEMPLATES.items():
            template = solutions._solution_template(
                cid, f"{cid}: {cid.title()}", "test description",
            )
            expected_sig = "def solve(" + ", ".join(info["params"]) + "):"
            self.assertIn(expected_sig, template,
                          msg=f"{cid} template missing signature: {expected_sig}")

    def test_template_documents_inputs(self):
        for cid, info in solutions._CHALLENGE_TEMPLATES.items():
            template = solutions._solution_template(
                cid, f"{cid}: {cid.title()}", "test description",
            )
            self.assertIn("Inputs passed to solve():", template,
                          msg=f"{cid} template missing 'Inputs passed to solve():' line")
            for name in info["params"]:
                self.assertIn(f"{name}:", template,
                              msg=f"{cid} template missing input description for '{name}'")

    def test_template_documents_return(self):
        for cid, info in solutions._CHALLENGE_TEMPLATES.items():
            template = solutions._solution_template(
                cid, f"{cid}: {cid.title()}", "test description",
            )
            self.assertIn(info["returns"], template,
                          msg=f"{cid} template missing return description")

    def test_template_starts_with_solve_call(self):
        """The starter file must be a valid Python file with a
        solve() function, not a stub."""
        for cid, info in solutions._CHALLENGE_TEMPLATES.items():
            template = solutions._solution_template(
                cid, f"{cid}: {cid.title()}", "test description",
            )
            self.assertIn("def solve(", template)
            self.assertIn("return None", template)
            # The sample I/O should be in the docstring if available.
            ch = get_challenge(cid)
            if ch is not None:
                # Sample lines exist for the registered challenges that
                # have a sample set. We just check the template is
                # importable as Python.
                compile(template, f"{cid}_template.py", "exec")


if __name__ == "__main__":
    unittest.main()
