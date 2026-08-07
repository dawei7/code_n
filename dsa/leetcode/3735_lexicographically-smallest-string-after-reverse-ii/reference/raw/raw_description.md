## Description

You are given a string `s` of length `n` consisting of lowercase English letters.

You must perform **exactly** one operation by choosing any integer `k` such that `1 <= k <= n` and either:

	- reverse the **first** `k` characters of `s`, or

	- reverse the **last** `k` characters of `s`.

Return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** string that can be obtained after **exactly** one such operation.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "dcab"</span>

**Output:** <span class="example-io">"acdb"</span>

**Explanation:**

	- Choose `k = 3`, reverse the first 3 characters.

	- Reverse `"dca"` to `"acd"`, resulting string `s = "acdb"`, which is the lexicographically smallest string achievable.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abba"</span>

**Output:** <span class="example-io">"aabb"</span>

**Explanation:**

	- Choose `k = 3`, reverse the last 3 characters.

	- Reverse `"bba"` to `"abb"`, so the resulting string is `"aabb"`, which is the lexicographically smallest string achievable.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "zxy"</span>

**Output:** <span class="example-io">"xzy"</span>

**Explanation:**

	- Choose `k = 2`, reverse the first 2 characters.

	- Reverse `"zx"` to `"xz"`, so the resulting string is `"xzy"`, which is the lexicographically smallest string achievable.

</div>

**Constraints:**

	- `1 <= n == s.length <= 10^5`

	- `s` consists of lowercase English letters.
