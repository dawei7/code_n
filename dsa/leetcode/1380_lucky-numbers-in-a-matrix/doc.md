# Lucky Numbers in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1380 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/lucky-numbers-in-a-matrix/) |

## Problem Description

### Goal

Given an $m \times n$ matrix whose integer values are all distinct, call an entry lucky when it satisfies two conditions at once: it is the minimum value in its row, and it is the maximum value in its column.

Return a list containing every lucky value in the matrix. A matrix may have no lucky value. The row and column dimensions are both positive, so every entry belongs to exactly one nonempty row and one nonempty column.

### Function Contract

**Inputs**

- `matrix`: an $m \times n$ rectangular matrix of distinct integers, where $1 \le m,n \le 50$.

**Return value**

- A list of all values that are simultaneously their row minimum and their column maximum.

### Examples

**Example 1**

- Input: `matrix = [[3,7,8],[9,11,13],[15,16,17]]`
- Output: `[15]`

**Example 2**

- Input: `matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]`
- Output: `[12]`

**Example 3**

- Input: `matrix = [[7,8],[1,2]]`
- Output: `[7]`
