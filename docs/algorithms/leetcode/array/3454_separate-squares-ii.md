# Separate Squares II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3454 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Segment Tree, Sweep Line |
| Official Link | [separate-squares-ii](https://leetcode.com/problems/separate-squares-ii/) |

## Problem Description & Examples
### Goal
Given a collection of axis-aligned squares, determine the horizontal line $y = k$ that divides the total area covered by the union of these squares into two equal parts. If multiple such lines exist, return the one with the smallest $y$-coordinate.

### Function Contract
**Inputs**

- `squares`: A list of lists, where each inner list `[x, y, l]` represents a square with its bottom-left corner at `(x, y)` and a side length of `l`.

**Return value**

- A float representing the $y$-coordinate that bisects the total area of the union of the squares.

### Examples
**Example 1**

- Input: `squares = [[0,0,1],[1,0,1]]`
- Output: `0.5`

**Example 2**

- Input: `squares = [[0,0,2],[1,1,1]]`
- Output: `0.75`

**Example 3**

- Input: `squares = [[0,0,1],[2,2,1]]`
- Output: `1.0`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of **Binary Search** on the answer (the $y$-coordinate) and a **Sweep Line** algorithm combined with a **Segment Tree** to calculate the area of the union of rectangles below a given $y$-coordinate efficiently.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N \cdot \log(\text{max\_coord}))$, where $N$ is the number of squares. The sweep line takes $O(N \log N)$ and we perform binary search over the coordinate range.
- **Space Complexity**: $O(N)$ to store the events and the segment tree nodes.
