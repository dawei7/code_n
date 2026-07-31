## General

**Fix the middle index without scanning both sides.** For a chosen middle
index $j$, the best valid left item is the greatest profit among earlier items
with price strictly below `prices[j]`. The best right item is defined
symmetrically among later items with a strictly greater price. These choices
are independent once $j$ is fixed, so their two maxima plus `profits[j]`
form the best triplet using that middle.

**Query profit maxima by price.** A Fenwick tree can store the maximum profit
seen at each price rather than a sum. During a left-to-right sweep, query the
prefix ending at `price - 1`; excluding `price` enforces the strict lower
comparison. Record that result for every possible middle, then update the
current price with its profit.

For the reverse sweep, transform a price $p$ to
`P - p + 1`. A larger original price has a smaller transformed index, so a
Fenwick prefix ending just before the current transformed index returns the
best strictly greater-price profit to the right. Whenever both side queries
are nonzero, combine them with the middle profit.

Each recorded side maximum comes from the correct side of $j$ because of its
sweep direction, and from a strictly compatible price because of the excluded
query endpoint. Thus every candidate is valid. Conversely, for any valid
triplet, the two Fenwick queries at its middle are at least as profitable as
its chosen side items, so the algorithm considers a candidate no worse.
Taking the maximum therefore yields the optimum; retaining `-1` means no
middle had both compatible sides.

## Complexity detail

Let $n=\lvert\texttt{prices}\rvert$ and
$P=\max_i\texttt{prices[i]}$. Each Fenwick query or update takes
$O(\log P)$ time, and each item performs a constant number of them, for
$O(n\log P)$ total time. The saved left maxima use $O(n)$ space and a Fenwick
tree uses $O(P)$ space, giving $O(n+P)$ auxiliary space.

## Alternatives and edge cases

- **Quadratic middle scan:** Scanning all earlier and later items for every middle is correct and uses $O(1)$ space, but its $O(n^2)$ time is suitable only for the smaller companion problem.
- **Segment tree:** Range-maximum queries over prices also give $O(n\log P)$ time and $O(P)$ space, with a larger implementation constant.
- **Enumerate every triplet:** Directly checking all index triples takes $O(n^3)$ time.
- **Equal prices:** Queries stop before the current price, so equal-priced items can never fill adjacent roles in the strictly increasing triplet.
- **Index order:** A highly profitable compatible price on the wrong side of the middle cannot be used; sweep direction enforces the index inequalities.
- **No valid triplet:** Positive profits let zero represent a missing side query; if every middle lacks a side, return `-1`.
- **Duplicate price updates:** The Fenwick node retains the greatest profit seen for that price, which is sufficient for every future middle.

