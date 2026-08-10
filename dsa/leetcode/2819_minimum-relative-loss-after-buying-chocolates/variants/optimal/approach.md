## General

**Express one chocolate's relative-loss contribution.** For a query `(k, m)`, a chocolate of price $p$ contributes differently on the two sides of $k$.

If $p \le k$, Bob pays the full $p$ and Alice pays zero, so Bob's relative loss contribution is $p$.

If $p>k$, Bob pays $k$ and Alice pays $p-k$, so the contribution is

$$
k-(p-k)=2k-p.
$$

The task for one query is therefore to select exactly $m$ prices with the smallest total under this V-shaped, then decreasing, cost rule.

**Sort once for all queries.** The code sorts `prices` in ascending order and builds prefix sums `s` with an initial zero. Then `s[t]` is the sum of the first $t$ prices, and any suffix sum can be obtained by subtraction.

On the low-price side $p \le k$, contribution $p$ increases with price. If the answer selects $l$ such chocolates, the best choices are the $l$ smallest prices.

On the high-price side $p>k$, contribution $2k-p$ decreases as price increases. If the answer selects $r$ such chocolates, the best choices are the $r$ largest prices.

Thus, for some split $l+r=m$, an optimum has the form “smallest $l$ prices plus largest $r$ prices.” The only remaining question is the best $l$.

**Write the cost of a split.** The prefix contributes `s[l]`. The sum of the largest $r$ actual prices is `s[n] - s[n - r]`. Transforming each through $2k-p$ gives total `2 * k * r - (s[n] - s[n - r])`.

Therefore, once `l` is known, the source computes

`s[l] + 2 * k * r - (s[n] - s[n - r])`.

The prefix and suffix never overlap because $l+r=m\le n$.

**Bound the number of low-side choices.** `bisect_right(prices, k)` counts prices at most $k$. The search upper bound is the smaller of that count and $m$, because there is no reason to classify more than $m$ selected items as low-prefix choices. The helper searches `l` in the half-open interval beginning at zero and ending at that bound.

It is possible during early search candidates for the suffix to reach a price at or below $k$. The marginal comparison automatically moves `l` upward when treating that price as a suffix item would be worse, except that a price exactly equal to $k$ has the same contribution under either formula. The final cost remains valid at equality.

**Compare adjacent split costs.** Suppose the current split uses $l$ prefix values and $r=m-l$ suffix values. Moving to $l+1$ adds `prices[l]` to the prefix and removes the smallest currently used suffix price, `prices[n - r]`, whose transformed contribution is `2*k - prices[n-r]`.

The cost change is

$$
\texttt{prices}[l]+\texttt{prices}[n-r]-2k.
$$

As $l$ increases, both indexed prices are nondecreasing, so this marginal change is nondecreasing. The split-cost sequence is convex: it decreases while the change is negative and stops decreasing once the change is nonnegative.

The binary-search condition

`prices[mid] < 2 * k - prices[n - right]`

is exactly the statement that the next prefix price is cheaper than the suffix contribution it would replace. If true, increasing `l` improves the cost, so the lower bound moves right. Otherwise, the current or an earlier split is optimal, so the upper bound moves left.

When the loop ends, `l` is the first split where another increase would not reduce loss. That is a minimum of the convex sequence. Equality can admit two equally good adjacent splits; choosing the earlier one is harmless.

**Why no middle price is useful.** Among prices at most $k$, replacing a selected larger low price with an unselected smaller one cannot increase loss. Among prices above $k$, replacing a selected smaller high price with an unselected larger one cannot increase loss because $2k-p$ becomes smaller. Repeated exchange forces every optimum into the prefix-plus-suffix form. Convex binary search then chooses its best size, proving the returned query result is globally minimal.

**Closure timing is valid.** Helper `f` refers to `prices` and `n` from the outer function. Although it is defined before `n` receives a value, Python resolves closed-over variables when the helper is called, not when it is defined. Every call occurs after sorting, prefix-sum construction, and `n = len(prices)`, so the values are ready.

The source sorts the caller's `prices` list in place. Every query reuses that sorted order and the same prefix sums, which is the key to handling up to $10^5$ queries efficiently.

## Complexity detail

Let $n$ be the number of prices and $q$ the number of queries. Sorting costs $O(n\log n)$ time. Constructing prefix sums takes $O(n)$.

For each query, `bisect_right` takes $O(\log n)$ and the custom binary search takes another $O(\log n)$. The final prefix/suffix arithmetic is constant time. Total time is

$$
O(n\log n+q\log n)=O((n+q)\log n).
$$

The prefix-sum list uses $O(n)$ additional space. Python sorting may use $O(n)$ temporary storage. The answer list contains $q$ required results. Auxiliary storage excluding the output is $O(n)$; including it is $O(n+q)$.

Integer totals can be negative because Alice may pay much more than Bob. Python integers handle both sign and the maximum accumulated magnitude without overflow.

## Alternatives and edge cases

- **Sort per query:** Transform every price into its query-specific contribution, sort those costs, and sum the first $m$. This is correct but costs $O(qn\log n)$.
- **Ternary search on split:** Convexity permits it, but the discrete marginal binary search finds the exact first nonnegative change more cleanly.
- **All prices at most `k`:** Contributions equal prices, so the optimum is the $m$ smallest values. The binary search moves toward that prefix selection.
- **All prices above `k`:** Contributions decrease with price, so the optimum is the $m$ largest values and `l` remains zero.
- **Price exactly `k`:** Both formulas give contribution $k$, so assigning it to the prefix or suffix at a boundary is equivalent.
- **Select every chocolate:** Prefix and suffix together cover all indices without overlap, and the formula returns the total relative loss.
- **Negative minimum loss:** This is valid and means Alice's total payment exceeds Bob's; no clamping should occur.
- **Duplicate prices:** Sorting, prefix sums, and marginal comparisons work with equality, and duplicate chocolates remain distinct choices.
- **In-place sorting:** Callers that require original price order must pass a copy; the exact source mutates `prices`.
- **Large query volume:** The one-time sort and prefix sums are what reduce each independent query to logarithmic time.
