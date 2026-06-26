# Maximum Units on a Truck

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1710 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting |
| Official Link | [maximum-units-on-a-truck](https://leetcode.com/problems/maximum-units-on-a-truck/) |

## Problem Description & Examples
### Goal
Each box type gives a count of boxes and units per box. Choose boxes to load onto a truck with limited capacity so the total units is as large as possible.

### Function Contract
**Inputs**

- `boxTypes`: a list of `[numberOfBoxes, unitsPerBox]` pairs.
- `truckSize`: the maximum number of boxes the truck can carry.

**Return value**

Return the maximum total units that can be loaded.

### Examples
**Example 1**

- Input: `boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4`
- Output: `8`

**Example 2**

- Input: `boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10`
- Output: `91`

**Example 3**

- Input: `boxTypes = [[2,4],[3,2]], truckSize = 3`
- Output: `10`

---

## Underlying Base Algorithm(s)
Use a greedy sort by `unitsPerBox` descending. Take as many boxes as possible from the most valuable remaining type, subtract from truck capacity, and continue until the truck is full or no boxes remain.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides sorting storage
