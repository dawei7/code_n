## Function Contract

**Inputs**

- `s`: One or more lowercase words with exactly one space between adjacent words.
- `k`: A valid zero-based index into the conceptual expanded string `t`.

Character positions restart at `1` after every separator. A separator itself contributes exactly one character to `t` and is not part of either neighboring word.

Let $n=\lvert\texttt{s}\rvert$ for the complexity bounds.

**Return value**

Return the one-character string `t[k]` without requiring `t` to be materialized.
