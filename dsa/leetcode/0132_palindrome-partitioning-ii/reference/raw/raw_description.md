## Description

Given a string `s`, partition `s` such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string">palindrome</span>.

Return *the **minimum** cuts needed for a palindrome partitioning of* `s`.

**Example 1:**

```
**Input:** s = "aab"
**Output:** 1
**Explanation:** The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

**Example 2:**

```
**Input:** s = "a"
**Output:** 0
```

**Example 3:**

```
**Input:** s = "ab"
**Output:** 1
```

**Constraints:**

	- `1 <= s.length <= 2000`

	- `s` consists of lowercase English letters only.
