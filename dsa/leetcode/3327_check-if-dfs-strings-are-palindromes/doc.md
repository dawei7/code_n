# Check if DFS Strings Are Palindromes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3327 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Tree, Depth-First Search, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-dfs-strings-are-palindromes](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/).

### Goal
Given a tree represented by parent pointers and a string of characters associated with each node, determine for every node whether the string formed by the DFS traversal of its subtree is a palindrome. The DFS traversal visits children in increasing order of their indices, then appends the current node's character after all children have been processed.

### Function Contract
**Inputs**

- `parent`: A list of integers where `parent[i]` is the parent of node `i` (root is 0 with `parent[0] = -1`).
- `s`: A string where `s[i]` is the character at node `i`.

**Return value**

- A list of booleans of length `n`, where the `i`-th element is `True` if the DFS string of the subtree rooted at `i` is a palindrome, and `False` otherwise.

### Examples
**Example 1**

- Input: `parent = [-1, 0, 0, 1, 1, 2, 2], s = "aabcbab"`
- Output: `[true, true, true, true, true, true, true]`

**Example 2**

- Input: `parent = [-1, 0, 0, 1, 1, 2, 2], s = "abcdeff"`
- Output: `[false, false, false, true, true, true, true]`

**Example 3**

- Input: `parent = [-1, 0], s = "ab"`
- Output: `[false, true]`

---

## Solution
### Approach
The problem is solved using a combination of DFS traversal to determine subtree ranges (entry and exit times) and Rolling Hashing to verify palindromic properties in constant time. By mapping the tree to a linear array via DFS entry/exit times, the subtree of any node becomes a contiguous segment. We maintain prefix and suffix hashes of the DFS string to check if the segment is equal to its reverse.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes. We perform a single DFS to compute entry/exit times and subtree sizes, and another pass to compute hashes.
- **Space Complexity**: `O(n)` to store the adjacency list, entry/exit arrays, and hash tables.

### Reference Implementations
<details>
<summary>python</summary>

```python
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(parent, s):
    n = len(parent)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        adj[parent[i]].append(i)

    # Sort children to ensure consistent DFS order
    for i in range(n):
        adj[i].sort()

    tin = [0] * n
    tout = [0] * n
    timer = 0
    dfs_order = []

    def dfs(u):
        nonlocal timer
        tin[u] = timer
        for v in adj[u]:
            dfs(v)
        dfs_order.append(s[u])
        timer += 1
        tout[u] = timer - 1

    dfs(0)

    # Rolling Hash parameters
    P = 131
    MOD = (1 << 61) - 1

    pow_p = [1] * (n + 1)
    for i in range(1, n + 1):
        pow_p[i] = (pow_p[i - 1] * P) % MOD

    pref = [0] * (n + 1)
    suff = [0] * (n + 1)

    for i in range(n):
        val = ord(dfs_order[i]) - ord('a') + 1
        pref[i + 1] = (pref[i] * P + val) % MOD

    for i in range(n - 1, -1, -1):
        val = ord(dfs_order[i]) - ord('a') + 1
        suff[i] = (suff[i + 1] * P + val) % MOD

    def get_hash_pref(l, r):
        return (pref[r + 1] - pref[l] * pow_p[r - l + 1]) % MOD

    def get_hash_suff(l, r):
        return (suff[l] - suff[r + 1] * pow_p[r - l + 1]) % MOD

    res = [False] * n
    for i in range(n):
        l, r = tin[i], tout[i]
        if get_hash_pref(l, r) == get_hash_suff(l, r):
            res[i] = True

    return res
```
</details>
