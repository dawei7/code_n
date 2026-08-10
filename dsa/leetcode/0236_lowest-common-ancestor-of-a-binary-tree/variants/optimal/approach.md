## General

**Let each subtree report what it found**

This is an ordinary binary tree, so node values provide no direction for
searching. The exact recursive method asks both child subtrees for a report.
A call returns one of three kinds of result:

- `None` if that subtree contains neither target;
- `p` or `q` if it contains one target but not evidence of both;
- the lowest common ancestor inside that subtree if it contains both.

The parent combines the left and right reports. If both are non-null, the two
target paths meet at the current root. If only one is non-null, all discovered
target evidence lies on that side and should be passed upward unchanged.

**The base case handles absence and target identity**

`if root in (None, p, q): return root` combines three base cases.

For `root is None`, the branch contains no target and returns `None`. If the
current node is `p` or `q`, it returns that node immediately. This uses the LCA
definition that a node is allowed to be a descendant of itself.

Returning immediately at a target is safe even though the other target might
lie below it. If the other target is in this target's subtree, the target node
itself is their LCA and is exactly the result that should propagate upward. If
the other target lies elsewhere, another recursive branch eventually reports
it; the first ancestor receiving both non-null reports becomes the LCA.

The platform passes the actual `TreeNode` objects for `p` and `q`, so the
comparison identifies target nodes rather than merely matching values. The
unique-value guarantee makes the external JSON-to-node resolution
unambiguous.

**Combine left and right reports after both calls**

For a non-null, non-target root, the source recursively evaluates its left
subtree and stores the result in `left`, then does the same for the right
subtree in `right`.

If both values are truthy, one target-related report came from each child side.
No node below the current root can be an ancestor of nodes in both disjoint
subtrees, so the current root is their lowest common ancestor. The expression
returns `root`.

If only `left` is non-null, the right subtree contains no target evidence. Any
LCA for both targets either is already represented by `left` or must be higher
in the tree, so the method returns `left`. The same reasoning applies
symmetrically to `right`. If both are `None`, `(left or right)` is `None`.

The compact return
`root if left and right else (left or right)` therefore encodes all four
combinations of child reports.

**Trace targets in different root subtrees**

In the reference tree with targets 5 and 1, recursion into the left subtree
eventually reaches node 5 and returns it. Recursion into the right subtree
reaches node 1 and returns it. At root 3, both `left` and `right` are non-null,
so node 3 is returned. It is the first node where the two target reports come
from separate child sides.

For targets 5 and 4, the call at node 5 hits the target base case and returns 5
without needing to descend to node 4. That is correct because node 5 is an
ancestor of node 4 and a target can be its own ancestor. Higher calls receive
only that one non-null report and propagate node 5 to the top.

**Why the first merge is the lowest common ancestor**

Consider a non-target call after its child recursions finish. A non-null child
report proves that child subtree contains at least one target, or already
contains their LCA. When both sides report, the targets occupy different child
subtrees. The current node is a common ancestor, and neither child subtree can
contain both targets, so no descendant can be a lower common ancestor.

If only one side reports, returning it postpones the decision without losing
information. Eventually either that report meets evidence from the other target
at an ancestor, or it is already a target ancestor returned by the base case.
Because both targets are guaranteed to exist in the full tree, the top-level
result is the required non-null node.

This reasoning also explains why `val` is never inspected. General binary-tree
LCA depends on topology and target identity, not numeric ordering.

**The exact source is recursive, contrary to the manifest summary**

The manifest says this branch simulates postorder traversal with explicit
frames to avoid Python recursion limits. The executable source directly calls
`lowestCommonAncestor` recursively on both children. It therefore uses the
language call stack and can encounter recursion-depth limits on a sufficiently
skewed tree, especially with the stated maximum of $10^5$ nodes.

The algorithmic space is still $O(h)$ for tree height $h$, matching the
manifest's asymptotic symbol, but the operational claim about avoiding
recursion is false for this source. The commented `TreeNode` definition remains
platform-provided harness structure.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. In the worst case the
recursive search visits every node once, doing constant work per visit, for
$O(n)$ time. Target base cases can prune descendants in some inputs, but they
do not improve the worst-case bound.

At most one root-to-leaf chain of calls is active at a time, so auxiliary stack
space is $O(h)$. This is $O(\log n)$ for a balanced tree and $O(n)$ for a
skewed tree. No parent map, visited set, or copied tree is allocated.

## Alternatives and edge cases

- **Explicit postorder frames:** Store `(node, state)` records in a stack and propagate target reports iteratively. It preserves $O(n)$ time and $O(h)$ space while avoiding Python call-stack limits, matching the manifest summary but adding state-management complexity.
- **Parent map plus ancestor set:** Iteratively discover parent references until both targets are found, store all ancestors of one target, then climb the other. It avoids recursion but uses $O(n)$ extra memory in the worst case.
- **Root is a target:** The base case returns it immediately. Since the other target exists somewhere in its tree, root is the LCA under the self-descendant definition.
- **Targets in opposite child subtrees:** Both recursive reports are non-null, so the current root is returned at their first split.
- **Targets in the same subtree:** Only one child report is non-null until recursion reaches their lower meeting point; higher nodes merely propagate that result.
- **A target is ancestor of the other:** Encountering the ancestor target returns it directly, which is the correct LCA.
- **Skewed tree:** Time remains linear, but recursive depth can reach $n$ and may exceed Python's default limit. An explicit stack is safer for the maximum constraint.
- **Unique values:** The method itself uses node objects rather than value ordering. Uniqueness matters primarily to the runner that resolves target values to node references.
- **Missing target:** The reference excludes it. Without both targets present, this compact recurrence could return the one target it did find rather than signal invalid input.
- **Distinct targets:** `p != q` is guaranteed. If they were the same node, the base case would return it, which is still a natural LCA result.
- **Input preservation:** Recursive calls inspect links only; no node value or child reference is changed.
