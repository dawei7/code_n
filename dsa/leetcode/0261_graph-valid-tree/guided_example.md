# Guided Example: Graph Valid Tree

We trace the step-by-step edge count necessity theorem ($|E| == n - 1$), Disjoint Set Union (DSU) cycle detection, and connectivity convergence on representative undirected graphs:

- **Input:** $n = 5, \quad \text{edges} = [[0, 1], [0, 2], [0, 3], [1, 4]]$
- **Required output:** `true` (Forms a single connected acyclic tree of 5 nodes and 4 edges)
- **Cycle Instance:** $n = 5, \quad \text{edges} = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]] \implies \text{false}$ (Contains a 3-cycle $\{1, 2, 3\}$ and $|E| = 5 \ne 4$)
- **Disconnected Forest Instance:** $n = 4, \quad \text{edges} = [[0, 1], [2, 3]] \implies \text{false}$ (Two disjoint components; $|E| = 2 \ne 3$)
- **Single Node Graph:** $n = 1, \quad \text{edges} = [] \implies \text{true}$ (Trivially a valid tree)

This instance demonstrates fundamental tree equivalence theorems in graph theory, shows why verifying $|E| == n - 1$ combined with zero cycle detections guarantees full connectivity, details DSU path compression operations, and runs in near-linear $O(N \cdot \alpha(N))$ time.

---

## 1. Instance & Teaching Goal

Given an undirected graph with $n = 5$ nodes and edges:
$$
\text{edges} = [[0, 1], [0, 2], [0, 3], [1, 4]]
$$
Determine whether the graph is a **valid tree**.

```text
Graph topology:
        0
      / | \
     1  2  3
     |
     4
```

### The Fundamental Tree Equivalence Theorem
In graph theory, for any undirected graph $G = (V, E)$ with $|V| = n$ vertices, $G$ is a **tree** if and only if any two of the following statements hold:
1. $G$ is **connected**.
2. $G$ is **acyclic** (contains no cycles).
3. $|E| = n - 1$.

This mathematical equivalence provides an immediate optimization:
- If $|E| \ne n - 1$, the graph **cannot be a tree**:
  - If $|E| < n - 1$, the graph is guaranteed to be **disconnected** (a forest of at least two components).
  - If $|E| > n - 1$, the graph is guaranteed to contain at least one **cycle**.
- If $|E| == n - 1$, we only need to test **acyclicity**: if no cycle exists, full connectivity is mathematically guaranteed!

---

## 2. Conceptual Foundation & Invariants

### DSU (Union-Find) with Path Compression
Maintain a parent array `parent = [0, 1, ..., n - 1]`:
1. **Initial Edge Count Check:**
   If $\text{len}(\text{edges}) \ne n - 1$:
   $$
   \text{return false}
   $$
2. **Find with Path Compression:**
   Recursively locate the representative root of component $x$, flattening the path:
   $$
   \text{find}(x) = \begin{cases}
   x, & \text{if } \text{parent}[x] == x \\
   \text{parent}[x] \leftarrow \text{find}(\text{parent}[x]), & \text{otherwise}
   \end{cases}
   $$
3. **Union and Cycle Detection:**
   For each edge $(u, v) \in \text{edges}$:
   - $\text{root}_u = \text{find}(u)$
   - $\text{root}_v = \text{find}(v)$
   - **Cycle Condition:**
     If $\text{root}_u == \text{root}_v$:
     Vertices $u$ and $v$ were already connected by an existing path! Adding edge $(u, v)$ creates an alternate path, forming a **cycle**.
     $$
     \text{return false}
     $$
   - Otherwise, link roots: $\text{parent}[\text{root}_u] = \text{root}_v$.
4. Return `true`.

> **Invariant.** After processing $k$ edges without finding a cycle, the graph consists of exactly $n - k$ connected tree components. When $k = n - 1$, exactly $1$ component remains.

---

## 3. Step-by-Step Worked Execution

We trace $n = 5$ with $\text{edges} = [[0, 1], [0, 2], [0, 3], [1, 4]]$:

### Step 1: Cardinality Guard
- Vertices: $n = 5$.
- Required edge count: $n - 1 = 4$.
- Given edge count: $\text{len}(\text{edges}) = 4$.
- $4 == 4 \implies$ Pre-condition passed!

---

### Step 2: Initialize DSU
$$
\text{parent} = [0, 1, 2, 3, 4] \quad (\text{Each node is its own root})
$$

---

### Step 3: Edge 1 — $[0, 1]$
- $\text{root}_0 = \text{find}(0) = 0$.
- $\text{root}_1 = \text{find}(1) = 1$.
- Distinct roots ($0 \ne 1$) $\implies$ No cycle.
- Union: set $\text{parent}[1] = 0$.
- State: $\text{parent} = [0, 0, 2, 3, 4]$.

---

### Step 4: Edge 2 — $[0, 2]$
- $\text{root}_0 = \text{find}(0) = 0$.
- $\text{root}_2 = \text{find}(2) = 2$.
- Distinct roots ($0 \ne 2$) $\implies$ No cycle.
- Union: set $\text{parent}[2] = 0$.
- State: $\text{parent} = [0, 0, 0, 3, 4]$.

