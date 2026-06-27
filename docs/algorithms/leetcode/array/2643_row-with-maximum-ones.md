# Row With Maximum Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2643 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [row-with-maximum-ones](https://leetcode.com/problems/row-with-maximum-ones/) |

## Problem Description & Examples
### Goal
Given a binary matrix (a 2D grid containing only 0s and 1s), identify the row index that contains the highest count of 1s. If multiple rows share the same maximum count, return the index of the row that appears first.

### Function Contract
**Inputs**

- `mat`: A list of lists of integers (`List[List[int]]`) representing an $m \times n$ binary matrix.

**Return value**

- A list of two integers: `[index, count]`, where `index` is the row number with the most 1s, and `count` is the total number of 1s found in that row.

### Examples
**Example 1**

- Input: `mat = [[0,1],[1,0]]`
- Output: `[0, 1]`

**Example 2**

- Input: `mat = [[0,0,0],[0,1,1]]`
- Output: `[1, 2]`

**Example 3**

- Input: `mat = [[0,0],[1,1],[0,0]]`
- Output: `[1, 2]`

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan (traversal) of the matrix. We iterate through each row, calculate the sum of its elements (which effectively counts the 1s since the matrix is binary), and maintain a running maximum to track the best row found so far.

---

## Complexity Analysis
- **Time Complexity**: $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns, as we must inspect every element in the matrix at least once.
- **Space Complexity**: $O(1)$, as we only store a few integer variables to track the current maximum index and count, regardless of the input size.
