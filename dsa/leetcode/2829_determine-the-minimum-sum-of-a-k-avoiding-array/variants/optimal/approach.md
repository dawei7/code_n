## General

To minimize the sum, prefer smaller positive integers whenever they can belong to some valid optimum. For each complementary pair $x$ and $k-x$ with $x < k-x$, choosing the smaller value $x$ is never worse than choosing its larger partner.

This selects the consecutive lower block from $1$ through $\lfloor k/2 \rfloor$. When `k` is even, the endpoint $k/2$ is safe: the restriction concerns two distinct elements, and duplicate values are already forbidden, so one copy cannot form a prohibited pair with itself.

Every integer strictly between $\lfloor k/2 \rfloor$ and $k$ is the larger complement of a selected lower-block value and must be skipped. All integers from $k$ onward are safe because adding any positive integer to one of them produces a sum greater than $k$. If more values are required, the minimum continuation is therefore the consecutive upper block beginning at `k`.

Let `small_count` be `min(n, k // 2)` and let `remaining` be `n - small_count`. The chosen values are exactly:

- $1,2,\ldots,\texttt{small_count}$; and
- $k,k+1,\ldots,k+\texttt{remaining}-1$.

Sum both arithmetic progressions directly. The lower block contributes

$$
\frac{\texttt{small_count}(\texttt{small_count}+1)}{2},
$$

and the upper block contributes

$$
\frac{\texttt{remaining}(2k+\texttt{remaining}-1)}{2}.
$$

**Why no other valid array has a smaller sum**

Within every complementary pair below `k`, replacing a chosen larger member by its unchosen smaller member preserves distinctness and validity while decreasing the sum. Thus an optimum uses the available lower members first. After all safe lower values are used, every still-smaller positive candidate is forbidden by one of them; the least possible remaining choices are consequently `k` and the consecutive integers after it. The two blocks are therefore componentwise no larger than the sorted elements of any valid alternative.

## Complexity detail

The method evaluates a fixed number of integer expressions regardless of `n` and `k`, so it takes $O(1)$ time and $O(1)$ auxiliary space.

The benchmark uses `n` as `size` and fixes `k = 50`. It distinguishes direct arithmetic-series evaluation from the natural greedy simulation that scans candidates and stores selected values.

## Alternatives and edge cases

- **Greedy set simulation:** Scan positive integers in increasing order, accepting a candidate when its complement is not already selected. This is correct and intuitive but uses $O(n+k)$ time and $O(n)$ space under the input bounds.
- **Enumerate candidate subsets:** Testing combinations can find the optimum but explores exponentially many choices and ignores the complementary-pair structure.
- **Even midpoint:** A single value `k // 2` is allowed when `k` is even because a forbidden pair must contain distinct array elements.
- **Small requested count:** If `n <= k // 2`, the answer is simply the sum of `1` through `n`.
- **Forbidden sum one:** No two positive integers sum to `1`, so the optimum is the first `n` positive integers.
- **Upper-block boundary:** Once the lower block is full, the next safe value is `k`, not `k // 2 + 1`.
- **Distinctness:** The construction contains no repeated value and the two blocks cannot overlap.
