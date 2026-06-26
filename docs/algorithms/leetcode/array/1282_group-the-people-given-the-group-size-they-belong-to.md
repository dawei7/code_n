# Group the People Given the Group Size They Belong To

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1282 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy |
| Official Link | [group-the-people-given-the-group-size-they-belong-to](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) |

## Problem Description & Examples
### Goal
Partition people into groups so that person `i` belongs to a group of size `groupSizes[i]`.

### Function Contract
**Inputs**

- `groupSizes`: required group size for each person index.

**Return value**

Any valid grouping of all indices.

### Examples
**Example 1**

- Input: `groupSizes = [3,3,3,3,3,1,3]`
- Output: `[[5],[0,1,2],[3,4,6]]`

**Example 2**

- Input: `groupSizes = [2,1,3,3,3,2]`
- Output: `[[1],[0,5],[2,3,4]]`

**Example 3**

- Input: `groupSizes = [1,1,1]`
- Output: `[[0],[1],[2]]`

---

## Underlying Base Algorithm(s)
Greedy bucket filling.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
