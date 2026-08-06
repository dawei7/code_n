## General
**Let each subtree report the surviving target path**

A completed subtree reports `None` when it contains neither target, a target when only that target's path survives, or the LCA after two target paths have met. A node equal to `p` or `q` reports itself immediately because the other target, guaranteed to exist in the full tree, can only make that node remain the answer or meet it above.

**Simulate recursive postorder with explicit frames**

Store `(node, state, left)` frames. State zero schedules the left subtree, state one saves its report and schedules the right subtree, and state two combines both reports. A single `result` register carries the report from the most recently completed child into its parent frame.

At every loop boundary, `result` is the complete report of the subtree whose frame was most recently removed. All frames still on the stack are unfinished ancestors, and each saved `left` value is exactly the report needed when that ancestor's right subtree finishes.

**Two non-null child reports meet at the answer**

When both child reports are non-null, the current node is their first meeting point and becomes the report. When only one is non-null, propagate it unchanged. When neither exists, preserve `None`.

No descendant of a node with two non-null child reports can contain both targets, so that node is their lowest common ancestor. A single report is the only possible target path in that subtree and remains valid higher up. Because the explicit states perform the same left, right, then combine order for every node, the report returned after the root frame completes is exactly the LCA.

## Complexity detail
Each of the $n$ nodes enters a constant number of frame states, giving $O(n)$ time. The stack stores only unfinished ancestors and at most one pending sibling frame per level, so it uses $O(h)$ space without relying on Python's call stack.

## Alternatives and edge cases
- **Recursive postorder:** expresses the same recurrence more briefly but can exceed Python's recursion limit on a legal deeply skewed tree.
- **Parent map plus ancestor set:** is iterative but uses $O(n)$ space even when the tree height is small.
- **Ancestor target:** returning a target immediately correctly handles the other target lying below it.
- **Opposite or same-side targets:** postorder reports combine at the first common ancestor regardless of tree shape or target placement.
