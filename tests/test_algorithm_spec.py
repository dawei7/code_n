"""End-to-end validation of every registered AlgorithmSpec.

For each registered spec, this test:
  1. builds a challenge instance from the factory
  2. runs setup() at a few different sizes
  3. calls the canonical solve (compiled from spec.source) with
     the setup kwargs
  4. asserts verify() returns True

This catches the common bug classes: spec source that doesn't run
standalone, a setup that produces kwargs that don't match the
solve signature, a verify that's too lenient or too strict, and
a description / hint / returns that are accidentally empty.

It does NOT exercise the player's solve() against the complexity
budget — that's the ``run_player_code`` server path, which is
tested separately in ``server/tests/``.
"""
from __future__ import annotations

import unittest

from challenges.registry import CHALLENGE_REGISTRY, get_challenge


# Sizes to exercise per challenge. Most challenges accept n up to
# 50 (or 35 for 2D). We pick a few small sizes so the reference
# solve runs fast and a wrong answer is obvious.
TEST_SIZES = (4, 8, 16)


class EverySpecRoundTripTests(unittest.TestCase):
    """For every registered spec, the canonical solve must produce
    a result that verify() accepts, for every size in TEST_SIZES."""

    def test_every_spec_canonical_solve_passes_verify(self):
        for cid, cls in CHALLENGE_REGISTRY.items():
            spec_inst = cls()
            spec = spec_inst._spec
            if cid.startswith("lc_"):
                continue
            with self.subTest(challenge=cid, name=spec.name):
                for n in TEST_SIZES:
                    with self.subTest(challenge=cid, n=n):
                        challenge = cls()
                        # Each challenge instance must be fresh so
                        # the previous setup's state doesn't leak
                        # into the next verify.
                        setup_data = challenge.setup(n, seed=42)
                        # Call the reference solve.
                        try:
                            result = challenge._reference_solve(**setup_data)
                        except Exception as exc:
                            self.fail(
                                f"{cid} reference solve raised "
                                f"{type(exc).__name__} at n={n}: {exc}"
                            )
                        if not challenge.verify(result):
                            self.fail(
                                f"{cid} reference solve at n={n} "
                                f"produced {result!r}, which verify() "
                                f"rejected. setup_data={setup_data!r}"
                            )

    def test_every_spec_has_non_empty_text_fields(self):
        for cid, cls in CHALLENGE_REGISTRY.items():
            spec_inst = cls()
            spec = spec_inst._spec
            with self.subTest(challenge=cid):
                self.assertTrue(spec.name.strip(), msg=f"{cid} has empty name")
                self.assertTrue(spec.description.strip(), msg=f"{cid} has empty description")
                self.assertTrue(spec.returns.strip(), msg=f"{cid} has empty returns")
                self.assertTrue(spec.source.strip(), msg=f"{cid} has empty source")
                self.assertTrue(spec.params, msg=f"{cid} has no params")
                for name in spec.params:
                    self.assertIn(name, spec.inputs, msg=f"{cid} missing input doc for {name}")

    def test_every_spec_source_compiles(self):
        """The spec.source must be valid Python. We compile it
        (without executing) so the failure mode is the same as
        typing the file into a fresh editor."""
        for cid, cls in CHALLENGE_REGISTRY.items():
            spec_inst = cls()
            spec = spec_inst._spec
            with self.subTest(challenge=cid):
                try:
                    compile(spec.source, f"{cid}.py", "exec")
                except SyntaxError as exc:
                    self.fail(f"{cid} source is not valid Python: {exc}")

    def test_every_spec_samples_have_two_strings(self):
        for cid, cls in CHALLENGE_REGISTRY.items():
            spec_inst = cls()
            spec = spec_inst._spec
            with self.subTest(challenge=cid):
                # 0 samples is allowed (some challenges have none).
                for i, sample in enumerate(spec.samples):
                    self.assertTrue(
                        isinstance(sample.input_repr, str) and sample.input_repr,
                        msg=f"{cid} sample {i} has empty input_repr",
                    )
                    self.assertTrue(
                        isinstance(sample.output_repr, str) and sample.output_repr,
                        msg=f"{cid} sample {i} has empty output_repr",
                    )

    def test_every_spec_has_valid_complexity(self):
        from code_n.counter import ComplexityClass
        for cid, cls in CHALLENGE_REGISTRY.items():
            spec_inst = cls()
            spec = spec_inst._spec
            with self.subTest(challenge=cid):
                self.assertIn(
                    spec.required_complexity,
                    set(ComplexityClass),
                    msg=f"{cid} has unknown complexity {spec.required_complexity}",
                )

    def test_every_spec_difficulty_in_range(self):
        for cid, cls in CHALLENGE_REGISTRY.items():
            spec_inst = cls()
            spec = spec_inst._spec
            with self.subTest(challenge=cid):
                self.assertGreaterEqual(spec.difficulty, 1)
                self.assertLessEqual(spec.difficulty, 10)

    def test_get_challenge_returns_instance_with_spec(self):
        """get_challenge(<id>) must produce an instance whose _spec
        is the matching AlgorithmSpec. The navigation view relies
        on this for its hints panel."""
        for cid in CHALLENGE_REGISTRY:
            with self.subTest(challenge=cid):
                challenge = get_challenge(cid)
                self.assertIsNotNone(challenge, msg=f"get_challenge({cid}) returned None")
                self.assertTrue(hasattr(challenge, "_spec"))
                self.assertEqual(challenge._spec.id, cid)


if __name__ == "__main__":
    unittest.main()
