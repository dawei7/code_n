# Lonely Pixel II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 533 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/lonely-pixel-ii/) |

## Problem Description
### Goal
Given a black-and-white picture and a positive integer `target`, inspect each black pixel at `(row, col)`. Its row and column must each contain exactly `target` black pixels.

The pixel qualifies only if every row that has a black pixel in column `col` is identical to its own row across all columns. Return the total number of qualifying black pixels, counting each coordinate separately. Matching row counts without identical row patterns is insufficient, and a column containing the required number of black pixels may contribute all of them when their rows satisfy the shared-pattern rule.

### Function Contract
**Inputs**

- `picture`: a rectangular matrix containing `"B"` and `"W"`
- `target`: the required number of black pixels in the qualifying row and column

**Return value**

- The number of black pixels satisfying both count conditions and the identical-row condition

### Examples
**Example 1**

- Input: `picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3`
- Output: `6`

**Example 2**

- Input: `picture = [["B","W","B"],["B","W","B"]], target = 2`
- Output: `4`

**Example 3**

- Input: `picture = [["B","W","B"],["B","W","B"],["B","W","B"]], target = 2`
- Output: `0`
