# Count Connected Components in LCM Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3378 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Union-Find, Number Theory |
| Official Link | [count-connected-components-in-lcm-graph](https://leetcode.com/problems/count-connected-components-in-lcm-graph/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and an integer `threshold`, construct a graph where each element in `nums` is a node. An edge exists between two nodes `u` and `v` if their least common multiple (LCM) is less than or equal to `threshold`. The objective is to determine the number of connected components in this graph.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the nodes in the graph.
- `threshold`: An integer representing the maximum allowed LCM for an edge to exist.

**Return value**

- An integer representing the total number of connected components formed by the nodes in `nums`.

### Examples
**Example 1**

- Input: `nums = [2, 3, 8, 4, 5], threshold = 14`
- Output: `3`

**Example 2**

- Input: `nums = [2, 4, 8, 3, 12], threshold = 5`
- Output: `2`

**Example 3**

- Input: `nums = [2, 3, 8, 4, 5], threshold = 20`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Disjoint Set Union (DSU)** data structure. Since the condition `lcm(u, v) <= threshold` is equivalent to `(u * v) / gcd(u, v) <= threshold`, we can optimize the edge creation process. Instead of checking all pairs, we iterate through all possible divisors `g` up to `threshold`. For each `g`, we identify all multiples of `g` present in `nums` and connect them to a representative node (or each other) if their LCM condition is satisfied.

---

## Complexity Analysis
- **Time Complexity**: `O(T log T + N α(N))`, where `T` is the `threshold`, `N` is the length of `nums`, and `α` is the inverse Ackermann function. The `T log T` factor arises from the harmonic series summation when iterating over multiples.
- **Space Complexity**: `O(T + N)` to store the DSU structure and the mapping of values to their presence in the input array.
