# Maximum Number of Eaten Apples

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1705 |
| Difficulty | Medium |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Official Link | [maximum-number-of-eaten-apples](https://leetcode.com/problems/maximum-number-of-eaten-apples/) |

## Problem Description & Examples
### Goal
Each day an apple tree may grow some apples, and those apples rot after a given number of days. At most one apple can be eaten per day. Maximize how many apples are eaten before they rot.

### Function Contract
**Inputs**

- `apples`: `apples[i]` is the number of apples grown on day `i`.
- `days`: `days[i]` is how many days those apples remain edible.

**Return value**

Return the maximum number of apples that can be eaten.

### Examples
**Example 1**

- Input: `apples = [1,2,3,5,2], days = [3,2,1,4,2]`
- Output: `7`

**Example 2**

- Input: `apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]`
- Output: `5`

**Example 3**

- Input: `apples = [2,1,10], days = [2,10,1]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Use a min-heap keyed by expiration day. On each day, add the new batch if any, discard expired or empty batches, then eat one apple from the batch that rots soonest. Continue after the input days while edible apples remain.

---

## Complexity Analysis
- **Time Complexity**: `O((n + eaten) log n)`
- **Space Complexity**: `O(n)`
