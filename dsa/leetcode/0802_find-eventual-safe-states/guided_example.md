# Guided Example: Find Eventual Safe States

We trace the step-by-step directed graph terminal node characterization ($\text{out-degree}(u) == 0$), cycle avoidance requirement, reverse graph edge inversion ($u \to v \implies v \to u$), Kahn's reverse topological pruning queue simulation, out-degree barrier reduction ($indeg[j] -= 1$), and safe node set extraction on representative directed cyclic graphs:

- **Input:**
  $$
  graph = [[1, 2], \; [2, 3], \; [5], \; [0], \; [5], \; [], \; []]
  $$
- **Required output:**
  $$
  [2, 4, 5, 6]
  $$
  - Graph safety definitions:
    - A node is a **terminal node** if it has zero outgoing edges ($\text{out-degree} = 0$).
    - A node is an **eventual safe node** if **every possible path** starting from that node eventually terminates at a terminal node.
    - If a path can become trapped in a directed cycle, any node capable of reaching that cycle is **unsafe**.
    - For the input graph (7 nodes: $0 \dots 6$):
      - Notice the directed cycle:
        $$
        0 \longrightarrow 1 \longrightarrow 3 \longrightarrow 0
        $$
      - Paths starting at 0, 1, or 3 can loop indefinitely around this cycle $\{0, 1, 3\}$, so nodes 0, 1, and 3 are **unsafe**.
      - Nodes 5 and 6 have no outgoing edges $\implies$ **Safe** (terminal nodes).
      - Node 2 only connects to 5 ($2 \to 5$) $\implies$ **Safe**.
      - Node 4 only connects to 5 ($4 \to 5$) $\implies$ **Safe**.
      - Eventual safe nodes: $[2, 4, 5, 6]$.
- **Reverse Graph & Kahn's Topological Peeling Invariant:**
  - **The Structural Inversion:**
    - Testing whether every forward walk terminates is difficult because cycles create infinite paths.
    - However, working **backwards from known terminal nodes** is clean and deterministic!
    - Construct the **reversed graph** $rg$:
      - For each directed edge $u \to v$ in $graph$, add edge $v \to u$ in $rg$.
    - Maintain the original out-degree of each node:
      $$
      indeg[u] = |graph[u]|
      $$
  - **Kahn's Queue Invariant:**
    - Seed a queue with all terminal nodes ($indeg[u] == 0$).
    - When a node $i$ is dequeued, it is certified safe.
    - For each predecessor $j$ that could reach $i$ ($j \in rg[i]$):
      - Decrement $j$'s remaining unverified outgoing edges:
        $$
        indeg[j] \leftarrow indeg[j] - 1
        $$
      - If $indeg[j] == 0$: **ALL outgoing edges from $j$ lead to certified safe nodes**!
      - Enqueue $j$ as newly certified safe.
  - Any node remaining with $indeg > 0$ after the queue empties is either part of a cycle or can reach a cycle, and is therefore unsafe.
- **Step-by-Step Worked Execution Trace on the 7-Node Graph:**
  - Original graph:
    - $0 \to [1, 2]$ (out-degree 2)
    - $1 \to [2, 3]$ (out-degree 2)
    - $2 \to [5]$ (out-degree 1)
    - $3 \to [0]$ (out-degree 1)
    - $4 \to [5]$ (out-degree 1)
    - $5 \to []$ (out-degree 0)
    - $6 \to []$ (out-degree 0)
  - Reverse adjacency list $rg$:
    - $0 \leftarrow [3]$
    - $1 \leftarrow [0]$
    - $2 \leftarrow [0, 1]$
    - $3 \leftarrow [1]$
    - $5 \leftarrow [2, 4]$
  - Out-degree tracking: $indeg = [2, 2, 1, 1, 1, 0, 0]$.
  - **Phase 0: Seed Queue with Terminal Nodes ($indeg == 0$):**
    - Nodes 5 and 6 have $indeg = 0$.
    - Queue:
      $$
      q = [5, \; 6]
      $$
  - **Step 1: Pop Node 5 (Safe):**
    - Inspect incoming edges in $rg[5]$: nodes 2 and 4.
    - **Predecessor 2:**
      - Decrement out-degree: $indeg[2] \leftarrow 1 - 1 = \mathbf{0}$.
      - All outgoing edges from 2 are now verified safe!
      - Enqueue: $q.\text{append}(2)$.
    - **Predecessor 4:**
      - Decrement out-degree: $indeg[4] \leftarrow 1 - 1 = \mathbf{0}$.
      - All outgoing edges from 4 are now verified safe!
      - Enqueue: $q.\text{append}(4)$.
    - Queue state:
      $$
      q = [6, \; 2, \; 4]
      $$
  - **Step 2: Pop Node 6 (Safe):**
    - Inspect $rg[6]$: empty (no node connects to 6).
    - Queue state:
      $$
      q = [2, \; 4]
      $$
  - **Step 3: Pop Node 2 (Safe):**
    - Inspect $rg[2]$: nodes 0 and 1.
    - **Predecessor 0:**
      - Decrement out-degree: $indeg[0] \leftarrow 2 - 1 = \mathbf{1}$.
      - $indeg[0] = 1 \ne 0$ (still has unverified edge to 1; do not enqueue).
    - **Predecessor 1:**
      - Decrement out-degree: $indeg[1] \leftarrow 2 - 1 = \mathbf{1}$.
      - $indeg[1] = 1 \ne 0$ (still has unverified edge to 3; do not enqueue).
    - Queue state:
      $$
      q = [4]
      $$
  - **Step 4: Pop Node 4 (Safe):**
    - Inspect $rg[4]$: empty.
    - Queue becomes empty!
  - **Phase 1: Harvest Safe Nodes ($indeg == 0$):**
    - Final $indeg$ vector:
      $$
      indeg = [1, \; 1, \; 0, \; 1, \; 0, \; 0, \; 0]
      $$
    - Nodes with $indeg == 0$:
      $$
      ans = [\mathbf{2}, \; \mathbf{4}, \; \mathbf{5}, \; \mathbf{6}]
      $$
    - Nodes 0, 1, 3 remain blocked at $indeg = 1$ due to cycle $\{0 \to 1 \to 3 \to 0\}$.
