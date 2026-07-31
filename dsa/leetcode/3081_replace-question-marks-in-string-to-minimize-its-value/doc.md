# Replace Question Marks in String to Minimize Its Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3081 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/) |

## Problem Description

### Goal

You are given a string `s` whose characters are lowercase English letters or question marks.

For a completed lowercase string $t$, define `cost(i)` as the number of positions before $i$ that contain the same character as `t[i]`. The value of $t$ is the sum of `cost(i)` over every index. For example, the value of `"aab"` is $0 + 1 + 0 = 1$.

Replace every `?` in `s` with a lowercase English letter so that the completed string has the minimum possible value. If several completions have that minimum value, return the lexicographically smallest one.

### Function Contract

**Inputs**

- `s`: A string containing only lowercase English letters and `?` characters.

The length satisfies $1 \leq \lvert s \rvert \leq 10^5$.

**Return value**

- The lexicographically smallest completed string among all replacements having minimum value.

### Examples

**Example 1**

- Input: `s = "???"`
- Output: `"abc"`
- Explanation: Three distinct letters give value zero, and `"abc"` is the lexicographically smallest such completion.

**Example 2**

- Input: `s = "a?a?"`
- Output: `"abac"`
- Explanation: The completed letter counts give value one, which is minimal; assigning the selected letters in sorted order produces the smallest string.
