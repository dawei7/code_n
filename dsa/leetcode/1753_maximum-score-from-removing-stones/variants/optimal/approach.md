## General
**Bound the score by total stone supply**

Every point consumes exactly two stones, so $S$ stones can support at most $\lfloor S/2\rfloor$ moves. This limit is decisive when the piles are balanced enough to keep forming cross-pile pairs until at most one stone remains.

**Bound the score by stones outside the largest pile**

No move can take two stones from the same pile. Consequently, every move that consumes a stone from the largest pile needs a partner outside it, and moves between the two smaller piles consume that outside supply even faster. The score can never exceed $S-M$, the total number of stones outside the largest pile.

**Take the smaller bound**

If $M>S-M$, pair every outside stone with the largest pile and attain exactly $S-M$ moves before only the largest pile remains. Otherwise, the largest pile does not dominate the combined remainder; repeatedly pairing two currently nonempty piles can consume all stones except possibly one and attain $\lfloor S/2\rfloor$. Both upper bounds are therefore tight, so the answer is

$$
\min\left(\left\lfloor\frac{S}{2}\right\rfloor,\ S-M\right).
$$

## Complexity detail
Computing one sum, one maximum, and the minimum of two arithmetic bounds takes $O(1)$ time. Only a fixed number of integer values is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Max-heap simulation:** Repeatedly remove from the two largest nonempty piles. This greedy process is correct, but takes time proportional to the returned score instead of constant time.
- **Case analysis after sorting:** Sorting three values and comparing the largest with the other two derives the same formula; sorting a fixed three-element collection is still $O(1)$.
- **Dominant pile:** When one pile exceeds the sum of the other two, unused stones necessarily remain in that pile.
- **Balanced piles:** If the largest pile is no larger than the combined remainder, all but at most one stone can be consumed.
- **Odd total:** The total-stone bound rounds down because each move consumes two stones.
- **Equal piles:** The result is determined by $\lfloor S/2\rfloor$.
- **Permutation symmetry:** Reordering `a`, `b`, and `c` cannot change the answer.
- **Maximum pile value:** Arithmetic must comfortably represent totals up to $3\cdot10^5$.
