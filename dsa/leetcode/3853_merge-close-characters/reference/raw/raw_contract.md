## Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters.
- `k`: The maximum allowed distance between the current indices of two equal characters that may merge.

At any stage, a pair of indices $i<j$ is eligible exactly when `s[i] == s[j]` and

$$
j-i\le\texttt{k}.
$$

The chosen eligible pair minimizes $i$ first and $j$ second. Its right character at index $j$ is deleted, its left character at index $i$ remains, and all later indices are recomputed in the shortened string before selecting another pair.

**Return value**

Return the stable string in which no equal characters have current-index distance at most `k`.
