# Maximum Employees to Be Invited to a Meeting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2127 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Depth-First Search, Graph Theory, Topological Sort |
| Official Link | [maximum-employees-to-be-invited-to-a-meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/) |

## Problem Description & Examples
### Goal
Seat the largest possible number of employees around one circular table so that each invited employee sits next to their favorite employee. Every employee names exactly one other employee as their favorite.

### Function Contract
**Inputs**

- `favorite`: `favorite[i]` is the employee favored by employee `i`.

**Return value**

The maximum number of employees that can be invited under the seating rule.

### Examples
**Example 1**

- Input: `favorite = [2, 2, 1, 2]`
- Output: `3`

**Example 2**

- Input: `favorite = [1, 2, 0]`
- Output: `3`

**Example 3**

- Input: `favorite = [3, 0, 1, 4, 1]`
- Output: `4`

---

## Underlying Base Algorithm(s)
View `favorite` as a functional graph. Remove indegree-zero nodes with a topological pass while computing the longest incoming chain ending at each remaining node. The answer is the larger of: the longest cycle of length at least three, or the sum over every mutual-favorite pair of both pair members plus the longest chain entering each member. Separate chains can be attached to opposite sides of every two-cycle.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
