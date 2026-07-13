# Maximum Genetic Difference Query

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1938 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Depth-First Search, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-genetic-difference-query](https://leetcode.com/problems/maximum-genetic-difference-query/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-genetic-difference-query/).

### Goal
For each query, look at one node and all of its ancestors. Among those node labels, find the value that gives the largest XOR with the query value.

### Function Contract
**Inputs**

- `parents`: parent index for each node, with `-1` marking the root.
- `queries`: pairs `[node, value]`.

**Return value**

Return one answer per query in the original query order.

### Examples
**Example 1**

- Input: `parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]`
- Output: `[2,3,7]`

**Example 2**

- Input: `parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]`
- Output: `[6,14,7]`

**Example 3**

- Input: `parents = [-1], queries = [[0,0],[0,7]]`
- Output: `[0,7]`

---

## Solution
### Approach
Build the rooted tree and group queries by node. During DFS, insert the current node label into a binary trie before visiting its subtree and remove it afterward. Each query at that node is answered by greedily choosing opposite bits in the active trie.

### Complexity Analysis
- **Time Complexity**: `O((n + q) * B)`, where `B` is the bit width of node/query values.
- **Space Complexity**: `O(n * B + q)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
