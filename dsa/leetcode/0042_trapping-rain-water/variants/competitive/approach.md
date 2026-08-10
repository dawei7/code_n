## General

**The shorter boundary determines what can be finalized**

For any bar, trapped depth is the shorter of the tallest boundary to its left and the tallest boundary to its right, minus the bar's own height. A two-pointer method avoids storing those maxima for every index by deciding which side already has enough information.

Pointers `left` and `right` begin at the two ends. If `height[left] < height[right]`, the left endpoint is the lower one. The right endpoint itself proves that a boundary at least as high as the lower bar exists on the other side, so future bars beyond `right` cannot change the fact that the left side is currently limiting. The algorithm can finalize the left endpoint and move `left` inward. Otherwise, it symmetrically finalizes the right endpoint and moves `right` inward.

This “process the lower side” rule is the core insight. Processing the taller side would be premature because the opposite, shorter boundary might still be the water-level limit.

**What `lower` and `level` represent**

Each iteration stores the consumed endpoint height in `lower`. It advances that endpoint immediately, but the saved value still represents the bar being accounted for.

`level` is the highest lower-boundary level established while consuming endpoints. It is updated with `level = max(level, lower)`. If the consumed bar raises the best established boundary, it becomes the new level and traps no water itself. If it lies below an already established level, `level - lower` units sit above it.

The algorithm adds exactly that nonnegative difference to `result`. Because each iteration consumes one endpoint, every index except the final meeting position is accounted for once. The meeting position cannot trap additional water outside the level already represented; treating it as a boundary with zero uncounted depth is consistent with stopping at `left == right`.

**Why one shared level is sufficient**

Standard presentations often keep separate `left_max` and `right_max`. This source compresses the same logic. At every step it consumes the smaller current endpoint. The unconsumed opposite endpoint is at least as high as `lower`, so the current bar has a closing wall across the remaining interval. A previously larger `level` arose only when an endpoint of that height was itself the smaller side; at that moment, an opposing boundary at least that high existed and remains part of the enclosing structure while lower interior bars are consumed.

Thus `level` is a guaranteed supported water line, not simply the maximum height seen from one arbitrary direction. The minimum-end selection is what makes that shared value valid. Updating it before adding ensures a new high boundary contributes zero rather than a negative amount.

For heights `[4, 2, 0, 3, 2, 5]`, the left endpoint is repeatedly lower than the fixed right height 5. The consumed sequence is 4, 2, 0, 3, and 2. `level` becomes 4 at the first bar, and the subsequent additions are 2, 4, 1, and 2, totaling 9. The remaining height 5 closes the basin.

**Handling equal endpoints**

When the endpoint heights are equal, the `else` branch consumes the right one. Either side would be safe: each endpoint supplies a boundary as high as the other. Choosing the right consistently avoids ambiguity and still removes one position, guaranteeing progress.

The expression `result += level - lower` cannot subtract water. `level` is updated to at least `lower` immediately beforehand. This is a compact way to combine “raise the boundary” and “fill below the boundary” without a separate conditional.

**Why the total is correct**

At an iteration, the smaller endpoint has an opposite wall at least as tall. Its supported water height is therefore determined by the best limiting level established on its own processed side, represented by `level`; no unseen exterior height can lower that already guaranteed boundary. If the bar reaches or exceeds the old level, it raises the level and contributes zero. If it is shorter, the exact trapped depth is the difference.

After accounting for that endpoint, moving its pointer discards no needed information because its height has already been incorporated into `level`. Repeating the argument finalizes one distinct column per iteration. When the pointers meet, all possible interior columns have been counted, so `result` is the total volume.

**Which class in the source is selected**

The file also contains `Solution2`, `Solution3`, and `Solution4`, illustrating peak-splitting, a suffix-maximum array, and a stack technique. The canonical judge entry is the class named `Solution`, whose `trap` method is the two-pointer algorithm explained here. The additional class names do not override `Solution` and should not be mistaken for steps executed by it.

## Complexity detail

Every loop iteration increments `left` or decrements `right`. Their distance begins at $n - 1$ and strictly decreases, so there are at most $n - 1$ iterations. Each performs constant-time comparisons and arithmetic, giving $O(n)$ time.

The selected `Solution` stores only `result`, two pointers, `level`, and `lower`. It allocates no arrays, stacks, or recursive frames proportional to input size, so auxiliary space is $O(1)$. The input list is read but not modified. These bounds exactly match the variant manifest.

## Alternatives and edge cases

- **Prefix and suffix maximum arrays:** Precompute the best boundary on each side of every index, then sum `min(left[i], right[i]) - height[i]`. It is the most direct implementation of the formula, with $O(n)$ time and $O(n)$ extra space.
- **Separate left and right maxima:** A more common two-pointer form stores `left_max` and `right_max` independently. It has the same $O(n)$ time and $O(1)$ space and may make the proof easier to localize to each side.
- **Split around the global tallest bar:** Find a maximum, scan toward it from the left, and then from the right. Each side is guaranteed a closing wall at the peak and uses constant extra storage.
- **Monotonic stack:** Keep decreasing-height indices and compute water when a right boundary closes a basin. It is linear-time but uses $O(n)$ space and counts horizontal layers rather than vertical columns.
- **No basin:** Monotone, flat, or single-bar inputs return zero because `level` never exceeds a consumed lower bar in a way that creates positive depth.
- **Equal endpoints:** The source consumes the right endpoint. This tie choice is safe because the left endpoint is an equally high closing wall.
- **Zero-height bars:** They contribute the full established `level` when enclosed; non-negative heights make all arithmetic straightforward.
- **Repeated maxima:** The method does not need to locate a unique tallest bar. Equal peaks are handled through ordinary endpoint comparisons.
- **One element:** `left == right` initially, so the loop does not run and zero is returned.
- **Empty input outside the stated constraints:** This source would initialize `right` to `-1` and still return zero without indexing inside the loop. That behavior is harmless but is not needed by the contract.
- **Large heights:** Python integers do not overflow when accumulating the volume; in fixed-width languages, the maximum possible sum should be checked against the chosen integer type.
