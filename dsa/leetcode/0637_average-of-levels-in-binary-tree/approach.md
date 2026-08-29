## General

**What the result is asking us to group**

The tree must be divided by depth. The root is the only node at depth zero, its children are at depth one, their children are at depth two, and so on. For each such level, we need two facts: the sum of the node values on that level and the number of nodes on that level. Their quotient is the requested average.

The important challenge is not computing an average by itself. It is making sure that values from two neighboring levels are never mixed. A breadth-first traversal is a natural fit because it visits the tree one horizontal layer at a time. A queue stores nodes whose values still need to be processed. At the beginning of every outer-loop iteration, that queue contains exactly the nodes of one complete level and no nodes from a later level.

**Why the queue length must be captured before processing the level**

The solution begins with the root in the queue. At the start of a level, it records `n = len(q)`. This snapshot is essential. While those `n` nodes are removed, their children are appended to the same queue. Therefore, the live queue length changes during the loop and cannot be used as the stopping condition for the current level.

Processing exactly the saved number `n` creates a clean boundary:

- the first `n` nodes are all nodes on the current level;
- every child appended during those `n` removals belongs to the next level;
- after exactly `n` removals, the old level is gone and the queue contains precisely the next level.

This explains why a single queue is enough. We do not need separate “current level” and “next level” queues because the saved size marks where one group ends and the next begins.

**How one level is evaluated**

For each outer iteration, the solution initializes the level sum `s` to zero and stores the level size in `n`. It then repeats the following operation exactly `n` times:

1. Remove the node at the front of the queue.
2. Add that node's value to `s`.
3. If the node has a left child, append that child.
4. If the node has a right child, append that child.

After those repetitions, `s` is the sum of every value at the level and `n` is the number of values that contributed to it. Thus `s / n` is exactly the level average. Appending that quotient at the end of each outer iteration also preserves the required top-to-bottom order.

Suppose the current queue is `[4, 9, -1]` when an iteration begins. The saved level size is three. Even if those nodes append five children, only the original three nodes are consumed in this iteration. The level sum becomes `4 + 9 - 1 = 12`, so the appended average is `12 / 3 = 4.0`. The five newly queued children wait for the next iteration.

**Why the traversal is correct**

The central fact can be maintained from one iteration to the next: immediately before an outer iteration, the queue contains all and only the nodes at the next unprocessed depth, in left-to-right order.

It is true initially because the queue contains only the root, which is the complete depth-zero level. Assume it is true for some level. The algorithm removes exactly every node from that level. A tree child's depth is exactly one greater than its parent's depth, so every appended child belongs to the following level. Every node on that following level has exactly one parent in the current level, so it is appended once; no unrelated node is appended. Consequently, when the iteration ends, the queue contains all and only the next level. This proves that the fact remains true.

Because the sum is formed from precisely the nodes described by that fact, the quotient appended during each iteration is the correct average for that level. The process ends after the deepest level because no more children are appended and the queue becomes empty. Therefore, every level contributes exactly one correct result and no nonexistent level contributes anything.

**Why ordinary division is appropriate**

The output type is a list of floating-point values. Python's `/` operator performs real-number division even when both operands are integers, so a level sum of five over two nodes becomes `2.5` rather than being truncated to two. A level containing one node naturally produces that node's value as a floating-point average.

The sum should be accumulated before division rather than repeatedly updating a running floating-point average. Integer addition is exact in Python, and doing only one division per level avoids unnecessary rounding operations. Python integers also grow beyond fixed 32-bit limits, so a wide level containing many large node values cannot overflow the accumulator even though individual values fit within the stated 32-bit range.

**What the variable named `root` means inside the loop**

The parameter initially refers to the actual tree root. Inside the loop, the same local name is reused for the node just removed from the queue. That reuse does not change the tree and does not lose information needed later: the original root has already been placed into the queue, and future progress depends only on queued nodes. A name such as `node` might be easier for a beginner to read, but the behavior of the given optimal solution is correct.

## Complexity detail

Let `N` be the total number of nodes and `W` be the maximum number of nodes present on any one level.

Every node enters the queue exactly once, when its parent is processed, except the root, which is inserted during initialization. Every node is also removed exactly once. The work done at removal is constant: one value addition, at most two child checks, and at most two queue appends. Across the entire tree, the running time is therefore `O(N)`.

The result contains one number per tree level. If `H` denotes the number of levels, the returned list itself occupies `O(H)` output space. The traversal queue can contain nodes from the current level and, while that level is being processed, some nodes from the next level. Its peak size is bounded by a constant multiple of the tree's maximum width, so the customary auxiliary-space bound is `O(W)`. This is the relevant working-space bound recorded for the approach. If returned output is included, total additional storage is `O(W + H)`.

The integer accumulator may represent a sum wider than a machine integer. In Python, very large integer arithmetic is not literally constant-time in the number of machine words, but under the standard algorithm-analysis model for the problem's bounded node values, each addition is treated as constant work. That convention gives the expected `O(N)` result.

## Alternatives and edge cases

- **Depth-first traversal with depth-indexed totals:** A recursive or iterative depth-first search can maintain one sum and count per depth, then divide afterward. It is also `O(N)` time, but it needs `O(H)` traversal-stack space and separate arrays of totals and counts. The breadth-first solution expresses the level grouping directly and can produce each average as soon as that level is finished.

- **Two explicit level lists:** Keeping one list for the current level and building another for the next level is correct, but it creates or replaces containers repeatedly. A deque with a saved level size provides the same boundary with straightforward constant-time removals from the front.

- **Removing from the front of a Python list:** Calling `pop(0)` on a normal list shifts all remaining elements and can make traversal unnecessarily quadratic on wide trees. `collections.deque` is the appropriate queue because `popleft()` and `append()` are constant-time operations.

- **Using the changing queue length as the loop bound:** Children are appended during processing, so repeatedly checking the current queue size can accidentally consume nodes from the next level. Capturing `len(q)` once before the inner loop is what keeps levels separate.

- **Initializing the best or sum with zero for all levels:** The sum may begin at zero because every node value is then added, including negative values. There is no “best average” comparison here, so an all-negative level is handled naturally and cannot be incorrectly replaced by zero.

- **Single-node tree:** The initial queue has one node, the saved count is one, no children may be appended, and the result is a one-element list containing that value divided by one.

- **Highly unbalanced tree:** Every level may contain only one node. The queue stays small, and the algorithm returns each node value as the average of its one-node level. The time remains linear in the number of nodes.

- **Very wide tree:** The queue must hold a whole level and possibly much of the next one, which is why the space bound depends on `W` rather than only on the height.

- **Missing children:** A missing left or right child is simply not appended. This preserves the actual tree structure; no placeholder nodes should enter the sum or count.

- **Empty root:** The stated contract guarantees at least one node, and the exact solution relies on that guarantee by initially queuing `root` without a null check. If an external caller were allowed to pass `None`, a guard returning an empty list would be required before creating the queue.
