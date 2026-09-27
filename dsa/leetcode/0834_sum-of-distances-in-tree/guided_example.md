# Guided Example: Sum of Distances in Tree

We trace the step-by-step tree re-rooting dynamic programming technique, bottom-up subtree size aggregation ($size[u] = 1 + \sum size[v]$), depth summation root initialization ($ans[0] = \sum depth[u]$), top-down centroid rerooting transition ($ans[v] = ans[u] + n - 2 \cdot size[v]$), and complete distance profile extraction on representative tree graphs:

- **Input:**
  $$
  n = 6, \quad edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
  $$
- **Required output:**
  $$
  [8, 12, 6, 10, 10, 10]
  $$
  - Tree distance specifications:
    - We have an undirected connected tree with $n$ vertices and $n - 1$ edges.
    - The distance between two nodes is the number of edges on the unique simple path between them.
    - Objective: Calculate $ans[u] = \sum_{v = 0}^{n - 1} \text{dist}(u, v)$ for every node $u \in [0, n - 1]$.
    - For the 6-node tree:
      - Node 0 connects to 1 and 2. Node 2 connects to 3, 4, 5.
      - Distances from Node 0:
        - To 0: 0
        - To 1: 1
        - To 2: 1
        - To 3, 4, 5: 2 each ($3 \times 2 = 6$)
        - Total: $0 + 1 + 1 + 2 + 2 + 2 = \mathbf{8}$.
      - Distances from Node 2:
        - To 2: 0
        - To 0: 1
        - To 3, 4, 5: 1 each ($3 \times 1 = 3$)
        - To 1: 2 (via 0)
        - Total: $0 + 1 + 3 + 2 = \mathbf{6}$.
      - Distances from Node 1:
        - To 1: 0
        - To 0: 1
        - To 2: 2
        - To 3, 4, 5: 3 each ($3 \times 3 = 9$)
        - Total: $0 + 1 + 2 + 9 = \mathbf{12}$.
      - Distances from Leaf Nodes 3, 4, 5: 10 each.
      - Output: `[8, 12, 6, 10, 10, 10]`.
- **Tree Re-Rooting DP Invariant:**
  - **The Rerooting Differential:**
    - Suppose we know $ans[u]$, the sum of distances from node $u$ to all nodes in the tree.
    - If we move the root across an edge $(u, v)$ to adjacent node $v$:
      - The tree is partitioned into two disjoint sets of nodes:
        1. Nodes in the subtree of $v$ (with cardinality $size[v]$).
        2. All other nodes in the tree (with cardinality $n - size[v]$).
      - For every node in $v$'s subtree, moving the root from $u$ to $v$ moves the root **1 step closer**:
        $$
        \Delta_1 = -size[v]
        $$
      - For every node outside $v$'s subtree, moving the root from $u$ to $v$ moves the root **1 step farther away**:
        $$
        \Delta_2 = +(n - size[v])
        $$
      - Combining both shifts gives the fundamental re-rooting formula:
        $$
        ans[v] = ans[u] - size[v] + (n - size[v]) = ans[u] + n - 2 \cdot size[v]
        $$
  - **Two-Pass Tree Traversal:**
    - **Pass 1 (Post-Order DFS from Node 0):**
      - Compute subtree sizes $size[u]$ and depth sum $ans[0] = \sum \text{depth}[u]$.
    - **Pass 2 (Pre-Order DFS from Node 0):**
      - Propagate $ans[v] = ans[u] + n - 2 \cdot size[v]$ down to all children.
