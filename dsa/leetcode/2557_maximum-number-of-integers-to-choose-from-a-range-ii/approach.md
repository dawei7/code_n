## General

**Why the smaller allowed values must be chosen first**

Every chosen integer contributes exactly one to the objective, while its numeric value is its cost against `maxSum`. If a selection contains an allowed value $b$ but omits a smaller allowed value $a$, replacing $b$ by $a$ keeps the count unchanged and cannot increase the sum. Repeating this exchange transforms any selection of a fixed size into the same-size prefix of the allowed integers.

Therefore, the optimal answer is the longest ascending prefix of allowed values whose sum fits the budget. The difficulty is that $n$ can be $10^9$, so scanning every integer from $1$ through $n$ is impossible. The solution skips entire consecutive ranges with arithmetic-series formulas.

**Turn banned values into allowed gaps**

The code appends sentinels `0` and `n + 1` to `banned`, removes duplicates with `set`, and sorts the result into `ban`. For every adjacent pair $(i,j)$ in this sorted list, all integers

$$
i+1,i+2,\ldots,j-1
$$

are allowed. Nothing strictly between two consecutive banned values can itself be banned.

The sentinels make the boundary gaps behave exactly like middle gaps. The values before the first real banned number lie after sentinel $0$, while values after the final real banned number lie before sentinel $n+1$. No separate first-gap or last-gap code is necessary.

The expression `j - i - 1` is the number of allowed integers in this gap. The algorithm visits gaps from left to right, which is also increasing numeric order, so it continues building the globally cheapest allowed prefix.

**Sum the first part of one gap**

Suppose the current left banned boundary is $i$, and the algorithm wants to take the first $c$ allowed values in the gap. Those values run from $i+1$ through $i+c$. Their arithmetic-series sum is

$$
S(c)=\frac{(i+1+i+c)c}{2}.
$$

This is the familiar formula “first plus last, times the number of terms, divided by two.” When $c=0$, the formula is zero. When $c$ equals `j - i - 1`, it is the cost of the whole gap.

Rather than adding values individually, the solution binary-searches for the largest $c$ such that `S(c) <= maxSum`. The search interval begins with `left = 0` and `right = j - i - 1`, so every possible prefix length is represented.

**Why binary search applies**

All values are positive. As $c$ increases, `S(c)` strictly increases, so feasibility has a monotone shape: zero items fit, then perhaps several positive prefix lengths fit, and after the first failure every larger length fails too.

The midpoint is computed as `(left + right + 1) >> 1`, which is the upper midpoint. If `S(mid)` fits, `left` becomes `mid`. Otherwise `right` becomes `mid - 1`. The upward rounding is important when only two candidates remain; it lets the search test the larger candidate instead of repeatedly choosing the old lower bound.

When the loop ends, `left` is the largest affordable number of values from this gap. The code adds it to `ans` and subtracts exactly `S(left)` from `maxSum`.

**Why processing later gaps remains correct**

If the entire current gap fits, the next unconsidered allowed integer lies in a later gap and is larger than everything already chosen. Continuing is exactly what the cheapest-prefix rule requires.

If only part of a gap fits, the remaining budget is smaller than the next integer in that same gap. Every value in a later gap is even larger, so none can be chosen. The exact implementation may still iterate through later gap pairs when the remaining budget is positive, because it breaks immediately only when `maxSum <= 0`. Those later binary searches simply return zero and do not change the answer. This is harmless, though an explicit early break after a partial gap could avoid the remaining iterations.

**Why the final count is optimal**

At every stage, `ans` counts the globally smallest allowed values taken so far, and the reduced `maxSum` is the exact unspent budget. The gap formula and binary search choose the longest affordable prefix of the next consecutive allowed block.

When no next allowed value fits, the selected values form the cheapest possible set of that size. Any set with one additional value must cost at least the prefix plus that next value, which exceeds the original budget. Therefore no larger count exists.

For example, with `banned = [1,4,6]`, $n=6$, and budget $4$, the sorted sentinels produce gaps containing `[2,3]` and `[5]`. In the first gap, taking one value costs $2$, while taking both costs $5$, so binary search chooses one. The remaining budget is $2$, too small for $3$ or any later allowed value. The answer is one.

The code does mutate the caller's `banned` list by appending the two sentinels. The sorted set `ban` is a separate list, but the original input retains those appended values after the function returns.

## Complexity detail

Let $m$ be the original length of `banned`. Creating a set and sorting at most $m+2$ distinct values costs $O(m\log m)$ time and $O(m)$ space. There are at most $m+1$ adjacent gaps. Each binary search examines $O(\log n)$ prefix lengths, so all gap searches cost $O(m\log n)$ time.

The total time is $O(m\log m+m\log n)$, which matches the manifest. The sorted unique list and temporary set use $O(m)$ auxiliary space. Arithmetic uses constant additional space; Python integers safely hold sums up to the stated $10^{15}$ budget and beyond the intermediate products required by the formula.

## Alternatives and edge cases

- **Scan every value:** A hash-set membership test while iterating from $1$ to $n$ is optimal for the smaller Range I constraints, but $n=10^9$ makes that approach infeasible here.
- **Solve a quadratic directly:** The inequality for `S(c)` can be rearranged and approximated with a square root. Binary search avoids floating-point rounding mistakes and is fast enough.
- **Prefix sums over all values:** Materializing an array of length $n$ defeats the purpose of gap compression and cannot fit the largest constraint.
- **Duplicate banned values:** `set(banned)` collapses duplicates, ensuring they do not create zero-width artificial gaps or extra work.
- **Banned endpoints:** Real banned values may include $1$ or $n$; the sentinels still produce correct empty boundary gaps.
- **Empty gap:** Consecutive banned values give `right = 0`. The binary-search loop does not run, and nothing is added or subtracted.
- **Exact budget use:** If a gap prefix costs exactly the remaining budget, the `<=` test accepts it and the subsequent zero-budget check stops.
- **Partial gap with budget left:** The leftover amount may be positive but smaller than the next allowed value. Later, larger gaps contribute zero, so correctness is unchanged.
- **Large arithmetic:** Fixed-width implementations should use 64-bit or wider arithmetic before multiplying the endpoints by the count.
- **Input mutation:** Appending sentinels changes `banned`. Copying it before extension would be necessary if the caller expects the original list to remain untouched.
