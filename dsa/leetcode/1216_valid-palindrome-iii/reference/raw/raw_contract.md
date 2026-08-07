## Function Contract

**Inputs**

- `s`: The string to test.
- `k`: The maximum number of characters that may be removed.

Let $n = \lvert\texttt{s}\rvert$. Removing characters retains a subsequence of `s`; the retained characters cannot be reordered.

**Return value**

Return `true` if some palindromic subsequence of `s` has length at least $n-k$. Otherwise, return `false`.
