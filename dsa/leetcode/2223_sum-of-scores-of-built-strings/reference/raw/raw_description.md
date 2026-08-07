## Description

You are **building** a string `s` of length `n` **one** character at a time, **prepending** each new character to the **front** of the string. The strings are labeled from `1` to `n`, where the string with length `i` is labeled `s_i`.

	- For example, for `s = "abaca"`, `s_1 == "a"`, `s_2 == "ca"`, `s_3 == "aca"`, etc.

The **score** of `s_i` is the length of the **longest common prefix** between `s_i` and `s_n` (Note that `s == s_n`).

Given the final string `s`, return* the **sum** of the **score** of every *`s_i`.

**Example 1:**

```
**Input:** s = "babab"
**Output:** 9
**Explanation:**
For s_1 == "b", the longest common prefix is "b" which has a score of 1.
For s_2 == "ab", there is no common prefix so the score is 0.
For s_3 == "bab", the longest common prefix is "bab" which has a score of 3.
For s_4 == "abab", there is no common prefix so the score is 0.
For s_5 == "babab", the longest common prefix is "babab" which has a score of 5.
The sum of the scores is 1 + 0 + 3 + 0 + 5 = 9, so we return 9.
```

**Example 2:**

```
**Input:** s = "azbazbzaz"
**Output:** 14
**Explanation:**
For s_2 == "az", the longest common prefix is "az" which has a score of 2.
For s_6 == "azbzaz", the longest common prefix is "azb" which has a score of 3.
For s_9 == "azbazbzaz", the longest common prefix is "azbazbzaz" which has a score of 9.
For all other s_i, the score is 0.
The sum of the scores is 2 + 3 + 9 = 14, so we return 14.
```

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.
