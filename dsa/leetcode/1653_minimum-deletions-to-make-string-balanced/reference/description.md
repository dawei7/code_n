## Description

You are given a string `s` consisting only of characters `'a'` and `'b'`​​​​.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and $s[i] = 'b'$ and $s[j]= 'a'$.

Return *the **minimum** number of deletions needed to make *`s`* **balanced***.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `s = "aababbab"`
- **Output:** `2`
- **Explanation:** You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aa<u>b</u>abb<u>a</u>b" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aab<u>a</u>bb<u>a</u>b" -> "aabbbb").
#### Example 2

- **Input:** `s = "bbaaaaabb"`
- **Output:** `2`
- **Explanation:** The only solution is to delete the first two characters.
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is `'a'` or `'b'`​​.