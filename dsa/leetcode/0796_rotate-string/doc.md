# Rotate String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 796 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotate-string/) |

## Problem Description

### Goal

Given strings `s` and `goal`, one shift operation removes the leftmost character of `s` and appends that same character to the right end.

Return `True` if applying the operation zero or more times can transform `s` exactly into `goal`, and `False` otherwise. Shifting preserves string length and character multiplicities, and after one full cycle of `len(s)` shifts the original ordering returns.

### Function Contract

**Inputs**

- `s`: a nonempty lowercase string.
- `goal`: another nonempty lowercase string.

**Return value**

- `True` exactly when `goal` is a cyclic rotation of `s`; otherwise, `False`.

### Examples

**Example 1**

- Input: `s = "abcde", goal = "cdeab"`
- Output: `True`
- Explanation: Moving `a` and then `b` from the front to the back produces `cdeab`.

**Example 2**

- Input: `s = "abcde", goal = "abced"`
- Output: `False`
- Explanation: Cyclic shifts preserve the circular order of the characters, which this target changes.

**Example 3**

- Input: `s = "a", goal = "a"`
- Output: `True`
- Explanation: Applying zero shifts is allowed, so an unchanged string is a rotation of itself.
