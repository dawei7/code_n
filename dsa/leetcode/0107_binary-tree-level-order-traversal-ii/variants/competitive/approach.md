## General

The competitive implementation performs breadth-first search with two explicit frontier lists. It records levels from root downward because that is the natural discovery order, then returns a shallow reversal of the outer result list.

`current` contains one complete depth. `next_level` accumulates its children, and `vals` holds the current row's values.

**Initial and empty cases**

If `root is None`, there are no nonempty levels, so the method returns `[]`.

Otherwise `current = [root]` establishes the invariant that the active list contains exactly one depth in left-to-right order.

**Building one level**

Each outer iteration creates fresh `next_level` and `vals` lists. The method scans `current` from beginning to end, appending every value to `vals`.

For each node, it appends the left child before the right child. Because parents are also scanned left-to-right, `next_level` becomes the following level in natural horizontal order.

After the scan, assigning `current = next_level` advances one depth, while `result.append(vals)` stores the row just completed. The two lists are separate, so children cannot be processed in the parent's row.

There is no mutation of `current` during its scan. That makes the level boundary explicit: every node in the old list belongs to the same depth, and every node placed in `next_level` belongs to the next depth. Once the loop finishes, the old frontier is no longer needed. This is the list-based counterpart of taking a queue-size snapshot.

Both `next_level` and `vals` are newly allocated on every outer iteration. Consequently, each returned row owns a distinct list, and advancing the frontier cannot accidentally change a row that was already saved.

**Why final reversal is sufficient**

After BFS, `result[d]` is the left-to-right value list for depth $d$. If there are $H$ levels, desired output position zero is old position $H-1$, position one is old position $H-2$, and so on.

`result[::-1]` produces exactly that outer order. It copies row references in reverse but leaves each row object and its integer ordering unchanged.

For `[[3], [9, 20], [15, 7]]`, the returned list is `[[15, 7], [9, 20], [3]]`. Reversing the flattened values or each row would be incorrect.

**Why the constructed rows are exactly the required rows**

Initially, `current` correctly represents depth zero. Assuming it correctly represents depth $d$, scanning it records every depth-$d$ value left-to-right. Appending children left-before-right and parents in frontier order constructs exactly depth $d+1$.

Induction gives correct top-down rows. Every node is reached once from its unique parent, so no value is missing or duplicated. Reversing the row sequence changes depth order from increasing to decreasing while preserving within-level order, proving the final result.

Missing children do not create placeholders and do not disturb this reasoning. They contribute nothing to `next_level`, while the real children of earlier parents still precede those of later parents. Thus sparse and irregular trees receive the same left-to-right guarantee as complete trees.

**Why plain lists are efficient here**

The method never removes the first element from `current`. It iterates sequentially and then discards the entire frontier reference. Appending to `next_level` is amortized constant time.

A naive queue based on repeated `pop(0)` would shift remaining elements and could become quadratic. The two-list frontier avoids that issue without importing `deque`.

## Complexity detail

Every one of the $n$ nodes is visited once, giving $O(n)$ BFS time. Reversing $H$ outer references costs $O(H)\subseteq O(n)$, so total time is $O(n)$.

The two frontier lists coexist and use $O(w)$ references up to a constant factor, where $w$ is maximum width.

During an iteration, `current` may still hold the whole present level while `next_level` grows toward the whole following level. Their combined number of node references is at most a constant multiple of the maximum width, so two lists do not turn the frontier term into $O(w^2)$ or $O(nw)$.

As in the Optimal source, the final slice allocates a new $H$-reference outer list while the original `result` remains alive. Thus strict peak storage is $O(w+H)$ beyond the row contents, which can be $O(n)$. The manifest's $O(w)$ is the conventional frontier-only bound that treats output and its outer ordering as result storage. The source header's $O(n)$ statement is the conservative exact peak.

The row lists themselves hold $n$ values in total and are the required output, so they account for $O(n)$ output space. The extra $H$ references from slicing are shallow: the integers and row lists are not duplicated. They still count toward strict peak auxiliary memory because the original and reversed outer lists coexist until the method returns.

An in-place `result.reverse()` avoids duplicating the outer container.

## Alternatives and edge cases

- **Deque frontier with fixed level size:** Standard BFS equivalent with $O(w)$ frontier space.
- **In-place result reversal:** Preserves linear time and removes the shallow-copy peak.
- **Insert rows at index zero:** Avoids a final reversal but Python list front insertion costs $O(H)$ each and can be quadratic on a skewed tree.
- **Recursive depth grouping:** Uses $O(h)$ call stack and still needs bottom-up ordering.
- **Empty tree:** Returns no rows.
- **One level:** Outer reversal is a no-op in content.
- **Wide tree:** Frontier storage can be linear.
- **Skewed tree:** Frontier is constant, but $H=n$ makes copied outer-list storage linear.
- **Row order:** Children remain left-before-right even though levels are returned bottom-up.
- **Fresh `vals`:** Prevents different output rows from sharing one mutable list.