- **Self-Loop Unsafe Trace ($graph = [[0]]$):**
  - Node 0 connects to itself ($0 \to 0$).
  - Out-degree is 1, never reaches 0 $\implies ans = []$.
- **Pure Directed Acyclic Graph Trace:**
  - All nodes eventually peel down to $indeg = 0 \implies$ all $n$ nodes are safe!

This instance demonstrates reverse topological sorting and core-periphery decomposition on directed state graphs, mathematically proves why pruning nodes with zero out-degree contractively eliminates the basin of attraction of directed cycles, and derives $O(V + E)$ runtime and $O(V + E)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a directed graph:
Find all **eventual safe nodes** (every path starting from the node ends at a terminal node without entering any cycle).

```text
graph:
  0 -> [1, 2]
  1 -> [2, 3]
  2 -> [5]
  3 -> [0]
  4 -> [5]
  5 -> [] (terminal)
  6 -> [] (terminal)

Cycle detected: 0 -> 1 -> 3 -> 0
Any path entering {0, 1, 3} can loop forever -> UNSAFE!
Safe nodes: 2, 4, 5, 6
Result: [ 2, 4, 5, 6 ]
```

### The Invariant of Kahn's Reverse Pruning
- Reverse all edges: $u \to v$ becomes $v \to u$.
- Nodes with out-degree 0 in the original graph are definitely safe.
- When all outgoing edges of node $j$ are confirmed safe ($indeg[j] == 0$), node $j$ becomes safe!

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse Adjacency & Out-Degree:
$$
rg[v] = \{ u \mid v \in graph[u] \}, \quad indeg[u] = |graph[u]|
$$

### 2. Backward Relaxation:
$$
\text{Pop safe } i \implies \forall j \in rg[i]: \; indeg[j] \leftarrow indeg[j] - 1
$$
$$
indeg[j] == 0 \implies \text{enqueue } j
$$

> **Directed Cycle Basin Invariant.** Let $\mathcal{C}$ be the union of all directed cycles in $G$. A node $u$ is unsafe if and only if there exists a directed walk $u \rightsquigarrow \mathcal{C}$. Reverse topological sort eliminates the complement $V \setminus \text{Pre}^*(\mathcal{C})$ in optimal linear time.

---

## 3. Step-by-Step Worked Execution

We trace the 7-node graph:

---

### Step 1: Initial Out-Degrees
- $indeg = [2, 2, 1, 1, 1, 0, 0]$.
- Seed queue with terminal nodes: `[5, 6]`.

---

### Step 2: Pop 5
- Predecessors 2 and 4 decrement to 0 $\implies$ enqueue 2, 4.

---

### Step 3: Pop 6
- No predecessors.

---

### Step 4: Pop 2
- Predecessors 0 and 1 decrement $2 \to 1$ (not 0).

---

### Step 5: Pop 4
- No predecessors. Queue empty!

---

### Step 6: Output
- Nodes with $indeg == 0$: **`[2, 4, 5, 6]`**.

---

## 4. Complete Execution Trace

| Dequeued Safe Node | Predecessors in $rg$ | Updated Out-Degrees ($indeg$) | Newly Certified Safe Nodes Enqueued |
|:---:|:---:|:---:|:---:|
| Initial Seed | — | — | `[5, 6]` |
| $5$ | $2, 4$ | $indeg[2] = 0, indeg[4] = 0$ | `2, 4` |
| $6$ | None | None | None |
| $2$ | $0, 1$ | $indeg[0] = 1, indeg[1] = 1$ | None |
| **$4$** | **None** | **None** | **None** |
| **Final** | — | — | **Safe: `[2, 4, 5, 6]`** |

---

## 5. Boundary Cases & Failure Modes

- **Completely Acyclic Graph (DAG):** All nodes peel to 0 $\implies$ returns all $n$ nodes $[0 \dots n - 1]$.
- **Isolated Self-Loops ($0 \to 0$):** $indeg$ stays $\ge 1 \implies$ excluded.
- **Graph with No Terminal Nodes (Pure Cycles):** Queue starts empty $\implies$ returns `[]`.
- **Single Node with No Edges ($[[]]$):** Terminal $\implies [0]$.

---

## 6. Traps & Common Anti-Patterns

- **Forward DFS without 3-Color Cycle Memoization:** Exploring paths forward without cycle memoization takes exponential time ($O(2^N)$). Reverse Kahn's algorithm runs in deterministic linear $O(V + E)$ time.
- **Forgetting to Sort the Output:** The problem requires safe nodes in ascending order; iterating $i = 0 \dots n - 1$ naturally produces sorted indices.
- **Misinterpreting Degree Counters:** In the reversed graph, $indeg[i]$ represents the *original out-degree* of node $i$. Only when *all* original outgoing edges are satisfied ($indeg == 0$) can the node be deemed safe.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building reverse graph: $\mathcal{O}(V + E)$.
  - Each node and edge processed at most once in queue: $\mathcal{O}(V + E)$.
  - Total Time: strictly linear $\mathcal{O}(V + E)$ where $V \le 10^4, E \le 4 \times 10^4$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(V + E)$ memory for the reverse adjacency list and degree array.
