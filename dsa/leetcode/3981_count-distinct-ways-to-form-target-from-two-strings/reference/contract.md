## Function Contract

`solve(word1, word2, target) -> int`

Let $n = \lvert\texttt{word1}\rvert$, $m = \lvert\texttt{word2}\rvert$, and $t = \lvert\texttt{target}\rvert$. Define the state-volume measure

$$
P = tnm.
$$

**Inputs**

- `word1`: The first lowercase source string.
- `word2`: The second lowercase source string.
- `target`: The lowercase string to form by ordered selections.

The selected indices must increase separately within each source. There is no ordering comparison between an index in `word1` and an index in `word2`.

**Output**

Return, modulo $10^9+7$, the number of distinct constructions that use at least one character from each source word.
