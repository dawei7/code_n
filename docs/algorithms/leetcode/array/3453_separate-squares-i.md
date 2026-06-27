# Separate Squares I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3453 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [separate-squares-i](https://leetcode.com/problems/separate-squares-i/) |

## Problem Description & Examples
### Goal
Given a list of axis-aligned squares defined by their bottom-left coordinates and side lengths, determine the horizontal line $y = k$ that divides the total area of all squares into two equal halves.

### Function Contract
**Inputs**

- `squares`: A list of lists, where each inner list `[x, y, l]` represents a square with its bottom-left corner at `(x, y)` and side length `l`.

**Return value**

- A float representing the y-coordinate $k$ such that the sum of the areas of the parts of the squares below $y = k$ equals the sum of the areas of the parts of the squares above $y = k$.

### Examples
**Example 1**

- Input: `squares = [[0,0,1],[2,2,1]]`
- Output: `1.5`

**Example 2**

- Input: `squares = [[0,0,2],[1,1,1]]`
- Output: `1.1666666667`

**Example 3**

- Input: `squares = [[0,0,1],[1,1,1]]`
- Output: `0.5`

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the total area below a horizontal line $y=k$ is a monotonically increasing function of $k$, we can search for the value $k$ within the range $[min(y), max(y+l)]$. For a chosen $k$, we calculate the area of each square intersecting the line $y=k$ by clipping the square's vertical range $[y, y+l]$ against $[0, k]$.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log(\frac{max\_coord}{\epsilon}))$, where $N$ is the number of squares, $max\_coord$ is the range of coordinates, and $\epsilon$ is the required precision (typically $10^{-5}$).
- **Space Complexity**: $O(1)$, as we only store a few variables for the binary search bounds and the calculated area.
