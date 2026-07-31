## General

**Identify the values that cannot remain.** The final condition fails exactly for elements strictly smaller than `k`. Because each operation removes the current minimum, every such element must be removed before the minimum can reach `k`. Values equal to `k` already satisfy the inclusive threshold and must not be counted.

**Count instead of simulating.** Scan `nums` once and add one for each value below `k`. No ordering structure is needed: any value below the threshold is smaller than every qualifying value only in the threshold sense that matters, and all of them inevitably disappear.

Let $c$ be the count produced by the scan. Fewer than $c$ operations leave at least one of those $c$ sub-threshold occurrences in the array, so the goal is not yet met. After exactly $c$ smallest-element removals, every sub-threshold occurrence is gone; the input guarantee leaves at least one value at least `k`, and every remaining value qualifies. Thus $c$ is both necessary and sufficient and is the minimum.

## Complexity detail

Let $n$ be the length of `nums`. The method performs one comparison per element, so its time complexity is $O(n)$. It stores only the running count, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort the array:** The first index whose value is at least `k` equals the answer, but sorting costs $O(n \log n)$ time and may mutate the input.
- **Minimum heap simulation:** Repeatedly popping values models the stated operation directly, but heap construction and removals add unnecessary overhead.
- **Repeated minimum search:** Finding and deleting the smallest element with full scans can take $O(n^2)$ time.
- **Inclusive boundary:** A value equal to `k` already satisfies the condition and contributes no operation.
- **No operations:** When every element is at least `k`, the answer is zero.
- **Only one qualifying value:** All other $n-1$ values are removed, and the guaranteed qualifying value remains.
- **Input order:** The count depends only on comparisons with `k`, not on where small values appear.
