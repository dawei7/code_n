# Guided Example: Number of Connected Components in an Undirected Graph

We trace the step-by-step undirected adjacency list representation, depth-first search component flooding, visited set membership caching (`vis`), and connected component counting on representative graph instances:

- **Input:** $n = 5, \quad \text{edges} = [[0, 1], [1, 2], [3, 4]]$
- **Required output:** $2$
  - Component 1: Vertices $\{0, 1, 2\}$ connected by edges $[0, 1]$ and $[1, 2]$
  - Component 2: Vertices $\{3, 4\}$ connected by edge $[3, 4]$
  - Total connected components: $2$
- **Single Component Instance:** $n = 5, \text{edges} = [[0, 1], [1, 2], [2, 3], [3, 4]] \implies 1$
- **Completely Disconnected Instance:** $n = 4, \text{edges} = [] \implies 4$ (Every isolated node is its own component)
- **Cyclic Graph Component:** A triangle graph $[[0, 1], [1, 2], [2, 0]]$ forms 1 connected component

This instance demonstrates connected component partition algorithms on undirected graphs, formalizes the distinction between fresh root exploration and intra-component recursion, proves why marking nodes in `vis` upon entrance prevents infinite cycle loops, and analyzes $O(V + E)$ linear time and space bounds.

---

## 1. Instance & Teaching Goal

Given $n = 5$ vertices labeled $0$ to $4$ and $3$ undirected edges:
$$
\text{edges} = [[0, 1], [1, 2], [3, 4]]
$$
Find the total number of connected components in the graph:

```text
Graph Topology:
  0 --- 1 --- 2        3 --- 4

Component 1: {0, 1, 2}
Component 2: {3, 4}

Total Components: 2
```

### Connected Component Invariant
An undirected graph partitions into disjoint equivalence classes of mutually reachable vertices:
- Starting a traversal (DFS or BFS) at any unvisited node $u$ traverses all vertices in $u$'s connected component.
- Marking all reached nodes in a `vis` set ensures that each component is counted **exactly once**.
- Isolated nodes with degree $0$ have no edges and are counted as single-vertex components.

---

## 2. Conceptual Foundation & Invariants

### 1. Bidirectional Adjacency List
Undirected edges must be recorded in both directions:
For each $[a, b] \in edges$:
- $g[a].\text{append}(b)$
- $g[b].\text{append}(a)$

### 2. Traversal Counting Function `dfs(i)`:
- If $i \in vis$: return $0$ (Already accounted for in a previously discovered component).
- If $i \notin vis$:
  - Add $i$ to $vis$.
  - For each neighbor $j \in g[i]$: call $dfs(j)$ (Return values from recursive neighbor calls are ignored).
  - Return $1$ (Signaling that node $i$ discovered exactly **one new component**).
- Result: $\sum_{i=0}^{n-1} dfs(i)$.

> **Invariant.** For each index $i \in [0, n-1]$, $dfs(i)$ returns $1$ if and only if $i$ belongs to a previously undiscovered connected component.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $n = 5$, $\text{edges} = [[0, 1], [1, 2], [3, 4]]$:
Adjacency lists:
- $0: [1]$
- $1: [0, 2]$
- $2: [1]$
- $3: [4]$
- $4: [3]$
Initialize `vis = set()`.

---

### Step 1: Process Node $i = 0$
- $0 \notin vis$.
- Mark: `vis.add(0)`.
- Follow neighbor $1 \in g[0]$:
  - $1 \notin vis \implies$ `vis.add(1)`.
  - Neighbors of 1:
    - $0 \in vis \implies$ returns 0.
    - Follow neighbor $2 \in g[1]$:
      - $2 \notin vis \implies$ `vis.add(2)`.
      - Neighbor $1 \in vis \implies$ returns 0.
- All reachable nodes from 0 visited: $\{0, 1, 2\}$.
- $dfs(0)$ returns **$1$** (Discovered Component 1!).
- Active `vis` set: $\{0, 1, 2\}$.

---

### Step 2: Process Node $i = 1$
- Check: $1 \in vis$ (**True**).
- $dfs(1)$ immediately returns **$0$**.

