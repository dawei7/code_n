# Number of Laser Beams in a Bank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2125 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, String, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-laser-beams-in-a-bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/).

### Goal
Count laser beams between security devices in a binary bank layout. Every device in one nonempty row connects to every device in the next nonempty row, while rows containing no devices are skipped.

### Function Contract
**Inputs**

- `bank`: a list of equal-length binary strings; `1` marks a security device.

**Return value**

The total number of laser beams.

### Examples
**Example 1**

- Input: `bank = ["011001", "000000", "010100", "001000"]`
- Output: `8`

**Example 2**

- Input: `bank = ["000", "111", "000"]`
- Output: `0`

**Example 3**

- Input: `bank = ["10", "01", "11"]`
- Output: `4`

---

## Solution
### Approach
Scan the rows and count the devices in each. Ignore zero counts. For every nonempty row, add `previous_count * current_count`, then make the current count the previous one.

### Complexity Analysis
- **Time Complexity**: `O(mn)` for an `m` by `n` bank
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
