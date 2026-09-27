# Guided Example: Shortest Path Visiting All Nodes

We trace the step-by-step state space expansion over vertex-bitmask Cartesian products $(u, mask)$, multi-source breadth-first search initialization ($\forall i: (i, 1 \ll i)$), node revisit allowance via bitmask progress tracking, unweighted shortest path guarantees, full bitmask termination ($mask == 2^n - 1$), and optimal covering walk extraction on representative graphs:

- **Input:**
  $$
  graph = [[1, 2, 3], [0], [0], [0]]
  $$
- **Required output:** `4`
  - All-node covering walk specifications:
    - We are given an undirected connected graph with $n$ nodes labeled $0 \dots n - 1$.
    - We may start the walk at **any** node, and stop at **any** node.
    - We may **revisit nodes** and **reuse edges** multiple times.
    - Objective: Find the **minimum total number of edges** traversed to visit every single node in the graph at least once.
    - For the 4-node star graph ($n = 4$):
      - Center node 0 connects to peripheral leaves 1, 2, and 3.
      - A minimal covering walk starts at a leaf (say 1) and visits all leaves:
        $$
        1 \longrightarrow 0 \longrightarrow 2 \longrightarrow 0 \longrightarrow 3
        $$
      - Walk step 1 ($1 \to 0$): visited $\{1, 0\}$. Length 1.
      - Walk step 2 ($0 \to 2$): visited $\{1, 0, 2\}$. Length 2.
      - Walk step 3 ($2 \to 0$): revisit center 0. Length 3.
      - Walk step 4 ($0 \to 3$): visited $\{1, 0, 2, 3\}$ (all nodes!). Length 4.
      - Total edges traversed: **`4`**.
- **State Space Augmentation & Bitmask BFS Invariant:**
  - **The Augmented State Representation:**
    - Because nodes can be revisited, a simple BFS tracking only the current node $u$ cannot distinguish between visiting a node for the first time versus backtracking through it to reach unvisited nodes.
    - Augment the state to a tuple:
      $$
      (u, \; mask)
      $$
      where:
      - $u \in \{0, 1, \dots, n - 1\}$: the current physical location in the graph.
      - $mask \in [0, 2^n - 1]$: an integer bitmask where the $k$-th bit is 1 if node $k$ has been visited, and 0 otherwise.
  - **Multi-Source Initialization:**
    - Since the walk can begin at any arbitrary node, enqueue all $n$ initial starting configurations at distance 0:
      $$
      \text{Initial States} = \{ (i, \; 1 \ll i) \mid i \in [0, n - 1] \}
      $$
      $$
      vis = \bigcup_{i=0}^{n-1} \{ (i, \; 1 \ll i) \}
      $$
  - **Level-Order BFS Transitions:**
    - At current state $(u, mask)$ with path length $ans$:
      - If $mask == 2^n - 1$ (all bits set): Every node has been visited! Return $ans$ immediately.
      - For each neighbor $v \in graph[u]$:
        - Transition to new state:
          $$
          (v, \; mask \mid (1 \ll v))
          $$
        - If $(v, new\_mask)$ has not been visited before, mark it visited and enqueue it.
    - Because each step advances distance by exactly 1, BFS guarantees that the first state to reach $mask = 2^n - 1$ achieves the global minimum path length.
