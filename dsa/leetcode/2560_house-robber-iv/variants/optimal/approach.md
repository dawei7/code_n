## General

**Search for the answer instead of choosing a subset directly**

The capability of a chosen set is its largest house value. Rather than enumerate non-adjacent subsets, suppose a candidate capability $x$ is fixed. Under that limit, a house is eligible exactly when `nums[i] <= x`. The question becomes:

“Can at least $k$ non-adjacent eligible houses be selected?”

This is a yes-or-no feasibility question. If capability $x$ works, every larger capability also works because it makes the same houses and possibly more houses eligible. If $x$ fails, every smaller capability fails because it cannot add any eligible house. Feasibility is therefore monotone:

`False, False, ..., False, True, True, ..., True`.

That monotonicity permits binary search for the first true capability.

**Greedily count eligible non-adjacent houses**

The helper `f(x)` scans the street from left to right. It stores `j`, the index of the most recently selected house, and `cnt`, the number selected.

A house at index $i$ is skipped in either of two cases:

- `v > x`, so robbing it would exceed the candidate capability;
- `i == j + 1`, so it is adjacent to the last selected house.

Otherwise the helper selects it, increments `cnt`, and assigns `j = i`. Starting `j` at $-2$ makes index $0$ non-adjacent to the imaginary previous selection, since $0\ne-1$.

This strategy always takes the earliest eligible house that does not conflict with the previous choice. It may feel risky to commit immediately, but for maximizing the number of selections it is optimal.

**Why choosing the earliest eligible house is safe**

Consider the first eligible house that greedy can take, at index $i$. Any valid selection from the remaining street either takes $i$ or first takes some later eligible index $t>i$. If it takes $t$, replace $t$ with $i$. The replacement remains eligible under the same capability. It cannot conflict with a selected house on the left because $i$ is the first available choice, and it leaves at least as much room on the right because $i<t$.

Thus an optimal maximum-count selection exists that agrees with greedy's first choice. After taking $i$, both greedy and that optimal selection must ignore $i+1$, leaving the same kind of problem starting at $i+2$. Applying the argument repeatedly shows that greedy selects the maximum possible number of eligible non-adjacent houses.

Therefore `f(x)` returns true exactly when capability $x$ permits at least $k$ houses, not merely when this particular heuristic happens to find them.

As a local pattern, suppose eligibility is `[True, True, False, True, True]`. Greedy takes indices $0$ and $3$. Choosing index $1$ instead of $0$ cannot produce more options, because it blocks index $2$ just as $0$ blocks index $1$, while starting later never opens extra space to the right.

**How the exact binary search is expressed**

The solution uses

`bisect_left(range(max(nums) + 1), True, key=f)`.

The virtual sequence `range(max(nums) + 1)` represents every integer capability from $0$ through the largest house value. A `range` is compact; it does not allocate a list containing up to $10^9$ integers.

With `key=f`, `bisect_left` compares the transformed values `f(0), f(1), ...` against `True`. Since false sorts before true and the predicate is monotone, it returns the index of the first true result. The range value at index $x$ is also $x$, so the returned insertion index is the minimum feasible capability itself.

Capability $0$ cannot select a positive-valued house, but including it makes a clean lower bound. Capability `max(nums)` makes every house eligible. The constraint $k\le(n+1)/2$ guarantees that selecting alternating indices can reach $k$, so at least one true value always exists in the searched range.

**Why the returned capability is optimal**

Let $x^\star$ be the value returned by the binary search. The helper says $x^\star$ is feasible, so greedy explicitly demonstrates that at least $k$ non-adjacent houses with values at most $x^\star$ can be robbed. Their maximum value is at most $x^\star$.

Every smaller value is infeasible by the first-true property. Since greedy computes the maximum possible count under a threshold, no selection of $k$ houses can have capability below $x^\star$. The value is both achievable and a lower bound on every valid solution, so it is the minimum capability.

For `nums = [2,3,5,9]` and $k=2$, threshold $4$ makes indices $0$ and $1$ eligible, but they are adjacent, so only one can be taken. Threshold $5$ also makes index $2$ eligible; greedy takes indices $0$ and $2$, reaching two. The first feasible threshold is therefore $5$.

## Complexity detail

Let $n$ be the number of houses and let $V=\max(\texttt{nums})$. One feasibility call scans all $n$ houses in $O(n)$ time and uses $O(1)$ space. Binary search over $V+1$ integer thresholds performs $O(\log V)$ calls. Computing `max(nums)` costs another $O(n)$ pass, so total time is $O(n\log V)$.

The `range` object, counters, and binary-search state use $O(1)$ auxiliary space. No subset or dynamic-programming table is stored. The input array is read but not modified.

## Alternatives and edge cases

- **Dynamic programming by count:** Tracking the best capability for every index and number of robbed houses can cost $O(nk)$ time or state, much more than value-space binary search.
- **Enumerate subsets:** The number of non-adjacent subsets is exponential, so direct enumeration is infeasible.
- **Binary-search only distinct values:** Sorting unique house values can reduce the conceptual search domain but costs $O(n)$ extra space and $O(n\log n)$ preprocessing; searching the integer range is already logarithmic in $10^9$.
- **Take the cheapest values globally:** Sorting by value alone ignores adjacency. Two very cheap houses may be neighbors and cannot both be selected.
- **One required house:** The answer is the minimum value in `nums` because adjacency is irrelevant when only one house is needed; the predicate search finds that value.
- **All equal values:** Every threshold below that value fails and that value succeeds, provided the promised $k$ is achievable.
- **Alternating eligible houses:** Greedy naturally takes indices $0,2,4,\ldots$ within a fully eligible run, which is the maximum possible count for that run.
- **Large value range:** `range` is lazy, so searching through capabilities up to $10^9$ does not consume proportional memory.
- **No early exit in `f`:** The helper continues scanning after reaching $k$. This adds no asymptotic cost and still returns the correct predicate.
