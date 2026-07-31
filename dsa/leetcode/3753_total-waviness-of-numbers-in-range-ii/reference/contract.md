## Function Contract

**Inputs**

- `num1`: The inclusive lower endpoint of the integer range.
- `num2`: The inclusive upper endpoint of the integer range.

Let $D$ be the maximum decimal digit count of either endpoint. Both peak and valley comparisons are strict, so an interior digit equal to either neighbor is not counted. The range may be far too large to enumerate.

**Return value**

Return the sum of the peak-and-valley counts of all integers from `num1` through `num2`, inclusive.
