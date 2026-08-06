## Function Contract

`solve(s1: str, s2: str) -> str`

Let $n = \lvert\texttt{s1}\rvert$ and $m = \lvert\texttt{s2}\rvert$.

**Inputs**

- `s1`: the nonempty source string from which one contiguous window is selected.
- `s2`: the nonempty target string whose characters must occur in order as a subsequence of that window.

**Return value**

Return the shortest qualifying substring of `s1`. On a length tie, return the window with the left-most starting index. Return `""` if no qualifying window exists.
