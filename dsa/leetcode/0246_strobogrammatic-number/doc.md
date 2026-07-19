# Strobogrammatic Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 246 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strobogrammatic-number/) |

## Problem Description
### Goal
Given a nonempty decimal string `num`, imagine rotating its written digits by 180 degrees. Rotation reverses the order of positions and transforms only valid digit pairs: `0`, `1`, and `8` map to themselves, while `6` and `9` map to each other.

Return `True` when the rotated result exactly reproduces the original string. Any digit without a valid rotated form makes the answer `False`, as does a mismatched pair at mirrored positions. The comparison uses the entire numeral as written rather than its parsed integer value, so positions and characters must agree exactly after rotation.

### Function Contract
**Inputs**

- `num`: a non-empty decimal string

**Return value**

`True` exactly when rotating every digit by 180 degrees and reversing their positions reproduces `num`.

### Examples
**Example 1**

- Input: `num = "69"`
- Output: `True`

**Example 2**

- Input: `num = "88"`
- Output: `True`

**Example 3**

- Input: `num = "962"`
- Output: `False`
