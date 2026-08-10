
## Solution

---

### Approach: Depth-First Search

#### Intuition

For the $i$-th query, after joining the two trees, the answer has two parts:

1. The number of nodes in the first tree that are an even distance from node $i$.
2. The number of nodes in the second tree that are an even distance from node $i$.

Suppose a tree contains $\textit{count}$ "target" nodes for node $u$, and node $v$ itself is a target of $u$. Then node $v$ also has exactly $\textit{count}$ target nodes.

To retrieve these counts quickly, we first color each tree with depth-first search: assign the root color 0 (white); every node at an even distance from the root also gets color 0, and every node at an odd distance gets color 1 (black). We record the total number of white and black nodes. For any node, the number of its target nodes equals the number of nodes that share its color.

This yields two arrays, $\textit{color}_1$ and $\textit{color}_2$, storing the colors of the nodes in the two trees, along with the counts of white and black nodes in each tree. Then, for the $i$-th query:

1. Look up $\textit{color}\text{_1}[i]$; the count of nodes with that color in the first tree gives the first part of the answer.
2. Regardless of how the trees are connected, node $i$ "sees" only one color in the second tree, so the second part is simply $\max(\text{white}_2,\ \text{black}_2)$.

#### Implementation

```python
class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def dfs(node, parent, depth, children, color):
            res = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, depth + 1, children, color)
            return res

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = dfs(0, -1, 0, children, color)
            return [res, n - res]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        res = [0] * n
        for i in range(n):
            res[i] = count1[color1[i]] + max(count2[0], count2[1])
        return res
```

#### Complexity Analysis

Let $n$ and $m$ be the numbers of nodes in the undirected trees represented by $\textit{edges}_1$ and $\textit{edges}_2$, respectively.

- Time complexity: $O(n + m)$.

  Coloring all nodes in both trees takes $O(n + m)$ time, and each query can then be answered in $O(1)$.

- Space complexity: $O(n + m)$.

  Two arrays are required to store the colors of the nodes in each tree.