## Function Contract

**Inputs**

- `nums`: The positive integer values whose positions determine their plus or minus signs.
- `swaps`: Distinct index pairs `[p_i, q_i]` that may be applied any number of times and in any order.

An index is positive in the alternating sum exactly when it is even. Values can move through a sequence of allowed pairs; they are not restricted to one direct listed swap.

**Return value**

Return the greatest alternating sum obtainable after any valid sequence of swaps, including the empty sequence.
