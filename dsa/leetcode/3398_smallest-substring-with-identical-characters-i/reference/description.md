## Description

You are given a binary string `s` of length `n` and an integer `numOps`.

You are allowed to perform the following operation on `s` **at most** `numOps` times:

- Select any index `i` (where $0 \le i < n$) and **flip** $s[i]$. If $s[i] = '1'$, change $s[i]$ to `'0'` and vice versa.

You need to **minimize** the length of the **longest** substring of `s` such that all the characters in the substring are **identical**.

Return the **minimum** length after the operations.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "000001", numOps = 1

**Output:** 2

**Explanation:**

By changing $s[2]$ to `'1'`, `s` becomes `"001001"`. The longest substrings with identical characters are `s[0..1]` and `s[3..4]`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "0000", numOps = 2

**Output:** 1

**Explanation:**

By changing $s[0]$ and $s[2]$ to `'1'`, `s` becomes `"1010"`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "0101", numOps = 0

**Output:** 1

</div>
### Constraints

- $1 \le n = \text{s.length} \le 1000$

- `s` consists only of `'0'` and `'1'`.

- $0 \le numOps \le n$