## General

Choose the middle index $j$ first. Once `nums[j]` is fixed, both outer positions must contain the single target value `2 * nums[j]`. If that target occurs $L$ times before $j$ and $R$ times after $j$, then this middle index contributes exactly $L\cdot R$ triplets: every left occurrence can be paired independently with every right occurrence.

Maintain two frequency maps while scanning from left to right. `right` initially counts the complete array and `left` is empty. At the start of an iteration, remove the current value from `right`; it then represents precisely the eligible indices $k>j$, which is especially important when the current value is zero. Meanwhile, `left` contains precisely the indices $i<j$ because the current value has not yet been inserted there.

Look up the target in both maps, add the product of the two counts, and finally insert the current value into `left`. Thus each product counts every valid triplet with middle index $j$ exactly once. No invalid index order is possible because the two maps contain only positions on their designated sides. Taking the running sum modulo $10^9+7$ preserves the required final residue.

## Complexity detail

Let $n$ be the array length and let $U$ be the number of distinct values. Building the right frequency map and processing all middle indices take $O(n)$ expected time with hash-map operations. The two maps store at most $U\le n$ keys, so auxiliary space is $O(n)$.

The benchmark defines $S=n$ and uses all-zero arrays. Every possible index triple is valid, which exercises large counts and modular reduction while forcing a correct pair-enumeration alternative to inspect $\Theta(S^2)$ outer-index pairs. The accepted frequency method performs one pass and remains $O(S)$.

## Alternatives and edge cases

- **Enumerate every index triplet:** Directly testing all $(i,j,k)$ choices is simple but costs $O(n^3)$ time.
- **Enumerate outer pairs:** For each pair $i<k$ with equal values, scanning or counting eligible middle indices still costs $O(n^2)$ without incremental frequencies.
- **Prefix and suffix tables:** Materializing a frequency map for every boundary supports the same contribution formula, but consumes much more than the two rolling maps.
- **Bounded frequency arrays:** Since values are bounded, arrays can replace hash maps; they give deterministic constant-time access but allocate storage for the whole value domain.
- **Zero:** Because $2\cdot0=0$, the current zero must be removed from `right` before its contribution is calculated, or the same index could be counted as both $j$ and $k$.
- **Repeated values:** Counts, rather than mere membership, are required because each distinct index choice contributes separately.
- **Index order:** Equal target values only on one side of a middle index cannot form a special triplet.
- **Modulo:** Reduce the accumulating answer as contributions are added because the unmodded number of triplets can be large.
