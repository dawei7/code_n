## Examples

**Example 1**

- **Input:** `n = 7, edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6]], query = [[5, 3, 4], [5, 3, 6]]`
- **Output:** `[0, 2]`
- **Explanation:**
  - Path from 5 to 3 is `[5, 2, 0, 3]`.
  - For query `[5, 3, 4]`, the node on path `[5, 2, 0, 3]` closest to 4 is node 0 (distance 2).
  - For query `[5, 3, 6]`, the node on path `[5, 2, 0, 3]` closest to 6 is node 2 (distance 1).

**Example 2**

- **Input:** `n = 3, edges = [[0, 1], [1, 2]], query = [[0, 1, 2]]`
- **Output:** `[1]`
- **Explanation:** Path from 0 to 1 is `[0, 1]`. The node on `[0, 1]` closest to 2 is node 1 (distance 1).

**Example 3**

- **Input:** `n = 3, edges = [[0, 1], [1, 2]], query = [[0, 0, 0]]`
- **Output:** `[0]`
- **Explanation:** Path from 0 to 0 is `[0]`. The node closest to 0 is node 0 itself (distance 0).
