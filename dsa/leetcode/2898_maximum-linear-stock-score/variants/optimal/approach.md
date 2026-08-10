## General

**Rewrite the pair condition into an invariant.** For two consecutively selected one-based indices $a<b$, linearity requires

$$
\texttt{prices[b]}-\texttt{prices[a]}=b-a.
$$

Move each index to the same side:

$$
\texttt{prices[b]}-b=\texttt{prices[a]}-a.
$$

Thus two indices can be consecutive in a linear selection exactly when their `price - index` values are equal. By transitivity, every index in one linear selection must share the same invariant.

Conversely, if several indices all share that invariant, then any two of them $a<b$ satisfy the rearranged equality, so selecting them in their original increasing order is linear. The problem is therefore not a subsequence dynamic program; it is grouping prices by one key.

**How the source handles zero-based enumeration.** Python `enumerate(prices)` yields indices `i = 0,1,...`, while the statement describes days as one-based. The source uses key `x - i` instead of `x - (i + 1)`. Every true one-based key is exactly one smaller:

$$
x-(i+1)=(x-i)-1.
$$

Subtracting the same constant from every key changes key labels but not which indices are equal-key groups. The grouping is therefore fully correct despite the indexing convention difference.

**Accumulate a score for each invariant.** `cnt` is a Counter used here as a numeric map. For each position and price `x`, the source performs `cnt[x - i] += x`. After the scan, `cnt[key]` is the sum of all prices whose indices belong to that linear group.

All prices are positive. Once a linear invariant group is chosen, including another member of the same group preserves linearity and strictly increases the score. Therefore the best selection for that key includes every one of its indices. No within-group optimization is needed.

Finally, `max(cnt.values())` chooses the group with the largest full sum.
Take any valid linear selection. Its adjacent pairs satisfy the invariant equality, so by chaining those equalities every selected index lies in one Counter group. Its score is at most that group's stored total because the stored total includes all positive prices in the group. Thus no valid selection beats the maximum Counter value.

For the reverse direction, choose the group attaining the maximum stored total and list its indices in original order. Every adjacent pair has equal invariant, so the price difference equals the index difference. This is a legal linear selection whose score is exactly the returned value. The upper and lower arguments prove optimality.

**Trace `prices = [1,5,3,7,8]`.** With zero-based indices, keys are `1,4,1,4,4`. The key-four group contains prices five, seven, and eight, whose sum is twenty. Their one-based indices are two, four, and five. Price changes are two then one, matching index changes two then one.

The key-one group contains prices one and three with sum four. Taking the maximum group sum returns twenty.

**Subsequence order is automatic.** The Counter forgets individual positions after grouping, but it does not need to reconstruct the selected indices because only the score is requested. All members can always be ordered by their original indices, producing a subsequence. Grouping does not authorize reordering; it merely proves the original ordering is valid.

**A single element is always linear.** The condition applies only to consecutive selected pairs. Any one-element selection satisfies it vacuously. Since the input is nonempty, the Counter has at least one value and `max` is safe.

## Complexity detail

Let $n$ be the number of days and $u$ the number of distinct invariant keys. The source scans once and performs expected constant-time hash updates, taking expected $O(n)$ time. Finding the maximum among $u$ totals costs $O(u)$, which is at most $O(n)$.

The Counter stores one entry per distinct key, so auxiliary space is $O(u)$ and $O(n)$ in the worst case. The maximum score can reach $10^{14}$; Python integers handle it, while fixed-width languages need 64-bit accumulation.

## Alternatives and edge cases

- **Dynamic programming over previous days:** It can test the linear relation pairwise but wastes $O(n^2)$ time when equality of one invariant solves the problem.
- **One-based key:** Using `price - (i + 1)` creates different numeric labels but exactly the same groups.
- **All keys equal:** Every day can be selected and the answer is the sum of all prices.
- **All keys distinct:** The best linear selection has one day, so return the largest individual price.
- **Positive-price guarantee:** It justifies including every member of a chosen group. Negative prices would require selecting a beneficial subset.
- **Repeated prices:** Equal prices at different indices usually have different keys; equality of price alone is not enough.
- **Large sums:** Use a wide integer type outside Python.
- **No reconstruction needed:** The problem requests only maximum score, so storing group totals is sufficient.
- **Dictionary default of zero:** Because every price is positive, a previously unseen invariant key may safely begin with total zero before the current price is added.
