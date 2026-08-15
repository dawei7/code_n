### 1. Description

You are given a string `s` of length `n` consisting of lowercase English letters.

You must perform **exactly** one operation by choosing any integer `k` such that $1 \le k \le n$ and either:

- reverse the **first** `k` characters of `s`, or

- reverse the **last** `k` characters of `s`.

Return the **lexicographically smallest** string that can be obtained after **exactly** one such operation.

### 2. Function Contract

**Inputs**

- `s`: The lowercase string on which one prefix or suffix reversal must be performed.

Both reversal endpoints are inclusive within the selected prefix or suffix. Choosing $k = 1$ is legal and leaves the visible string unchanged, while still satisfying the exactly-one-operation requirement.

**Return value**

Return the smallest result in lexicographic order among all `2n` legal prefix- and suffix-reversal choices.

### 3. Examples

#### Example 1

- **Input:** s = "dcab"

- **Output:** "acdb"

- **Explanation:** 

- Choose $k = 3$, reverse the first 3 characters.

- Reverse `"dca"` to `"acd"`, resulting string `s = "acdb"`, which is the lexicographically smallest string achievable.

#### Example 2

- **Input:** s = "abba"

- **Output:** "aabb"

- **Explanation:** 

- Choose $k = 3$, reverse the last 3 characters.

- Reverse `"bba"` to `"abb"`, so the resulting string is `"aabb"`, which is the lexicographically smallest string achievable.

#### Example 3

- **Input:** s = "zxy"

- **Output:** "xzy"

- **Explanation:** 

- Choose $k = 2$, reverse the first 2 characters.

- Reverse `"zx"` to `"xz"`, so the resulting string is `"xzy"`, which is the lexicographically smallest string achievable.

### 4. Constraints

- $1 \le n = \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters.
