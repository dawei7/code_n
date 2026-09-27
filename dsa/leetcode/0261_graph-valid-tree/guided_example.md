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
   - Otherwise, link the roots: $\text{parent}[\text{root}_v] = \text{root}_u$, so the merged component keeps $\text{root}_u$ as its representative.
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

### Parent-Array Evolution on a Branched Instance

The representative instance always merges into node $0$, so its parent array
looks uniformly flat. A branched instance with shuffled endpoint order,
$n = 6$ and $\text{edges} = [[4, 5], [2, 4], [3, 1], [0, 2], [1, 2]]$, produces
the same verdict through a much less uniform array and exposes what "one
component" really means.

| Step | Edge $[u, v]$ | $\text{find}(u)$ | $\text{find}(v)$ | Merge performed | `parent` after the merge | Components |
|:---:|:---:|:---:|:---:|:---|:---|:---:|
| 0 | — | — | — | — | `[0, 1, 2, 3, 4, 5]` | 6 |
| 1 | $[4, 5]$ | 4 | 5 | $\text{parent}[5] = 4$ | `[0, 1, 2, 3, 4, 4]` | 5 |
| 2 | $[2, 4]$ | 2 | 4 | $\text{parent}[4] = 2$ | `[0, 1, 2, 3, 2, 4]` | 4 |
| 3 | $[3, 1]$ | 3 | 1 | $\text{parent}[1] = 3$ | `[0, 3, 2, 3, 2, 4]` | 3 |
| 4 | $[0, 2]$ | 0 | 2 | $\text{parent}[2] = 0$ | `[0, 3, 0, 3, 2, 4]` | 2 |
| 5 | $[1, 2]$ | 3 | 0 | $\text{parent}[0] = 3$ | `[3, 3, 0, 3, 2, 4]` | **1 (tree)** |

Step 5 is the instructive one. The endpoints $1$ and $2$ are not roots: walking
from $1$ reaches $3$, and walking from $2$ reaches $0$, which is why the edge is
accepted rather than reported as a cycle. After the merge, every chain converges
to root $3$ — $5 \to 4 \to 2 \to 0 \to 3$ is the longest — even though the final
array is *not* uniformly filled with one label. A valid tree therefore requires
only that all `find` walks converge to a single representative; it does not
require a flat array, and a cycle test that compared `parent[x]` with a single
expected value instead of calling `find` would flag this valid tree as broken.

### Contrast: Cycle Detection Failure
$\text{edges} = [[0, 1], [1, 2], [2, 0]]$ with $n = 3$:
1. Edge $[0, 1]$ merges $0$ and $1$.
2. Edge $[1, 2]$ merges $1$ and $2$ into component $0$.
3. Edge $[2, 0]$:
   - $\text{find}(2) = 0$
   - $\text{find}(0) = 0$
   - Both endpoints share root $0 \implies$ **Cycle detected! Return `false`!**

That three-node instance is rejected by the cardinality guard before union-find
is ever consulted, since $\lvert E \rvert = 3 \ne n - 1 = 2$. The trace above
therefore isolates the cycle condition; the first row of the next table is the
case where the guard genuinely passes and union-find alone must catch the cycle.

### Which Mechanism Rejects Each Instance

The equivalence theorem splits every input into one of two regimes, and each
authored instance falls cleanly into one of them. Reading down the deciding
column shows that the guard is a necessity test and union-find supplies the
sufficiency half.

| Instance | $n$ | $\lvert E \rvert$ | $n - 1$ | Deciding mechanism | Verdict | Missing or excess structure |
|:---|:---:|:---:|:---:|:---|:---:|:---|
| `[[0, 1], [0, 2], [0, 3], [1, 4]]` | 5 | 4 | 4 | Union-find (guard passes) | `true` | None: four merges span all five nodes |
| `[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]` | 5 | 5 | 4 | Cardinality guard | `false` | One edge too many; the triangle $\{1, 2, 3\}$ is never examined |
| `[]` | 1 | 0 | 0 | Union-find (guard passes) | `true` | The degenerate tree on a single node |
| `[[1, 0]]` | 2 | 1 | 1 | Union-find (guard passes) | `true` | None; endpoint order carries no direction |
| `[]` | 2 | 0 | 1 | Cardinality guard | `false` | One edge short: two isolated nodes |
| `[[0, 1], [1, 2], [3, 4], [4, 5]]` | 6 | 4 | 5 | Cardinality guard | `false` | Acyclic yet split into two components, so the guard is doing real work |
| `[[0, 1], [1, 2], [2, 0]]` | 4 | 3 | 3 | Union-find (guard passes) | `false` | Cyclic *and* disconnected: node $3$ is isolated, so both failures coexist |
| `[[4, 5], [2, 4], [3, 1], [0, 2], [1, 2]]` | 6 | 5 | 5 | Union-find (guard passes) | `true` | None |
| `[[0, 1999]]` | 2000 | 1 | 1999 | Cardinality guard | `false` | 1998 edges short of spanning |

