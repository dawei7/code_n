# Relocate Marbles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2766 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Simulation |
| Official Link | [relocate-marbles](https://leetcode.com/problems/relocate-marbles/) |

## Problem Description & Examples
### Goal
Given an initial collection of marbles at specific integer positions, perform a series of relocation operations. Each operation specifies a source position and a target position; all marbles currently at the source are moved to the target. After all operations are completed, return a sorted list of all unique positions currently occupied by at least one marble.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial positions of the marbles.
- `moveFrom`: A list of integers where `moveFrom[i]` is the position from which marbles are moved in the $i$-th operation.
- `moveTo`: A list of integers where `moveTo[i]` is the position to which marbles are moved in the $i$-th operation.

**Return value**

- A sorted list of integers representing all final positions that contain at least one marble.

### Examples
**Example 1**

- Input: `nums = [1, 6, 7, 8], moveFrom = [1, 7, 2], moveTo = [2, 9, 5]`
- Output: `[5, 6, 8, 9]`

**Example 2**

- Input: `nums = [1, 1, 3, 3], moveFrom = [1, 3], moveTo = [2, 2]`
- Output: `[2]`

**Example 3**

- Input: `nums = [0], moveFrom = [0], moveTo = [1]`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
The problem is best solved using a Hash Set to track the current positions of the marbles. Since multiple marbles can occupy the same position, and we only care about the existence of a marble at a coordinate, a set allows for $O(1)$ average time complexity for removals and insertions. After processing all moves, we extract the elements from the set and sort them.

---

## Complexity Analysis
- **Time Complexity**: $O(N + M + K \log K)$, where $N$ is the number of initial marbles, $M$ is the number of move operations, and $K$ is the number of unique final positions. The set operations take $O(N + M)$, and sorting the final positions takes $O(K \log K)$.
- **Space Complexity**: $O(K)$, as we store the unique positions in a set.
