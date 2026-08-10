## General

A valid path may start and end anywhere, but it cannot repeat a node or branch into three directions. This creates two related quantities at every node:

- the best complete path whose highest node is the current node; and
- the best one-ended gain that can be extended upward through the parent.

The selected postorder DFS computes the extendable gain as its return value and updates a shared `ans` with complete paths.

**Why children must be processed first**

To decide whether a path through a node should include its left or right subtree, the algorithm needs the best downward gain each child can contribute. Those values are known only after solving the children.

Postorder traversal—left, right, current—provides exactly that order. Each child returns the largest sum of a path that begins at the child and continues downward through at most one branch.

An absent child returns zero because it contributes no node and no gain.

**Why negative gains become zero**

The path is not required to include a child. If a child's best downward gain is negative, attaching it would reduce the sum. `max(0, dfs(child))` models the choice to omit that entire side.

Zero does not represent an empty final answer. It is only an optional contribution to a path that already contains the current real node.

This distinction matters when all values are negative. The algorithm may omit both children, but it still evaluates `root.val` as a nonempty one-node path.

**The complete path through a node**

After obtaining nonnegative `left` and `right` gains, the best path whose highest point is the current node has sum:

$$
\texttt{root.val}+\texttt{left}+\texttt{right}.
$$

It may use both children because it starts somewhere in one child branch, travels up to the current node, and travels down the other child branch. The current node has at most two neighbors within that path, so the sequence is valid.

If one gain is zero, the candidate uses only the other side. If both are zero, the candidate is the current node alone. One expression covers all four structural choices.

`ans` is updated with this candidate at every node, so the maximum path is found even when it does not pass through the original tree root.

**Why the returned gain uses only one side**

The caller may attach the returned path to the current node's parent. That adds a third possible direction above the node.

If the returned structure already used both left and right child branches, adding the parent edge would make the current node have three neighbors in the supposed path. That is a fork, not a single sequence.

Therefore the extendable return is:

$$
\texttt{root.val}+\max(\texttt{left},\texttt{right}).
$$

It chooses at most one child branch. The two-sided candidate is considered for the global answer but never propagated upward.

**Why `ans` starts at negative infinity**

The tree is nonempty, but every node may have a negative value. Initializing `ans` to zero would incorrectly allow an empty path and return zero for a tree such as `[-3]`.

Negative infinity ensures the first real node candidate replaces the initial value. Since each node can form a one-node path, the final answer is at least the maximum node value and always corresponds to a nonempty path.

**Why all valid paths are considered**

Every simple path in a rooted tree has a unique highest node: the node on that path closest to the original root.

At that highest node, the path either uses no child branch, one child branch, or one branch from each child. The candidate formed there includes the best nonnegative gain available for exactly those directions and is at least as large as that particular path.

Conversely, each candidate combines downward paths that meet only at the current node, so it is itself valid. Updating across every possible highest node therefore finds exactly the maximum valid path sum.

**Tracing the value 42 example**

Leaves nine, fifteen, and seven return their own positive values. At node twenty, left gain is fifteen and right gain is seven.

The complete candidate through twenty is `20 + 15 + 7 = 42`, so `ans` becomes forty-two. Its extendable return is `20 + max(15, 7) = 35`; returning forty-two would incorrectly try to pass a two-sided path through parent `-10`.

At root `-10`, the best complete candidate is lower than forty-two, so the global answer remains the path `15 -> 20 -> 7`.

**All-negative behavior**

At a negative leaf, both child gains clamp to zero. The complete candidate is its negative value, and the return is also that value.

Its parent clamps the returned negative gain to zero, refusing to extend through it. Because each leaf already updated `ans`, the best single negative node is still retained.

**Source dependencies**

The source expects `Optional`, `TreeNode`, and `inf` from the surrounding environment. A standalone module needs appropriate typing and node definitions plus `from math import inf`, or it can initialize with `float("-inf")`.

The method does not mutate the input tree or inspect relationships beyond `left`, `right`, and `val`.

## Complexity detail

Let $n$ be the node count and $h$ the maximum root-to-leaf node count. Every node is visited once and performs constant local work, so time is $O(n)$.

The recursive stack contains at most one active root-to-descendant path, using $O(h)$ auxiliary space. This is $O(\log n)$ for a balanced tree and $O(n)$ for a chain.

Only scalar gains and `ans` are stored beyond the stack. The returned integer needs constant output space.

With up to 30,000 nodes, a highly skewed legal tree can exceed Python's default recursion limit. An explicit postorder stack avoids that runtime limitation while retaining $O(h)$ asymptotic space.

## Alternatives and edge cases

- **Iterative postorder frames:** Use enter and exit states plus child-result holders. It avoids interpreter recursion limits and preserves $O(h)$ stack space.
- **Return `(subtree_best, extendable_gain)`:** Eliminates `nonlocal ans` by returning both quantities explicitly.
- **Enumerate all node pairs:** Every pair determines a path, but calculating all paths is at least quadratic and unnecessary.
- **Clamp the current node to zero:** Incorrect because the final path must be nonempty; only optional child contributions may be discarded.
- **Return both child gains to the parent:** Incorrect because it creates a branch with three incident path edges.
- **Non-root optimum:** The global update at every node is necessary.
- **Single node:** Returns that value, including when it is negative.
- **All-negative tree:** Returns the least negative node rather than zero.
- **Zero-valued nodes:** They can connect positive branches without reducing the sum.
- **One child:** The two-sided candidate naturally reduces to node plus that positive gain.
- **Both positive children:** Both may appear in a complete path through the node.
- **Negative child subtree:** Its contribution is omitted, but paths entirely inside it were already considered locally.
- **Nonempty contract:** Makes negative-infinity initialization safe to replace during traversal.
- **Recursion limit:** Iterative postorder is safer for a 30,000-node chain.
- **Missing names:** `Optional`, `TreeNode`, and `inf` must be available.
