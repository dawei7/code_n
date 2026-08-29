## General

Each output entry summarizes one tree depth. Breadth-first search naturally groups nodes by depth, so the solution processes one complete queue level at a time and takes its maximum.

If `root is None`, the tree has no rows. The method returns the initially empty `ans` immediately. This guard also prevents a null object from entering the queue.

For a nonempty tree, `q` starts with the root. At the beginning of each outer `while` iteration, the queue contains exactly the nodes in the current row, ordered from left to right.

That queue statement is true at depth zero because the queue contains only the root. Suppose it is true at some depth. The loop removes every parent at that depth and appends each existing child. Every node at the next depth has exactly one parent in a tree, so every such child is appended exactly once, and no node from another depth is appended. The queue therefore contains exactly the following row when the iteration ends. This induction is what makes the level-by-level interpretation reliable rather than merely visual intuition about BFS.

**Initialize a maximum that works for every legal value.** `x = -inf` begins below every integer node value. This matters because node values may all be negative. Initializing to zero would incorrectly report zero for a row such as `[-5, -2]` even though zero is not present.

**Snapshot one row's size.** `range(len(q))` captures how many nodes belong to the current row. The inner loop pops exactly that many nodes. Children appended during the loop belong to the next row and do not increase the fixed range.

For every popped `node`, `x = max(x, node.val)` keeps the largest value seen in the current row. The left and right children, when present, are appended for the next outer iteration.

After the first node, `x` equals that node's value because every finite integer is larger than negative infinity. After each later node, taking the maximum preserves the greatest value among all nodes processed so far. By the time the fixed number of pops is complete, the processed prefix is the entire row, so `x` is the maximum of that whole row.

After all current-row nodes have been processed, `x` is appended to `ans`. The queue then contains exactly the next row, establishing the invariant again.

For tree `[1, 3, 2, 5, 3, null, 9]`:

- the first queue level contains `[1]` and contributes one;
- the second contains `[3, 2]` and contributes three;
- the third contains `[5, 3, 9]` and contributes nine.

The answer is `[1, 3, 9]`.

Observe that the children of the root are already being stored while the first row's maximum is finalized, but they are never compared with the root. On the second iteration, the grandchildren are similarly stored without entering the second row's comparison. The snapshot is therefore not a minor implementation detail: it is the mechanism that keeps each output entry attached to one depth.

**Why every row receives exactly one answer.** Each node is enqueued by its parent and dequeued once. The fixed inner-loop count prevents next-row children from being mixed into the current maximum. One `ans.append(x)` occurs after each complete level and nowhere else. Thus answer index `d` corresponds exactly to tree depth `d`.

Correctness follows from the queue invariant. At one outer iteration, the inner loop examines every and only node in that row. Repeated `max` therefore produces that row's largest value. Children construct the complete next row. Induction covers every depth until the queue empties, yielding the required maximum sequence.

The left-to-right ordering is not required for computing a maximum, but standard child insertion preserves a valid level-order traversal. The crucial property is grouping by depth, not horizontal ordering.

Only one pass over the tree is necessary. A method that first computes the height and then rescans the tree separately for every depth would repeatedly visit upper nodes and could become quadratic on a skewed tree. Here, the queue supplies the row membership at the moment each node is visited, so the maximum and the traversal are completed together.

## Complexity detail

Let $n$ be the number of nodes and $w$ the maximum tree width. Every node is enqueued, dequeued, and compared once, so time is $O(n)$.

The queue can hold $O(w)$ nodes and at worst $O(n)$. The output has one value per tree height level, at most $O(n)$. The manifest gives the worst-case $O(n)$ space bound.

If output storage is excluded from auxiliary-space accounting, the working memory is $O(w)$. A complete tree can have a final level containing roughly half of all nodes, so $w$ can be proportional to $n$; the worst-case auxiliary bound remains $O(n)$. On a completely skewed tree, however, $w=1$ and the queue itself stays constant-sized.

## Alternatives and edge cases

- **Recursive DFS with depth:** When first visiting a depth, append its value; on later visits, update that depth's maximum. It uses $O(h)$ stack space plus output.
- **Iterative DFS:** Store `(node, depth)` pairs and update an answer array by depth. It avoids recursion but does not group rows as directly as BFS.
- **Empty tree:** The early return produces an empty list.
- **Single node:** Its row maximum is its own value.
- **All negative values:** `-inf` initialization ensures the least negative actual value wins rather than an artificial zero.
- **Wide final row:** The queue may hold many nodes, which explains the $O(n)$ worst-case space.
- **Snapshot level size:** Iterating until the live queue is empty would consume descendants too and collapse all rows into one maximum.
- **Duplicate values:** They do not affect the maximum operation; only the largest numeric value matters.
