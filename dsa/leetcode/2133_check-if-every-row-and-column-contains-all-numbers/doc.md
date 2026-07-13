# Check if Every Row and Column Contains All Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2133 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-every-row-and-column-contains-all-numbers](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/).

### Goal
Check whether every row and every column of an `n x n` matrix contains each integer from `1` through `n` exactly once.

### Function Contract
**Inputs**

- `matrix`: an `n x n` integer matrix.

**Return value**

`true` when all rows and columns satisfy the required set of values; otherwise `false`.

### Examples
**Example 1**

- Input: `matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]`
- Output: `true`

**Example 2**

- Input: `matrix = [[1, 1, 1], [1, 2, 3], [1, 2, 3]]`
- Output: `false`

**Example 3**

- Input: `matrix = [[1]]`
- Output: `true`

---

## Solution
### Approach
For each index, scan its row and corresponding column while recording seen values. Reject an out-of-range value or duplicate immediately. With `n` positions and valid values restricted to `1..n`, absence of duplicates proves that every required value is present.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` reusable checking space

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
