# Count Ways to Group Overlapping Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2580 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [count-ways-to-group-overlapping-ranges](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/) |

## Problem Description & Examples
### Goal
Given a collection of closed intervals, determine the number of ways to partition these intervals into two distinct groups such that every interval in a group is connected to every other interval in the same group (either directly or transitively through overlapping intervals). Essentially, we are counting the number of disjoint connected components of intervals, where each component can be independently assigned to one of two groups. The result should be $2^k \pmod{10^9 + 7}$, where $k$ is the number of disjoint components.

### Function Contract
**Inputs**

- `ranges`: A list of lists, where each inner list `[start, end]` represents a closed interval.

**Return value**

- An integer representing the number of ways to group the intervals modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `ranges = [[6,10],[5,15]]`
- Output: `2`

**Example 2**

- Input: `ranges = [[1,3],[10,20],[2,5],[4,8]]`
- Output: `4`

**Example 3**

- Input: `ranges = [[1,2],[3,4]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved by identifying connected components of intervals. By sorting the intervals based on their start times, we can perform a linear scan to merge overlapping intervals. If an interval starts after the end of the current merged range, it signifies the start of a new, independent component. The total number of ways is then $2^{\text{number of components}} \pmod{10^9 + 7}$.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the number of ranges, due to the initial sorting step. The subsequent linear scan takes $O(N)$.
- **Space Complexity**: $O(1)$ or $O(N)$ depending on the sorting implementation's space requirements.
