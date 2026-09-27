# Guided Example: Network Delay Time

We trace the step-by-step directed weighted graph representation, single-source shortest path initialization ($dist[k] = 0, dist[v] = \infty$), Dijkstra greedy node settlement ($\min_{u \notin S} dist[u]$), adjacent edge relaxation ($dist[v] \leftarrow \min(dist[v], dist[u] + w)$), bottleneck transmission delay calculation ($ans = \max dist$), and unreachable node detection on representative network topologies:

- **Input:**
  - Network edges: $times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]$
  - Total nodes: $n = 4$ (labeled $1, 2, 3, 4$)
  - Signal source: $k = 2$
- **Required output:** `2`
  - Transmission criteria:
    - Directed edges $(u, v, w)$ indicate that a signal travels from node $u$ to node $v$ taking $w$ time units.
    - The signal originates from node $k$ at time $t = 0$ and propagates simultaneously along all outgoing paths.
    - Each node receives the signal at the earliest possible arrival time (the shortest path distance from $k$).
    - Objective: Find the **minimum time required for ALL $n$ nodes** to receive the signal.
    - If any node in the network is unreachable, return `-1`.
    - For the input network:
      - Source 2 reaches Node 1 in time 1 (path $2 \to 1$, weight 1).
      - Source 2 reaches Node 3 in time 1 (path $2 \to 3$, weight 1).
      - From Node 3, the signal reaches Node 4 in time $1 + 1 = 2$ (path $2 \to 3 \to 4$, total weight 2).
      - Times of arrival for all 4 nodes: $\{Node\ 1: 1, \; Node\ 2: 0, \; Node\ 3: 1, \; Node\ 4: 2\}$.
      - The last node to receive the signal is Node 4 at time 2.
      - Total delay: **2**.
- **Dijkstra's Algorithm & Edge Relaxation Invariant:**
  - **Distance Array & Settlement Set ($S$):**
    - Maintain $dist[1 \dots n]$ initialized to $\infty$, with source $dist[k] = 0$.
    - Maintain a boolean set of settled nodes $vis$.
  - **Greedy Selection Invariant:**
    - At each step, select the unsettled node $u \notin vis$ with the minimal tentative distance:
      $$
      u = \arg\min_{v \notin vis} dist[v]
      $$
    - Because all edge weights are non-negative ($w \ge 0$), the tentative distance $dist[u]$ is mathematically guaranteed to be the exact, immutable shortest path distance from $k$ to $u$.
    - Mark $u$ as settled ($vis[u] \leftarrow \text{true}$).
  - **Edge Relaxation:**
    - For every outgoing directed edge $(u, v)$ with latency $w$:
      $$
      dist[v] \leftarrow \min(dist[v], \; dist[u] + w)
      $$
  - **Bottleneck Completion Time:**
    - The entire network is fully activated when the furthest node has received the signal:
      $$
      ans = \max_{1 \le i \le n} dist[i]
      $$
    - If any node has $dist[i] == \infty$, that node never received the signal $\implies$ return `-1`.
- **Step-by-Step Worked Execution Trace on the 4-Node Network:**
  - Node indices: $1, 2, 3, 4$. Source: $k = 2$.
  - **Phase 0: Initialization:**
    $$
    dist = [\infty, \; \mathbf{0}, \; \infty, \; \infty], \quad vis = [\text{F}, \text{F}, \text{F}, \text{F}]
    $$
  - **Iteration 1 (Settle Source Node 2):**
    - Unsettled nodes: $\{1, 2, 3, 4\}$.
    - Node with minimum distance: Node 2 ($dist[2] = 0$).
    - Mark settled: $vis[2] \leftarrow \mathbf{true}$.
    - Relax outgoing edges from Node 2:
      - Edge $(2 \to 1, w = 1)$:
        $$
        dist[1] \leftarrow \min(\infty, \; 0 + 1) = \mathbf{1}
        $$
      - Edge $(2 \to 3, w = 1)$:
        $$
        dist[3] \leftarrow \min(\infty, \; 0 + 1) = \mathbf{1}
        $$
    - Distances after Iteration 1:
      $$
      dist = [\mathbf{1}, \; \mathbf{0}, \; \mathbf{1}, \; \infty]
      $$
  - **Iteration 2 (Settle Node 1):**
    - Unsettled nodes: $\{1, 3, 4\}$ with distances $[1, 1, \infty]$.
    - Choose Node 1 ($dist[1] = 1$).
    - Mark settled: $vis[1] \leftarrow \mathbf{true}$.
    - Outgoing edges from Node 1: None.
    - Distances unchanged: $[1, 0, 1, \infty]$.
  - **Iteration 3 (Settle Node 3):**
    - Unsettled nodes: $\{3, 4\}$ with distances $[1, \infty]$.
    - Choose Node 3 ($dist[3] = 1$).
    - Mark settled: $vis[3] \leftarrow \mathbf{true}$.
    - Relax outgoing edges from Node 3:
      - Edge $(3 \to 4, w = 1)$:
        $$
        dist[4] \leftarrow \min(\infty, \; 1 + 1) = \mathbf{2}
        $$
    - Distances after Iteration 3:
      $$
      dist = [1, \; 0, \; 1, \; \mathbf{2}]
      $$
  - **Iteration 4 (Settle Node 4):**
    - Unsettled nodes: $\{4\}$ with distance $2$.
    - Choose Node 4 ($dist[4] = 2$).
    - Mark settled: $vis[4] \leftarrow \mathbf{true}$.
    - Outgoing edges from Node 4: None.
  - **Phase 3: Evaluate Max Distance:**
    - All 4 nodes are settled:
      $$
      dist = [Node\ 1: 1, \; Node\ 2: 0, \; Node\ 3: 1, \; Node\ 4: 2]
      $$
    - Check reachability: No node has $\infty$ distance.
    - Compute maximum delay:
      $$
      ans = \max(1, 0, 1, 2) = \mathbf{2}
      $$
