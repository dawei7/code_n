## Description

Given strings `s1` and `s2`, return *the minimum contiguous substring part of *`s1`*, so that *`s2`* is a subsequence of the part*.

If there is no such window in `s1` that covers all characters in `s2`, return the empty string `""`. If there are multiple such minimum-length windows, return the one with the **left-most starting index**.
### Function Contract

`solve(s1: str, s2: str) -> str`

Let $n = \lvert\texttt{s1}\rvert$ and $m = \lvert\texttt{s2}\rvert$.

**Inputs**

- `s1`: the nonempty source string from which one contiguous window is selected.
- `s2`: the nonempty target string whose characters must occur in order as a subsequence of that window.

**Return value**

Return the shortest qualifying substring of `s1`. On a length tie, return the window with the left-most starting index. Return `""` if no qualifying window exists.

### Examples
#### Example 1

- **Input:** $s1 = "abcdebdde", s2 = "bde"$
- **Output:** `"bcde"`
- **Explanation:**
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.
#### Example 2

- **Input:** $s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"$
- **Output:** `""`
### Constraints

- $1 \le \text{s1.length} \le 2 * 10^{4}$

- $1 \le \text{s2.length} \le 100$

- `s1` and `s2` consist of lowercase English letters.