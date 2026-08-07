## Description

Given an array of keywords `words` and a string `s`, make all appearances of all keywords `words[i]` in `s` bold. Any letters between `<b>` and `</b>` tags become bold.

Return `s` *after adding the bold tags*. The returned string should use the least number of tags possible, and the tags should form a valid combination.

**Example 1:**

```
**Input:** words = ["ab","bc"], s = "aabcd"
**Output:** "a**abc**d"
**Explanation:** Note that returning "a**a<b>b**c</b>d" would use more tags, so it is incorrect.
```

**Example 2:**

```
**Input:** words = ["ab","cb"], s = "aabcd"
**Output:** "a**ab**cd"
```

**Constraints:**

	- `1 <= s.length <= 500`

	- `0 <= words.length <= 50`

	- `1 <= words[i].length <= 10`

	- `s` and `words[i]` consist of lowercase English letters.

**Note:** This question is the same as <a href="https://leetcode.com/problems/add-bold-tag-in-string/description/" target="_blank">616. Add Bold Tag in String</a>.
