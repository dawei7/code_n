## General

**Breadth-first search preserves level order**

The requested node must have the same depth as `u` and be immediately to its right. Breadth-first search naturally visits a binary tree one level at a time. Enqueuing each left child before the right child also preserves left-to-right order within a level.

The source initializes `q = deque([root])`. At the start of every outer `while` iteration, the queue begins with exactly all nodes of the current level in left-to-right order. Children appended during the iteration belong to the next level and go behind every unprocessed current-level node.

**Freezing the current level size**

The inner loop is:

`for i in range(len(q) - 1, -1, -1)`.

Python evaluates `len(q)` once when creating the `range`. If the current level contains $L$ nodes, the loop values are $L-1,L-2,\ldots,0$, exactly $L$ iterations.

The descending value `i` is used as a count of how many current-level nodes remain after the node about to be popped:

- when `i > 0`, at least one node remains on this level;
- when `i == 0`, the popped node is the level’s rightmost node.

Although children are appended and change the live queue length, they do not change this fixed loop range.

**Queue ordering during one level**

Each iteration removes `root = q.popleft()`. The local variable name `root` is reused for the current node; the original root reference is no longer needed after the queue is initialized.

If the current node is not `u`, its left child is appended first if present, followed by its right child. Those next-level nodes go to the queue’s rear.

Crucially, all not-yet-processed nodes from the current level remain at the front. Thus, before the current level is exhausted, `q[0]` is the next node to the right on that same level, even though children may already be waiting farther back.

**Returning the neighbor or null**

When `root == u`, the source returns:

`q[0] if i else None`.

If `i > 0`, the front of the queue is the next unprocessed node of the current level. Because BFS order is left to right, it is the nearest node to `u`’s right.

If `i == 0`, `u` is the last node of its level. The queue might already contain children for the next level, but returning `q[0]` would be wrong because that node has a different depth. The conditional returns `None` instead.

The function exits immediately when `u` is found. The contract guarantees `u` belongs to the tree, so execution always reaches a return. Python would implicitly return `None` if the outer loop ended unexpectedly, but that path is not needed for valid input.

**Why node identity matters**

The argument `u` is a tree-node object, not merely a value to search for. The comparison `root == u` identifies that node. Standard `TreeNode` objects use identity equality unless customized. The statement also guarantees all values are distinct, so value-based identification would be unambiguous, but the exact source compares node objects.

**A queue trace**

For a level containing nodes `[4,5,6]`, the loop begins with `i` values two, one, zero.

If `u` is node four, four is popped while `i = 2`. The queue front is five, so five is returned.

If `u` is node five, node four is first popped and its children, if any, are appended behind five and six. When five is popped with `i = 1`, queue front is still six, not a child, so six is returned.

If `u` is six, it is popped with `i = 0`. Even if next-level children are in the queue, the method returns `None`.

**Why the invariant is maintained**

Initially, the queue contains only the root, which is the complete first level in left-to-right order.

Assume the queue begins an outer iteration with one complete level. The inner loop pops exactly its frozen number of nodes in order. For each, it appends left then right children. These appended children collectively form the next level in left-to-right parent order and child order. After exactly $L$ pops, no current-level node remains and the queue contains precisely that next level. The invariant holds by induction.

When `u` is encountered, the conditional uses this invariant to return exactly the immediate same-level successor or null.

## Complexity detail

Let $N$ be the number of tree nodes and $W$ the maximum number of nodes on any level.

Each node is enqueued and dequeued at most once. The search can return early, but in the worst case it visits all $N$ nodes, so time complexity is $O(N)$.

The queue holds current-level nodes and may simultaneously accumulate children for the next level. Its size is bounded by a constant factor of the tree’s maximum width, giving $O(W)$ auxiliary space and $O(N)$ in the worst case for a broad tree.

No recursion is used, so a skewed tree does not risk recursion-depth failure.

## Alternatives and edge cases

- **BFS with an explicit level-size ascending loop:** Store `level_size = len(q)` and loop from zero upward. It is equivalent; the checked-in descending index makes “nodes remaining to the right” directly testable as `i`.
- **BFS with a null sentinel:** A sentinel can mark level boundaries, but it adds special queue entries. The frozen-size technique avoids them.
- **Two queues:** One for the current level and one for children makes boundaries explicit but uses more moving parts.
- **Depth-first search:** A left-to-right preorder can record `u`’s depth and take the next visited node at that depth. It uses $O(H)$ stack space but level adjacency is less direct.
- **Root is `u`:** The first level has one node, `i == 0`, so the result is `None`.
- **`u` is rightmost:** The zero loop index prevents returning a child from the next level.
- **`u` has no sibling but another cousin is rightward:** BFS order includes all nodes on the level, so the nearest cousin is returned.
- **Missing children:** Only existing children are enqueued; gaps do not create placeholder nodes and do not affect actual node order.
- **Single-node tree:** The root is popped as the last level node and returns null.
- **Very wide tree:** Queue space grows with width, matching the manifest’s $O(W)$ bound.
- **Skewed tree:** Width stays one, so queue space is constant even when height is $N$.
- **Reusing `root` variable:** It changes only the local reference; the queue already owns every node needed for traversal.
- **Guaranteed membership:** No explicit fallback is required, though Python’s implicit `None` would be returned if `u` were absent.
