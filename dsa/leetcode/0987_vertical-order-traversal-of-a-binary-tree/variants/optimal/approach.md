## General

**Translate the required order into sortable coordinates**

Every node has three pieces of information that determine its position in the answer:

1. its column, because columns must appear from left to right;
2. its row, because nodes within one column must appear from top to bottom;
3. its value, because nodes sharing both a row and a column must be ordered by value.

This is exactly lexicographic ordering by `(column, row, value)`. The algorithm traverses the tree once to attach these coordinates to every node, sorts all resulting tuples, and then groups adjacent tuples having the same column.

The traversal order itself is not used as a tie-breaker. That is important: a preorder depth-first visit may encounter one same-position node before another, but the contract requires their numeric values to decide the order.

**Assign coordinates during depth-first traversal**

The helper `dfs(root, i, j)` receives a node at row `i` and column `j`. The root begins at `(0, 0)`.

For a non-null node, the code stores

`nodes.append((j, i, root.val))`.

Although the helper parameters are row then column, the tuple deliberately stores column first. Python sorts tuples lexicographically from left to right, so placing `j` first gives column the highest priority, `i` second gives row the next priority, and `root.val` last resolves exact coordinate ties.

The recursive coordinate updates match the problem definition:

- the left child uses row `i + 1` and column `j - 1`;
- the right child uses row `i + 1` and column `j + 1`.

A null child contributes no tuple and returns immediately.

**Why every coordinate is correct**

The root is assigned the required origin. Assume a parent's recorded coordinate is correct. The left and right recursive calls apply exactly the specified row and column offsets, so both child coordinates are correct. By induction down every root-to-node path, the tuple recorded for every reachable node has its true position.

Each tree node is reached once from its unique parent, so no node is omitted or recorded twice.

**One global sort enforces all three priorities**

After traversal, `nodes.sort()` sorts tuples in ascending order.

Consider two nodes:

- If their columns differ, the smaller column tuple comes first regardless of row or value. This gives leftmost-to-rightmost column order.
- If their columns match but rows differ, the smaller row comes first. Since the root has row zero and rows increase downward, this is top-to-bottom order.
- If both column and row match, Python compares the third component and places the smaller node value first.

Thus the sorted flat list is already in the exact order in which values must appear across and within output columns. The original DFS visit order becomes irrelevant.

For example, in the complete tree `[1, 2, 3, 4, 5, 6, 7]`, nodes five and six both receive coordinate `(row = 2, column = 0)`. Their stored tuples are `(0, 2, 5)` and `(0, 2, 6)`, so value five precedes value six even if a different traversal encountered six first.

**Group the sorted tuples by column**

The final loop reads tuples as `for j, _, val in nodes`. The underscore receives the row because the sort has already used it; grouping now needs only the column and value.

Variable `prev` stores the column of the current output group. Whenever `j != prev`, the loop appends a new empty inner list and updates `prev`. Then `ans[-1].append(val)` places the value in that current column.

Sorting guarantees that all tuples for one column are contiguous. Once the loop moves to a larger column, the old column can never appear again, so a single comparison with `prev` is sufficient—no dictionary lookup is required.

**Why `-2000` is a safe initial sentinel**

Before the first tuple, no output group exists. The sentinel `prev = -2000` ensures the first real column differs and causes the first inner list to be created.

With at most one thousand nodes, the most negative possible real column occurs in an all-left chain and is no less than `-999`. Therefore, `-2000` cannot equal a legal column under the constraints.

Even if the method were called with a null root despite the stated nonempty-tree constraint, `nodes` would remain empty, the grouping loop would not access `ans[-1]`, and the method would return an empty list.

**Trace the first example by tuples**

For `[3, 9, 20, null, null, 15, 7]`, DFS records:

- root three as `(0, 0, 3)`;
- node nine as `(-1, 1, 9)`;
- node twenty as `(1, 1, 20)`;
- node fifteen as `(0, 2, 15)`;
- node seven as `(2, 2, 7)`.

After sorting, the order is

`(-1, 1, 9), (0, 0, 3), (0, 2, 15), (1, 1, 20), (2, 2, 7)`.

Grouping by the first coordinate produces `[[9], [3, 15], [20], [7]]`. Notice that node fifteen appears in column zero after the shallower root, exactly as required.

**Why the grouped result is complete and correctly ordered**

The DFS coordinate argument proves that `nodes` contains one correct tuple for every node. Tuple sorting places any two tuples in the required relative order by column, then row, then value. Therefore, reading the sorted sequence from left to right gives the precise flattened vertical traversal.

The grouping pass changes only the container boundaries: it starts a new list exactly when the column changes and preserves the already-correct order of values. It neither drops nor duplicates a tuple. Consequently, `ans` contains every column once, in ascending column order, with all of its nodes in the required internal order.

**Why BFS is not necessary here**

Breadth-first search naturally visits smaller rows first, but it still cannot resolve same-row, same-column nodes purely by arrival order because the required tie-breaker is value. Since sorting is needed anyway, DFS is simpler and equally correct: it gathers coordinates without maintaining a queue, and the global sort normalizes the visit order afterward.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height.

DFS visits every node once and creates one tuple per node, taking `O(N)` time. Sorting `N` tuples takes `O(N \log N)` time, and the grouping loop takes another `O(N)`. Sorting dominates, so total time is `O(N \log N)`.

The `nodes` list stores `N` tuples. The DFS call stack uses `O(H)` frames, which is `O(N)` in a completely skewed tree. The returned answer stores all `N` values. Total space including the output is `O(N)`, and auxiliary space apart from the output is also `O(N)` because of the coordinate list and recursion.

Tuple comparison examines only three integer components, so each comparison is constant time.

## Alternatives and edge cases

- **Breadth-first traversal plus global sorting:** A queue can gather the same `(column, row, value)` tuples. It has the same asymptotic bounds; sorting still supplies the value tie-break.
- **Dictionary partitioned by column:** Store `(row, value)` pairs per column, track minimum and maximum columns, and sort each group separately. It mirrors the output shape and can reduce practical sorting work, but uses more bookkeeping.
- **Nested maps and heaps:** Group by column and row and keep values in heaps. This enforces priorities incrementally but is considerably more complex than one tuple sort.
- **Relying only on BFS order:** BFS guarantees row order but not ascending value when two nodes share the same position, so it can return the wrong tie order.
- **Inorder traversal:** Its left-node-right visit sequence does not by itself implement column, row, and value ordering. Explicit coordinates and sorting are still required.
- **Nodes at the same column but different rows:** The row component puts the shallower node first regardless of value.
- **Nodes at the same row and column:** The value component is the final tuple tie-breaker; duplicate equal values may appear in either order because they are indistinguishable in the output.
- **Negative columns:** Left moves naturally produce negative integers, and ordinary ascending sorting places them before column zero.
- **Completely skewed tree:** Each node occupies a distinct column, but recursive depth becomes `N`; this is the worst case for call-stack space.
- **Single-node tree:** The tuple list contains `(0, 0, value)`, the sentinel creates one group, and the result is `[[value]]`.
- **Null child references:** The helper returns before recording anything, so missing children do not affect coordinates or grouping.
- **Sentinel safety:** `-2000` lies outside the legal column range for at most one thousand nodes. A sentinel-free grouping method could instead test whether `ans` is empty.
