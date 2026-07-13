# Minimize Rounding Error to Meet Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1058 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-rounding-error-to-meet-target](https://leetcode.com/problems/minimize-rounding-error-to-meet-target/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-rounding-error-to-meet-target/).

### Goal
Each decimal price must be rounded either down or up to an integer. Choose the rounding direction for every price so the rounded integers sum to `target`, while minimizing the total absolute rounding error. Return the minimum error formatted with exactly three digits after the decimal point, or `-1` if the target cannot be reached.

### Function Contract
**Inputs**

- `prices`: List of decimal strings with three fractional digits.
- `target`: Desired sum after rounding all prices.

**Return value**

Minimum rounding error as a string with three decimal places, or `"-1"`.

### Examples
**Example 1**

- Input: `prices = ["0.700", "2.800", "4.900"], target = 8`
- Output: `"1.000"`

**Example 2**

- Input: `prices = ["1.500", "2.500", "3.500"], target = 8`
- Output: `"1.500"`

**Example 3**

- Input: `prices = ["1.200", "2.300"], target = 10`
- Output: `"-1"`

---

## Solution
### Approach
Start by flooring every price. If the floor sum is already above `target`, or the ceiling sum is below `target`, the answer is impossible. Otherwise, let `need = target - floor_sum`; exactly `need` non-integer prices must be rounded up.

For a fractional part `f`, flooring contributes error `f` and ceiling contributes error `1 - f`. Rounding up changes the total error by `1 - 2f`, so choose the `need` fractional parts with the smallest changes, which are the largest fractional parts.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` for sorting fractional parts.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
