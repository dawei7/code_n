## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integer score values.
- `s`: A binary string with the same length as `nums`.

Let $N=\lvert\texttt{nums}\rvert=\lvert s\rvert$. Swaps change only the positions of the characters in `s`; they do not reorder `nums`, change the number of ones, or allow a one to move rightward across a zero.

**Return value**

Return the maximum sum of `nums[i]` over positions that can contain `'1'` after any number of legal `"01" -> "10"` swaps, including no swaps.
