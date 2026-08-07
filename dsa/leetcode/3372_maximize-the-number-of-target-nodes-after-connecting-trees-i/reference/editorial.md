[TOC]

## Solution

---

### Approach: Depth-First Search

#### Intuition

According to the problem statement, for the $i$-th query, when we connect the $i$-th node of the first tree to a node $j$ of the second tree, the distances from node $i$ to nodes in the second tree decrease, so more target nodes become reachable.

We must therefore compute:

* $\textit{count}\text{\_1}[i]$: the number of nodes in the **first** tree within distance $\le k$ of node $i$;
* $\textit{count}\text{\_2}[j]$: the number of nodes in the **second** tree within distance $\le k-1$ of node $j$.

Because $\textit{count}\text{\_2}[j]$ does not depend on the specific query, we can pre-compute it with a depth-first search (DFS) on the second tree. Afterward, we take the maximum value over all $j$, denoted $\textit{maxCount}_2 = \max_j \textit{count}\text{\_2}[j]$.

For each query $i$, we run a DFS on the first tree to obtain $\textit{count}\text{\_1}[i]$ and then return

$\textit{count}\text{\_1}[i] + \textit{maxCount}_2$

as the answer.

#### Implementation

```python
class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        def dfs(
            node: int, parent: int, children: List[List[int]], k: int
        ) -> int:
            if k < 0:
                return 0
            res = 1
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, children, k - 1)
            return res

        def build(edges: List[List[int]], k: int) -> List[int]:
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = [0] * n
            for i in range(n):
                res[i] = dfs(i, -1, children, k)
            return res

        n = len(edges1) + 1
        count1 = build(edges1, k)
        count2 = build(edges2, k - 1)
        maxCount2 = max(count2)
        res = [count1[i] + maxCount2 for i in range(n)]
        return res
```

#### Complexity Analysis

Let $n$ and $m$ be the numbers of nodes in the undirected trees defined by $\textit{edges}_1$ and $\textit{edges}_2$, respectively.

- Time complexity: $O(n^2 + m^2)$.

  We run a depth-first search (DFS) starting from every node in each tree, and each DFS visits all nodes of its tree.

- Space complexity: $O(n + m)$.

  We use two auxiliary arrays - one for each tree.