---

### Step 3: Process Node $i = 2$
- Check: $2 \in vis$ (**True**).
- $dfs(2)$ immediately returns **$0$**.

---

### Step 4: Process Node $i = 3$
- $3 \notin vis$.
- Mark: `vis.add(3)`.
- Follow neighbor $4 \in g[3]$:
  - $4 \notin vis \implies$ `vis.add(4)`.
  - Neighbor $3 \in vis \implies$ returns 0.
- All reachable nodes from 3 visited: $\{3, 4\}$.
- $dfs(3)$ returns **$1$** (Discovered Component 2!).
- Active `vis` set: $\{0, 1, 2, 3, 4\}$.

---

### Step 5: Process Node $i = 4$
- Check: $4 \in vis$ (**True**).
- $dfs(4)$ immediately returns **$0$**.

---

### Step 6: Total Components
Sum over all $i \in [0, 4]$:
$$
\text{Total} = dfs(0) + dfs(1) + dfs(2) + dfs(3) + dfs(4) = 1 + 0 + 0 + 1 + 0 = \mathbf{2}
$$

---

## 4. Complete Execution Trace

```text
n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Adjacency:
  0: [1]
  1: [0, 2]
  2: [1]
  3: [4]
  4: [3]

i=0: not in vis -> mark {0, 1, 2} -> returns 1 (Component 1)
i=1: in vis     -> returns 0
i=2: in vis     -> returns 0
i=3: not in vis -> mark {3, 4}    -> returns 1 (Component 2)
i=4: in vis     -> returns 0

Total Count = 1 + 0 + 0 + 1 + 0 = 2
```

| Outer Node $i$ | Initially in `vis`? | Action Taken | Nodes Reached in Traversal | `vis` Set After Call | Return Value $dfs(i)$ | Cumulative Count |
|:---:|:---:|:---|:---:|:---|:---:|:---:|
| **0** | **No** | **Explore Component** | $\{0, 1, 2\}$ | $\{0, 1, 2\}$ | **1** | **1** |
| 1 | Yes | Skip | - | $\{0, 1, 2\}$ | 0 | 1 |
| 2 | Yes | Skip | - | $\{0, 1, 2\}$ | 0 | 1 |
| **3** | **No** | **Explore Component** | $\{3, 4\}$ | $\{0, 1, 2, 3, 4\}$ | **1** | **2** |
| 4 | Yes | Skip | - | $\{0, 1, 2, 3, 4\}$ | 0 | 2 |

---

## 5. Algorithmic Correctness

**Soundness.** Undirected graph connectivity is an equivalence relation. A DFS from vertex $u$ visits all vertices connected to $u$ by a path. Because every visited vertex is recorded in `vis`, subsequent iterations over vertices in the same component return $0$. Only the first explored vertex of each component returns $1$.

**Completeness.** The outer loop iterates over every vertex $i \in [0, n-1]$. No vertex can be overlooked, even if it has degree $0$ (isolated). Since every connected component contains at least one vertex that triggers a fresh DFS call, all connected components are counted.

---

## 6. Traps This Instance Exposes

- **Undirected Edges Stored One-Way:** Forgetting to add the reverse direction `g[b].append(a)` treats the graph as directed, causing components with opposing arrows to be falsely counted as separate components.
- **Marking After Neighbor Loop:** If `vis.add(i)` is placed *after* the neighbor loop, an edge from $u$ to $v$ will immediately call $u$ back from $v$, causing infinite recursion and call stack overflow.
- **Counting Isolated Vertices:** An isolated vertex with no edges still constitutes a valid connected component of size 1. Sizing the adjacency list by $n$ ensures isolated nodes are evaluated.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V + E)$, where $V = n$ is the number of vertices and $E$ is the number of edges.
  - Constructing the adjacency list takes $O(V + E)$ time.
  - Each vertex is visited by the outer loop once and traversed in DFS once.
  - Each undirected edge is traversed exactly twice (once from each endpoint).
- **Auxiliary Space Complexity:** $O(V + E)$ auxiliary memory for the adjacency list $g$ and visited set `vis`.
