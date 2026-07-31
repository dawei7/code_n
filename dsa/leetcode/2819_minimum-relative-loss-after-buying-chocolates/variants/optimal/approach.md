## General

**Express one chocolate's relative loss**

For threshold `k`, a price `p <= k` contributes `p` to Bob's payment and zero to Alice's, so its relative loss is `p`. A price `p > k` contributes `k - (p - k) = 2 * k - p`. Thus the loss as a function of sorted price increases through `k`, then decreases beyond `k`.

**Every optimum is a prefix plus a suffix**

Among prices at most `k`, the smallest losses are the smallest prices, so any chosen items from that side form a prefix of the sorted array. Above `k`, the expression `2 * k - p` decreases as `p` grows, so chosen items from that side form a suffix.

Suppose a query needs `m` chocolates and chooses `t` from the low prefix. It must choose `m - t` from the high suffix. If `c` prices are at most `k`, feasibility requires

$$
\max(0,m-(n-c)) \leq t \leq \min(m,c).
$$

Prefix sums evaluate a feasible split in constant time:

$$
L(t)=P[t]+2k(m-t)-\bigl(P[n]-P[n-(m-t)]\bigr),
$$

where $P[r]$ is the sum of the first $r$ sorted prices.

**Binary-search the convex split**

Increasing `t` by one replaces the smallest currently selected suffix price at index `n - m + t` with the next prefix price at index `t`. The marginal change is

$$
L(t+1)-L(t)=\texttt{prices[t]}+\texttt{prices[n-m+t]}-2k.
$$

Both indexed prices are non-decreasing with `t`, so this marginal change is monotone. Binary-search the first feasible `t` where it becomes non-negative; that is a minimum of the discrete convex function. If it stays negative, the search reaches the largest feasible split.

Every possible subset can be improved or preserved by replacing its low-side selections with the cheapest low prices and its high-side selections with the most expensive high prices, so some optimum has the prefix-suffix form. The binary search minimizes over every feasible form, proving that its loss is globally minimal.

## Complexity detail

Let $n$ be the number of prices and $q$ the number of queries. Sorting and building prefix sums cost $O(n\log n)$ time. Each query uses binary search to locate the threshold boundary and another binary search for the optimal split, both in $O(\log n)$ time. Total time is $O((n+q)\log n)$. The sorted prices, prefix sums, and returned answers use $O(n+q)$ total storage, of which $O(n)$ is auxiliary working space beyond the required output.

## Alternatives and edge cases

- **Transform and sort every query:** Computing every price's query-specific loss and sorting those losses is correct but costs $O(qn\log n)$ time.
- **Ternary search the split:** The objective is convex, but the monotone discrete marginal permits a simpler exact binary search without comparing neighboring totals repeatedly.
- **Evaluate all feasible splits:** Prefix sums make each split constant-time, yet scanning up to $n$ splits per query is still $O(qn)$.
- A threshold below every price makes all candidate losses `2 * k - p`, so the most expensive prices are best.
- A threshold at least every price makes loss equal to price, so the cheapest prices are best.
- When `m = n`, every chocolate must be selected even if some individual losses are unfavorable.
- Duplicate prices may straddle neither side of the threshold because all values equal to `k` belong to the fully-paid prefix.
- The minimum relative loss may be negative and can require 64-bit integer arithmetic.
- A zero marginal means either adjacent split is optimal; choosing the first non-negative position is sufficient.
