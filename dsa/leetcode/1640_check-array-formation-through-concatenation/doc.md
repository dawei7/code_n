# Check Array Formation Through Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1640 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-array-formation-through-concatenation](https://leetcode.com/problems/check-array-formation-through-concatenation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-array-formation-through-concatenation/).

### Goal
Determine whether `arr` can be formed by concatenating the given pieces in some
order, without rearranging values inside any piece.

### Function Contract
**Inputs**

- `arr`: the target array.
- `pieces`: arrays that may be concatenated.

**Return value**

`true` if the pieces can form `arr`; otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [85], pieces = [[85]]`
- Output: `true`

**Example 2**

- Input: `arr = [15, 88], pieces = [[88], [15]]`
- Output: `true`

**Example 3**

- Input: `arr = [49, 18, 16], pieces = [[16, 18, 49]]`
- Output: `false`

---

## Solution
### Approach
Map the first value of each piece to that piece. Scan `arr` from left to right;
at each position, the value must start an unused piece, and the full piece must
match the next segment of `arr` exactly.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(p)`, where `p` is the number of pieces.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
