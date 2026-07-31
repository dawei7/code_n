## General

**Separate the modulo groups**

Each inequality connects indices `i - k` and `i`, which have the same remainder modulo `k`. Therefore the array splits into `k` independent sequences

$$
\texttt{arr[r]},\ \texttt{arr[r+k]},\ \texttt{arr[r+2k]},\ldots
$$

for remainders $0 \le r < k$. Making every such sequence non-decreasing is both necessary and sufficient for the whole array to be K-increasing.

**Keep the largest valid subsequence**

Within one group, unchanged values must form a non-decreasing subsequence. If its longest possible length is $L$ in a group of length $g$, then at least $g-L$ values must change. Conversely, the values outside that subsequence can always be replaced with positive integers chosen between or around the retained values, so $g-L$ changes are sufficient.

Compute the longest non-decreasing subsequence length with a `tails` array. For each value, use `bisect_right` to find the first tail strictly greater than it. Append when none exists; otherwise replace that tail. Right-biased insertion is essential because equal values may extend a non-decreasing subsequence.

The length of `tails` is the group's longest non-decreasing subsequence length. Add `group_length - len(tails)` for every remainder. Since groups contain disjoint indices, their individually minimal replacement counts sum to the global minimum.

## Complexity detail

Every one of the $n$ values performs one binary search in a tails array of length at most $n$, so the time is $O(n\log n)$. Across one group at a time, the largest tails array and extracted traversal use at most $O(n)$ space.

## Alternatives and edge cases

- **Quadratic subsequence dynamic programming:** Compare every earlier value in each group to compute its best non-decreasing subsequence ending there. This is correct but takes $O(n^2)$ time when `k = 1`.
- **Greedy adjacent repairs:** Changing a value as soon as one inequality fails can destroy choices for later comparisons and does not necessarily minimize replacements.
- Equal values must be retained together when possible, which requires `bisect_right` rather than `bisect_left`.
- When `k = n`, every group has one value and no operation is needed.
- Groups can differ in length by one; each must use its actual number of elements.
- Replacement values may be any positive integers, so only the maximum number of original values that can remain constrains the optimum.
