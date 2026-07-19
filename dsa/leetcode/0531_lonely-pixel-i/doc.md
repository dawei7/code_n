# Lonely Pixel I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 531 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/lonely-pixel-i/) |

## Problem Description
### Goal
Given a rectangular picture whose cells are black `B` or white `W`, call a black pixel lonely when its row contains exactly one black pixel and its column also contains exactly one black pixel.

Return the number of lonely black pixels. A pixel must satisfy both conditions at its own coordinate; a row or column with several black pixels disqualifies each of them for that dimension. White pixels never count, diagonal black pixels do not directly conflict unless they share a row or column, and the function returns only the count rather than their coordinates.

### Function Contract
**Inputs**

- `picture`: a rectangular matrix containing `"B"` for black and `"W"` for white pixels

**Return value**

- The number of black pixels whose row and column each contain exactly one black pixel

### Examples
**Example 1**

- Input: `picture = [["W","W","B"],["W","B","W"],["B","W","W"]]`
- Output: `3`

**Example 2**

- Input: `picture = [["B","B"],["B","W"]]`
- Output: `0`

**Example 3**

- Input: `picture = [["W","W"],["W","W"]]`
- Output: `0`
