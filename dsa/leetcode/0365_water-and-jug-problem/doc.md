# Water and Jug Problem

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 365 |
| Difficulty | Medium |
| Topics | Math, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/water-and-jug-problem/) |

## Problem Description
### Goal
Two unmarked jugs have nonnegative capacities `x` and `y`, and an unlimited water supply is available. A legal action fills one jug completely, empties one jug, or pours from one jug into the other until the source empties or the destination fills.

Return whether some sequence of legal actions can leave exactly `target` total units across the two jugs. The target may reside in either jug or be split between them. Target zero is immediately measurable, while any target greater than $x + y$ is impossible. No partial fill or pour may stop at an arbitrary unmarked quantity.

### Function Contract
**Inputs**

- `x`: the non-negative capacity of the first jug
- `y`: the non-negative capacity of the second jug
- `target`: the non-negative amount to measure across the two jugs

**Return value**

- `True` if the allowed operations can leave exactly `target` total units in the jugs; otherwise `False`.

### Examples
**Example 1**

- Input: `x = 3, y = 5, target = 4`
- Output: `True`

**Example 2**

- Input: `x = 2, y = 6, target = 5`
- Output: `False`

**Example 3**

- Input: `x = 1, y = 2, target = 3`
- Output: `True`
