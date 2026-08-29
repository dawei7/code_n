## General

The required rows are ordered deepest-to-root, but discovering tree depths is easiest from root-to-deepest with ordinary breadth-first search. The selected solution first builds normal level order, then reverses the outer list of completed rows.

Values inside each row must remain left-to-right. Only row order changes.

**Queue invariant and level boundary**

At the beginning of each outer iteration, `q` contains exactly one tree level in left-to-right order.

`range(len(q))` captures the current frontier size before any children are appended. If it is $k$, the inner loop removes exactly $k$ nodes. Children added during those removals remain for the next outer iteration, preventing levels from mixing.

A fresh list `t` stores current values. Each parent is dequeued left-to-right, and its left child is appended before its right child. Therefore the queue left after the loop is the next level in correct left-to-right order.

The timing of `len(q)` matters. Python evaluates it once while constructing the `range`; it does not keep asking how long the growing queue is. For example, if the current level has two parents and they contribute three children, the loop still runs twice, not five times. Without that frozen boundary, those children could be removed immediately and mixed into their parents' row.

The fresh `t` also matters. Appending one new list per depth gives every output row its own container. Reusing and clearing a single list would make previously appended entries refer to the same mutable object and would destroy earlier rows.

**Why build top-down first**

The root is known immediately, while the deepest level is not known until traversal finishes. Attempting to emit final order online would require inserting each newly discovered row before all earlier rows or storing it elsewhere.

Appending top-down rows is constant amortized time. The final `ans[::-1]` then reverses only the sequence of row references. It does not reverse values inside a row and does not copy individual integers.

**Trace through the Reference example**

Starting with root three, the first frontier produces `[3]` and enqueues nine and twenty. The next produces `[9, 20]` and enqueues fifteen and seven. The final produces `[15, 7]`.

Before reversal:

`ans = [[3], [9, 20], [15, 7]]`.

The outer slice returns:

`[[15, 7], [9, 20], [3]]`.

Notice that `[15, 7]` remains left-to-right. Reversing every row would solve the zigzag problem instead.

**Why every node and depth is correct**

The root establishes the frontier invariant. Assuming a frontier contains exactly depth $d$, processing its fixed initial length records exactly those nodes. Adding real children in parent order constructs exactly depth $d+1$.

Every non-root node has one parent and is enqueued once. Every queued node is removed once and contributes one value. Thus the top-down rows are complete and duplicate-free. Reversing their outer order maps depth zero through $H-1$ into $H-1$ through zero, exactly the contract.

This argument does not depend on the tree being complete or balanced. A missing child is simply not enqueued. The remaining real children retain the order induced by their left-to-right parents, which is precisely the order a breadth-first view of that depth requires.

**Exact source dependencies**

The selected file uses `deque` without importing it. A nonempty standalone call raises `NameError` at `deque([root])` unless the harness injects the name. It needs `from collections import deque`.

The empty case returns before evaluating `deque`, so it happens to work even without the import.

## Complexity detail

Each of the $n$ nodes is enqueued and dequeued once, so BFS costs $O(n)$. Reversing the outer list touches $H$ row references, where $H$ is the number of levels and $H\le n$; therefore total time remains $O(n)$.

Let $w$ be maximum width. The queue contains portions of at most two adjacent frontiers and needs $O(w)$ references.

More precisely, during a level transition the queue can contain unprocessed nodes of the current depth together with children already appended for the next depth. Both portions are bounded by a constant multiple of the tree's maximum width, so this coexistence does not change the $O(w)$ frontier bound.

There is a subtle exact-source space qualification. `ans[::-1]` allocates a second outer list with $H$ row references while original `ans` still exists. The row lists and values are required output, but this duplicated outer container adds $O(H)$ peak storage. Strictly, the exact peak is $O(w+H)$, potentially $O(n)$ for a skewed tree. The manifest's $O(w)$ describes BFS frontier space while treating output construction and its final shallow reversal as output-related.

The completed row lists collectively contain exactly $n$ integer entries and therefore occupy $O(n)$ output space regardless of the tree's shape. That required returned data is normally excluded from auxiliary-space claims. Distinguishing required output storage, traversal workspace, and the temporary copied outer list explains why several apparently different space bounds can all appear in discussions of this algorithm.

Using `ans.reverse()` and returning `ans` would eliminate the second outer list and make the auxiliary frontier claim cleaner.

## Alternatives and edge cases

- **In-place outer reversal:** Call `ans.reverse()` after BFS. It changes row order without an $O(H)$ copied container.
- **Deque of rows:** Add each completed level with `appendleft`, then convert for return; conversion still builds the required output list.
- **Recursive DFS by depth:** Build top-down rows using $O(h)$ stack space, then reverse.
- **Empty root:** Returns `[]`.
- **Single node:** Reversing a one-row list changes nothing.
- **Sparse levels:** Only real nodes appear, always left-to-right within their depth.
- **Do not reverse inner rows:** Bottom-up changes depth order only.
- **Missing import:** Add `collections.deque`.
- **Skewed tree:** $w=1$ but $H=n$, exposing the final-slice space nuance.