- **Step-by-Step Worked Execution Trace on the 6-Node Tree:**
  - Adjacency list:
    - $g[0] = [1, 2]$
    - $g[1] = [0]$
    - $g[2] = [0, 3, 4, 5]$
    - $g[3] = [2], \; g[4] = [2], \; g[5] = [2]$
  - **Pass 1: Bottom-Up Post-Order DFS (`dfs1(0, -1, 0)`):**
    - Leaves $1, 3, 4, 5$:
      - $size[1] = 1, \text{depth}[1] = 1$
      - $size[3] = 1, \text{depth}[3] = 2$
      - $size[4] = 1, \text{depth}[4] = 2$
      - $size[5] = 1, \text{depth}[5] = 2$
    - Node 2:
      - Has children $3, 4, 5$ and depth 1.
      - $size[2] = 1 + size[3] + size[4] + size[5] = 1 + 1 + 1 + 1 = \mathbf{4}$.
    - Node 0 (Root):
      - Depth 0.
      - $size[0] = 1 + size[1] + size[2] = 1 + 1 + 4 = \mathbf{6}$.
    - Root distance sum:
      $$
      ans[0] = \text{depth}[0] + \text{depth}[1] + \text{depth}[2] + \text{depth}[3] + \text{depth}[4] + \text{depth}[5]
      $$
      $$
      ans[0] = 0 + 1 + 1 + 2 + 2 + 2 = \mathbf{8}
      $$
    - Subtree size vector:
      $$
      size = [6, \; 1, \; 4, \; 1, \; 1, \; 1]
      $$
  - **Pass 2: Top-Down Pre-Order Rerooting (`dfs2(0, -1, 8)`):**
    - Initial root state: $ans[0] = \mathbf{8}$.
    - **Step to Child 1 from Parent 0:**
      $$
      ans[1] = ans[0] + n - 2 \cdot size[1] = 8 + 6 - 2(1) = 14 - 2 = \mathbf{12}
      $$
    - **Step to Child 2 from Parent 0:**
      $$
      ans[2] = ans[0] + n - 2 \cdot size[2] = 8 + 6 - 2(4) = 14 - 8 = \mathbf{6}
      $$
    - **Steps from Parent 2 to its Children ($3, 4, 5$):**
      - **To Child 3:**
        $$
        ans[3] = ans[2] + n - 2 \cdot size[3] = 6 + 6 - 2(1) = 12 - 2 = \mathbf{10}
        $$
      - **To Child 4:**
        $$
        ans[4] = ans[2] + n - 2 \cdot size[4] = 6 + 6 - 2(1) = \mathbf{10}
        $$
      - **To Child 5:**
        $$
        ans[5] = ans[2] + n - 2 \cdot size[5] = 6 + 6 - 2(1) = \mathbf{10}
        $$
  - **Assembly of Global Distance Array:**
    $$
    ans = [8, \; 12, \; 6, \; 10, \; 10, \; 10]
    $$
- **Star Graph Centroid Trace ($n = 4$, edges: $[[0, 1], [0, 2], [0, 3]]$):**
  - Root 0 is the center: distances to leaves are $1 + 1 + 1 = 3 \implies ans[0] = \mathbf{3}$.
  - Each leaf $v$: $ans[v] = ans[0] + 4 - 2(1) = 3 + 2 = \mathbf{5}$ (1 to root, 2 to other leaves).
  - Result: $[3, 5, 5, 5]$.
- **Single Node Tree Trace ($n = 1$, edges = `[]`):**
  - $ans[0] = \mathbf{0}$.

This instance demonstrates tree metric spaces and global potential propagation via group actions on cut partitions, mathematically proves why edge cut bipartitioning reduces $O(N^2)$ all-pairs shortest paths to two linear DFS sweeps, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an undirected tree of $n$ nodes:
Find the sum of distances from **each node** to all other nodes.

```text
Edges: (0, 1), (0, 2), (2, 3), (2, 4), (2, 5)

Tree layout:
        0
       / \
      1   2
         /|\
        3 4 5

Root at 0:
  Distances from 0: [ 0, 1, 1, 2, 2, 2 ] -> sum = 8

Re-rooting to 2:
  Nodes in 2's subtree (2, 3, 4, 5) are 1 step closer (-4).
  Nodes outside (0, 1) are 1 step further (+2).
  ans[2] = 8 - 4 + 2 = 6

Result: [ 8, 12, 6, 10, 10, 10 ]
```

### The Invariant of Re-Rooting Dynamic Programming
- Transition from parent $u$ to child $v$:
  $$
  ans[v] = ans[u] - size[v] + (n - size[v]) = ans[u] + n - 2 \cdot size[v]
  $$
- Two passes:
  1. Bottom-up: compute subtree sizes and $ans[0]$.
  2. Top-down: propagate answers to all children using the formula.

---

## 2. Conceptual Foundation & Invariants

