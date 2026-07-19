# Positions of Large Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 830 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/positions-of-large-groups/) |

## Problem Description

### Goal

In a lowercase English string `s`, equal consecutive letters form groups. Each group is maximal: it begins either at index `0` or immediately after a different letter, and it ends either at the last index or immediately before a different letter. Represent a group by its inclusive zero-based interval `[start, end]`.

A group is large when it contains at least three characters. Return the intervals of all large groups in increasing order of `start`. Report each maximal group once; a longer run does not also contribute its shorter length-three subranges.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 1000$
- Let $g$ be the number of large groups in `s`.

**Return value**

- A list of inclusive intervals `[start, end]`, one for each large maximal group, ordered by increasing `start`

### Examples

**Example 1**

- Input: `s = "abbxxxxzzy"`
- Output: `[[3, 6]]`
- Explanation: `"xxxx"` is the only group whose length is at least three.

**Example 2**

- Input: `s = "abc"`
- Output: `[]`
- Explanation: Each group has length one.

**Example 3**

- Input: `s = "abcdddeeeeaabbbcd"`
- Output: `[[3, 5], [6, 9], [12, 14]]`
- Explanation: The large groups are `"ddd"`, `"eeee"`, and `"bbb"`.
