## General

**Separate the changing array from the information queries need.** A position `i` is a peak exactly when all three conditions hold:

$$
0<i<n-1,\qquad \texttt{nums}[i-1]<\texttt{nums}[i],\qquad
\texttt{nums}[i]>\texttt{nums}[i+1].
$$

A type-1 query does not need the peak values themselves. It only needs to count how many positions in a range currently satisfy that predicate. Imagine an indicator array `peak` in which `peak[i]` is $1$ for a peak and $0$ otherwise. Then a range answer is simply a range sum over this indicator array.

Rebuilding all indicators for every query would cost $O(n)$ per query. The exact solution instead stores the indicators in a Fenwick tree, also called a Binary Indexed Tree. This data structure supports adding a delta at one position and asking for a prefix sum in $O(\log n)$ time. A range sum from $a$ through $b$ is the difference between two prefixes:

$$
\operatorname{sum}(a..b)=\operatorname{prefix}(b)-\operatorname{prefix}(a-1).
$$

**Understand the Fenwick tree's indexing.** The helper class stores an array `c` and uses the standard one-based update rules `x += x & -x` and `x -= x & -x`. The solution passes original array indices $1$ through $n-2$ directly to it. This works neatly because index $0$ and index $n-1$ can never be peaks and therefore do not need entries. The tree is created with logical size `n - 1`; every possible peak index is at most `n - 2`, safely inside that size.

`tree.update(i, delta)` changes the stored peak count at position `i`. `tree.query(i)` returns the number of stored peaks from position $1$ through `i`. The inner helper named `update` first rejects endpoints, then examines the current three-number neighborhood. It forwards the supplied delta only if `i` is currently a peak.

During initialization, the solution examines every original interior position and calls `update(i, 1)`. The Fenwick tree then represents exactly the current set of peaks.

**Translate a subarray query to its interior.** For a requested subarray `nums[left..right]`, its first element at `left` and last element at `right` cannot count as peaks even if either is a peak in the complete array. Only original positions from `left + 1` through `right - 1` are eligible. The code therefore sets

`l = q[1] + 1` and `r = q[2] - 1`.

If `l > r`, the subarray has no interior position, so the answer is zero. Otherwise, the Fenwick range-sum formula becomes

`tree.query(r) - tree.query(l - 1)`.

For any eligible index strictly inside the query boundaries, its two neighbors in the full array are also inside the queried subarray. Consequently, its global peak indicator is exactly its peak status within that subarray. This is why the same stored indicator array answers every interval.

**A point update can change only three peak statuses.** Suppose `nums[idx]` receives a new value. A peak predicate mentions only a center and its immediate neighbors. The changed value can appear in the predicates centered at:

- `idx - 1`, where it is the right neighbor;
- `idx`, where it is the center;
- `idx + 1`, where it is the left neighbor.

Every other predicate reads the same three values as before and therefore cannot change. This locality is the key improvement: one array assignment never requires rescanning the whole array.

The exact update procedure has three stages. First, while `nums` still holds the old value, it calls `update(i, -1)` for those three candidate centers. If a candidate is presently a peak, its stored $1$ is removed; otherwise nothing happens. Second, it performs `nums[idx] = val`. Third, it calls `update(i, 1)` for the same centers under the new array values, adding each newly valid peak.

Removing old facts before changing `nums` is essential. If the assignment happened first, the helper could no longer determine which indicators had been stored under the old neighborhood. Likewise, merely adding new peaks without subtracting old ones would leave stale counts or create values greater than one in the tree.

**Why the data structure stays truthful.** Immediately after initialization, each interior tree position equals its peak predicate. Assume that statement is true before a query. A count query does not mutate anything, so it remains true. For a point update, every potentially affected old indicator is removed, the value changes, and every potentially affected new indicator is added. Unaffected positions remain correct because their neighborhoods did not change. Thus the statement remains true after every query. Since a type-1 answer sums precisely the eligible interior indicators, every appended answer is the requested number of peaks.

Consider `nums = [3, 1, 4, 2, 5]`. Initially, index $2$ is a peak because $1<4>2$. Changing index $3$ from $2$ to $4$ can affect centers $2$, $3$, and $4$. The old indicator at $2$ is removed. In the new array `[3, 1, 4, 4, 5]`, index $2$ is no longer strictly greater than its right neighbor, and neither other candidate is a peak. A later full-range query correctly returns zero.

## Complexity detail

Let $n$ be the array length and $q$ the number of queries. A Fenwick update or prefix query follows parent links determined by the least significant set bit, so it performs $O(\log n)$ iterations.

Initialization checks $n-2$ possible peak centers. In the exact source, every actual peak triggers a Fenwick update and every non-peak only performs constant predicate work. Its worst-case time is $O(n\log n)$. Each type-1 query performs at most two prefix queries, hence $O(\log n)$. Each type-2 query checks three positions before and three after the assignment; at most six Fenwick updates occur, so it is also $O(\log n)$. Across all queries, the bound is $O((n+q)\log n)$.

The Fenwick array has $n$ integer slots up to constant differences, so it uses $O(n)$ auxiliary space. The answer list uses $O(a)$ space for $a$ type-1 queries; that is required output storage and can be $O(q)$. Apart from the tree and returned answers, the algorithm uses constant temporary space. The solution mutates the supplied `nums` list so that later queries observe all prior updates.

## Alternatives and edge cases

- **Segment tree:** Store peak indicators in a segment tree and use point updates plus range-sum queries. It has the same $O(\log n)$ operation bounds but uses more code and a larger constant factor than a Fenwick tree for this sum-only task.
- **Recount every requested subarray:** Scanning `left + 1` through `right - 1` is simple and needs no tree, but a long interval costs $O(n)$ and up to $10^5$ such queries can make the total quadratic.
- **Rebuild after each value change:** Recomputing all peaks after a type-2 query ignores the local three-center dependency and also costs $O(n)$ per update.
- **Ordered set of peak indices:** A balanced ordered set can update the same three positions, but counting how many stored indices lie in an interval requires order-statistics support. A basic Python set or sorted list does not provide both updates and rank queries efficiently.
- **Subarray endpoints:** Even when `nums[left]` is greater than its global neighbors, it is the first element of the queried subarray and must not count. Shifting to `left + 1` and `right - 1` enforces this rule.
- **Intervals of length one or two:** They have no interior position. The `l > r` check returns zero without issuing a misleading range query.
- **Global endpoints:** Candidate centers `0` and `n - 1` are rejected by the helper. This makes updates at either end safe: only the adjacent interior position can acquire or lose peak status.
- **Strict inequality and equal neighbors:** A plateau such as `[..., 4, 4, ...]` contains no peak at either equal value. The source uses `<` and `>`, not non-strict comparisons.
- **Assigning the same value:** The code still removes the old local indicators and adds them back. The result is unchanged and remains correct; no special case is required.
- **Sequential query semantics:** `nums[idx] = val` deliberately mutates the array. Every subsequent query operates on the accumulated state, not the original input.
- **Fenwick index zero:** Standard Fenwick updates cannot start at zero because `x & -x` would also be zero and the loop would not advance. The wrapper's endpoint rejection guarantees `tree.update` is never called with zero.
