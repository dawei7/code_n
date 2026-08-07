## Function Contract

**Inputs**

- `phrases`: The list of lowercase, single-space-separated phrases from which ordered pairs are chosen.

Define the total input character count as

$$
S = \sum_{x \in \texttt{phrases}} \lvert x \rvert.
$$

Let $G$ be the total number of characters across all compatible merged candidates before duplicate strings are removed, and let $R$ be the number of distinct returned puzzles.

**Return value**

- Return the distinct valid merges as a lexicographically sorted list of strings. A phrase may not be paired with itself at the same index, even when its first and last words match.
