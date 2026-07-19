## General
**Change the frame of reference**

Incrementing every element except one raises the shared baseline by one while leaving that excluded element one unit lower relative to the others. Subtracting that common increment from all elements shows the move is equivalent, for equality purposes, to decrementing exactly the excluded element by one.

**The minimum value is the only reachable target that avoids waste**

Under the equivalent operation, values only decrease. Every element must therefore meet at or below the original minimum. Choosing a lower target adds the same unnecessary distance for all `n` elements, so an optimum makes every value equal to the original minimum.

**Sum independent distances**

If `m` is the minimum, an element `x` needs exactly $x - m$ equivalent decrements. Each move affects one relative element, so these requirements add without overlap. The answer is `sum(nums) - n * m`, which is both achievable by performing those decrements and necessary because every excess unit must be removed.

## Complexity detail
One scan can accumulate the sum and minimum, giving $O(n)$ time. Only those aggregate values are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sort then compare with the minimum:** computes the same distances but costs $O(n \log n)$ time and may mutate the input.
- **Simulate original moves:** is easy to visualize but can require an enormous number of updates unrelated to the input length.
- **Search every value for the minimum:** redundant pairwise comparisons can turn a linear task into $O(n^2)$.
- **Already equal values:** every distance is zero, so no move is required.
- **Negative values:** differences from the minimum remain nonnegative and the same formula applies.
- **One element:** incrementing zero other elements is unnecessary; the answer is zero.
- **Large magnitudes:** use an integer type wide enough for the sum and product in fixed-width languages.
