## Function Contract

`solve(s, t) -> bool`

Let $n = \lvert\texttt{s}\rvert$ and $m = \lvert\texttt{t}\rvert$.

**Inputs**

- `s`: The lowercase string that may have at most one character replaced.
- `t`: The lowercase string in which the resulting `s` must appear as a subsequence.

A replacement changes one chosen position of `s` to any lowercase English letter. It is legal to perform no replacement.

**Output**

Return `true` if an allowed version of `s` is a subsequence of `t`; otherwise, return `false`.
