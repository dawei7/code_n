## Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

For every prefix length $k$ from $1$ through $\lvert\texttt{s}\rvert$, compare the number of distinct letters among `s[0:k]` with $k \bmod 3$.

**Return value**

Return an integer equal to the number of prefix lengths for which those two values are equal.
