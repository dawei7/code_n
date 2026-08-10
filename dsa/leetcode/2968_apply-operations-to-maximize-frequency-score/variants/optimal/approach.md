## General

**Reframe the score as choosing values to equalize**

One operation increases or decreases an element by one, so making selected values all equal to a target $x$ costs the sum of their absolute distances from $x$. The frequency score is the greatest number of elements that can be made equal with total cost at most `k`.

The implementation sorts `nums`. In sorted order, an optimal selection of a fixed size can be represented by a contiguous window. If a selection contains two values with an unselected value between them, replacing a farther selected endpoint by that in-between value cannot increase the cost of equalizing the group. Repeating this exchange removes gaps. Thus it is enough to test sorted windows rather than arbitrary subsets.

For a chosen window `nums[i:j]`, the cheapest common target is a median of that window because absolute-deviation sums are minimized at medians. The code uses the upper median at index `p = (i + j) // 2` and sets `x = nums[p]`.

**Compute a window’s cost in constant time**

A prefix-sum array `s` is built with an initial zero, so `s[r] - s[l]` is the sum of `nums[l:r]`.

For values on the left of the median, every value is at most `x`. Their total increment cost is

`(p - i) * x - (s[p] - s[i])`.

For values from `p` through `j - 1`, every value is at least `x`. Their total decrement cost is

`(s[j] - s[p]) - (j - p) * x`.

The median itself contributes zero and can safely be included in the right formula. Adding the two expressions gives the exact minimum operations for that window in $O(1)$ time.

For example, a sorted window `[1, 4, 6, 9]` uses upper median six. The left cost is $(6-1)+(6-4)=7$, and the right cost is $(6-6)+(9-6)=3$, totaling ten. The prefix formulas compute the same result through counts and sums rather than visiting all four values.

**Binary-search the maximum feasible length**

Function `check(m)` tests whether any contiguous sorted window of length `m` has median cost at most `k`. It slides `i` from zero through `n - m`, sets `j = i + m`, computes the median and cost, and returns true immediately upon finding a feasible window.

Feasibility is monotone in the length: if a set of $m$ values can be made equal within budget, removing one or more selected values cannot increase the cost, so every smaller length is also feasible. This false-after-true shape allows binary search over lengths from one through $N$.

The outer loop keeps a half-open search interval `[left, right)` with `left` feasible and `right` beyond the candidate range. It chooses the upper midpoint `mid = (left + right + 1) // 2`. If `check(mid)` succeeds, `left` moves up to `mid`; otherwise `right` becomes `mid - 1`. When they meet, `left` is the largest feasible frequency score.

**Why contiguous median windows are sufficient**

Take any optimal chosen multiset of $m$ sorted positions. If it skips an input value lying between two selected values, swapping that intermediate value for one of the more distant selected values moves a point toward the chosen group’s median region and cannot increase the minimum absolute-deviation cost. Repeated exchanges transform the selection into $m$ consecutive sorted positions with no larger cost.

For any such window, a median minimizes the cost. The prefix calculation evaluates exactly that minimum. Therefore, `check(m)` returns true if and only if some size-$m$ selection is achievable. Binary search over this exact predicate returns the global maximum.

**Exact implementation behavior**

`nums.sort()` modifies the input list. The prefix array is a separate list of length $N+1$. The nested `check` function closes over sorted `nums`, `s`, `n`, and `k`; it does not modify them.

Both increment and decrement operations are represented symmetrically through absolute distance. A one-direction frequency method that only raises smaller values would not be sufficient for this problem because decreasing larger values is also allowed.

## Complexity detail

Sorting takes $O(N\log N)$ time. Building prefix sums takes $O(N)$. Binary search performs $O(\log N)$ feasibility checks, and each check examines at most $N$ windows with $O(1)$ work per window. This contributes $O(N\log N)$ time, so the total is $O(N\log N)$.

The prefix-sum list uses $O(N)$ auxiliary space. Python’s sort may also use $O(N)$ temporary memory, so the overall auxiliary bound is $O(N)$. The feasibility scan itself uses constant state.

Integer costs may be large because they multiply a value by a window length, but Python integers avoid fixed-width overflow.

## Alternatives and edge cases

- **Choose arbitrary subsets:** Enumerating combinations is exponential. Sorting plus the no-gap exchange argument reduces candidates to contiguous windows.
- **Recompute every window cost directly:** Summing absolute differences for each window makes one check $O(Nm)$; prefix sums reduce each cost to $O(1)$.
- **Only increase toward the maximum:** That solves a different one-direction operation model. Here values can also decrease, making a median the correct target.
- **Two-pointer optimization:** More specialized methods can sometimes derive a direct scan, but binary search with exact median costs is clear and remains $O(N\log N)$.
- **`k = 0`:** Only values already equal can form a score greater than one. Median cost zero detects their sorted runs.
- **One element:** Length one always costs zero, so the initialized search returns one.
- **Even-size windows:** Any target between the two middle values minimizes total absolute distance. Choosing the upper median gives the same minimum cost.
- **Duplicate values:** They naturally produce zero distance and can enlarge feasible windows without consuming budget.
- **Input mutation:** Sorting changes `nums`. A copied sort would preserve it at the cost of another $O(N)$ allocation.
- **Feasibility monotonicity:** Removing elements from a feasible group can only lower its equalization cost, which is the exact reason binary search is valid.
