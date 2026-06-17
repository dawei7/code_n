"""Unit tests for execution_trace._serialize_locals.

The BFS Grid challenge surfaced a bug where ``_serialize_locals`` stored
the player's mutable containers (list / set / dict) by reference. The
BFS mutates ``frontier`` and ``visited`` in place across all its
iterations, so by the time the renderer read the stored locals, every
captured frame showed the *final* state of the BFS - the variable
panel at step 0 would display the post-goal frontier and the full
visited set instead of the start state. The fix snapshots the
containers so each frame freezes the values at the moment of capture.

The BFS end-to-end test that used to live here (``TrackedGrid`` +
``OperationCounter``) was removed in v0.8.5 along with the runtime
counter. The remaining tests are pure unit tests of
``_serialize_locals``'s snapshot semantics.
"""
from __future__ import annotations

import unittest

from code_n.execution_trace import _serialize_locals


class SerializeLocalsSnapshotTests(unittest.TestCase):
    def test_serialize_locals_copies_lists(self):
        """Direct unit test: a list captured by _serialize_locals must
        be a NEW list, not a reference to the player's list.
        """
        original = [1, 2, 3]
        snapshot = _serialize_locals({"x": original})
        self.assertEqual(snapshot["x"], [1, 2, 3])
        # Mutate the original AFTER serialization. The snapshot
        # must still see the old values.
        original.append(99)
        self.assertEqual(snapshot["x"], [1, 2, 3])
        # And the snapshot must be a different object, so the
        # renderer could sort / consume it without touching the
        # player's list.
        self.assertIsNot(snapshot["x"], original)

    def test_serialize_locals_copies_sets(self):
        original = {1, 2, 3}
        snapshot = _serialize_locals({"v": original})
        self.assertEqual(snapshot["v"], {1, 2, 3})
        original.add(99)
        self.assertEqual(snapshot["v"], {1, 2, 3})
        self.assertIsNot(snapshot["v"], original)

    def test_serialize_locals_copies_dicts(self):
        original = {"a": 1}
        snapshot = _serialize_locals({"d": original})
        self.assertEqual(snapshot["d"], {"a": 1})
        original["b"] = 2
        self.assertEqual(snapshot["d"], {"a": 1})
        self.assertIsNot(snapshot["d"], original)

    def test_serialize_locals_leaves_immutable_alone(self):
        """Scalars, strings, and tuples don't need a copy - they
        can't be mutated. Verify _serialize_locals doesn't make
        a wasteful copy of them.
        """
        a_tuple = (1, 2, 3)
        a_string = "hello"
        snapshot = _serialize_locals(
            {"t": a_tuple, "s": a_string, "n": 42}
        )
        self.assertIs(snapshot["t"], a_tuple)
        self.assertIs(snapshot["s"], a_string)
        self.assertEqual(snapshot["n"], 42)


if __name__ == "__main__":
    unittest.main()
