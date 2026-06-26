# Maximum Score of a Node Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2242 |
| Difficulty | Hard |
| Topics | Array, Graph Theory, Sorting, Enumeration |
| Official Link | [maximum-score-of-a-node-sequence](https://leetcode.com/problems/maximum-score-of-a-node-sequence/) |

## Problem Description & Examples
### Goal
Find four distinct graph nodes forming a three-edge sequence `a-b-c-d`. Its score is the sum of the four node scores. Return the maximum sequence score, or `-1` if no such sequence exists.

### Function Contract
**Inputs**

- `scores`: a score for each node.
- `edges`: undirected graph edges.

**Return value**

The maximum score of any valid four-node sequence, or `-1`.

### Examples
**Example 1**

- Input: `scores = [5, 2, 9, 8, 4]`, `edges = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]`
- Output: `24`

**Example 2**

- Input: `scores = [9, 20, 6, 4, 11, 12]`, `edges = [[0, 3], [5, 3], [2, 4], [1, 3]]`
- Output: `-1`

**Example 3**

- Input: `scores = [1, 2, 3, 4]`, `edges = [[0, 1], [1, 2], [2, 3]]`
- Output: `10`

---

## Underlying Base Algorithm(s)
For each node, retain only its three highest-scoring neighbors; at most two candidates can be disqualified by coinciding with the other nodes in a sequence. Treat every edge `(b, c)` as the middle edge and try each retained neighbor `a` of `b` with each retained neighbor `d` of `c`, accepting combinations with four distinct nodes.

---

## Complexity Analysis
- **Time Complexity**: `O(n + m)` with constant-sized neighbor lists
- **Space Complexity**: `O(n)`
