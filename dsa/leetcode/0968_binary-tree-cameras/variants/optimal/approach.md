## General

**A parent needs three facts about each child**

A camera monitors its node, parent, and immediate children. For a subtree, minimum cost depends on its root's status relative to its parent.

The helper returns `(a, b, c)`:

- `a`: minimum cameras when the subtree root has a camera;
- `b`: minimum cameras when the root has no camera but is monitored;
- `c`: minimum cameras when the root is not monitored, while every lower node is monitored.

The uncovered state is useful because a camera at the parent can cover that root later.

**Null-subtree states**

For `None`, return `(infinity, 0, 0)`.

A nonexistent node cannot hold a camera, so camera state is impossible. Infinity prevents transitions from selecting it.

It costs zero for an absent subtree to be considered covered or awaiting parent coverage because there is no real node to violate either condition.

**State `a`: place a root camera**

A root camera monitors both child roots. Each child may therefore be in any state: camera, covered, or uncovered and relying on the current camera.

Choose the cheapest state independently for each child and add one:

`a = min(la, lb, lc) + min(ra, rb, rc) + 1`.

**State `b`: covered without a root camera**

At least one immediate child must have a camera to monitor the root.

The other child cannot be uncovered because the root has no camera to cover it. It must have a camera or already be covered.

Valid combinations are:

- left camera, right covered: `la + rb`;
- left covered, right camera: `lb + ra`;
- cameras on both: `la + ra`.

Their minimum is `b`.

**State `c`: root remains uncovered**

Neither child may have a camera, because a child camera would monitor the root.

Both child roots must nevertheless be covered, so they both use state `b`:

`c = lb + rb`.

The parent may later place a camera.

**Why the whole root cannot use `c`**

The tree root has no parent. If it remains uncovered, no outside camera can rescue it.

The solution returns `min(a, b)`, requiring the root to hold a camera or be covered by a child camera.

**Leaf example**

A leaf has two null children.

- Camera state costs one.
- Covered-without-camera state is impossible because no child can hold a camera.
- Uncovered state costs zero because there are no lower real nodes.

This is correct: a leaf may wait for its parent's camera, but if it must be covered entirely inside its own subtree, it needs a camera.

**Why the DP is correct**

The three states distinguish every possible interaction between a subtree root and its parent. For each state, the formula enumerates all and only legal child-state combinations.

Assuming child costs are optimal, independently choosing the cheapest legal combination gives the optimal current cost. Structural induction proves all tuples.

At the top, excluding the uncovered state enforces monitoring of every node, so the returned minimum is globally optimal.

**Why child subproblems combine independently**

Once the current root's state is fixed, camera choices in the left subtree do not monitor nodes deep in the right subtree, and vice versa. Their only shared interaction is through whether each child root monitors or relies on the current root.

The three state values summarize that boundary completely, allowing costs to be added.

**Why the three states are mutually informative**

It is not enough to store only “covered” versus “uncovered.” A covered child root might be covered by its own camera or by a camera one level below. Those cases affect the parent differently: only a camera on the child itself monitors the parent.

Separating `a` from `b` preserves this information. Separating `c` tells the parent when its own camera is required to cover a child root. Together, the states contain exactly the boundary information and no complete camera placement history.

**Why cameras deeper than a child cannot cover the current root**

A camera reaches only its own node, parent, and immediate children. A grandchild camera can cover the child but not the current root.

That is why state `b` requires an actual child state `a` rather than merely a covered child. The transition respects the one-edge monitoring radius precisely.

**An internal-node example**

Suppose both children are uncovered state `c`. Placing a camera at the current root makes both valid, which state `a` permits by taking child minima including `c`.

Without a root camera, neither uncovered child can be rescued, so states `b` and `c` never combine with child `c`. This illustrates how the formulas exclude hidden coverage gaps.

## Complexity detail

Let `N` be node count and `H` height.

Every node is processed once with constant state arithmetic, giving `O(N)` time.

The recursion stack uses `O(H)` space. The manifest's `O(N)` is a valid worst case for a chain; balanced trees use `O(log N)`.

## Alternatives and edge cases

- **Greedy postorder states:** Mark nodes as needing coverage, covered, or containing a camera, placing cameras above uncovered children. It is also linear.
- **Try every camera subset:** Exponential and ignores subtree independence.
- **Camera at every leaf parent:** Helpful intuition but needs careful root and chain handling.
- **Single node:** The root cannot remain uncovered, so one camera is required.
- **Null child:** Its camera cost is infinity, preventing imaginary placement.
- **Root covered by one child:** State `b` permits exactly one child camera.
- **Both child cameras:** Included when their subtrees make it cheapest.
- **Uncovered internal root:** Valid only when its parent will cover it.
- **No mutation:** The tree is read only.
- **Deep tree:** Recursion may approach `N` frames and hit Python's recursion limit.
