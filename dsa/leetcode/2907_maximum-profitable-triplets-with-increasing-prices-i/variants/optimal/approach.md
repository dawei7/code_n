## General

We need choose indices $i<j<k$ such that their prices are strictly increasing:

$$
\texttt{prices}[i]<\texttt{prices}[j]<\texttt{prices}[k].
$$

The score of the choice is `profits[i] + profits[j] + profits[k]`, and we want the maximum score. Price determines whether a triplet is legal; profit determines which legal triplet is best. A highly profitable item cannot be used if its position or price violates the required chain.

Checking every triple directly would need three nested loops. The source removes one loop by fixing the middle index $j$. Once $j$ is known, the two remaining decisions are independent:

- choose an index $i<j$ with `prices[i] < prices[j]`;
- choose an index $k>j$ with `prices[j] < prices[k]`.

No additional comparison between $i$ and $k$ is necessary. Both inequalities through the middle already imply `prices[i] < prices[k]`, and their positions on opposite sides of $j$ already imply $i<k$.

**Find the most profitable eligible item on the left**

For each middle $j$, `left` starts at zero. The first inner loop scans every earlier index $i$ from $0$ through $j-1$. An item is eligible only if its price is strictly below the middle price. Among eligible items, the condition `left < profits[i]` retains the greatest profit seen.

After this loop:

$$
\texttt{left}
=
\max\{\texttt{profits}[i]\mid 0\le i<j,\ \texttt{prices}[i]<\texttt{prices}[j]\},
$$

if that set is nonempty. Otherwise `left` remains zero. The constraints make every actual profit positive, so zero unambiguously means that no eligible earlier item was found.

**Find the most profitable eligible item on the right**

The second inner loop performs the symmetric search after $j$. It examines $k=j+1$ through $n-1$, accepts only `prices[j] < prices[k]`, and stores the maximum corresponding profit in `right`.

Thus a positive `right` represents a real later item with a strictly larger price. Equal prices are excluded on both sides because the contract asks for a strictly increasing sequence, not a non-decreasing one.

**Combine the side choices only when both exist**

If either side remains zero, $j$ cannot be the middle of a valid triplet. The code does not form a candidate in that case.

When both are positive, the best total for this particular middle is

`left + profits[j] + right`.

The current middle's own profit is always included exactly once. The result variable `ans` keeps the maximum candidate across all middle indices. It begins at `-1`, which is the required result when no valid triplet exists.

**Why independent maxima are compatible**

Choosing the left maximum cannot interfere with the right maximum. Every item considered for `left` is located before $j$ and is cheaper than the middle. Every item considered for `right` is located after $j$ and is more expensive than the middle. Therefore the two stored maxima came from distinct positions and, together with $j$, automatically satisfy both index order and price order.

This is different from problems where two choices share a budget or cannot reuse a value. Here, after fixing the middle, there is no constraint coupling the two sides. Maximizing their profit contributions separately maximizes their sum.

**Why the result is globally optimal**

Consider any valid triplet $(i,j,k)$. When the outer loop reaches this same middle $j$, index $i$ appears in the left scan's eligible set. Therefore `left >= profits[i]`. Index $k$ appears in the right scan's eligible set, so `right >= profits[k]`. The candidate computed for $j$ is consequently at least as profitable as this arbitrary triplet.

In the other direction, every candidate the algorithm records comes from actual scanned indices: a cheaper earlier item, the current middle, and a more expensive later item. Hence no candidate is an impossible upper bound; it is the profit of a real valid triplet.

The first direction says the algorithm cannot finish below the true optimum. The second says it cannot finish above the true optimum using an invalid combination. Together they prove that the returned finite answer is exactly the maximum valid profit.

**A concrete trace**

Suppose `prices = [10, 2, 3, 4]` and `profits = [5, 2, 7, 10]`.

- At $j=1$, price $2$ has no cheaper item before it, so `left` remains zero.
- At $j=2$, price $3$ has the earlier price $2$ with profit $2$, and the later price $4$ with profit $10$.
- The candidate is $2+7+10=19$.
- At $j=3$, no later item exists, so `right` remains zero.

The answer is $19$. Notice that the item with price $10$ is earlier than the middle but is ineligible because its price is too high. The scans filter by both position and price rather than choosing the globally greatest profits.

## Complexity detail

Let $n$ be the number of items.

For a fixed middle $j$, the left loop checks $j$ positions and the right loop checks $n-j-1$ positions. Their sum is always $n-1$. Repeating this for all $n$ possible middles performs $n(n-1)$ constant-time checks, so running time is $\Theta(n^2)$ and therefore $O(n^2)$.

The implementation stores only `n`, `ans`, `left`, `right`, and loop variables. It does not build candidate lists or copy either input array. Auxiliary space is $O(1)$.

This complexity follows the exact checked-in source. More advanced range-query structures could improve the asymptotic time, but the quadratic scan is the deliberate method used for this version and its input bound.

## Alternatives and edge cases

- **Enumerate every triplet:** Three loops directly test all $i<j<k$ combinations in $O(n^3)$ time. Fixing $j$ and keeping only side maxima removes an unnecessary factor of $n$.
- **Fenwick tree or segment tree by price:** Coordinate-compressed range-maximum queries can obtain best profits for smaller or larger prices more quickly. They add data-structure complexity that the exact source and this version's constraints do not require.
- **Precompute every side maximum:** Arrays of best eligible left and right profit can also be constructed, but eligibility depends on the current price, so a simple prefix maximum without price-aware queries is insufficient.
- **Equal prices:** Items with a price equal to the middle cannot be selected. Replacing either strict comparison with a non-strict one would accept invalid triplets.
- **No eligible left item:** Even an excellent middle and right pair cannot form a length-three triplet; `left == 0` prevents a false candidate.
- **No eligible right item:** The same reasoning applies symmetrically when `right == 0`.
- **Strictly decreasing or constant prices:** No middle has both required sides, so `ans` remains `-1`.
- **Positive-profit guarantee:** Zero is a safe “not found” sentinel only because legal profits are strictly positive. If zero or negative profits were allowed, eligibility would need a separate Boolean or a different sentinel.
- **Several items share the greatest eligible profit:** Any one of them is enough because only the maximum total value is requested, not the indices.
- **Large numeric totals:** The result adds only three profits. Python integers do not overflow; a fixed-width implementation should choose a type that covers the stated profit bounds.
