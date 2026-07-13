# Merge Triplets to Form Target Triplet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1899 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [merge-triplets-to-form-target-triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/).

### Goal
A triplet is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [a_i, b_i, c_i]` describes the `i`-th triplet. You are also given an integer array `target = [x, y, z]` that describes the target triplet you want to obtain.

To obtain the target triplet, you may apply the following operation on `triplets` any number of times (possibly zero):
- Choose two indices `i` and `j` (possibly same) and update `triplets[j]` to be `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

Return `True` if it is possible to obtain target, or `False` otherwise.

### Function Contract
**Inputs**

- `triplets`: List[List[int]]
- `target`: List[int]

**Return value**

bool - True if target can be formed

### Examples
**Example 1**

- Input: `triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]], target = [2, 7, 5]`
- Output: `True`

**Example 2**

- Input: `triplets = [[7, 1, 1], [5, 1, 3], [5, 1, 5]], target = [7, 1, 5]`
- Output: `True`

**Example 3**

- Input: `triplets = [[10, 1, 4], [7, 2, 5]], target = [10, 2, 5]`
- Output: `True`

---

## Solution
### Approach
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
