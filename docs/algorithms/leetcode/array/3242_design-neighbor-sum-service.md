# Design Neighbor Sum Service

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3242 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Design, Matrix, Simulation |
| Official Link | [design-neighbor-sum-service](https://leetcode.com/problems/design-neighbor-sum-service/) |

## Problem Description & Examples
### Goal
Design a data structure that stores a 2D grid of unique integers and provides efficient methods to calculate the sum of specific neighbors for a given value. The service must support two types of neighbor queries: "adjacent" (up, down, left, right) and "diagonal" (top-left, top-right, bottom-left, bottom-right).

### Function Contract
**Inputs**

- `grid`: A 2D list of integers representing the initial state of the service.
- `value`: An integer present in the grid for which the neighbor sum is requested.

**Return value**

- `adjacentSum(value)`: Returns the sum of the four immediate orthogonal neighbors of the given value.
- `diagonalSum(value)`: Returns the sum of the four immediate diagonal neighbors of the given value.

### Examples
**Example 1**

- Input: `grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]`
- Output: `adjacentSum(1) = 0+2+4 = 6`, `diagonalSum(1) = 3+5 = 8`

**Example 2**

- Input: `grid = [[1, 2, 0, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]`
- Output: `adjacentSum(5) = 2+4+6+9 = 21`, `diagonalSum(5) = 1+3+8+10 = 22`

---

## Underlying Base Algorithm(s)
The solution utilizes a Hash Map (dictionary) to store the coordinates `(row, col)` for every integer value in the grid. This allows for O(1) lookup of a value's position. Once the position is retrieved, the neighbor sums are calculated by checking the grid boundaries and summing the values at the corresponding relative offsets.

---

## Complexity Analysis
- **Time Complexity**: 
    - Initialization: O(N*M) where N and M are grid dimensions, to map all values.
    - Queries: O(1) per query, as we perform a constant number of lookups and additions.
- **Space Complexity**: O(N*M) to store the mapping of values to their grid coordinates.
