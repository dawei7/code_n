# Last Stone Weight II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_195` |
| Frontend ID | 1049 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [last-stone-weight-ii](https://leetcode.com/problems/last-stone-weight-ii/) |

## Problem Description & Examples
### Goal
You are given an array of integers `stones` where `stones[i]` is the weight of the `i`-th stone.

We play a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed,
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is at most one stone left. Return the minimum possible weight of the left stone. If no stones are left, return `0`.

### Function Contract
**Inputs**

- `stones`: List[int]

**Return value**

int - minimum remaining weight

### Examples
**Example 1**

- Input: `stones = [2, 7, 4, 1, 8, 1]`
- Output: `1`

**Example 2**

- Input: `stones = [14, 2, 9]`
- Output: `3`

**Example 3**

- Input: `stones = [19, 3]`
- Output: `16`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
