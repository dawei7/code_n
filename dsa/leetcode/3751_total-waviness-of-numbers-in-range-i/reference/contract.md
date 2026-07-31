## Function Contract

**Inputs**

- `num1`: The inclusive lower endpoint of the integer range.
- `num2`: The inclusive upper endpoint of the integer range.

Let $R=\texttt{num2}-\texttt{num1}+1$ be the number of values in the range, and let $D$ be the maximum decimal digit count among them. Both peak and valley comparisons are strict, so an interior digit equal to either neighbor is not counted.

**Return value**

Return the sum of the peak-and-valley counts of all $R$ integers.
