# Count Substrings Starting and Ending with Given Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3084 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-substrings-starting-and-ending-with-given-character](https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/) |

## Problem Description

### Goal

You are given a lowercase string `s` and a lowercase character `c`. A substring is a nonempty contiguous segment of `s`, identified by a starting index and an ending index with the start not exceeding the end.

Count every substring whose first character and last character are both equal to `c`. A one-character substring qualifies when that character is `c`, because its starting and ending indices are the same. Return the total number of qualifying index intervals; equal substring contents at different positions are counted separately.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters, where $1 \le \lvert s \rvert \le 10^5$.
- `c`: A single lowercase English letter used as both the required starting and ending character.

**Return value**

- The number of contiguous substrings of `s` that start and end with `c`.

### Examples

#### Example 1

- **Input:** `s = "abada", c = "a"`
- **Output:** `6`
- **Explanation:** The three occurrences of `a` form three one-character substrings and three substrings whose endpoints are different occurrences.

#### Example 2

- **Input:** `s = "zzz", c = "z"`
- **Output:** `6`
- **Explanation:** Every nonempty substring qualifies, giving three length-one, two length-two, and one length-three substring.
