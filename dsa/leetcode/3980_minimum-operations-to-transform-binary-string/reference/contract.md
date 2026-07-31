## Function Contract

`solve(s1, s2) -> int`

Let $n = \lvert\texttt{s1}\rvert = \lvert\texttt{s2}\rvert$.

**Inputs**

- `s1`: The initial binary string that operations modify conceptually.
- `s2`: The binary target string of the same length.

The input strings contain only `'0'` and `'1'`. The function need not mutate either string object.

**Output**

Return the minimum number of legal operations needed to transform `s1` into `s2`. Return `-1` if no sequence of the permitted operations reaches the target.
