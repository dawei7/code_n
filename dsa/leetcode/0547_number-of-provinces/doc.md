# Number of Provinces

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 547 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-provinces/) |

## Problem Description
### Goal
Given the symmetric matrix `isConnected`, entry $[i][j] = 1$ means cities `i` and `j` are directly connected. Cities are also indirectly connected when a chain of direct connections links them.

A province is a maximal group in which every city is connected directly or indirectly to the others and has no connection path to a city outside the group. Return the number of provinces. A city connected only to itself forms one province, cycles do not create additional provinces, and every city must belong to exactly one component.

### Function Contract
**Inputs**

- `isConnected`: an `n × n` matrix where `isConnected[i][j] = 1` means cities `i` and `j` are directly connected

**Return value**

- The number of provinces formed by direct and transitive city connections

### Examples
**Example 1**

- Input: `isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]`
- Output: `2`

**Example 2**

- Input: `isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]`
- Output: `3`

**Example 3**

- Input: `isConnected = [[1]]`
- Output: `1`
