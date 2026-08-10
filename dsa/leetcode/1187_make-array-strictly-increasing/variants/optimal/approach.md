## General

The challenge is not merely to fix each local inversion greedily. Replacing a value with something smaller may create more room for later values, even when the original value was currently legal. The exact solution uses dynamic programming around the original values that are kept and fills the gaps between them with values from `arr2`.

**Sort and remove duplicate replacement values**

The code first sorts `arr2`. Strictly increasing replacement blocks need distinct values in increasing order, so duplicate copies offer no additional possibility. It removes duplicates in place: `m` is the number of unique values written so far, and each newly encountered value is copied to `arr2[m]` only when it differs from the previous retained value. The final slice `arr2[:m]` keeps the sorted unique prefix.

Sorting enables binary search and makes consecutive slices of `arr2` ready-made increasing replacement sequences.

**Add fixed sentinels at both ends**

The augmented array is

`arr = [-inf] + arr1 + [inf]`.

Negative infinity is a permanent kept value smaller than every legal input. It provides a left boundary before the first real element. Positive infinity is a permanent kept value larger than every legal input. Treating it as the final kept value lets the same transition replace a trailing block of `arr1` without special end logic.

The dynamic-programming meaning is precise: `f[i]` is the minimum number of replacements needed to make the augmented prefix through index `i` strictly increasing while keeping `arr[i]` unchanged. Initially, `f[0] = 0` because the prefix containing only negative infinity needs no operation. All other states begin as infinity, meaning not yet reachable.

**Transition by keeping the preceding original value**

At index `i`, if `arr[i - 1] < arr[i]`, the immediately preceding augmented value can remain unchanged. Any valid construction counted by `f[i - 1]` can append `arr[i]` without another operation, so the code sets `f[i] = f[i - 1]`.

This is only one option. Even when the adjacent originals are increasing, replacing some preceding values can yield a cheaper feasible path for the rest of the array, so the solution also examines replacement blocks.

**Transition by replacing the whole gap before `arr[i]`**

Suppose the previous kept augmented position is `i - k - 1`. Then the `k` positions from `i - k` through `i - 1` are all replaced. The final sequence across this gap must satisfy

$$
\texttt{arr[i-k-1]} < b_1 < b_2 < \cdots < b_k < \texttt{arr[i]},
$$

where the $b$ values come from the deduplicated `arr2`.

The code computes `j = bisect_left(arr2, arr[i])`. Thus `arr2[0:j]` contains exactly the replacement values strictly smaller than the current kept value. To place `k` increasing replacements below `arr[i]`, it uses the last `k` of those values, from `arr2[j - k]` through `arr2[j - 1]`.

Why choose the largest available block? Its first value `arr2[j - k]` is as large as possible among any choice of `k` distinct replacements below `arr[i]`. A larger first value is easiest to place above the preceding kept boundary. If even this best possible first value is not greater than `arr[i - k - 1]`, no other length-`k` selection can work. If it is greater, the sorted unique block automatically increases and its last value is below `arr[i]`.

The loop tries

`k` from one through `min(i - 1, j)`.

There are only `i - 1` replaceable real positions before index `i` because augmented index zero is the fixed negative-infinity sentinel. There are only `j` unique replacement values below `arr[i]`. Both limits are necessary.

When the boundary check succeeds, the candidate cost is

`f[i - k - 1] + k`.

The earlier state already makes everything through the previous kept position increasing. The gap uses exactly `k` operations, and the boundary inequalities connect all pieces. Taking the minimum over all choices finds the cheapest construction that keeps `arr[i]`.

**Why considering only consecutive replacement blocks is complete**

Look at any final strictly increasing arrangement and mark the positions whose original `arr1` values were kept. Between two consecutive kept positions, every original position was replaced; otherwise there would be another kept marker in the gap. The dynamic program considers exactly such gaps.

For a gap of length `k` ending before kept value `arr[i]`, any feasible solution needs `k` distinct `arr2` values between the two kept boundaries. The largest `k` values below `arr[i]` make the left-boundary inequality no harder than any other selection. Therefore, the transition detects the gap whenever any feasible replacement set exists.

By induction over kept positions, `f[i]` is the minimum cost for its stated condition. The positive-infinity sentinel is always kept at the end, so `f[n - 1]` covers every real array position, including solutions that replace the final several values. If that state remains infinite, no increasing arrangement exists and the code returns `-1`; otherwise it returns the minimum operation count.

## Complexity detail

Let $n$ be the length of `arr1` and $m$ be the original length of `arr2`. Let $u$ be the number of distinct values in `arr2` after deduplication.

Sorting costs $O(m\log m)$ time, and in-place deduplication plus slicing costs $O(m)$. The augmented dynamic program has $n+2$ positions. Each position performs one $O(\log u)$ binary search and then tries at most $\min(n,u)$ gap lengths. The total time is

$$
O\left(m\log m+n\log u+n\min(n,u)\right).
$$

A simple bound using $u\leq m$ is $O(m\log m+nm)$, and when $n$ and $m$ are of comparable maximum size the quadratic transition scan dominates. The binary search is outside the inner `k` loop, so it does not multiply every transition by a logarithmic factor.

The exact code stores the deduplicated `arr2` list, an augmented array of length $n+2$, and an `f` array of the same length. Its auxiliary storage is $O(n+m)$ when counting these created lists. The DP portion alone uses $O(n)$ beyond the replacement array. The returned integer uses constant space.

## Alternatives and edge cases

- **Map-based prefix dynamic programming:** Track reachable previous values and their minimum costs, using binary search for the smallest replacement greater than each previous value. It is conceptually direct but can maintain up to $O(m)$ states per position.
- **Top-down memoization:** Recurse on the current index and previous chosen value. Memoization avoids repeated subproblems, but recursion depth and a potentially large state map make the iterative gap DP attractive.
- **Greedy replacement of only current inversions:** This can fail because replacing an already legal value with a smaller one may be necessary to leave room for future elements.
- **Duplicate values in `arr2`:** They cannot occupy two positions of a strictly increasing replacement block. Deduplication removes useless copies and makes index counts correspond to distinct choices.
- **Already strictly increasing `arr1`:** Every adjacent keep transition succeeds, propagating zero operations through the positive-infinity sentinel.
- **Replace a prefix:** The previous kept position is the negative-infinity sentinel. The `k <= i - 1` bound permits replacing all real positions before the current kept value without replacing the sentinel.
- **Replace a suffix:** The positive-infinity sentinel acts as the current kept value, so its transition can replace the final block of real elements.
- **Replace the entire array:** At the positive-infinity sentinel, choose a gap whose previous kept position is negative infinity. This is possible only when enough distinct `arr2` values exist.
- **Strict rather than non-decreasing order:** Both boundary checks use `<`, and `bisect_left` restricts replacements to values strictly below the current kept value. Equal adjacent values are never accepted.
- **Impossible instance:** If no chain reaches the final sentinel, `f[n - 1]` remains infinity and the method returns `-1`.
- **Zero-valued inputs:** Negative infinity is safely smaller than zero and every allowed input, so it creates no artificial restriction on the first real choice.
