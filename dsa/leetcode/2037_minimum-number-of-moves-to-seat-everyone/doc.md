# Minimum Number of Moves to Seat Everyone

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2037 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-moves-to-seat-everyone](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/).

### Goal
Move students along a line so every student sits in a distinct seat, minimizing total moves.

### Function Contract
**Inputs**

- `seats`: seat positions.
- `students`: student positions.

**Return value**

Return the minimum total movement distance.

### Examples
**Example 1**

- Input: `seats = [3,1,5], students = [2,7,4]`
- Output: `4`

**Example 2**

- Input: `seats = [4,1,5,9], students = [1,3,2,6]`
- Output: `7`

**Example 3**

- Input: `seats = [2,2,6,6], students = [1,3,2,6]`
- Output: `4`

---

## Solution
### Approach
Sort both positions. Matching the leftmost remaining student to the leftmost remaining seat is optimal by the exchange argument for absolute distances.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` beyond sorting.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
