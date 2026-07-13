# Valid Arrangement of Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2097 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Graph Theory, Eulerian Circuit |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [valid-arrangement-of-pairs](https://leetcode.com/problems/valid-arrangement-of-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/valid-arrangement-of-pairs/).

### Goal
Reorder directed pairs so the end of each pair equals the start of the next pair, using every pair exactly once.

### Function Contract
**Inputs**

- `pairs`: directed edges `[start, end]`.

**Return value**

Return any valid arrangement of all pairs.

### Examples
**Example 1**

- Input: `pairs = [[5,1],[4,5],[11,9],[9,4]]`
- Output: `[[11,9],[9,4],[4,5],[5,1]]`

**Example 2**

- Input: `pairs = [[1,3],[3,2],[2,1]]`
- Output: `[[1,3],[3,2],[2,1]]`

**Example 3**

- Input: `pairs = [[1,2],[1,3],[2,1]]`
- Output: `[[1,2],[2,1],[1,3]]`

---

## Solution
### Approach
Treat pairs as directed graph edges and find an Eulerian trail with Hierholzer's algorithm. Start at a node with outdegree one greater than indegree when one exists; otherwise any node with outgoing edges works. Reverse the postorder trail to obtain edge order.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
