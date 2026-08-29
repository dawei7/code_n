## General

**Breadth-first search naturally separates levels**

A queue-based breadth-first traversal visits the tree level by level. Initially, `q` contains only `root`, which is level one.

At the beginning of every `while q` iteration, the queue contains exactly all nodes of one level and no nodes from a later level. The solution increments `i` to that level's one-based number and resets `s` to zero for its sum.

**Freeze the current queue length**

`range(len(q))` evaluates the queue size before processing the level. Exactly that many nodes are removed and added to `s`.

While those nodes are processed, their left and right children are appended. The captured length prevents those children from being consumed in the same iteration. When the loop finishes, the queue contains exactly the next level.

Without this boundary, newly appended descendants could be mixed into the current sum and the level numbers would lose their meaning.

**Track the best sum and earliest level**

`mx` starts at negative infinity. Tree values may be negative, so initializing the maximum to zero would be wrong for a tree whose every level sum is negative.

After one level has been summed, the code updates only when

`mx < s`.

The strict inequality matters. Levels are encountered in increasing numerical order. If a later level ties the current maximum, the condition is false and the earlier recorded `ans` remains unchanged. This implements the requirement to return the smallest level among equal maximum sums.

When a strictly larger sum appears, `mx` becomes that sum and `ans = i` records its level.

**Enqueue only real children**

For each node, a non-null left child and a non-null right child are appended. Missing children add neither a node nor a zero value. This makes each next-level queue contain precisely the nodes that actually exist in the binary tree.

The contract guarantees at least one node, so `root` is real. The first iteration always assigns `ans` because every finite root value is greater than negative infinity.

**Trace the first example**

The first queue contains only value one, so level one has sum one and becomes the initial best.

Its children seven and zero form the next queue. Level two sums to seven, which exceeds one, so the answer becomes two.

The final level contains seven and negative eight, with sum negative one. It does not exceed seven, so level two remains the result.

**Why the algorithm is correct**

By induction on loop iterations, the queue at the beginning of iteration `i` contains exactly the nodes at tree level `i`. This is true initially for the root. Processing all current nodes appends exactly their children, which are precisely the nodes one level deeper, so the property continues.

Therefore, `s` is the exact sum of values at level `i`. After processing a prefix of levels, `mx` is the greatest sum seen and `ans` is the smallest level attaining it: a larger sum replaces the pair, while an equal sum preserves the earlier level.

When the queue becomes empty, every tree level has been processed. The maintained `ans` is consequently the smallest level whose sum is globally maximal.

The solution never needs to store all level sums. Once a level has been compared with the current best, only the best pair is needed.

## Complexity detail

Let `n` be the number of tree nodes. Every node enters the queue once, leaves once, contributes its value once, and has its two child references inspected once. Total time is `O(n)`.

Let `w` be the maximum number of nodes on any level. The queue never holds more than the current and next frontier during processing, which is `O(w)` for a binary tree up to a constant-factor relationship between adjacent widths. The required auxiliary space is `O(w)`.

All other variables use constant space, and no recursion stack is present.

## Alternatives and edge cases

- **Depth-first search with a level-sum array:** DFS can accumulate each node into a list indexed by depth, also in `O(n)` time, but stores `O(h)` sums plus an `O(h)` recursion stack.
- **Store every breadth-first level as a separate list:** This works but allocates more temporary structure than a single queue and captured level size.
- **Initialize `mx` to zero:** This fails when every level sum is negative. Negative infinity safely accepts the first actual level.
- **Update on `mx <= s`:** That replaces an earlier tied level with a later one, violating the smallest-level tie rule. The comparison must be strict.
- **Single-node tree:** The first and only level is recorded and level one is returned.
- **All negative values:** The least negative level sum wins because `mx` starts below every real sum.
- **Equal maximum sums:** The first occurrence is retained automatically by traversal order and strict updating.
- **Missing children:** They are not queued and do not contribute artificial zero values.
- **A skewed tree:** Each level has one node, so queue space is constant even though tree height is `n`.
- **A wide balanced tree:** Queue storage reaches the maximum level width, explaining the `O(w)` bound.
