## General

**Fix the middle item.** Every valid triplet has one index $j$ between its other two indices. Once $j$ is fixed, the left and right choices become independent: the left item only needs an index below $j$ and a price below `prices[j]`, while the right item only needs an index above $j$ and a price above `prices[j]`.

**Keep only each side's best compatible profit.** Scan all earlier indices to find the maximum `profits[i]` among items with `prices[i] < prices[j]`. Separately scan all later indices for the maximum `profits[k]` among items with `prices[j] < prices[k]`. If both maxima exist, combining them with `profits[j]` is the best valid triplet whose middle index is $j$.

This combination is valid because its indices have the required order by construction, and both strict price comparisons were checked. It is optimal for this particular $j$ because replacing either side maximum with another compatible item cannot increase the sum. Every globally valid triplet has some middle index considered by the outer loop, so taking the largest candidate over all middle indices yields the overall maximum. If no middle admits both sides, no valid triplet exists and the answer remains `-1`.

## Complexity detail

Let $n=\lvert\texttt{prices}\rvert=\lvert\texttt{profits}\rvert$. For each of $O(n)$ possible middle indices, the two side scans inspect $O(n)$ items, giving $O(n^2)$ time. The scan stores only a few indices, maxima, and the answer, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every triplet:** Checking all $\binom{n}{3}$ index triples is straightforward and correct, but takes $O(n^3)$ time instead of exploiting the independence of the two sides.
- **Fenwick tree or segment tree:** After coordinate-compressing prices, prefix and suffix maximum queries can reduce the running time to $O(n\log n)$ with $O(n)$ space. That stronger method is useful for the larger companion problem but is unnecessary for the $n\le 2000$ bound here.
- **Equal prices:** Price comparisons are strict. Items with a price equal to the middle price cannot be used on either side.
- **Profitable but misplaced item:** A very profitable item contributes nothing if its index or price cannot fit its assigned side of the middle.
- **No compatible middle:** Return `-1` even if an increasing pair exists; the contract requires exactly three items.
- **Positive profits:** All profits are positive, so a side maximum can use `-1` as a clear missing-value sentinel.

