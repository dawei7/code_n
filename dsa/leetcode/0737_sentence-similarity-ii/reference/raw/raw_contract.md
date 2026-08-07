## Function Contract

`solve(sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool`

Let $n$ be the common sentence length when the two lengths match, let $p = \lvert\texttt{similarPairs}\rvert$, and let $w$ be the number of distinct words appearing in those pairs.

**Inputs**

- `sentence1`: the first nonempty ordered array of words.
- `sentence2`: the second nonempty ordered array of words.
- `similarPairs`: two-word relationships whose undirected, transitive connections form similarity groups.

**Return value**

Return `True` exactly when the sentences have the same length and every pair of words at a matching position is either identical or belongs to the same similarity group. Otherwise, return `False`.
