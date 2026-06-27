# Minimum Reverse Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2612 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Breadth-First Search, Union-Find, Ordered Set |
| Official Link | [minimum-reverse-operations](https://leetcode.com/problems/minimum-reverse-operations/) |

## Problem Description & Examples
### Goal
Given an array of length `n` initialized with zeros, except for a target position `p` which is one, and a set of forbidden indices, determine the minimum number of operations required to move the one to every possible index in the array. An operation consists of choosing a subarray of length `k` and reversing it, provided the subarray does not contain any forbidden indices and the current position of the one is within the chosen subarray. If an index is unreachable, return -1.

### Function Contract
**Inputs**

- `n` (int): The total length of the array.
- `p` (int): The initial index of the value 1.
- `banned` (List[int]): A list of indices that cannot be part of any reversed subarray.
- `k` (int): The length of the subarray to be reversed.

**Return value**

- `List[int]`: An array of length `n` where the `i`-th element is the minimum number of operations to move the 1 to index `i`, or -1 if unreachable.

### Examples
**Example 1**

- Input: `n = 4, p = 0, banned = [1, 2], k = 4`
- Output: `[0, -1, -1, 1]`

**Example 2**

- Input: `n = 5, p = 0, banned = [2, 4], k = 3`
- Output: `[0, -1, -1, -1, -1]`

**Example 3**

- Input: `n = 4, p = 2, banned = [], k = 3`
- Output: `[-1, -1, 0, 1]`

---

## Underlying Base Algorithm(s)
The problem is modeled as a Breadth-First Search (BFS) on a graph where indices are nodes and edges represent valid reversals. To optimize the transition, we observe that reversing a subarray of length `k` starting at index `i` moves the 1 from `i` to `i + k - 1 - 2 * (i - start)`. By maintaining two sets of available indices (one for even parity and one for odd parity), we can efficiently find and remove reachable indices in $O(n \log n)$ time using `SortedList` or similar structures to avoid redundant checks.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the length of the array. Each index is visited once, and set operations (finding and deleting) take logarithmic time.
- **Space Complexity**: $O(n)$ to store the distance array, the banned set, and the sets of available indices.
