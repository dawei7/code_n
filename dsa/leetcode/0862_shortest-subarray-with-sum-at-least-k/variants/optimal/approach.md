## General
**Turn subarray sums into prefix differences**

A subarray ending just before prefix index $j$ and starting at prefix index $i$ is valid exactly when $P[j]-P[i]\geq k$. For a fixed endpoint $j$, a larger starting index gives a shorter subarray, while a smaller prefix value makes the sum easier to reach. The useful starts must balance both properties.

Maintain their indices in a deque. Indices increase from front to back because they are processed in order, and their prefix values also increase strictly. The deque therefore contains only starts that are not dominated by a newer start with an equal or smaller prefix.

**Resolve valid starts at the front**

At a current prefix $P[j]$, repeatedly test the front index `i`. If $P[j]-P[i]\geq k$, record `j - i` and remove `i`. This endpoint is the earliest one that makes `i` valid; every future endpoint would produce a longer subarray from the same start, so `i` can never improve the answer again. Continue because later deque entries yield shorter lengths and may also satisfy the threshold.

**Discard dominated starts at the back**

Before inserting $j$, remove every back index `i` with $P[i]\geq P[j]$. The new index $j$ is later and has a no-larger prefix. For any future endpoint $t$, if $P[t]-P[i]\geq k$, then $P[t]-P[j]\geq k$ as well, and `t - j` is shorter than `t - i`. Thus the older candidate is never preferable.

Every removed front has already contributed its shortest valid subarray, and every removed back is provably dominated. Any start that could belong to an optimal answer remains until its optimal endpoint is examined, so the minimum recorded length is correct.

## Complexity detail
There are $n+1$ prefix indices. Each is appended to the deque once and removed from the front or back at most once, so all deque operations total $O(n)$ time. The deque can retain $O(n)$ prefix-index and prefix-value pairs, giving $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all subarrays:** Accumulating every start-to-end sum is correct but takes $O(n^2)$ time in the worst case.
- **Ordinary sliding window:** Shrinking when the sum reaches `k` is valid for nonnegative arrays, but negative entries can make both extension and contraction non-monotonic.
- **Prefix sums plus binary search:** The raw prefix array is not sorted when negative values occur; extra ordered structures typically raise the cost to $O(n\log n)$.
- **Min-heap of prefix sums:** It can find qualifying starts, but it does not directly prioritize the latest qualifying index needed for the shortest length and costs logarithmic time.
- **Single qualifying element:** Front removals immediately record length `1`, which is globally minimal.
- **No qualifying subarray:** The sentinel best length remains unchanged and the algorithm returns `-1`.
- **Equal prefix sums:** The earlier index is dominated by the later one and must be removed from the back.
- **Large absolute sums:** Prefix totals may exceed 32-bit range, so fixed-width implementations should use a sufficiently wide integer type.
