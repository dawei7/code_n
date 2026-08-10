## General

We must select a subsequence whose values sum exactly to `target` and maximize the number of selected elements. A subsequence preserves the original order, but because the objective and constraint depend only on which positive elements are chosen, this is a 0/1 knapsack problem:

- every array element may be taken at most once;
- its “weight” is its numeric value;
- its “value” is one unit of subsequence length;
- the required total weight is exactly `target`.

The exact source uses a two-dimensional dynamic-programming table. This detail matters: although the Optimal manifest describes descending one-dimensional updates and claims $O(target)$ space, the checked-in solution does not perform that optimization. Its real storage is $O(n\cdot target)$.

**Define a state that remembers how many elements are available**

Let

$$
\texttt{f}[i][j]
=
\text{maximum length of a subsequence chosen from the first }i
\text{ elements whose sum is exactly }j.
$$

The first dimension prevents an element from being chosen repeatedly. Row $i$ makes a decision about the $i$th input element and reads only row $i-1$.

A state can be unreachable. It cannot safely be initialized to zero, because zero is a legitimate length for sum $0$, while a positive sum may not be formable at all. The solution uses negative infinity:

`f = [[-inf] * (target + 1) for _ in range(n + 1)]`.

The one reachable base state is `f[0][0] = 0`. With no elements, the empty subsequence forms sum $0$ with length $0$. No positive sum is reachable.

**Make the skip-or-take decision**

The loop enumerates `nums` beginning at row index $1$. Let `x` be the current element and let row $i-1$ represent all decisions involving earlier elements.

For every desired sum $j$ from $0$ through `target`, there are two possibilities.

First, skip `x`. The best length remains whatever was achievable before:

`f[i][j] = f[i - 1][j]`.

Second, take `x`. This is possible only if `j >= x`. The earlier selected elements must then sum to `j - x`, and taking the current element increases their length by one:

`f[i - 1][j - x] + 1`.

The state keeps the better of skipping and taking:

$$
\texttt{f}[i][j]
=
\max\left(
\texttt{f}[i-1][j],
\texttt{f}[i-1][j-x]+1
\right).
$$

If `f[i - 1][j - x]` is negative infinity, adding one leaves it negative infinity, so an unreachable predecessor cannot create a false reachable state. This avoids a separate conditional reachability test.

**Why reading the previous row enforces 0/1 usage**

The take transition reads `f[i - 1][j - x]` rather than `f[i][j - x]`. Thus the subsequence being extended was constructed without the current element. After adding `x` once, the algorithm moves into row $i$ and never uses row $i$ as a take predecessor for the same element.

If the current row were used, one array entry could be taken repeatedly, turning the problem into unbounded knapsack and producing invalid subsequences.

**Why subsequence order is automatically respected**

Rows process elements from left to right. Any state in row $i-1$ uses a subsequence of the first $i-1$ elements. Appending the current $i$th element places it after all previously selected indices, preserving their original order. The table does not need to store the indices themselves.

Conversely, every subsequence of the first $i$ elements either excludes the current element or includes it as its last chosen element. These are exactly the skip and take cases, so the transition considers every valid possibility.

**Why the stored length is optimal**

We can prove the state definition by induction on $i$.

For $i=0$, only sum $0$ is possible and the initialization is exact. Assume row $i-1$ contains the maximum lengths for all sums using the earlier elements. Any subsequence considered for `f[i][j]` either:

- does not contain `x`, in which case its length is at most `f[i - 1][j]`; or
- contains `x`, in which case removing that final selected element leaves a subsequence of the first $i-1$ elements summing to `j-x`, with length at most `f[i - 1][j - x]`.

The transition takes the maximum of the best result in both exhaustive cases. Each finite candidate is constructible, so the result is exactly optimal.

After all $n$ elements, `f[n][target]` is the maximum requested length. Since array values and `target` are positive, a subsequence summing to `target` must contain at least one element. Therefore a final value greater than zero is a valid answer, while a nonpositive value means the target is unreachable. The return expression maps the latter case to `-1`.

For example, with `nums = [1, 2, 1, 1]` and `target = 3`, the table can form $3$ as `1 + 2` with length $2$, or as `1 + 1 + 1` with length $3$. Because every state stores the maximum length rather than merely reachability, the final answer becomes $3$.

**Why sums above the target can be ignored**

All input values are positive. Once a selected sum exceeds `target`, adding more values can never reduce it back to `target`. It is therefore sufficient to allocate columns $0$ through `target`. This pruning would not be valid if negative numbers were permitted.

## Complexity detail

Let $n$ be the length of `nums` and let $T=\texttt{target}$.

The solution fills $(n+1)(T+1)$ table entries. Each entry performs constant-time assignments, comparisons, and arithmetic, so time complexity is $O(nT)$.

The actual table also contains $(n+1)(T+1)$ numeric entries. Its auxiliary-space complexity is therefore $O(nT)$, not $O(T)$.

The manifest's $O(T)$ space statement describes a standard optimized variant: keep one array and iterate sums downward for each number. That optimization is not present in the exact source being explained. A faithful complexity analysis must report the behavior of the checked-in implementation, while recognizing that its time bound still matches the manifest.

Python's list-of-lists representation adds row-object overhead, but it does not change the asymptotic $O(nT)$ space bound.

## Alternatives and edge cases

- **One-dimensional descending knapsack:** Store only `dp[j]` and process `j` from `target` down to `x` for each element. This achieves the manifest's $O(T)$ space while keeping $O(nT)$ time. Descending order is mandatory to prevent using one element more than once.
- **One-dimensional ascending updates:** This is incorrect for the 0/1 problem. A state updated earlier in the same element's iteration could be reused, effectively selecting that element multiple times.
- **Store only reachability:** A Boolean table can tell whether `target` is attainable, but it cannot choose the longest among multiple attainable subsequences. Each state must retain the greatest length.
- **Enumerate all subsequences:** There are $2^n$ inclusion choices. Dynamic programming merges all choices with the same processed prefix and sum into one best result.
- **Target formed in several ways:** The `max` transition deliberately prefers the representation with more selected elements, even if another representation reaches the same sum earlier.
- **Unreachable target:** Negative infinity prevents nonexistent sums from participating in valid transitions. The final state is converted to `-1`.
- **An element larger than the target:** It can never be taken because no column has `j >= x`. The skip transition carries all previous states forward unchanged.
- **Repeated values:** Occurrences at different indices are distinct selectable elements. Separate rows allow each occurrence to be used once, which is exactly the subsequence rule.
- **Positive-number assumption:** It justifies ignoring sums greater than `target` and makes any valid target subsequence nonempty. Negative or zero values would require revisiting the state range and final validity test.
- **Empty subsequence:** It is represented only by `f[0][0] = 0` and propagated at sum zero. Because the target is positive, it cannot be returned as a solution.
- **Space-report mismatch:** The checked-in source is still mathematically correct, but its two-dimensional allocation may consume substantially more memory than the Optimal manifest promises. The explanation and complexity claim must follow the implementation actually present.
