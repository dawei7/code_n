## Examples

**Example 1**

- Input: `adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]`
- Output: `[[2, 4], [1, 3], [2, 4], [1, 3]]`
- Explanation: The graph has four nodes. Node 1 neighbors nodes 2 and 4; node 2 neighbors 1 and 3; node 3 neighbors 2 and 4; and node 4 neighbors 1 and 3. The clone has the same adjacency while using distinct node objects.

```text
Original graph       Deep copy
  1 ----- 2           1' ---- 2'
  |       |            |       |
  |       |            |       |
  4 ----- 3           4' ---- 3'
```

**Example 2**

- Input: `adjList = [[]]`
- Output: `[[]]`
- Explanation: The single empty inner list represents one node with `val = 1` and no neighbors.

```text
Original: (1)       Deep copy: (1')
```

**Example 3**

- Input: `adjList = []`
- Output: `[]`
- Explanation: The graph is empty and therefore has no nodes to clone.