- **Step-by-Step Worked Execution Trace on the 4-Node Star Graph:**
  - Target full mask:
    $$
    mask_{\text{target}} = (1 \ll 4) - 1 = 1111_2 = \mathbf{15}
    $$
  - Initialize queue at distance $ans = 0$:
    - $(0, 0001_2 = 1)$
    - $(1, 0010_2 = 2)$
    - $(2, 0100_2 = 4)$
    - $(3, 1000_2 = 8)$
  - **Layer 0 ($ans = 0$):**
    - None of the initial states have $mask = 15$.
    - Expand all neighbors to distance 1:
      - From $(1, 0010_2)$: neighbor is 0 $\implies$ state $(0, 0010_2 \mid 0001_2 = 0011_2 = 3)$.
      - From $(2, 0100_2)$: neighbor is 0 $\implies$ state $(0, 0101_2 = 5)$.
      - From $(3, 1000_2)$: neighbor is 0 $\implies$ state $(0, 1001_2 = 9)$.
      - From $(0, 0001_2)$: neighbors are 1, 2, 3 $\implies$ states $(1, 3), (2, 5), (3, 9)$.
  - **Layer 1 ($ans = 1$):**
    - Queue contains 2-node visited states at distance 1.
    - None have $mask = 15$.
    - Expand neighbors to distance 2:
      - From $(0, 0011_2)$: neighbors are 2 and 3:
        - To 2: state $(2, 0011_2 \mid 0100_2 = 0111_2 = 7)$.
        - To 3: state $(3, 0011_2 \mid 1000_2 = 1011_2 = 11)$.
      - From $(0, 0101_2)$: to 1 gives $(1, 7)$, to 3 gives $(3, 1101_2 = 13)$.
      - From $(0, 1001_2)$: to 1 gives $(1, 11)$, to 2 gives $(2, 13)$.
  - **Layer 2 ($ans = 2$):**
    - Queue contains 3-node visited states at distance 2 (e.g. $(2, 7)$, $(3, 11)$, etc.).
    - Expand neighbors to distance 3:
      - From state $(2, 0111_2)$ (at leaf 2, visited $\{0, 1, 2\}$):
        - Only neighbor is center 0:
        - Transition: $(0, 0111_2 \mid 0001_2 = 0111_2 = 7)$ (revisiting center 0!).
        - Enqueue $(0, 7)$ at distance 3.
  - **Layer 3 ($ans = 3$):**
    - Queue processes state $(0, 0111_2)$ at center 0 with nodes $\{0, 1, 2\}$ visited.
    - Neighbors of 0 are 1, 2, 3:
      - To neighbor 3:
        $$
        mask_{new} = 0111_2 \mid (1 \ll 3) = 0111_2 \mid 1000_2 = 1111_2 = \mathbf{15}
        $$
      - Enqueue $(3, 15)$ at distance 4!
  - **Layer 4 ($ans = 4$):**
    - Pop state $(3, 15)$:
      $$
      mask = 15 == (1 \ll 4) - 1 \implies \mathbf{All\ Nodes\ Visited!}
      $$
    - Return current distance:
      $$
      ans = \mathbf{4}
      $$
- **Linear Chain Graph Trace ($0 - 1 - 2 - 3$):**
  - Path $0 \to 1 \to 2 \to 3$ visits all 4 nodes without any revisits.
  - BFS discovers $(3, 15)$ at layer 3 $\implies ans = 3 = n - 1$.
- **Single Node Graph Trace ($n = 1, graph = [[]]$):**
  - Initial state $(0, 1)$ has $mask = (1 \ll 1) - 1 = 1$.
  - Returns immediately at layer 0 $\implies ans = \mathbf{0}$.

