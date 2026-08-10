## General

**Sort limits so uniqueness becomes a simple descending cap.** Each tower needs a positive integer height no larger than its own maximum, and all chosen heights must differ. The source sorts `maximumHeight` in ascending order, then iterates over the reversed slice `maximumHeight[::-1]`. Thus it processes towers from the largest allowed maximum to the smallest.

Once heights are assigned in this order, it is sufficient to make every new height strictly smaller than the previous assigned height. A strictly decreasing sequence is automatically unique. Variable `mx` stores that previous height. For the first tower, `mx` is positive infinity, so its own limit is binding. For every later limit `x`, the assignment becomes

`x = min(x, mx - 1)`.

The chosen height is therefore no greater than its tower's limit and no greater than one below the preceding assignment. It is the largest integer satisfying both restrictions.

For sorted descending limits $4,3,3,2$, the assignments are $4,3,2,1$, totaling $10$. When a limit leaves a gap, the greedy method preserves it: descending limits $15,10$ receive $15$ and $10$, because the second limit is already below $14$.

**Why towers may be reasoned about in sorted order.** Tower identities matter only through their maximum limits; the objective is the sum of assigned heights. Consider two towers with limits $A\ge B$ but assigned distinct heights $p<q$. Swapping those heights remains feasible: $q\le B\le A$, so the larger height fits the larger-limit tower, and $p<q\le B$, so the smaller height fits the smaller-limit tower. The sum is unchanged.

Repeatedly applying this exchange shows that any feasible assignment can be rearranged so larger limits receive heights no smaller than those received by smaller limits. Because heights are unique, those assigned heights are strictly descending when the limits are processed in descending order. The greedy algorithm therefore searches a canonical ordering without excluding an optimal total.

**Why choosing the largest feasible height is globally optimal.** At the first position, no feasible descending assignment can exceed that tower's limit, so greedy chooses the maximum possible first height. Assume greedy's assignments through the previous position are componentwise at least as large as the corresponding heights of any feasible canonical assignment. At the current position, every feasible height is bounded both by the current limit and by one less than its own previous height. Greedy uses the largest value allowed by the current limit and its greedily chosen predecessor.

Another useful view is an exchange argument: if an alleged optimum uses a smaller current height while the greedy height is available, raising it to the greedy value preserves the limit and uniqueness with the already larger preceding height. It also leaves at least as much, not less, room in the sense relevant to total maximum because later heights only need to be smaller; a larger current cap cannot force later values upward or invalidate values already below the smaller assignment. Therefore declining the greedy height cannot improve any later choice and only reduces the sum.

**Detect impossibility exactly when the greedy value reaches zero.** If `min(limit, mx - 1) <= 0`, no positive integer remains below the previous chosen height while respecting the current limit. Because greedy has kept every preceding height as large as possible, could choosing those earlier heights smaller help? It cannot create more distinct positive heights under the current and later small caps. More formally, after processing $r$ towers in descending order, a feasible canonical assignment needs $r$ distinct positive values descending through the current cap. Greedy constructs the componentwise largest such sequence. If even its current upper bound is nonpositive, every other feasible sequence's current value is no larger, so none can be positive. Returning `-1` is therefore exact.

**Account for source behavior.** `maximumHeight.sort()` mutates the caller's array into ascending order. The reverse iteration uses `maximumHeight[::-1]`, which creates a separate reversed list; it does not undo the mutation. The result is only the maximum sum, so the source never records which original tower received which chosen height. That is sufficient because assignment reconstruction is not requested.

The source assumes `inf` is available from the surrounding imports. After the first `min` call, `x` and then `mx` are ordinary integers.

## Complexity detail

Let $n$ be the number of towers. Sorting dominates at $O(n\log n)$ time. Creating the reversed slice and scanning it each take $O(n)$ time, so total time remains $O(n\log n)$.

The reversed slice explicitly allocates $O(n)$ references. Python's in-place sorting may also use temporary memory, bounded by $O(n)$ in the worst case. The algorithm's scalar state is constant, but the exact source's total auxiliary space is $O(n)$, matching the manifest. Iterating with `reversed(maximumHeight)` would avoid the slice allocation, though sorting can still require implementation-dependent workspace.

## Alternatives and edge cases

- **Set of used heights with downward search:** For each tower, repeatedly decrement until an unused height appears. Without a disjoint-set optimization, long runs of collisions can make this quadratic.
- **Disjoint-set predecessor structure:** It can find the largest unused height under each limit, but sorting plus the descending cap is simpler and already optimal for this objective.
- **Process limits ascending:** One can reason from small towers first, but choosing their heights greedily upward is easier to get wrong because a small early choice can consume a height useful to a tighter later tower. Descending processing gives one direct upper bound.
- **No sorting:** Input order has no useful relation to limits. Enforcing descent in arbitrary order can reject feasible assignments or lose total sum.
- **All limits are distinct and widely separated:** Every tower may take its full limit if those limits are already unique; `min(limit, mx - 1)` preserves any sufficient gap.
- **Repeated limits:** The first can take the limit, and subsequent towers step downward one by one until another smaller limit becomes binding.
- **Limit equal to one:** That tower must receive height one. If another still-unassigned tower also requires a positive height below it in descending order, the instance is impossible.
- **Single tower:** It receives its maximum height, which is positive by constraint.
- **Example `[2,2,1]`:** Descending processing chooses $2$, then $1$, then reaches zero for the final limit, proving no three distinct positive heights fit.
- **Large limits and total:** The sum can exceed 32-bit range when $n=10^5$ and limits approach $10^9$. Python integers are safe; fixed-width implementations need 64-bit arithmetic.
- **Input mutation:** The source leaves `maximumHeight` sorted ascending. Copy before sorting if caller-visible preservation is required.
- **Reverse-slice memory:** `[::-1]` costs linear extra space. `reversed(...)` would stream the same order without that particular allocation.
- **Recovering assignments by original index:** Store each limit with its original index before sorting and write greedy heights back to an output array. The current problem asks only for the sum, so that bookkeeping is omitted.
