# Minimum String Length After Removing Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2696 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/) |

## Problem Description

### Goal

Given a string `s` containing only uppercase English letters, repeatedly remove occurrences of either `"AB"` or `"CD"`. Each operation may choose any current occurrence of one of those two substrings.

After a removal, the characters on its left and right become adjacent. That concatenation can create a new removable occurrence that did not exist before, so the process may continue through several newly exposed pairs.

Return the minimum length obtainable after performing any number of valid removals.

### Function Contract

**Inputs**

- `s`: A string of uppercase English letters with $1 \leq \lvert s \rvert \leq 100$.

**Return value**

Return an integer equal to the smallest possible length after removing any sequence of `"AB"` and `"CD"` occurrences.

### Examples

#### Example 1

- **Input:** `s = "ABFCACDB"`
- **Output:** `2`
- **Explanation:** Successive removals can leave `"FC"`.

#### Example 2

- **Input:** `s = "ACBBD"`
- **Output:** `5`
- **Explanation:** Neither removable pair occurs, so the string is unchanged.
