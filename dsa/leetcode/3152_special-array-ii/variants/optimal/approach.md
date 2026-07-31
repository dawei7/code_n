## General

A query fails precisely when its range contains at least one adjacent pair with equal parity. The individual values do not otherwise matter, so reduce the array to boundary violations between consecutive positions.

Define `violations[i]` as the number of equal-parity adjacent pairs whose right endpoint is at most `i`. Start with zero at index $0$. For every later index, copy the preceding count and add one exactly when `nums[i - 1]` and `nums[i]` have the same remainder modulo $2$.

For a query `[left, right]`, the relevant pair boundaries have right endpoints from `left + 1` through `right`. Their count is therefore

$$
\texttt{violations[right]}-\texttt{violations[left]}.
$$

The range is special exactly when this difference is zero, which is equivalent to the two prefix counts being equal. This also handles a singleton automatically: when `left == right`, the two counts are the same.

Every equal-parity boundary is recorded once during preprocessing. The prefix difference selects exactly the boundaries inside each query, so a `true` answer means every adjacent pair in that subarray alternates, while a `false` answer is backed by at least one actual violation. Thus every reported boolean matches the definition.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and $q = \lvert\texttt{queries}\rvert$. Building the prefix counts takes $O(n)$ time, and each query takes $O(1)$ time, for $O(n+q)$ total time.

The prefix array stores $n$ counts, so the auxiliary space is $O(n)$. The returned $q$ booleans are output space.

## Alternatives and edge cases

- **Sorted violation indices plus binary search:** Record only equal-parity boundaries, then binary-search for one inside each query. This uses space proportional to the number of violations but takes $O((n+q)\log n)$ time in the worst case.
- **Direct scan per query:** Checking every adjacent pair inside each requested subarray is simple and correct, but overlapping long queries can require $O(nq)$ total time; it is the principal slower benchmark comparison.
- **Maximal alternating runs:** Label every index by its alternating-run start, then compare the labels of each query's endpoints. This also achieves $O(n+q)$ time and $O(n)$ space.
- A singleton query is always special because its range contains no pair boundary.
- A violation immediately outside `[left, right]` must not affect that query; subtracting `violations[left]` excludes the left external boundary.
- Duplicate queries and arbitrary query order are valid, and answers must preserve that order.
- Violations at either endpoint pair are included because query bounds are inclusive.
