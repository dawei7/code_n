## Description

Given a string `s` and an integer `k`, return the total number of substrings of `s` where **at least one** character appears **at least** `k` times.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "abacb", k = 2

**Output:** 4

**Explanation:**

The valid substrings are:

- "`aba"` (character `'a'` appears 2 times).

- `"abac"` (character `'a'` appears 2 times).

- `"abacb"` (character `'a'` appears 2 times).

- `"bacb"` (character `'b'` appears 2 times).

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abcde", k = 1

**Output:** 15

**Explanation:**

All substrings are valid because every character appears at least once.

</div>
### Constraints

- $1 \le \text{s.length} \le 3 * 10^{5}$

- $1 \le k \le \text{s.length}$

- `s` consists only of lowercase English letters.