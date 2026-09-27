# Guided Example: Redundant Connection

We trace the step-by-step Disjoint Set Union (DSU / Union-Find) representative root tracking, recursive path compression ($p[x] = find(p[x])$), dynamic component unioning, cycle detection via shared-component ancestry ($find(u) == find(v)$), and latest-occurring redundant edge isolation on representative unweighted undirected graphs:

- **Input:** $edges = [[1, 2], [1, 3], [2, 3]]$
- **Required output:** `[2, 3]`
  - Graph theory context:
    - A tree with $n$ vertices has exactly $n - 1$ edges, is connected, and contains **zero cycles**.
    - The input graph contains $n$ vertices and $n$ edges, which means exactly **one redundant edge** was added, introducing a single fundamental cycle.
    - Removing any edge along the cycle restores tree topology.
    - Tie-breaking requirement: If multiple edges could be removed, return the edge that **appears last** in the input list.
- **Disjoint Set Union & Incremental Spanning Tree Invariant:**
  - **The Spanning Tree Property:**
    - If an edge $(u, v)$ connects two vertices that currently belong to **different connected components** ($find(u) \ne find(v)$):
      - This edge is an essential bridge for connectivity.
      - We union the two components: $p[find(u)] \leftarrow find(v)$.
      - No cycle is created.
  - **The Cycle Closure Invariant:**
    - If an edge $(u, v)$ connects two vertices that **already belong to the same connected component** ($find(u) == find(v)$):
      - A path already exists between $u$ and $v$ through previously processed tree edges.
      - Introducing $(u, v)$ creates an alternate path, thereby completing a simple cycle!
    - Because we process edges in the exact forward order of the input, the edge that triggers $find(u) == find(v)$ is precisely the **latest-occurring edge on that cycle**.
    - Returning this edge immediately satisfies both connectivity and the tie-breaking rule.
- **Step-by-Step Worked Execution Trace on $edges = [[1, 2], [1, 3], [2, 3]]$ ($n = 3$):**
  - Setup: $n = 3$ nodes (indices $0, 1, 2$ for 1-indexed nodes $1, 2, 3$).
  - Initialize parent pointers where every node is its own representative:
    $$
    p = [0, \; 1, \; 2]
    $$
    - Node 1: component $\{1\}$
    - Node 2: component $\{2\}$
    - Node 3: component $\{3\}$
  - **Edge 1: $[1, 2]$:**
    - Query representatives:
      $$
      pa = find(0) = 0, \quad pb = find(1) = 1
      $$
    - Compare components:
      $$
      pa \ne pb \quad (0 \ne 1) \implies \mathbf{Disjoint\ Components}
      $$
    - Union components: link root $0$ to root $1$:
      $$
      p[0] \leftarrow 1 \implies p = [1, \; 1, \; 2]
      $$
    - Component state: $\{1, 2\}$ and $\{3\}$.
  - **Edge 2: $[1, 3]$:**
    - Query representatives:
      $$
      pa = find(0) = find(p[0]) = find(1) = \mathbf{1}
      $$
      $$
      pb = find(2) = \mathbf{2}
      $$
    - Compare components:
      $$
      pa \ne pb \quad (1 \ne 2) \implies \mathbf{Disjoint\ Components}
      $$
    - Union components: link root $1$ to root $2$:
      $$
      p[1] \leftarrow 2 \implies p = [1, \; 2, \; 2]
      $$
    - Component state: $\{1, 2, 3\}$ (all three nodes are now connected into a single tree).
  - **Edge 3: $[2, 3]$:**
    - Query representatives:
      $$
      pa = find(1) = find(p[1]) = find(2) = \mathbf{2}
      $$
      $$
      pb = find(2) = \mathbf{2}
      $$
    - Compare components:
      $$
      pa == pb \quad (\mathbf{2 == 2}) \implies \mathbf{Cycle\ Detected!}
      $$
    - Node 2 and Node 3 are already connected via the path $2 - 1 - 3$.
    - Adding edge $[2, 3]$ creates the cycle $1 - 2 - 3 - 1$.
    - Because this is the edge closing the cycle in forward input order, it is the redundant connection to remove!
    - Return **`[2, 3]`**.
- **Larger Graph with Tree Branches ($edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]$):**
  - Edges $[1, 2], [2, 3], [3, 4]$ union into component $\{1, 2, 3, 4\}$.
  - Edge $[1, 4]$: both $1$ and $4$ share root $4 \implies$ Cycle detected!
  - Return `[1, 4]`.
  - Notice: Branch edge $[1, 5]$ is never reached because the redundant edge was already isolated.

