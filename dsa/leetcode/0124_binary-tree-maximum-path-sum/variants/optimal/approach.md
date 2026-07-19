## General
**Separate a parent-extendable arm from a complete turning path**

For each node, recursively compute the best downward gain beginning at each child. Clip a negative gain to zero because including it would reduce any path through the current node. The value returned to the parent may include the current node plus at most one child arm: returning both would branch and could not be embedded in a simple parent path without revisiting the node.

**A complete path may use both child arms exactly once**

The best complete path whose highest—turning—node is current includes `node.val + max(0, left_gain) + max(0, right_gain)`. It may begin in one subtree, pass through current, and end in the other. Update the global answer with this candidate before returning the one-arm gain upward.

**Helper return and global answer have different contracts**

The helper returns the maximum sum of a nonempty downward path starting at its node and continuing through at most one child. The global value is the best unrestricted nonempty simple path found anywhere in fully processed subtrees. Keeping these meanings separate prevents an invalid two-armed gain from being extended by a parent.

**Trace a two-arm optimum and its one-arm return**

At node `20`, gains `15` and `7` are both positive, so the turning path totals $15 + 20 + 7 = 42$. Upward, node `20` can contribute only $20 + 15 = 35$ through one branch.

**Every simple path has one highest turning node**

Relative to the root, any simple path has a unique highest node. From there it uses at most one downward arm in each child subtree. Negative arms can only reduce the sum, while the best positive child gain is the optimal arm on that side.

The algorithm evaluates the node value plus both optimal usable arms as the best path turning at each node. Every valid path appears under its highest node, and the global maximum therefore includes the optimal one. Returning upward only the better single arm preserves the requirement that a parent extension remain a simple path.

## Complexity detail
Each of `n` nodes is visited once with constant work, giving $O(n)$ time. Recursion occupies one root-to-leaf path, so auxiliary space is $O(h)$.

## Alternatives and edge cases
- **Enumerate every pair of endpoints:** repeats paths and is at least quadratic.
- **Return both child gains upward:** would create a branched structure rather than a valid simple path.
- **Initialize the answer to zero:** incorrectly rejects all-negative trees, whose best path is one node.
- Initialize the global answer from a real node value or negative infinity so an all-negative tree selects its least negative node.
- The optimal path may be a singleton, one downward arm, or two arms meeting at a node; the turning-point candidate covers all three after clipping child gains.
