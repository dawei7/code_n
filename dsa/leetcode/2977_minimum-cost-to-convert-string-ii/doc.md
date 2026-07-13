# Minimum Cost to Convert String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2977 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Graph Theory, Trie, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-convert-string-ii](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/).

### Goal
Given two strings `source` and `target` of equal length, and a set of transformation rules where converting a substring `original[i]` to `changed[i]` incurs a specific `cost[i]`, determine the minimum total cost to transform `source` into `target`. If the transformation is impossible, return -1.

### Function Contract
**Inputs**

- `source` (str): The initial string.
- `target` (str): The desired string.
- `original` (List[str]): List of starting substrings for transformations.
- `changed` (List[str]): List of resulting substrings for transformations.
- `cost` (List[int]): List of costs associated with each transformation.

**Return value**

- `int`: The minimum cost to transform `source` to `target`, or -1 if impossible.

### Examples
**Example 1**

- Input: `source = "abcd"`, `target = "acde"`, `original = ["ab","ac"], changed = ["ac","bc"], cost = [2,1]`
- Output: `-1`

**Example 2**

- Input: `source = "abcdefgh"`, `target = "acdeeghh"`, `original = ["bcd","fgh","th"], changed = ["cde","thh","gh"], cost = [1,3,5]`
- Output: `9`

**Example 3**

- Input: `source = "abcdefg"`, `target = "affgefg"`, `original = ["bcd","efg"], changed = ["fge","fge"], cost = [1,2]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a combination of:
1. **Trie (Prefix Tree)**: To efficiently map all unique substrings involved in transformations to integer IDs.
2. **Floyd-Warshall Algorithm**: To compute the all-pairs shortest paths between all unique substrings identified in the Trie.
3. **Dynamic Programming**: A linear DP approach where `dp[i]` represents the minimum cost to transform the prefix of `source` up to index `i` into the corresponding prefix of `target`.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot L^2 + K^3)$, where $N$ is the length of the strings, $L$ is the maximum length of a transformation substring, and $K$ is the number of unique substrings. The $K^3$ comes from Floyd-Warshall, and $N \cdot L^2$ from the DP transitions.
- **Space Complexity**: $O(K^2 + K \cdot L)$, primarily for the distance matrix and the Trie structure.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections

def solve(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    # Map all unique substrings to IDs
    trie = {}
    def get_id(s, create=False):
        node = trie
        for char in s:
            if char not in node:
                if not create: return -1
                node[char] = {}
            node = node[char]
        if '#' not in node:
            if not create: return -1
            node['#'] = len(ids)
            ids.append(s)
        return node['#']

    ids = []
    for s in original: get_id(s, True)
    for s in changed: get_id(s, True)

    n_nodes = len(ids)
    dist = [[float('inf')] * n_nodes for _ in range(n_nodes)]
    for i in range(n_nodes): dist[i][i] = 0

    for o, c, w in zip(original, changed, cost):
        u, v = get_id(o), get_id(c)
        dist[u][v] = min(dist[u][v], w)

    # Floyd-Warshall for all-pairs shortest paths
    for k in range(n_nodes):
        for i in range(n_nodes):
            if dist[i][k] == float('inf'): continue
            for j in range(n_nodes):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    n = len(source)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # DP with Trie lookups
    for i in range(n):
        if dp[i] == float('inf'): continue

        # Option 1: Characters match, no cost
        if source[i] == target[i]:
            dp[i+1] = min(dp[i+1], dp[i])

        # Option 2: Try all possible transformations starting at i
        curr_s, curr_t = trie, trie
        for j in range(i, n):
            if source[j] not in curr_s or target[j] not in curr_t:
                break
            curr_s = curr_s[source[j]]
            curr_t = curr_t[target[j]]

            if '#' in curr_s and '#' in curr_t:
                u, v = curr_s['#'], curr_t['#']
                if dist[u][v] != float('inf'):
                    dp[j+1] = min(dp[j+1], dp[i] + dist[u][v])

    return dp[n] if dp[n] != float('inf') else -1
```
</details>
