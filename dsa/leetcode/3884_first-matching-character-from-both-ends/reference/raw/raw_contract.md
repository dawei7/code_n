## Function Contract

**Inputs**

- `s`: A non-empty string of lowercase English letters.

Let $n=\lvert\texttt{s}\rvert$. The mirror of an index $i$ is $m(i)=n-i-1$, so valid indices are tested against pairs `s[i]` and `s[m(i)]`.

**Return value**

Return the minimum index $i$ for which `s[i] == s[n - i - 1]`. Return `-1` when no such index exists.
