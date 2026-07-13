# Count Connected Components in LCM Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3378 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Union-Find, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-connected-components-in-lcm-graph](https://leetcode.com/problems/count-connected-components-in-lcm-graph/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-connected-components-in-lcm-graph/).

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

- Input: `nums = [2, 4, 8, 3, 9], threshold = 5`
- Output: `4`

**Example 2**

- Input: `nums = [2, 4, 8, 3, 9, 12], threshold = 10`
- Output: `2`

**Example 3**

- Input: `nums = [2, 6, 30, 35], threshold = 12`
- Output: `3`

---

## Solution
### Approach
The problem is solved using the **Disjoint Set Union (DSU)** data structure. Since the condition `lcm(u, v) <= threshold` is equivalent to `(u * v) / gcd(u, v) <= threshold`, we can optimize the edge creation process. Instead of checking all pairs, we iterate through all possible divisors `g` up to `threshold`. For each `g`, we identify all multiples of `g` present in `nums` and connect them to a representative node (or each other) if their LCM condition is satisfied.

### Complexity Analysis
- **Time Complexity**: `O(T log T + N α(N))`, where `T` is the `threshold`, `N` is the length of `nums`, and `α` is the inverse Ackermann function. The `T log T` factor arises from the harmonic series summation when iterating over multiples.
- **Space Complexity**: `O(T + N)` to store the DSU structure and the mapping of values to their presence in the input array.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], threshold: int) -> int:
    parent = list(range(threshold + 1))

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(a: int, b: int) -> None:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    representative = [0] * (threshold + 1)

    for value in nums:
        if value > threshold:
            continue
        for multiple in range(value, threshold + 1, value):
            if representative[multiple] == 0:
                representative[multiple] = value
            else:
                union(value, representative[multiple])

    components = sum(1 for value in nums if value > threshold)
    roots = {find(value) for value in nums if value <= threshold}
    return components + len(roots)
```
</details>
