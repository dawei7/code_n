## Function Contract

`solve(sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool`

Let $n$ be the common sentence length when the two lengths match, and let $p = \lvert\texttt{similarPairs}\rvert$.

**Inputs**

- `sentence1`: the first nonempty ordered array of words.
- `sentence2`: the second nonempty ordered array of words.
- `similarPairs`: distinct two-word pairs that declare direct similarity.

**Return value**

Return `True` exactly when the sentences have the same length and every pair of words at a matching position is either identical or directly similar in either listed orientation. Otherwise, return `False`.
