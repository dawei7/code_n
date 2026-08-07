## Description

Given a list of strings `dict` where all the strings are of the same length.

Return `true` if there are 2 strings that only differ by 1 character in the same index, otherwise return `false`.

**Example 1:**

```
**Input:** dict = ["abcd","acbd", "aacd"]
**Output:** true
**Explanation:** Strings "a**b**cd" and "a**a**cd" differ only by one character in the index 1.
```

**Example 2:**

```
**Input:** dict = ["ab","cd","yz"]
**Output:** false
```

**Example 3:**

```
**Input:** dict = ["abcd","cccc","abyd","abab"]
**Output:** true
```

**Constraints:**

	- The number of characters in `dict <= 10^5`

	- `dict[i].length == dict[j].length`

	- `dict[i]` should be unique.

	- `dict[i]` contains only lowercase English letters.
