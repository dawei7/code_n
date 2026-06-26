# Eliminate Maximum Number of Monsters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1921 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [eliminate-maximum-number-of-monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/) |

## Problem Description & Examples
### Goal
Monsters move toward the city at constant speeds. You can eliminate one monster at each integer minute before monsters move at that minute. Maximize how many monsters are eliminated before any reaches the city.

### Function Contract
**Inputs**

- `dist`: initial distances of monsters.
- `speed`: speeds of monsters.

**Return value**

Return the number of monsters eliminated before losing.

### Examples
**Example 1**

- Input: `dist = [1,3,4], speed = [1,1,1]`
- Output: `3`

**Example 2**

- Input: `dist = [1,1,2,3], speed = [1,1,1,1]`
- Output: `1`

**Example 3**

- Input: `dist = [3,2,4], speed = [5,3,2]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Compute each monster's arrival minute as `ceil(dist[i] / speed[i])`. Sort arrival times. At minute `t`, you can eliminate the `t`th monster only if its arrival time is greater than `t`; otherwise it has already arrived and the game ends.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
