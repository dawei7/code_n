# Determine Whether Matrix Can Be Obtained By Rotation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1886 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [determine-whether-matrix-can-be-obtained-by-rotation](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/).

### Goal
Determine whether a square matrix can equal a target matrix after rotating it by `0`, `90`, `180`, or `270` degrees clockwise.

### Function Contract
**Inputs**

- `mat`: the starting square matrix.
- `target`: the target square matrix.

**Return value**

Return `True` if some allowed rotation of `mat` equals `target`, otherwise `False`.

### Examples
**Example 1**

- Input: `mat = [[0,1],[1,0]], target = [[1,0],[0,1]]`
- Output: `True`

**Example 2**

- Input: `mat = [[0,1],[1,1]], target = [[1,0],[0,1]]`
- Output: `False`

**Example 3**

- Input: `mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]`
- Output: `True`

---

## Solution
### Approach
Check the four rotations. Either physically rotate `mat` up to three times, or compare coordinates directly using rotation mappings such as `(r, c) -> (c, n - 1 - r)` for a 90-degree rotation.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)` if comparing by coordinate mappings

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
