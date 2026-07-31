## Function Contract

`solve(nums) -> int`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: A nonempty array of positive integers from which Alice must choose one inclusive range.

Alice also chooses an integer $k>1$. Within her selected range, each multiple of $k$ contributes positively to the difference and each nonmultiple contributes negatively. The range may contain one element.

**Output**

Return `(maximum score difference * smallest maximizing k) mod 1_000_000_007`. The maximum difference can be negative, but the returned residue is in the usual nonnegative modulo range.
