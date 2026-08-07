## Description

You are given a string `text`. You should split it to k substrings $(\text{subtext}_{1}, \text{subtext}_{2}, ..., \text{subtext}_{k})$ such that:

- $\text{subtext}_{i}$ is a **non-empty** string.

- The concatenation of all the substrings is equal to `text` (i.e., $\text{subtext}_{1} + \text{subtext}_{2} + ... + \text{subtext}_{k} = text$).

- $\text{subtext}_{i} = \text{subtext}_{k} - i + 1$ for all valid values of `i` (i.e., $1 \le i \le k$).

Return the largest possible value of `k`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $text = "ghiabcdefhelloadamhelloabcdefghi"$
- **Output:** `7`
- **Explanation:** We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
#### Example 2

- **Input:** $text = "merchant"$
- **Output:** `1`
- **Explanation:** We can split the string on "(merchant)".
#### Example 3

- **Input:** $text = "antaprezatepzapreanta"$
- **Output:** `11`
- **Explanation:** We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".
### Constraints

- $1 \le \text{text.length} \le 1000$

- `text` consists only of lowercase English characters.