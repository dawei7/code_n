## Description

You are given a string `s` of length `n` consisting of lowercase English letters.

You must perform **exactly** one operation by choosing any integer `k` such that $1 \le k \le n$ and either:

- reverse the **first** `k` characters of `s`, or

- reverse the **last** `k` characters of `s`.

Return the **lexicographically smallest** string that can be obtained after **exactly** one such operation.
### Function Contract

**Inputs**

- `s`: The lowercase string whose prefix or suffix must be reversed once.

The chosen segment must touch the first or last character and may have any length from `1` through `s.length`. Choosing $k = 1$ is a valid operation and leaves the string unchanged.

**Return value**

Return the smallest string in lexicographic order among every legal prefix reversal and suffix reversal.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "dcab"

**Output:** "acdb"

**Explanation:**

- Choose $k = 3$, reverse the first 3 characters.

- Reverse `"dca"` to `"acd"`, resulting string `s = "acdb"`, which is the lexicographically smallest string achievable.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abba"

**Output:** "aabb"

**Explanation:**

- Choose $k = 3$, reverse the last 3 characters.

- Reverse `"bba"` to `"abb"`, so the resulting string is `"aabb"`, which is the lexicographically smallest string achievable.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "zxy"

**Output:** "xzy"

**Explanation:**

- Choose $k = 2$, reverse the first 2 characters.

- Reverse `"zx"` to `"xz"`, so the resulting string is `"xzy"`, which is the lexicographically smallest string achievable.

</div>
### Constraints

- $1 \le n = \text{s.length} \le 1000$

- `s` consists of lowercase English letters.