### 1. Edge Bipartition Metric:
Every edge $e = (u, v)$ partitions $V$ into $V_v$ (subtree of $v$) and $V \setminus V_v$.
$$
\text{dist}(v, w) = \begin{cases}
\text{dist}(u, w) - 1 & w \in V_v \\
\text{dist}(u, w) + 1 & w \notin V_v
\end{cases}
$$

### 2. Global Rerooting Operator:
$$
\sum_{w \in V} \text{dist}(v, w) = \sum_{w \in V} \text{dist}(u, w) - |V_v| + |V \setminus V_v|
$$
$$
ans[v] = ans[u] + n - 2 \cdot size[v]
$$

> **Potential Translation Invariant.** The Wiener potential function $W(u) = \sum_v d(u, v)$ on trees satisfies the discrete gradient relation $\nabla_e W = |V_u| - |V_v| = n - 2 |V_v|$. Since the tree graph is cycle-free, integrating this gradient from an arbitrary base vertex yields the exact potential field globally.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Compute Sizes and $ans[0]$
- $size = [6, 1, 4, 1, 1, 1]$.
- $ans[0] = 0 + 1 + 1 + 2 + 2 + 2 = \mathbf{8}$.

---

### Step 2: Reroot to Child 1
- $ans[1] = 8 + 6 - 2(1) = \mathbf{12}$.

---

### Step 3: Reroot to Child 2
- $ans[2] = 8 + 6 - 2(4) = \mathbf{6}$.

---

### Step 4: Reroot from 2 to Children 3, 4, 5
- $ans[3] = 6 + 6 - 2(1) = \mathbf{10}$.
- $ans[4] = 6 + 6 - 2(1) = \mathbf{10}$.
- $ans[5] = 6 + 6 - 2(1) = \mathbf{10}$.

---

### Step 5: Output
$$
[8, \; 12, \; 6, \; 10, \; 10, \; 10]
$$

---

## 4. Complete Execution Trace

| Step | Current Node $v$ | Parent Node $u$ | Subtree Size $size[v]$ | Formula $ans[u] + n - 2 \cdot size[v]$ | Computed Distance Sum $ans[v]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Base Root | $0$ | None | $6$ | Direct Depth Sum | **$8$** |
| Step $0 \to 1$ | $1$ | $0$ | $1$ | $8 + 6 - 2(1)$ | **$12$** |
| Step $0 \to 2$ | $2$ | $0$ | $4$ | $8 + 6 - 2(4)$ | **$6$** |
| Step $2 \to 3$ | $3$ | $2$ | $1$ | $6 + 6 - 2(1)$ | **$10$** |
| Step $2 \to 4$ | $4$ | $2$ | $1$ | $6 + 6 - 2(1)$ | **$10$** |
| **Step $2 \to 5$** | **$5$** | **$2$** | **$1$** | **$6 + 6 - 2(1)$** | **`10`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node ($n = 1$):** Returns `[0]`.
- **Linear Path Graph ($0 - 1 - 2 - \dots - n-1$):** Re-rooting traverses down the chain; ends have maximal distance sum, center has minimal sum.
- **Star Graph:** Center has distance sum $n - 1$, leaves have $n - 1 + 2(n - 2)$.
- **Large Tree ($N = 30,000$):** Two linear passes execute $\le 6 \times 10^4$ function calls; completes in $< 20$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Running BFS from Every Node ($O(N^2)$):** For $N = 30,000$, $N^2 = 9 \times 10^8$ operations, causing severe Time Limit Exceeded. Re-rooting DP achieves strictly $O(N)$ runtime.
- **Using Subtree Size of Parent Instead of Child:** The formula subtracts $size[v]$ (the child's subtree size), NOT $size[u]$.
- **Recursion Depth Overflow:** In deep chain trees, ensure recursion limit allows depth $N$ or use an iterative post-order traversal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building adjacency list: $\mathcal{O}(N)$ where $N \le 30,000$.
  - Post-order DFS (`dfs1`): visits every node and edge once $\implies \mathcal{O}(N)$.
  - Pre-order DFS (`dfs2`): visits every node and edge once $\implies \mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the graph adjacency list, `size` array, and call stack.