The four-node row is the one to remember: it is the only instance whose edge
count matches $n - 1$ while the graph is still not a tree, which is exactly why
the guard cannot be the whole algorithm and the cycle test cannot be skipped.

---

## 5. Algorithmic Correctness

**Soundness.** A tree cannot contain cycles. If DSU finds $\text{find}(u) == \text{find}(v)$, an existing path already connects $u$ and $v$; adding the edge forms a cycle, so returning `false` is correct. If the algorithm returns `true`, it verified that the graph has $|E| = n - 1$ edges and no cycles.

**Completeness.** By the Tree Equivalence Theorem, an acyclic graph with $n - 1$ edges on $n$ vertices must have exactly $n - (n - 1) = 1$ connected component. Therefore, the graph is guaranteed to be fully connected without needing a separate BFS/DFS traversal.

---

## 6. Traps This Instance Exposes

- **Missing the $|E| == n - 1$ Guard:** Without checking $|E| == n - 1$, a graph with 4 nodes and edges $[[0, 1], [2, 3]]$ would pass the cycle test, but it is a disconnected forest of two separate trees. Checking $|E| == n - 1$ rejects it upfront in $O(1)$ time.
- **Self-Loops and Multi-Edges:** If an edge links a node to itself $[u, u]$, $\text{find}(u) == \text{find}(u)$ triggers immediately, rejecting the self-loop as a cycle.
- **Direct Parent vs Root Assignment:** When unioning components you must attach one *root* beneath the other — $\text{parent}[\text{root}_v] = \text{root}_u$, the direction traced in Step 3. Assigning $\text{parent}[v] = u$ for the raw endpoints, without first finding their roots, corrupts the structure by making a non-root node the parent of a whole component.

### Boundary Map: What Each Guard Does at the Edges

The constraints promise $1 \le n \le 2000$, $a_i \ne b_i$, and no repeated
edges, so the first two rows below lie outside the legal input domain. They are
listed because the method's behavior there shows that neither guard is
load-bearing on an unstated assumption.

| Boundary scenario | Instance | Cardinality guard | Union-find if the guard passes | Verdict |
|:---|:---|:---|:---|:---:|
| Self-loop (excluded by $a_i \ne b_i$) | $n = 2$, `[[0, 0]]` | Passes: $1 = 1$ | $\text{find}(0)$ equals $\text{find}(0)$ immediately, so the edge is reported as a cycle | `false` |
| Repeated undirected edge (excluded by the no-repeat rule) | $n = 3$, `[[0, 1], [1, 0]]` | Passes: $2 = 2$ | The second copy joins two endpoints already inside one component | `false` |
| Reversed endpoints | $n = 2$, `[[1, 0]]` | Passes: $1 = 1$ | Merges the two roots regardless of which endpoint comes first | `true` |
| One edge short | $n = 2$, `[]` | Rejects: $0 \ne 1$ | Never runs | `false` |
| Acyclic but split | $n = 6$, `[[0, 1], [1, 2], [3, 4], [4, 5]]` | Rejects: $4 \ne 5$ | Never runs, although all four merges would have succeeded | `false` |
| One edge too many | $n = 4$, `[[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]` | Rejects: $5 \ne 3$ | Never runs; with more than $n - 1$ edges a cycle exists by pigeonhole | `false` |
| Smallest legal graph | $n = 1$, `[]` | Passes: $0 = 0$ | No edges to process, so one component remains and $n - (n - 1) = 1$ holds | `true` |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot \alpha(N))$, where $N$ is the number of nodes and $\alpha$ is the Inverse Ackermann function ($\alpha(N) < 5$ for all practical input sizes). Initializing the array takes $O(N)$. We process $N - 1$ edges, with each `find` and `union` taking amortized $O(\alpha(N))$ time. Runtime is virtually indistinguishable from strictly linear $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the `parent` array.
