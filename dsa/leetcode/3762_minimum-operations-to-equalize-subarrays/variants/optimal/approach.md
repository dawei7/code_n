## General

Adding or subtracting `k` never changes a value's remainder modulo `k`. Therefore, a queried subarray can be equalized if and only if all its elements have the same remainder. Record a prefix count of adjacent remainder changes; a range is compatible exactly when that count is unchanged between its endpoints.

For a compatible range, write each value as `nums[i] = k * normalized[i] + remainder`. One operation changes `normalized[i]` by one, so making the range equal to a normalized target $t$ costs

$$
\sum_{i=l}^{r}\lvert\texttt{normalized[i]}-t\rvert.
$$

This sum is minimized by any median. The remaining task is therefore to obtain a range median plus the counts and sums on both sides of it.

Coordinate-compress the normalized values and build a persistent count-and-sum segment-tree version for every array prefix. Subtracting the version before `l` from the version after `r` represents exactly the multiset in `[l,r]`. Descend the two roots together to find the lower median. Whenever the descent goes right, accumulate the count and sum of the skipped left branch. At the median leaf, combine those accumulators with the equal values and the total range sum. If the median is $m$, the answer is

$$
mC_L-S_L+S_R-mC_R,
$$

where $C_L,S_L$ cover values at or below the chosen median and $C_R,S_R$ cover those above it. This is precisely the sum of absolute deviations and therefore the minimum operation count.

## Complexity detail

Let $n$ be the array length and $q$ the number of queries. Coordinate compression costs $O(n\log n)$. Building all persistent versions costs $O(n\log n)$ time and space. Remainder compatibility is checked in $O(1)$, while each compatible query takes $O(\log n)$ for the median and accumulated sums. Total time is $O((n+q)\log n)$ and auxiliary space is $O(n\log n)$.

## Alternatives and edge cases

- **Sort every queried subarray:** This directly exposes its median but costs up to $O(qn\log n)$ across many large queries.
- **Range sums without order statistics:** Prefix sums alone cannot identify a query's median when values are unsorted.
- **Ignore remainders:** Values in different residue classes modulo `k` can never become equal, regardless of operation count.
- **Singleton query:** One value is already equal to itself, so every length-one range returns `0`.
- **Even range length:** Either middle value minimizes the absolute-deviation sum; choosing the lower median gives the same cost.
- **Repeated values:** The persistent counts retain multiplicity, which is required both for the median rank and the total cost.
- **Independent queries:** Never apply one query's hypothetical updates to the shared input array.
