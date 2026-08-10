## General

The algorithm separates two questions:

1. Are two trees exactly identical from their current roots?
2. Does any node in the larger tree begin an identical copy of `subRoot`?

Helper `same(p, q)` answers the first question recursively.

**Handle missing nodes structurally.** If either `p` or `q` is `None`, the helper returns `p is q`.

This is true only when both are `None`. If one exists and the other does not, the structures differ even if all previously compared values matched.

Using identity here is safe because the only accepted case in this branch is the singleton object `None` on both sides.

**Match value and both child structures.** For two real nodes, the helper returns true only when:

- `p.val == q.val`;
- their left subtrees are identical;
- their right subtrees are identical.

Logical `and` short-circuits. A value mismatch avoids unnecessary child comparisons, and a failed left comparison avoids the right comparison.

This exact structure check prevents a tree with an extra descendant from matching a smaller pattern. In the second example, values at the apparent root may agree, but the extra zero causes one corresponding pair to be real versus null, so `same` returns false.

The outer `isSubtree` search treats each node in `root` as a possible match start.

If `root is None`, no candidate node remains, so it returns false. The source supplies a nonempty `subRoot`, making this base case appropriate.

Otherwise it evaluates:

- `same(root, subRoot)`;
- search the left subtree;
- search the right subtree.

The OR expression short-circuits at the first success.

For the first example, the search eventually reaches node value four. `same` verifies values four, one, and two and matching null child positions, so true propagates back.

**Why all possible subtree roots are examined.** A subtree is defined by choosing one node and taking all its descendants. The outer recursion visits the current node and then every node in both child subtrees. Therefore every legal candidate root is considered exactly once unless an earlier match permits early return.

**Why every true result is valid.** True can originate only from `same` at some real node of the larger tree. That helper proves equal root values and recursively equal left/right structure and values through all descendants, exactly matching the subtree definition.

**Why every valid subtree is found.** If `subRoot` occurs at larger-tree node `v`, outer DFS eventually reaches `v`. The exact recursive correspondence makes `same(v, subRoot)` true.

The whole larger tree can match because the very first candidate is `root` itself.

Consider a larger tree containing many nodes with value one and a smaller tree that is a long chain of ones ending in a different final value. At each candidate, `same` may traverse almost the full chain before discovering the mismatch. This is the pattern that realizes the multiplicative worst case and explains why early value checks do not guarantee linear time.

The outer recursive calls occur only after `same(root, subRoot)` fails. Python evaluates the OR operands from left to right. It searches the left subtree before the right, but this order is not semantically important because any matching candidate is sufficient.

Null placement is as important as values. A root with left child two is not identical to a root with right child two, even though preorder value sequences without null markers could look the same. `same(p.left, q.left)` and `same(p.right, q.right)` preserve orientation explicitly.

Node values alone are insufficient. The same sequence of values arranged with different left/right links must fail, which null-position comparisons enforce.

**Exact complexity distinction.** The solution is a direct search, not the linear serialization or tree-hash method implied by the manifest. In the worst case, many larger-tree nodes have the same value as `subRoot`'s root and `same` compares much of the smaller tree at each candidate.

## Complexity detail

Let $n$ be the node count of `root` and $m$ that of `subRoot`. Outer search visits up to $n$ candidate nodes, and one `same` call can inspect $O(m)$ nodes. Exact worst-case time is $O(nm)$, not the manifest's $O(n+m)$.

Recursion for the outer search and equality check uses stack depth based on tree heights, up to $O(n+m)$ in skewed worst cases. No explicit linear containers are allocated. The manifest's linear time/space corresponds to serialization with linear string matching or robust tree hashing, not this exact source.

Calls do not generally hold $n$ separate equality traversals simultaneously; the bound describes the maximum combined nesting of an outer search path and one active structural comparison.

## Alternatives and edge cases

- **Serialize with null markers plus KMP:** It can achieve $O(n+m)$ time; null markers and value boundaries are essential to avoid structural false matches.
- **Tree hashing:** Compute robust subtree hashes and compare candidates, with collision considerations.
- **Compare preorder values only:** It loses null structure and can report different shapes as equal.
- **Whole-tree match:** Checked at the initial root.
- **Extra child:** Structural comparison rejects it.
- **Repeated values:** They may trigger many expensive candidate comparisons but do not harm correctness.
- **Leaf `subRoot`:** Any larger-tree leaf or internal node with the same value is tested; an internal node fails due to extra children.
- **No match:** Every candidate is exhausted and false is returned.
- **Short-circuiting:** Stops child work after a mismatch or stops search after a match.
- **Deep skewed trees:** Recursion depth may exceed Python's default limit.