This instance demonstrates incremental graphic matroid spanning forest construction and Disjoint Set Union cycle identification, mathematically proves why forward greedy component maintenance isolates the latest cycle-forming edge, and derives nearly linear $O(N \cdot \alpha(N))$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an undirected graph with $n$ nodes and $n$ edges (a tree with 1 extra edge):
Find the edge whose removal restores a tree.
If multiple edges qualify, return the one that appears **last in the input**.

```text
edges = [ [1, 2], [1, 3], [2, 3] ]

Step 1: Edge [1, 2] -> Union(1, 2) -> Component {1, 2}
Step 2: Edge [1, 3] -> Union(1, 3) -> Component {1, 2, 3}
Step 3: Edge [2, 3] -> Both 2 and 3 are ALREADY in Component {1, 2, 3}!
                       Adding [2, 3] closes a cycle!

Redundant Edge: [2, 3]
```

### The Invariant of Union-Find Cycle Detection
- In an undirected forest, adding an edge $(u, v)$ creates a cycle if and only if $u$ and $v$ already share the same representative root ($find(u) == find(v)$).
- Processing edges in their given order guarantees the first cycle-creating edge found is the last-occurring edge on that cycle.

---

## 2. Conceptual Foundation & Invariants

### 1. The Disjoint Set Find with Path Compression:
$$
find(x) = \begin{cases} x & \text{if } p[x] == x \\ p[x] \leftarrow find(p[x]) & \text{otherwise} \end{cases}
$$

### 2. Edge Processing Loop:
For each edge $(a, b)$:
$$
pa = find(a), \quad pb = find(b)
$$
$$
\text{If } pa == pb \implies \text{return } [a, b]
$$
$$
\text{Else } p[pa] \leftarrow pb
$$

> **Graphic Matroid Cycle Invariant.** In the graphic matroid $M(G)$, the set of edges forming a forest is an independent set. The first edge whose insertion causes linear dependence over the vertex incidence matrix corresponds precisely to the unique fundamental cycle of $G$.

---

## 3. Step-by-Step Worked Execution

We trace $edges = [[1, 2], [1, 3], [2, 3]]$:

---

### Step 1: Edge $[1, 2]$
- $find(1) = 1, find(2) = 2$.
- $1 \ne 2 \implies Union(1, 2)$.

---

### Step 2: Edge $[1, 3]$
- $find(1) = 2, find(3) = 3$.
- $2 \ne 3 \implies Union(2, 3)$.

---

### Step 3: Edge $[2, 3]$
- $find(2) = 3$.
- $find(3) = 3$.
- $find(2) == find(3) \implies$ Cycle!
- Return **`[2, 3]`**.

---

## 4. Complete Execution Trace

| Edge Processed | Node $u$ Component | Node $v$ Component | Equal Roots? | DSU Action Taken | State of Forest |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $[1, 2]$ | Root 1 | Root 2 | No | $Union(1, 2)$ | $\{1, 2\}$, $\{3\}$ |
| $[1, 3]$ | Root 2 | Root 3 | No | $Union(2, 3)$ | $\{1, 2, 3\}$ |
| **$[2, 3]$** | **Root 3** | **Root 3** | **Yes (`3 == 3`)** | **Cycle Encountered** | **`[2, 3]` Identified** |

---

## 5. Boundary Cases & Failure Modes

- **Triangle Cycle ($N = 3$):** Minimal cycle length $\implies$ accurately detected at 3rd edge.
- **Large Cycle ($N = 1000$):** Spanning tree builds $N-1$ edges, then the final edge closes the large polygon.
- **Tree Branch Attached to Cycle:** Disjoint set union ignores tree branches after the cycle edge is returned.

---

## 6. Traps & Common Anti-Patterns

- **Building Full Adjacency List First ($O(N^2)$ DFS cycle finding):** DSU finds the cycle online during a single pass in $O(N \alpha(N))$ time without building graph adjacency lists.
- **1-Indexed vs 0-Indexed Node Offsets:** Watch for 1-indexed node numbers $1 \dots n$; map to $0 \dots n-1$ when indexing arrays.
- **Missing Path Compression:** Without path compression, trees can degenerate into linear chains, raising find operations from $O(\alpha(N))$ to $O(N)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $N$ edges processed.
  - Each edge performs at most 2 `find` operations and 1 `union` operation.
  - With path compression, amortized cost per operation is $\mathcal{O}(\alpha(N))$ where $\alpha$ is the Inverse Ackermann function ($\alpha(N) < 5$ for all practical $N$).
  - Total Time: $\mathcal{O}(N \cdot \alpha(N)) \approx \mathcal{O}(N)$. Completes in $< 1$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the parent array $p$.