- **Unreachable Node Trace ($times = [[1, 2, 1]], n = 2, k = 2$):**
  - Directed edge exists only from $1 \to 2$.
  - Signal sent from $k = 2$ cannot travel to Node 1.
  - $dist[1] = \infty \implies$ returns **`-1`**.
- **Single Node Network ($n = 1, k = 1$):**
  - Signal immediately active at source.
  - Max distance $= 0 \implies$ returns **`0`**.

This instance demonstrates Dijkstra's single-source shortest path algorithm on directed graphs and bottleneck activation modeling, mathematically proves why non-negative edge weights preserve subpath optimality under greedy settlement, and derives $O(V^2)$ (dense) or $O(E \log V)$ (sparse heap) runtime and $O(V + E)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a directed graph with $n$ nodes and edge travel times:
Send a signal from node $k$.
Find the **minimum time for ALL nodes to receive the signal**.
Return -1 if any node is unreachable.

```text
Times:
  2 -> 1 (time 1)
  2 -> 3 (time 1)
  3 -> 4 (time 1)
n = 4, start at k = 2

Signal propagation:
  At t = 0: Node 2 has signal
  At t = 1: Node 1 and Node 3 receive signal
  At t = 2: Node 4 receives signal from Node 3

All 4 nodes received the signal by t = 2!
Result: 2
```

### The Invariant of Dijkstra's Shortest Path
- Each node receives the signal at its shortest path distance from source $k$.
- Time for all nodes to receive the signal equals the **maximum shortest path distance**: $\max_{v} dist[v]$.
- If any $dist[v] == \infty$, the graph is disconnected from $k \implies -1$.

---

## 2. Conceptual Foundation & Invariants

### 1. Distance Array Initialization:
$$
dist[k] = 0, \quad dist[v] = \infty \quad \forall v \ne k
$$

### 2. Greedy Node Settlement & Relaxation:
$$
u = \arg\min_{v \notin vis} dist[v]
$$
$$
dist[v] \leftarrow \min(dist[v], \; dist[u] + w(u, v))
$$
$$
ans = \begin{cases} -1 & \text{if } \exists v: dist[v] = \infty \\ \max_{v} dist[v] & \text{otherwise} \end{cases}
$$

> **Dijkstra Settlement Invariant.** In any directed graph with non-negative edge weights $w: E \to \mathbb{R}_{\ge 0}$, the sequence of settled vertices satisfies $dist[u_1] \le dist[u_2] \le \dots \le dist[u_n]$, where each settled distance represents the exact shortest path metric $d(k, u_i)$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Start at Node 2
- $dist[2] = 0$.
- Relax edges $(2, 1)$ and $(2, 3)$:
  - $dist[1] = 1$.
  - $dist[3] = 1$.

---

### Step 2: Settle 1 and 3
- Settle Node 1 ($dist = 1$). No outgoing edges.
- Settle Node 3 ($dist = 1$). Relax $(3, 4) \implies dist[4] = 1 + 1 = 2$.

---

### Step 3: Settle 4
- Settle Node 4 ($dist = 2$).

---

### Step 4: Output
- Distances: $[1, 0, 1, 2]$.
- $\max(dist) = \mathbf{2}$.

---

## 4. Complete Execution Trace

| Iteration | Node Settled | Current Shortest Distance | Outgoing Edges Relaxed | Updated Distances $[dist[1], dist[2], dist[3], dist[4]]$ |
|:---:|:---:|:---:|:---:|:---:|
| Initial | — | — | — | $[\infty, 0, \infty, \infty]$ |
| $1$ | Node $2$ | $0$ | $2 \to 1$ ($1$), $2 \to 3$ ($1$) | $[1, 0, 1, \infty]$ |
| $2$ | Node $1$ | $1$ | None | $[1, 0, 1, \infty]$ |
| $3$ | Node $3$ | $1$ | $3 \to 4$ ($1$) | $[1, 0, 1, 2]$ |
| $4$ | Node $4$ | $2$ | None | **$[1, 0, 1, 2]$** |
| **Result** | — | — | **Maximum = 2** | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **Unreachable Node:** At least one node remains $\infty \implies$ returns $-1$.
- **Single Node Network ($n = 1$):** $dist[1] = 0 \implies$ returns 0.
- **Multiple Disconnected Components:** Cannot reach all nodes $\implies$ returns $-1$.
- **Cycles in Graph:** Non-negative weights guarantee Dijkstra terminates without infinite cycling.

---

## 6. Traps & Common Anti-Patterns

- **1-Based vs 0-Based Indexing:** The problem labels nodes $1 \dots n$. Be consistent when mapping to array indices $0 \dots n - 1$.
- **Summing Distances instead of Maximum:** The signal travels in parallel; total time is the **maximum** distance to any node, not the sum of distances.
- **Using BFS on Weighted Graphs:** Unweighted BFS finds shortest path by edge count, not by weighted time. Dijkstra's algorithm is required for weighted graphs.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Dense matrix Dijkstra: $N$ iterations to find minimum distance node ($O(N^2)$).
  - Edge relaxation across all iterations: $O(E)$.
  - Total Time: strictly $\mathcal{O}(N^2)$ with adjacency matrix, or $\mathcal{O}(E \log N)$ with a min-heap. For $N = 100$, completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ for the adjacency matrix (or $\mathcal{O}(N + E)$ for adjacency list) and $\mathcal{O}(N)$ for distances.
