## Function Contract

**Inputs**

- `text`: a non-empty lowercase English string to search.
- `words`: a non-empty array of distinct, non-empty lowercase English strings.

Let $N = \lvert\texttt{text}\rvert$, let $W = \lvert\texttt{words}\rvert$, and let

$$
L = \max_{w \in \texttt{words}} \lvert w \rvert.
$$

Each returned pair `[i, j]` uses inclusive zero-based boundaries and therefore represents `text[i:j + 1]`.

**Return value**

- Every pair `[i, j]` whose represented substring is a member of `words`, sorted first by `i` and then by `j`.
