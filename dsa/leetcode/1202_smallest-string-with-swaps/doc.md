# Smallest String With Swaps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1202 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-string-with-swaps](https://leetcode.com/problems/smallest-string-with-swaps/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-string-with-swaps/).

### Goal
Given index pairs that may be swapped any number of times, return the lexicographically smallest string reachable from `s`.

### Function Contract
**Inputs**

- `s`: original lowercase string.
- `pairs`: index pairs that allow swaps between connected positions.

**Return value**

The smallest string obtainable through any sequence of allowed swaps.

### Examples
**Example 1**

- Input: `s = "dcab"`, `pairs = [[0,3],[1,2]]`
- Output: `"bacd"`

**Example 2**

- Input: `s = "dcab"`, `pairs = [[0,3],[1,2],[0,2]]`
- Output: `"abcd"`

**Example 3**

- Input: `s = "cba"`, `pairs = [[0,1],[1,2]]`
- Output: `"abc"`

---

## Solution
### Approach
Union-Find connected components and sorting.

### Complexity Analysis
- **Time Complexity**: `O(n log n + p alpha(n))`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(s, pairs):
    parent = list(range(len(s)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in pairs:
        union(a, b)

    groups = defaultdict(list)
    for i, ch in enumerate(s):
        groups[find(i)].append(ch)
    for chars in groups.values():
        chars.sort(reverse=True)

    result = []
    for i in range(len(s)):
        result.append(groups[find(i)].pop())
    return "".join(result)
```
</details>
