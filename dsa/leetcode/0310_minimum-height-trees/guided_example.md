# Guided Example: Minimum Height Trees

We trace the step-by-step tree centroid characterization, diameter midpoint reduction, topological leaf peeling (Kahn-style degree-1 trimming), and center node extraction on representative undirected tree instances:

- **Input:** $n = 4, \quad \text{edges} = [[1, 0], [1, 2], [1, 3]]$
- **Required output:** $[1]$ (Star graph with central hub node $1$; rooting at $1$ yields height $1$, while rooting at any other node yields height $2$)
- **Two Centroids Instance:** $n = 6, \; \text{edges} = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]] \implies [3, 4]$ (Even diameter path yields two adjacent centroids, both giving minimum tree height $2$)
- **Single Node Base Case:** $n = 1, \; \text{edges} = [] \implies [0]$ (Trivially root $0$ with height $0$)
- **Two Nodes Base Case:** $n = 2, \; \text{edges} = [[0, 1]] \implies [0, 1]$ (Both nodes have height $1$)

This instance demonstrates tree centroid identification via inward boundary peeling, mathematically proves why a tree can have at most two centroids (the midpoints of the tree's diameter), explains why peripheral leaves cannot be minimum height roots, and executes in strictly $O(N)$ linear time and auxiliary space.

---

## 1. Instance & Teaching Goal

Given a tree of $n = 4$ nodes and $3$ edges:
$$
\text{edges} = [[1, 0], [1, 2], [1, 3]]
$$
Find the root(s) that minimize the resulting tree's height (the length of the longest downward path to any leaf).

```text
Tree topology (Star Graph):
       0
       |
  2 -- 1 -- 3

Testing all possible roots:
- Root 0: Path to 2 has length 2, path to 3 has length 2 -> Height = 2
- Root 2: Path to 0 has length 2, path to 3 has length 2 -> Height = 2
- Root 3: Path to 0 has length 2, path to 2 has length 2 -> Height = 2
- Root 1: Paths to 0, 2, 3 all have length 1            -> Height = 1 (MINIMUM!)

Optimal root: [1]
```

### Why Naive BFS from Every Node Fails
- Running BFS from each of the $N$ nodes to measure its height takes $O(N \cdot (V + E)) = O(N^2)$ time. For $N = 2 \times 10^4$, $N^2 \approx 4 \times 10^8$ operations, causing Time Limit Exceeded.
- **Topological Leaf Peeling ($O(N)$):**
  - Leaves (nodes with degree 1) lie on the outer perimeter of the tree.
  - A leaf can never be a minimum-height root in a multi-node tree: moving the root from a leaf to its neighbor decreases distance to all other nodes.
  - Peeling away leaves layer by layer contracts the tree inward until only **1 or 2 centroid nodes** remain.

---

## 2. Conceptual Foundation & Invariants

### The Tree Centroid Theorem
Let the diameter of a tree be $D$ (length of the longest simple path).
- If $D$ is even ($2k$), there is **exactly one** middle node at distance $k$ from both endpoints.
- If $D$ is odd ($2k + 1$), there are **exactly two** adjacent middle nodes.
The minimum-height trees are rooted exclusively at these diameter midpoints.

### Topological Leaf Peeling Algorithm:
1. **Base Case:** If $n == 1$, return `[0]`.
2. **Degree Initialization:**
   Build adjacency list $g$ and compute `degree[u]` for every node $u$.
3. **Queue Initial Leaves:**
   Enqueue all nodes with `degree[u] == 1`:
   $$
   q = \text{deque}(u \text{ for } u \in [0, n-1] \text{ if } \text{degree}[u] == 1)
   $$
4. **Iterative Layer Peeling:**
   While $q$ is non-empty:
   - Clear candidate list `ans`.
   - For all nodes $a$ in current layer ($\text{len}(q)$):
     - Pop $a$, append to `ans`.
     - For each neighbor $b \in g[a]$:
       - Decrement `degree[b] -= 1`.
       - If `degree[b] == 1`, enqueue $b$ for the next layer.
5. When $q$ becomes empty, `ans` contains the nodes from the **final layer** (the 1 or 2 centroids)!

> **Invariant.** Simultaneously trimming all degree-1 leaves shrinks every longest path by 1 on both ends without shifting the midpoint. The last layer processed contains the exact centroid(s).

---

## 3. Step-by-Step Worked Execution

We trace the leaf peeling on $n = 4$, $\text{edges} = [[1, 0], [1, 2], [1, 3]]$:

---

### Step 1: Degree and Graph Setup
Adjacency list $g$:
- $0: [1]$
- $1: [0, 2, 3]$
- $2: [1]$
- $3: [1]$

Degree array:
$$
\text{degree} = [1, \; 3, \; 1, \; 1]
$$
Nodes with degree 1: $\{0, 2, 3\}$.
Initial queue: $q = \text{deque}([0, 2, 3])$.

---

### Step 2: Peeling Layer 1 (Outer Leaves)
Current queue size: 3.
Clear `ans`.
Pop and process all 3 leaves in Layer 1:

1. **Pop Node 0:**
   - Append to `ans = [0]`.
   - Neighbor is Node 1.
   - Decrement: $\text{degree}[1] \leftarrow 3 - 1 = 2$.
2. **Pop Node 2:**
   - Append to `ans = [0, 2]`.
   - Neighbor is Node 1.
   - Decrement: $\text{degree}[1] \leftarrow 2 - 1 = 1$.
   - $\text{degree}[1] == 1 \implies$ Enqueue Node 1! ($q.\text{append}(1)$).
3. **Pop Node 3:**
   - Append to `ans = [0, 2, 3]`.
   - Neighbor is Node 1.
   - Decrement: $\text{degree}[1] \leftarrow 1 - 1 = 0$.

End of Layer 1:
- Queue for next layer: $q = \text{deque}([1])$.
- Active degrees: $\text{degree}[1] = 0$.

---

### Step 3: Peeling Layer 2 (Centroid Layer)
Current queue size: 1.
Clear `ans`.
Pop all nodes in Layer 2:

1. **Pop Node 1:**
   - Append to `ans = [1]`.
   - Neighbors of 1: all neighbors $\{0, 2, 3\}$ have already been processed and degree $\le 0$.
   - No new nodes reach degree 1.

End of Layer 2:
- Queue is empty ($q = []$).
- Loop terminates.

---

### Step 4: Final Output
The last layer recorded in `ans` is:
$$
\mathbf{[1]}
$$

---

## 4. Complete Execution Trace

```text
n = 4, edges = [[1, 0], [1, 2], [1, 3]]
Initial degrees: {0: 1, 1: 3, 2: 1, 3: 1}
Initial leaves: q = [0, 2, 3]

Layer 1 (Leaves):
  pop 0 -> degree[1] becomes 2
  pop 2 -> degree[1] becomes 1 -> enqueue 1
  pop 3 -> degree[1] becomes 0
  ans was [0, 2, 3]
  Next q = [1]

Layer 2 (Center):
  ans cleared -> ans = []
  pop 1 -> ans = [1]
  Next q = [] (Empty -> Stop)

Result: [1]
```

| Layer | Nodes in Queue $q$ | Leaves Popped | Neighbors Updated | New Nodes Reaching Degree 1 | `ans` Snapshot |
|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | `[0, 2, 3]` | 0, 2, 3 | $\text{degree}[1]: 3 \to 2 \to 1 \to 0$ | Node 1 | `[0, 2, 3]` |
| **2** | **`[1]`** | **1** | None | None | **`[1]` (Centroid)** |
| **Done** | `[]` | - | - | - | **Final: `[1]`** |

---

### Two Centroids Contrast ($n = 6$)
Path: $0 - 3 - 4 - 5$ with extra branches on 3.
- Layer 1 peels outer leaves: $\{0, 1, 2, 5\}$.
- Nodes 3 and 4 reach degree 1 simultaneously.
- Layer 2 peels: $\{3, 4\}$.
- Result: `[3, 4]`.

---

## 5. Algorithmic Correctness

**Soundness.** Trimming all degree-1 nodes removes the outermost perimeter of the tree. If a node is a leaf, its maximum distance to other nodes is strictly greater than the maximum distance from its adjacent internal neighbor. Thus, no leaf can be an MHT root when $n > 2$. Removing leaves preserves the exact set of diameter midpoints.

**Completeness.** Every node and edge is accounted for in the degree array. The process terminates when no more degree-1 nodes can be formed, which in any finite tree occurs when 1 or 2 nodes remain. The last processed layer contains all valid centroids without omission.

---

## 6. Traps This Instance Exposes

- **Base Case $n = 1$:** When $n = 1$, `edges` is empty. The single node 0 has degree 0, not 1, so it would never be enqueued by the degree-1 check. A defensive guard `if n == 1: return [0]` is mandatory.
- **Immediate Enqueueing without Layer Isolation:** Processing newly added leaves within the same loop iteration corrupts the concentric layer boundaries. Peeling must proceed strictly level-by-level using `for _ in range(len(q))` or a remaining-node counter.
- **Undirected Edges:** Edges are bidirectional. Both `g[a].append(b)` and `g[b].append(a)` must be populated, and both `degree[a]` and `degree[b]` incremented.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ linear time, where $N$ is the number of nodes. The tree has $N - 1$ edges. Building adjacency lists takes $O(N)$. Each node enters and leaves the queue exactly once, and each edge is traversed twice (once from each endpoint).
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the adjacency list $g$, degree array, and queue buffers.
