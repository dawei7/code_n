## General

For a proposed common value $x$, index `i` contributes $\lvert\texttt{nums[i]}-x\rvert\texttt{cost[i]}$. Thus each `cost[i]` acts as the weight of its corresponding value, and the objective is a sum of weighted absolute distances.

Sort `(value, weight)` pairs by value and let $W$ be the total weight. Move from left to right while accumulating weight. Choose the first value whose inclusive prefix weight is at least $W/2$; this is a weighted median.

To see why it is optimal, consider moving a target one unit to the right between consecutive sorted values. The contribution from weight strictly to the left increases by that weight, while the contribution from weight strictly to the right decreases by that weight. Before half of the total weight has been reached, moving right cannot increase the objective; after half has been reached, moving farther right cannot decrease it. The selected weighted median is therefore at a minimum of this convex, piecewise-linear cost function.

Finally, sum the weighted distance from every original value to the selected target. Choosing the first crossing also handles an exact half-weight split: every integer between the two central weighted values has the same minimum, so the chosen existing value is valid.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Sorting the paired values takes $O(n\log n)$ time. The weighted-median scan and final cost calculation each take $O(n)$ time, so the total is $O(n\log n)$.

The sorted list contains $n$ pairs and uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Binary search on the convex objective:** Comparing the cost at adjacent targets locates a minimum in $O(n\log V)$ time, where $V=\max(\texttt{nums})-\min(\texttt{nums})+1$; it avoids sorting but repeatedly scans the array.
- **Evaluate every distinct input value:** The optimum can be chosen from `nums`, but evaluating all candidates independently takes $O(n^2)$ time when all values differ.
- **Prefix and suffix weighted sums:** After sorting, costs for every distinct target can be updated or calculated from prefix aggregates in $O(n\log n)$ total time, matching the asymptotic bound with more bookkeeping.
- **Already equal values:** The weighted median is that shared value and the answer is zero.
- **Single element:** No operation is required, regardless of its weight.
- **Dominant weight:** A single index carrying at least half of the total weight can force its value to be an optimal target even when most positions contain another value.
- **Even weight split:** More than one target can attain the same minimum; returning the cost at either weighted median remains correct.
- **Large products:** The result can exceed 32-bit integer range, so the calculation must use sufficiently wide integer arithmetic.
