## Function Contract

**Inputs**

- `s`: A non-empty string containing only decimal digits.

Let $N=\lvert\texttt{s}\rvert$, and let $D$ be the greatest number of decimal digits in an index from $0$ through $N-1$. The decimal representation of an index uses no leading zero, except that zero itself is represented by `"0"`.

A qualifying substring must be contiguous and must end at the index it represents. Because equality requires the same length, each index has exactly one candidate substring to test: the suffix of `s[0..i]` whose length is the number of digits in `i`.

**Return value**

Return an integer array containing precisely the good indices in increasing order.
