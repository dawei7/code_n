## Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.
- `x`: The lowercase letter that must follow every occurrence of `y` in the result.
- `y`: The lowercase letter that must precede every occurrence of `x` in the result.

The two distinguished letters are different. Let $n=\lvert\texttt{s}\rvert$.

**Return value**

Return any permutation `t` of `s` for which the last occurrence of `y` is before the first occurrence of `x` whenever both letters occur. If either letter is absent, every permutation automatically satisfies the relative-order condition.
