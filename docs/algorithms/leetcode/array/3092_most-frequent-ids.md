# Most Frequent IDs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3092 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Heap (Priority Queue), Ordered Set |
| Official Link | [most-frequent-ids](https://leetcode.com/problems/most-frequent-ids/) |

## Problem Description & Examples
### Goal
Given two arrays representing IDs and their corresponding frequency changes over time, track the maximum frequency of any ID after each update. An update consists of adding a specific value (positive or negative) to the frequency count of a given ID. After every update, return the current highest frequency among all IDs present in the system.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the IDs being updated.
- `freq`: A list of integers representing the change in frequency for the corresponding ID at the same index.

**Return value**

- A list of integers where each element corresponds to the maximum frequency observed after the update at that index.

### Examples
**Example 1**

- Input: `nums = [2,3,2,1], freq = [3,2,-3,1]`
- Output: `[3,3,2,2]`

**Example 2**

- Input: `nums = [5,5,3], freq = [2,-2,1]`
- Output: `[2,0,1]`

**Example 3**

- Input: `nums = [1,1,1], freq = [1,1,1]`
- Output: `[1,2,3]`

---

## Underlying Base Algorithm(s)
The problem is solved using a Hash Map (to store the current frequency of each ID) combined with a Max-Heap (to track the maximum frequency). Since Python's `heapq` does not support arbitrary deletions, we use "lazy removal": we store `(-frequency, id)` tuples in the heap. When querying the top, we verify if the frequency at the top of the heap matches the current frequency stored in our Hash Map. If it does not, the entry is stale and is discarded.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of updates. Each update involves a heap push and potentially multiple heap pops (lazy removal), both of which are logarithmic.
- **Space Complexity**: `O(N)`, required to store the frequency map and the heap, which can grow up to the size of the number of updates.
