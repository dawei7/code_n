# Remove All Adjacent Duplicates In String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1047 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) |

## Problem Description

### Goal

The string `s` consists of lowercase English letters. One duplicate removal chooses two letters that are both adjacent and equal, then removes that pair from the string.

Keep making duplicate removals until no adjacent equal pair remains. Removing one pair may bring another equal pair together, so those newly adjacent letters must also be considered. Return the final string after every possible removal. The final result is guaranteed to be unique regardless of which available pair is removed first.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $N$, where $1 \le N \le 10^5$.

**Return value**

- The unique string remaining after repeatedly deleting adjacent equal-letter pairs until no such pair exists.

### Examples

**Example 1**

- Input: `s = "abbaca"`
- Output: `"ca"`
- Explanation: Removing `"bb"` gives `"aaca"`; the newly exposed `"aa"` is then removed.

**Example 2**

- Input: `s = "azxxzy"`
- Output: `"ay"`