This instance demonstrates metric traveling salesman walk optimization over graph-bitmask product manifolds and shortest paths in Cayley state spaces, mathematically proves why breadth-first search on the augmented digraph $(V \times \mathcal{P}(V), E_{\text{aug}})$ yields exact minimum-length covering walks, and derives $O(N \cdot 2^N)$ execution time and $O(N \cdot 2^N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an undirected connected graph:
Find the **shortest path** that visits every node at least once (nodes and edges may be revisited).

```text
graph:
  0 connects to 1, 2, 3 (Star graph)

Shortest walk:
  1 -> 0 -> 2 -> 0 -> 3
  Revisits center node 0 to reach leaf 3.
  Total edges = 4

Result: 4
```

### The Invariant of the Augmented State Space
- Simple BFS fails because nodes can be revisited.
- State is $(u, mask)$ where $u$ is current node and $mask$ is the bitmask of visited nodes.
- Total states: $n \cdot 2^n$ (manageable because $n \le 12$).
- The first state popped with $mask == 2^n - 1$ has the minimum distance.

---

## 2. Conceptual Foundation & Invariants

### 1. State Space Graph:
$$
\mathcal{V} = \{ (u, S) \mid u \in V, \; S \subseteq V \}, \quad |\mathcal{V}| = n \cdot 2^n
$$
$$
(u, S) \longrightarrow (v, S \cup \{v\}) \iff (u, v) \in E
$$

### 2. Multi-Source BFS Initialization:
$$
Q_0 = \{ (i, \{i\}) \mid i \in V \}
$$
$$
ans = \min_{(v, V) \in \mathcal{V}} \text{dist}(Q_0, (v, V))
$$

> **Quotient TSP Embedding Invariant.** The minimum covering walk on $G$ is the unweighted geodesic shortest path on the product digraph $G \times \mathcal{H}_n$, where $\mathcal{H}_n$ is the Boolean hypercube lattice. Because edges have unit length, level-synchronous BFS computes the exact geodesic distance in linear time relative to the augmented state space.

---

## 3. Step-by-Step Worked Execution

We trace the 4-node star graph:

---

### Step 1: Initialize
- Enqueue $(0, 1), (1, 2), (2, 4), (3, 8)$ at $ans = 0$.

---

### Step 2: Expand to $ans = 1$
- Nodes reach adjacent nodes with 2 bits set (e.g. $(0, 3)$ from $1 \to 0$).

---

### Step 3: Expand to $ans = 2$
- Nodes reach 3 bits set (e.g. $(2, 7)$ from $0 \to 2$).

---

### Step 4: Expand to $ans = 3$
- Backtrack from 2 to 0 $\implies (0, 7)$.

---

### Step 5: Expand to $ans = 4$
- Move from 0 to 3 $\implies (3, 15)$.
- $mask = 15$ is all 4 bits set!
- Return $\mathbf{4}$.

---

## 4. Complete Execution Trace

| BFS Layer ($ans$) | Representative State $(u, mask)$ | Visited Node Set | Action Taken | Next Enqueued State |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | $(1, 0010_2)$ | $\{1\}$ | Move to center 0 | $(0, 0011_2)$ |
| $1$ | $(0, 0011_2)$ | $\{0, 1\}$ | Move to leaf 2 | $(2, 0111_2)$ |
| $2$ | $(2, 0111_2)$ | $\{0, 1, 2\}$ | Revisit center 0 | $(0, 0111_2)$ |
| $3$ | $(0, 0111_2)$ | $\{0, 1, 2\}$ | Move to leaf 3 | $(3, 1111_2)$ |
| **$4$** | **$(3, 1111_2)$** | **$\{0, 1, 2, 3\}$** | **Full mask reached!** | **`Return 4`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node ($n = 1$):** Initial state has $mask = (1 \ll 1) - 1 \implies ans = 0$.
- **Complete Graph ($K_n$):** Hamiltonian path visits all nodes in $n - 1$ steps without revisits.
- **Tree Graphs:** Naturally require backtracking through internal vertices to reach leaves.
- **Maximum Graph ($N = 12$):** $12 \times 2^{12} = 49,152$ states; BFS evaluates in $< 25$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Searching for Simple Hamiltonian Paths ($O(N!)$):** A simple path may not visit all nodes without revisits. Forcing non-revisiting paths misses the optimal walk.
- **Starting from Only Node 0:** The optimal path might need to start at a specific leaf (like node 1 in the star graph). Multi-source initialization covers all possible starting vertices.
- **Re-Visiting Without Progress:** Tracking visited states as `(node, mask)` allows revisiting a node only when new nodes have been absorbed into the mask, preventing infinite cycles.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Total states in augmented graph: $N \cdot 2^N$.
  - From each state, at most $N$ edges are explored: $\mathcal{O}(N^2 \cdot 2^N)$.
  - For $N \le 12$: $144 \times 4096 \approx 5.9 \times 10^5$ operations. Completes in $< 30$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N \cdot 2^N)$ memory for the BFS queue and visited state set ($< 50,000$ entries).
