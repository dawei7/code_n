## General
**Replace the evolving process with fixed ranks**

The smallest value never changes. Every occurrence of the second-smallest distinct value must be reduced once to reach that minimum. Every occurrence of the third-smallest distinct value must be reduced twice: first to the second-smallest level and then to the minimum. More generally, an element requires one operation for each distinct array value smaller than it.

This count is independent of which equal maximum is chosen first. The smallest-index tie rule fixes the order of individual operations, but all copies at a given level eventually cross the same lower levels and therefore contribute the same amount.

**Accumulate contributions in sorted order**

Sort a copy of the array in ascending order. Maintain `smaller_levels`, the number of distinct transitions encountered so far. Whenever the current value differs from the previous sorted value, increment that counter. Add the current counter to the answer for every element.

For `[1,1,2,2,3]`, the sorted contributions are `0, 0, 1, 1, 2`, totaling `4`. These are exactly the level crossings made by the original reduction process. Since every operation moves one element down by exactly one distinct level, summing all required crossings counts every operation once and proves that the accumulated total is correct.

## Complexity detail
Sorting $N$ values takes $O(N\log N)$ time. The subsequent scan visits each position once, adding $O(N)$ time, so the overall bound remains $O(N\log N)$. The sorted copy uses $O(N)$ auxiliary space. The answer can be as large as $\frac{N(N-1)}{2}$ when all values are distinct, so implementations in fixed-width languages need a sufficiently wide integer type.

## Alternatives and edge cases
- **Frequency table:** Because values are bounded, count each value and scan the legal value range, adding `frequency * smaller_levels` at occupied levels. This takes $O(N+V)$ time and $O(V)$ space for value bound $V=5\cdot10^4$.
- **Literal simulation:** Repeatedly finding the largest and next-largest values follows the statement directly but can require $\Theta(N^2)$ operations even before accounting for the searches.
- **All values equal:** No distinct lower level exists and the answer is `0`.
- **Duplicate values:** Every copy contributes separately, but equal copies share the same number of smaller distinct levels.
- **Smallest-index tie rule:** It determines operation order only; it does not change the total number of level crossings.
- **Maximum operation count:** With $N$ distinct values, the answer is $0+1+\cdots+(N-1)$.
