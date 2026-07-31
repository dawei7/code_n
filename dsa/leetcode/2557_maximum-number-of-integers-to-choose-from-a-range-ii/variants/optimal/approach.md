## General

For any fixed number of selections, choosing the smallest available values produces the minimum possible sum. If a feasible selection contains a larger allowed value while a smaller allowed value is unused, exchanging the larger one for the smaller one cannot increase the sum. Repeating this exchange shows that the answer is always a prefix of the allowed integers in ascending order.

Scanning all values through `n` is impossible when $n$ can reach $10^9$. Instead, deduplicate and sort the banned values. Consecutive banned values divide $[1,n]$ into gaps containing only allowed integers. If a gap begins at $a$ and contains $L$ values, taking its first $x$ values costs

$$
\frac{x(2a+x-1)}{2}.
$$

This cost increases with $x$, so binary search finds the largest prefix of the gap that fits the remaining budget. Add that prefix length to the answer and subtract its cost. If the entire gap fits, continue after the banned boundary. If only part fits, return immediately: every unprocessed allowed value is larger, so none can support a selection with more elements than the cheapest prefix already considered.

The final sentinel `n + 1` closes the last allowed gap without a separate case. Filtering banned values to $[1,n]$ is harmless under the stated contract and keeps the adapter robust; converting them to a set ensures duplicates create only one boundary.

## Complexity detail

Let $m$ be the length of `banned`, and let $k$ be the number of distinct in-range banned values. Deduplication takes $O(m)$ expected time, sorting takes $O(k \log k)$ time, and at most $k+1$ gap searches each take $O(\log n)$ time. Thus the overall bound is $O(m + k \log k + k \log n)$, summarized conservatively as $O(m \log m + m \log n)$. The sorted boundaries use $O(k)$ space, which is $O(m)$.

## Alternatives and edge cases

- **Linear greedy scan:** Visiting every integer from $1$ through $n$ and taking each allowed value is correct, but its $O(n+m)$ time is infeasible when $n$ is near $10^9$.
- **Closed-form square root:** A quadratic formula can estimate how many values fit inside one gap in constant time, but integer rounding still needs careful correction; binary search is simple and exact.
- **Duplicate banned values:** Deduplication is necessary so repeated values do not create negative or repeated gaps.
- **Budget exhausted inside a gap:** Once the cheapest remaining allowed value cannot be added, no later value can improve the count, so returning early is sound.
- **All values banned:** Every gap has length zero and the accumulated count remains zero.
- **Large arithmetic:** Gap sums can approach `maxSum` near $10^{15}$, so implementations in fixed-width languages must use 64-bit integer arithmetic.
