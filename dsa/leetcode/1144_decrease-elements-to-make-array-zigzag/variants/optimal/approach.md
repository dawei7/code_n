## General
**Choose which parity contains the valleys.** Each valid zigzag form is completely determined by whether even indices or odd indices must be strictly smaller than their neighbors. Evaluate both choices and take the smaller cost.

**Lower each selected position only as far as necessary.** For a selected valley at index `i`, let $b_i$ be the smaller existing value among its available neighbors. The valley must end below $b_i$. If `nums[i] < b_i`, it costs nothing; otherwise it needs exactly `nums[i] - b_i + 1` decrements. A missing neighbor at an endpoint imposes no restriction.

**Why the local costs are independent.** Selected valley indices differ by two, so no two selected positions are adjacent. Their neighboring peak values therefore remain unchanged while calculating a fixed parity. Lowering a selected value to one below its smaller neighbor is both sufficient for its two strict comparisons and necessary because values can only decrease. Summing these forced minima gives the optimum for that parity, and the minimum of the two parity totals gives the global optimum.

## Complexity detail
Each index is inspected a constant number of times across the two parity choices, so the running time is $O(n)$. The two accumulated costs and a few temporary values use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Unit-by-unit simulation:** Repeatedly decrementing a valley until it becomes small enough is correct, but its time depends on the magnitudes of the values rather than only on $n$.
- **Modify a copied array:** Building each candidate zigzag explicitly is unnecessary because selected valleys are nonadjacent; direct cost calculation avoids $O(n)$ extra space.
- **Single element:** An array of length one satisfies both comparison patterns vacuously, so the answer is `0`.
- **Equal neighbors:** Strict inequalities require at least one decrement; equality is not already zigzag.
- **Endpoints:** The first and last elements compare with only their one existing neighbor.
- **Negative final values:** Repeated decrements may lower an element below zero, which is permitted because the constraints describe only the input values.
