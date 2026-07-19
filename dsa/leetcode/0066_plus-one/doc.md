# Plus One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 66 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/plus-one/) |

## Problem Description
### Goal
An array `digits` stores a nonnegative integer with its most significant decimal digit first. Each entry lies from `0` through `9`, and the representation has no leading zero unless the number itself is zero. It may be longer than a built-in numeric type can hold.

Add one to the represented value and return the canonical digit array for the result. Carries may pass through a suffix of nines and may create a new leading digit, as when `[9, 9]` becomes `[1, 0, 0]`. No other leading zeroes should appear.

### Function Contract
**Inputs**

- `digits`: a nonempty `List[int]` of decimal digits with no leading zero

**Return value**

The canonical digit list representing the input value plus one.

### Examples
**Example 1**

- Input: `digits = [1,2,3]`
- Output: `[1,2,4]`

**Example 2**

- Input: `digits = [4,3,2,1]`
- Output: `[4,3,2,2]`

**Example 3**

- Input: `digits = [9]`
- Output: `[1,0]`
