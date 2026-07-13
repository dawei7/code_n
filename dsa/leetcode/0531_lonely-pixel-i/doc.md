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

### Required Complexity

- **Time:** $O(rows \cdot cols)$
- **Space:** $O(rows + cols)$

<details>
<summary>Approach</summary>

#### General

**Count black pixels along both axes**

Create one count per row and one per column. Scan every cell once; when a black pixel is found, increment its row count and column count.

**Test the complete loneliness condition**

Scan the picture again. A black pixel contributes exactly when its stored row count and column count are both one. The two conditions are independent: uniqueness in only one direction is insufficient.

**Why every counted pixel is exactly a lonely pixel**

The first pass records the complete black-pixel totals for every row and column. Thus a black cell passes the second-pass test precisely when no other black cell shares either axis with it. Every lonely pixel passes, and no non-lonely pixel can pass.

#### Complexity detail

Both scans visit `rows * cols` cells, giving $O(rows \cdot cols)$ time. The row and column count arrays use $O(rows + cols)$ auxiliary space.

#### Alternatives and edge cases

- **Rescan a row and column for every black pixel:** is simple but can take $O(rows \cdot cols \cdot (rows + cols))$ time on a dense picture.
- **Sets of candidate coordinates:** can track first and repeated black positions, but count arrays are simpler and have the same asymptotic space.
- **All-white picture:** contains no candidates and returns zero.
- **Dense black picture:** every black pixel shares both axes and none is lonely.
- **One-row or one-column picture:** a black pixel is lonely only when it is the sole black pixel in that entire line.
- **Rectangular picture:** row and column counts must use their separate dimensions.

</details>
