## General

The competitive implementation uses two explicit BFS frontier lists. It always scans each level from left to right, builds the next frontier in the same natural order, and reverses only the completed values when the output depth requires right-to-left reading.

`current` is the active level. `next_level` is built for the following level, and `vals` collects the active nodes' values.

**Empty and initial states**

An empty root returns `[]`. For a real root, `result = []` and `current = [root]`. The invariant is that `current` contains exactly one depth in left-to-right order.

At the start of every outer iteration, fresh `next_level` and `vals` lists prevent one level's state from aliasing another.

**Building the natural frontier**

The `for node in current` loop processes parents from left to right. Each value is appended to `vals`. Each real left child is appended before its sibling right child.

This order means children of an earlier parent precede children of every later parent, while siblings retain left-before-right order. Therefore `next_level` is the following depth in natural horizontal order.

Children are added to a separate list, so they cannot be processed in the same row. After the loop, `current = next_level` advances exactly one depth.

**Choosing whether to reverse**

Before appending the row, the expression checks `len(result) % 2`.

`len(result)` equals the current zero-based depth because one row has been appended for every earlier level. At depth zero it is even, so `vals` is stored unchanged. At depth one it is odd, so `vals[::-1]` is stored. The parity alternates automatically as `result` grows.

This avoids maintaining a separate direction variable. The output list itself supplies the level number.

**Why reversal does not affect traversal**

`vals[::-1]` creates a reversed value list but leaves `current`, `next_level`, and tree nodes untouched. BFS discovery continues in natural order on every level.

If the algorithm instead reversed `current` or enqueued children in alternating orders, it would need different child rules on each depth to prevent cross-parent mistakes. Reversing only values isolates the zigzag requirement from traversal.

**Trace through the Reference example**

With `current = [3]`, `vals` becomes `[3]`, and `next_level` becomes `[9, 20]`. Since `result` is empty, depth is even and `[3]` is appended.

Processing `[9, 20]` creates natural `vals = [9, 20]` and children `[15, 7]`. One row already exists, so odd parity stores `[20, 9]`.

Processing `[15, 7]` creates the natural row and no children. Two rows already exist, so even parity stores `[15, 7]`. The next frontier is empty and traversal ends.

**Correctness argument**

The initial frontier contains exactly depth zero in natural order. Assuming `current` is correct for one depth, scanning it and appending left then right children constructs exactly the next depth in natural order.

The parity test stores the current values in left-to-right order for even depths and reversed order for odd depths. Since one result row is added per iteration, the parity corresponds exactly to depth. Induction proves every returned row's membership, ordering, and alternation.

Every node is reached from its unique parent, appears in one frontier, and contributes one value, so none is missed or duplicated.

## Complexity detail

Each of the $n$ nodes is visited once. Reversed slicing across odd levels copies at most $n$ values in total, so time is $O(n)$.

Let $w$ be maximum width. `current` and `next_level` coexist and together use $O(w)$ node references up to a constant factor. `vals` or its reversed copy is retained in `result`; excluding output, auxiliary space is $O(w)$, matching the manifest.

The source header states $O(n)$ space, which is a valid looser bound and also describes total memory when the returned $n$ values are included.

During a reverse-output iteration, `vals` and `vals[::-1]` coexist briefly. Both have the current level's width, at most $w$. Along with `current` and `next_level`, this remains a constant multiple of $w$, so it does not change the auxiliary frontier bound. Once the row is appended and the iteration ends, the original `vals` list is released.

The two-frontier method uses list append and sequential iteration only. It never removes index zero from a list, avoiding the element-shifting cost that would make a naive list-based queue inefficient.

## Alternatives and edge cases

- **Single deque frontier:** Save the current queue length for each level and use a direction flag.
- **Build row from both ends:** A deque can `append` or `appendleft`, avoiding the row reversal copy.
- **Recursive DFS by depth:** Store one deque per depth and alternate insertion ends; stack usage is $O(h)$.
- **Empty tree:** Returns no rows.
- **Single node:** `len(result)` is zero, so the only row stays forward.
- **Wide reverse level:** Slicing reverses in linear time; repeated front insertion into a list could be quadratic.
- **Sparse level:** Missing children are skipped without disturbing real-node order.
- **Fresh lists:** Reusing `vals` or `next_level` across iterations without reinitializing would corrupt stored rows or frontiers.
- **Parity source:** `len(result)` is valid only because exactly one row is appended per completed frontier.
- **Reversal ownership:** The reverse slice is a new list, so storing it cannot later be affected by the temporary natural-order `vals`.
- **Natural-order frontier:** Never reverse `next_level`; only the displayed values alternate.
