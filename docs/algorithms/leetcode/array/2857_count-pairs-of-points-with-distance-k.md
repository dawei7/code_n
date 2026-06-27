# Count Pairs of Points With Distance k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2857 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Bit Manipulation |
| Official Link | [count-pairs-of-points-with-distance-k](https://leetcode.com/problems/count-pairs-of-points-with-distance-k/) |

## Problem Description & Examples
### Goal
Given a list of 2D coordinates and an integer `k`, determine the number of pairs of points `(i, j)` such that `i < j` and the bitwise XOR sum of their coordinates `(x1 ^ x2) + (y1 ^ y2)` equals exactly `k`.

### Function Contract
**Inputs**

- `coordinates`: A list of lists, where each inner list contains two integers `[x, y]` representing a point.
- `k`: An integer representing the target sum of the XORed coordinates.

**Return value**

- An integer representing the total count of unique pairs `(i, j)` that satisfy the condition.

### Examples
**Example 1**

- Input: `coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5`
- Output: `2`

**Example 2**

- Input: `coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0`
- Output: `10`

**Example 3**

- Input: `coordinates = [[6,2],[1,3]], k = 1`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem relies on the properties of the XOR operation. Since `(x1 ^ x2) + (y1 ^ y2) = k`, we can iterate through all possible values `i` from `0` to `k`. For a fixed point `(x1, y1)` and a chosen `i`, we know that `x1 ^ x2 = i` and `y1 ^ y2 = k - i`. This implies `x2 = x1 ^ i` and `y2 = y1 ^ (k - i)`. By using a hash map to store the frequency of points encountered so far, we can count valid pairs in a single pass.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k)`, where `n` is the number of points. For each point, we iterate `k+1` times to check potential XOR combinations.
- **Space Complexity**: `O(n)`, as we store the frequency of points in a hash map.
