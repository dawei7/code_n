## General

**Breadth-first traversal matches tree levels**

The answer depends on sums of complete levels, so breadth-first search is the natural traversal. A queue holds exactly the nodes waiting at the current or later levels.

It begins with the root in `deque([root])` and `level = 1`, matching the statement's one-based level numbering.

At the start of each outer `while` iteration, `len(q)` is the number of nodes in the current level. The inner loop captures that length once and removes exactly that many nodes. Children are appended to the back, but because the iteration count is fixed, those children remain for the next outer iteration rather than being mixed into the current sum.

Variable `t` accumulates `node.val` for the complete current level.

**Track the earliest minimum**

`s` stores the smallest level sum seen so far, and `ans` stores its level number. Initially `s = inf`, so the root level always becomes the first candidate.

After a level is summed, the code updates only when

`s > t`.

The strict inequality is how ties are resolved. If a later level has the same minimum sum, `s > t` is false, so the earlier, lower-numbered level remains in `ans`.

Here “lowest level” in a tie means the smallest level number, closest to the root. Processing levels in ascending order and refusing equal-value replacement enforces that rule.

**Queue invariant**

At the beginning of the iteration for level $\ell$, the queue contains exactly all tree nodes at level $\ell$ and no nodes from an earlier level.

This holds initially for the root. Removing every current node and appending each non-null child adds exactly all nodes one edge farther from the root. No other nodes are added. After the fixed-size inner loop ends, the queue therefore contains exactly level $\ell+1$.

The invariant proves that `t` is the sum of one whole level and that `level` labels it correctly.


Every tree level is processed exactly once in increasing level order. After processing the first $\ell$ levels, `s` is their minimum sum and `ans` is the earliest level attaining it:

- a strictly smaller new sum replaces both;
- a larger sum changes nothing;
- an equal sum changes nothing, preserving the earlier level.

By induction, after the queue becomes empty, these values summarize all levels. `ans` is therefore the required minimum-sum level with the correct tie break.

**Examples and value behavior**

If root value is 5 and each later level also sums to 5, the strict update keeps level 1.

If level sums are 36, 27, and 24, each smaller sum replaces the previous candidate, leaving level 3.

The local constraints make node values positive, but the algorithm would also work with negative values. It compares full sums and initializes with positive infinity, so no assumption that deeper levels have larger sums is made.

**Why depth-first traversal is less direct**

A DFS could accumulate sums in an array indexed by depth, then scan that array. BFS avoids storing a separate sum for every level and knows when one complete level has finished, allowing the minimum to be updated immediately.

The platform supplies the `TreeNode` class. The solution only traverses its `left` and `right` links and does not recreate the harness type.

## Complexity detail

Let $n$ be the number of tree nodes.

Every node is enqueued once, dequeued once, and contributes to one addition. Time is $O(n)$.

The queue holds at most the tree's maximum width $w$, so auxiliary space is $O(w)$ and $O(n)$ in the worst case for a broad tree. The scalar sums and level variables use $O(1)$ additional space.

The traversal is iterative and does not risk recursion depth on a skewed tree.

The result is one integer. The tree structure is not modified.

Level sums can reach $10^{14}$ under the constraints; Python integers handle them without overflow.

## Alternatives and edge cases

- **DFS with depth sums:** Accumulate `sums[depth]` recursively or iteratively, then return the first index of the minimum. It uses $O(h)$ or $O(number\ of\ levels)$ additional state.
- **Recursive BFS:** It is possible but adds call-stack overhead without simplifying level boundaries.
- **Update on `>=`:** Incorrect for the tie rule because it would replace an earlier minimum with a later equal level.
- **Single-node tree:** The root is the only level and is selected from the initial infinity comparison.
- **Skewed tree:** Each level contains one node; queue size stays one while time remains linear.
- **Complete tree:** The final level may contain $\Theta(n)$ nodes, giving worst-case queue space.
- **Equal level sums:** The first occurrence remains because comparison is strict.
- **Large positive values:** Only exact integer addition and comparison are used.
- **Null children:** They are not enqueued, so they contribute neither nodes nor values.
- **One-based levels:** `level` starts at 1 and increments after processing, matching the contract.
- **Non-null root:** The node-count constraint guarantees at least one node; otherwise dequeuing `None` would fail.
- **Input preservation:** Child pointers and node values are only read.
