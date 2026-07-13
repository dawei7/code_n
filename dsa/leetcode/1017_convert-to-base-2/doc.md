# Convert to Base -2

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1017 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [convert-to-base-2](https://leetcode.com/problems/convert-to-base-2/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/convert-to-base-2/).

### Goal
Convert a non-negative integer into its representation in base `-2`, using only digits `0` and `1`.

### Function Contract
**Inputs**

- `n`: Non-negative integer.

**Return value**

String representation of `n` in base `-2`.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `"110"`

**Example 2**

- Input: `n = 3`
- Output: `"111"`

**Example 3**

- Input: `n = 4`
- Output: `"100"`

---

## Solution
### Approach
Use repeated division by `-2`, just like ordinary base conversion, but adjust the quotient whenever the remainder would be negative. Each step produces a digit `0` or `1`; collect these digits from least significant to most significant and reverse them at the end.

The special value `0` is represented as `"0"`.

### Complexity Analysis
- **Time Complexity**: `O(log n)`.
- **Space Complexity**: `O(log n)` for the output digits.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
