# Find the Longest Semi-Repetitive Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2730 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/) |

## Problem Description

### Goal

Given a string of decimal digits, find the greatest length of a contiguous substring that contains at most one adjacent pair of equal digits.

Every adjacent position is considered separately. Thus `"0010"` is semi-repetitive because only its first two digits form an equal pair, while `"00101022"` is not because it contains both `00` and `22`. Overlapping pairs also count separately: `"111"` contains two equal adjacent pairs, one at each boundary between consecutive characters.

### Function Contract

**Inputs**

- `s`: A digit string with $1 \le \lvert s \rvert \le 50$ and characters from `0` through `9`.

**Return value**

Return the length of the longest substring of `s` containing at most one index $i$ for which `s[i] == s[i - 1]`.

### Examples

#### Example 1

- **Input:** `s = "52233"`
- **Output:** `4`
- **Explanation:** `"5223"` has the single equal pair `22`; including the final `3` would add the pair `33`.

#### Example 2

- **Input:** `s = "5494"`
- **Output:** `4`
- **Explanation:** The whole string has no equal adjacent pair, so it is semi-repetitive.

#### Example 3

- **Input:** `s = "1111111"`
- **Output:** `2`
- **Explanation:** Any two adjacent characters form one allowed pair, whereas any three contain two overlapping pairs.
