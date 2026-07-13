# Finding 3-Digit Even Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2094 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Recursion, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [finding-3-digit-even-numbers](https://leetcode.com/problems/finding-3-digit-even-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/finding-3-digit-even-numbers/).

### Goal
Using the given digits at most as often as they appear, form every three-digit even number with no leading zero.

### Function Contract
**Inputs**

- `digits`: available digits.

**Return value**

Return all possible numbers in increasing order.

### Examples
**Example 1**

- Input: `digits = [2,1,3,0]`
- Output: `[102,120,130,132,210,230,302,310,312,320]`

**Example 2**

- Input: `digits = [2,2,8,8,2]`
- Output: `[222,228,282,288,822,828,882]`

**Example 3**

- Input: `digits = [3,7,5]`
- Output: `[]`

---

## Solution
### Approach
Either enumerate numbers from `100` to `998` by twos and compare digit counts, or backtrack over hundreds, tens, and even ones digits while respecting available counts. Sorting the generated set gives increasing order.

### Complexity Analysis
- **Time Complexity**: `O(1)` relative to input size because only 450 even three-digit numbers exist.
- **Space Complexity**: `O(1)` excluding output.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
