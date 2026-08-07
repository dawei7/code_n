## Function Contract

`solve(nums: list[int], sequences: list[list[int]]) -> bool`

### Inputs

- `nums`: A permutation of the integers in the inclusive range $[1,n]$.
- `sequences`: A nonempty collection of distinct, nonempty subsequences of `nums`.

Let $n = \lvert\texttt{nums}\rvert$, and let

$$
S = \sum_i \lvert\texttt{sequences}[i]\rvert.
$$

### Output

Return `true` if `nums` is the only shortest sequence that contains every row of `sequences` as a subsequence. Return `false` if `nums` is not shortest or if another shortest supersequence exists.
