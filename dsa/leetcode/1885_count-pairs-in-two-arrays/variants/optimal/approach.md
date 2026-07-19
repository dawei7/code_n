## General
**Transform the pair inequality**

For each position define

$$
d_i=\texttt{nums1[i]}-\texttt{nums2[i]}.
$$

Moving the `nums2` terms to the left shows that a pair is valid exactly when $d_i+d_j>0$. The original positions no longer affect validity beyond requiring two distinct elements, so the difference array may be sorted.

**Count a whole block at once**

Sort the differences and place pointers at the smallest and largest remaining values. If `differences[left] + differences[right] > 0`, then every value from `left` through `right - 1` also forms a positive sum with the current right value. Add `right - left` pairs and decrement `right`.

If that smallest-plus-largest sum is nonpositive, the left value cannot pair successfully with any remaining value, because `right` is already the largest. Increment `left` and discard it. Continue until the pointers meet.

**Why every pair is counted exactly once**

Each successful step counts all still-unprocessed pairs whose larger sorted endpoint is `right`, then removes that endpoint. Each unsuccessful step proves that no pair using `left` can qualify before removing it. Thus no valid pair is missed, invalid pairs are never added, and no endpoint pair can be counted twice.

## Complexity detail
Building the $N$ differences takes $O(N)$ time. Sorting costs $O(N\log N)$, and the two pointers move inward at most $N-1$ times, so total time is $O(N\log N)$. The difference array occupies $O(N)$ auxiliary space. The result may be as large as $\binom{N}{2}$, so implementations must use a sufficiently wide integer type where necessary.

## Alternatives and edge cases
- **All index pairs:** Directly testing every $(i,j)$ is correct but takes $O(N^2)$ time.
- **Binary search per endpoint:** After sorting, search for the first partner greater than $-d_j$ for each $j$; this also takes $O(N\log N)$ time.
- **One element:** No pair exists, so return `0`.
- **Strict inequality:** A difference sum of exactly zero must not be counted.
- **All positive differences:** Every one of the $\binom{N}{2}$ pairs qualifies.
- **All nonpositive differences:** No pair can qualify.
- **Duplicate differences:** They remain separate indexed elements and contribute with their full multiplicity.