---

### Step 5: Edge 3 — $[0, 3]$
- $\text{root}_0 = \text{find}(0) = 0$.
- $\text{root}_3 = \text{find}(3) = 3$.
- Distinct roots ($0 \ne 3$) $\implies$ No cycle.
- Union: set $\text{parent}[3] = 0$.
- State: $\text{parent} = [0, 0, 0, 0, 4]$.

---

### Step 6: Edge 4 — $[1, 4]$
- Find root of 1: $\text{parent}[1] = 0 \implies \text{find}(1) = 0$.
- Find root of 4: $\text{find}(4) = 4$.
- Distinct roots ($0 \ne 4$) $\implies$ No cycle.
- Union: set $\text{parent}[4] = 0$.
- State: $\text{parent} = [0, 0, 0, 0, 0]$.

All $n - 1 = 4$ edges processed with zero cycles detected!
**Return `true`!**

---

## 4. Complete Execution Trace

```text
n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Edge check: len(edges) == 4 == 5 - 1 -> Pass

Initial parent: [0, 1, 2, 3, 4]

Edge [0, 1]: find(0)=0, find(1)=1 -> Union: parent[1] = 0 -> parent: [0, 0, 2, 3, 4]
Edge [0, 2]: find(0)=0, find(2)=2 -> Union: parent[2] = 0 -> parent: [0, 0, 0, 3, 4]
Edge [0, 3]: find(0)=0, find(3)=3 -> Union: parent[3] = 0 -> parent: [0, 0, 0, 0, 4]
Edge [1, 4]: find(1)=0, find(4)=4 -> Union: parent[4] = 0 -> parent: [0, 0, 0, 0, 0]

All edges valid -> Return True
```

| Step | Edge $[u, v]$ | $\text{find}(u)$ | $\text{find}(v)$ | Same Component? | Action | Components Remaining |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | Setup | - | - | - | Initialize parent array | 5 |
| **1** | $[0, 1]$ | 0 | 1 | No ($0 \ne 1$) | Merge: $\text{parent}[1] = 0$ | 4 |
| **2** | $[0, 2]$ | 0 | 2 | No ($0 \ne 2$) | Merge: $\text{parent}[2] = 0$ | 3 |
| **3** | $[0, 3]$ | 0 | 3 | No ($0 \ne 3$) | Merge: $\text{parent}[3] = 0$ | 2 |
| **4** | $[1, 4]$ | 0 | 4 | No ($0 \ne 4$) | Merge: $\text{parent}[4] = 0$ | **1 (Tree Spanned)** |
| **End** | - | - | - | - | **`true`** | 1 |

### Contrast: Cycle Detection Failure
$\text{edges} = [[0, 1], [1, 2], [2, 0]]$ with $n = 3$:
1. Edge $[0, 1]$ merges $0$ and $1$.
2. Edge $[1, 2]$ merges $1$ and $2$ into component $0$.
3. Edge $[2, 0]$:
   - $\text{find}(2) = 0$
   - $\text{find}(0) = 0$
   - Both endpoints share root $0 \implies$ **Cycle detected! Return `false`!**

---

## 5. Algorithmic Correctness

**Soundness.** A tree cannot contain cycles. If DSU finds $\text{find}(u) == \text{find}(v)$, an existing path already connects $u$ and $v$; adding the edge forms a cycle, so returning `false` is correct. If the algorithm returns `true`, it verified that the graph has $|E| = n - 1$ edges and no cycles.

**Completeness.** By the Tree Equivalence Theorem, an acyclic graph with $n - 1$ edges on $n$ vertices must have exactly $n - (n - 1) = 1$ connected component. Therefore, the graph is guaranteed to be fully connected without needing a separate BFS/DFS traversal.

---

## 6. Traps This Instance Exposes

- **Missing the $|E| == n - 1$ Guard:** Without checking $|E| == n - 1$, a graph with 4 nodes and edges $[[0, 1], [2, 3]]$ would pass the cycle test, but it is a disconnected forest of two separate trees. Checking $|E| == n - 1$ rejects it upfront in $O(1)$ time.
- **Self-Loops and Multi-Edges:** If an edge links a node to itself $[u, u]$, $\text{find}(u) == \text{find}(u)$ triggers immediately, rejecting the self-loop as a cycle.
- **Direct Parent vs Root Assignment:** When unioning components, you must assign $\text{parent}[\text{root}_u] = \text{root}_v$. Assigning $\text{parent}[u] = v$ without finding roots corrupts the tree structure.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot \alpha(N))$, where $N$ is the number of nodes and $\alpha$ is the Inverse Ackermann function ($\alpha(N) < 5$ for all practical input sizes). Initializing the array takes $O(N)$. We process $N - 1$ edges, with each `find` and `union` taking amortized $O(\alpha(N))$ time. Runtime is virtually indistinguishable from strictly linear $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the `parent` array.
