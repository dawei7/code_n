## Function Contract

**Inputs**

- `s`: a nonempty pattern whose characters are `"I"` or `"D"`

**Return value**

- Return the lexicographically smallest permutation of the integers from $1$ through $\lvert \texttt{s} \rvert + 1$
  whose adjacent comparisons match `s`.

The result has length $\lvert \texttt{s} \rvert + 1$ and uses every integer in that range exactly once.
