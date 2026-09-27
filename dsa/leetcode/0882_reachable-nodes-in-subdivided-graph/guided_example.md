# Guided Example: Reachable Nodes in Subdivided Graph

We trace the step-by-step weighted graph abstraction ($cnt + 1$ edge lengths), Dijkstra shortest path tree computation, remaining move radius evaluation, dual-end edge overlap deduplication, and total node reachability derivation on representative subdivided graphs:

- **Input:**
  $$
  edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]], \quad maxMoves = 6, \quad n = 3
  $$
- **Required output:** `13`
  - Subdivided graph anatomy & rules:
    - We are given an undirected graph with $n = 3$ original nodes labeled $0, 1, 2$.
    - Each edge $(u, v)$ is subdivided by inserting $cnt$ new nodes directly onto the edge.
    - Walking from $u$ to $v$ directly across the edge takes $cnt + 1$ individual unit steps.
    - We start at node $0$ with a maximum step budget $maxMoves = 6$.
    - Objective: Find the total number of nodes (both original nodes and newly inserted subdivision nodes) that can be reached from node $0$ within $maxMoves$ steps.
    - Breakdown for this instance:
      - Major nodes reached: Nodes $0, 1, 2$ (all $3$ are within distance $6$).
      - Along edge $(0, 1)$ ($10$ new nodes): $7$ nodes reached ($6$ from node 0, $1$ from node 1).
      - Along edge $(0, 2)$ ($1$ new node): $1$ node reached (fully traversed).
      - Along edge $(1, 2)$ ($2$ new nodes): $2$ nodes reached (fully traversed).
      - Total reachable nodes: $3 + 7 + 1 + 2 = \mathbf{13}$.
- **The Weighted Dijkstra & Dual-End Invariant:**
  - **Edge Weight Representation:**
    - Explicitly modeling each of the thousands of subdivision nodes would create an enormous graph ($V \approx 10^7$).
    - Instead, we treat each edge $(u, v)$ as a single weighted edge with weight:
      $$
      w(u, v) = cnt + 1
      $$
    - The original graph has only $n \le 3000$ vertices and $|E| \le 10000$ edges.
  - **Dijkstra on Original Nodes:**
    - Compute the shortest path distance $dist[u]$ from source $0$ to every major node $u \in [0, n - 1]$ using Dijkstra's algorithm.
    - A major node $u$ is reachable if and only if $dist[u] \le maxMoves$.
  - **Dual-End Penetration on Subdivided Edges:**
    - For each edge $(u, v)$ with $cnt$ subdivision nodes:
      - From endpoint $u$, the remaining moves available to penetrate into the edge is $\max(0, maxMoves - dist[u])$. We can cover up to $a = \min(cnt, \max(0, maxMoves - dist[u]))$ nodes.
      - From endpoint $v$, the remaining moves available to penetrate from the other side is $\max(0, maxMoves - dist[v])$. We can cover up to $b = \min(cnt, \max(0, maxMoves - dist[v]))$ nodes.
      - Since both traversals move toward each other along the same chain of $cnt$ nodes, the total unique subdivision nodes covered is:
        $$
        \text{covered}(u, v) = \min(cnt, \; a + b)
        $$
      - Capping at $cnt$ naturally eliminates double-counting overlapping meets!

---

## 1. Instance & Teaching Goal

Given $n = 3, maxMoves = 6$, and edges $(0, 1, 10), (0, 2, 1), (1, 2, 2)$:
Find all reachable original and subdivision nodes.

```text
Original Graph with Edge Weights (cnt + 1):
  (0) ---- 11 ---- (1)
    \             /
     2           3
      \         /
         (2)

Dijkstra Shortest Paths from Node 0:
  dist[0] = 0  (<= 6, Reached!)
  dist[2] = 0 + 2 = 2 (<= 6, Reached!)
  dist[1] = min(11, dist[2] + 3) = min(11, 2 + 3) = 5 (<= 6, Reached!)

Subdivision Node Penetration:
  Edge (0, 1, 10): from 0: min(10, 6 - 0) = 6
                   from 1: min(10, 6 - 5) = 1
                   total = min(10, 6 + 1) = 7
  Edge (0, 2, 1):  from 0: min(1, 6 - 0) = 1
                   from 2: min(1, 6 - 2) = 1
                   total = min(1, 1 + 1) = 1
  Edge (1, 2, 2):  from 1: min(2, 6 - 5) = 1
                   from 2: min(2, 6 - 2) = 2
                   total = min(2, 1 + 2) = 2

Total = 3 (major) + 7 + 1 + 2 = 13
```

The teaching goal is to show how contracting chains of dummy vertices into weighted edges preserves exact path metrics without memory explosion.

---

## 2. Conceptual Foundation & Invariants

### 1. Weighted Adjacency:
For each undirected edge $(u, v, cnt)$:
$$
\text{weight}(u, v) = cnt + 1
$$

### 2. Major Node Distances:
$$
dist[u] = \text{shortest path distance from node } 0 \text{ to } u
$$
Count of reachable major nodes:
$$
\text{Major Count} = \sum_{u=0}^{n-1} \mathbb{I}[dist[u] \le maxMoves]
$$

### 3. Edge Chain Coverage:
For each edge $e = (u, v, cnt)$:
$$
a = \min(cnt, \; \max(0, maxMoves - dist[u]))
$$
$$
b = \min(cnt, \; \max(0, maxMoves - dist[v]))
$$
$$
\text{Reachable Nodes on Edge } e = \min(cnt, \; a + b)
$$

---

## 3. Step-by-Step Worked Execution

We trace $maxMoves = 6, n = 3$:
Edges:
- Edge $(0, 1)$: $cnt = 10 \implies \text{weight} = 11$.
- Edge $(0, 2)$: $cnt = 1 \implies \text{weight} = 2$.
- Edge $(1, 2)$: $cnt = 2 \implies \text{weight} = 3$.

---

### Phase 1: Dijkstra Shortest Path Search
Initialize distances: $dist[0] = 0, dist[1] = \infty, dist[2] = \infty$.
Priority queue: $[(0, 0)]$.

---

#### Step 1: Pop $(d=0, u=0)$
- Explore neighbors of $0$:
  - Neighbor $2$ (weight $2$):
    $$
    d + 2 = 0 + 2 = 2 < \infty \implies dist[2] \leftarrow 2
    $$
    Push $(2, 2)$ to queue.
  - Neighbor $1$ (weight $11$):
    $$
    d + 11 = 0 + 11 = 11 < \infty \implies dist[1] \leftarrow 11
    $$
    Push $(11, 1)$ to queue.

---

#### Step 2: Pop $(d=2, u=2)$
- Explore neighbors of $2$:
  - Neighbor $0$: $2 + 2 = 4 > dist[0] = 0$. Skip.
  - Neighbor $1$ (weight $3$):
    $$
    d + 3 = 2 + 3 = 5 < dist[1] = 11 \implies dist[1] \leftarrow 5
    $$
    Push $(5, 1)$ to queue.

---

#### Step 3: Pop $(d=5, u=1)$
- Neighbors of $1$:
  - Neighbor $0$: $5 + 11 = 16 > 0$.
  - Neighbor $2$: $5 + 3 = 8 > 2$.
- No updates.

---

#### Final Distances:
$$
dist = [0, 5, 2]
$$

---

### Phase 2: Tally Reachable Major Nodes
- $dist[0] = 0 \le 6 \implies \mathbf{Reached}$
- $dist[1] = 5 \le 6 \implies \mathbf{Reached}$
- $dist[2] = 2 \le 6 \implies \mathbf{Reached}$
- Major nodes reached: $1 + 1 + 1 = \mathbf{3}$.

---

### Phase 3: Tally Reachable Subdivision Nodes on Edges

---

#### Edge 1: $(u=0, v=1, cnt=10)$
- From $u=0$: remaining moves $= 6 - dist[0] = 6 - 0 = 6$.
  $$
  a = \min(10, 6) = 6
  $$
- From $v=1$: remaining moves $= 6 - dist[1] = 6 - 5 = 1$.
  $$
  b = \min(10, 1) = 1
  $$
- Total on this edge:
  $$
  \min(10, a + b) = \min(10, 6 + 1) = \mathbf{7}
  $$

---

#### Edge 2: $(u=0, v=2, cnt=1)$
- From $u=0$: remaining moves $= 6 - 0 = 6 \implies a = \min(1, 6) = 1$.
- From $v=2$: remaining moves $= 6 - 2 = 4 \implies b = \min(1, 4) = 1$.
- Total on this edge:
  $$
  \min(1, a + b) = \min(1, 1 + 1) = \mathbf{1}
  $$

---

#### Edge 3: $(u=1, v=2, cnt=2)$
- From $u=1$: remaining moves $= 6 - 5 = 1 \implies a = \min(2, 1) = 1$.
- From $v=2$: remaining moves $= 6 - 2 = 4 \implies b = \min(2, 4) = 2$.
- Total on this edge:
  $$
  \min(2, a + b) = \min(2, 1 + 2) = \mathbf{2}
  $$

---

### Phase 4: Summing All Reachable Nodes
$$
ans = 3 + 7 + 1 + 2 = \mathbf{13}
$$

---

## 4. Complete Execution Trace

| Component | Entity Evaluated | Shortest Distance / Parameters | Remaining Moves Available | Reach Calculation | Unique Nodes Reached | Running Total |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Major Node | Node $0$ | $dist[0] = 0$ | $6$ | $0 \le 6$ | $1$ | $1$ |
| Major Node | Node $1$ | $dist[1] = 5$ | $1$ | $5 \le 6$ | $1$ | $2$ |
| Major Node | Node $2$ | $dist[2] = 2$ | $4$ | $2 \le 6$ | $1$ | $3$ |
| Edge Chain | $(0, 1)$ | $cnt = 10$ | From 0: 6, From 1: 1 | $\min(10, 6 + 1)$ | $7$ | $10$ |
| Edge Chain | $(0, 2)$ | $cnt = 1$ | From 0: 6, From 2: 4 | $\min(1, 1 + 1)$ | $1$ | $11$ |
| **Edge Chain** | **$(1, 2)$** | **$cnt = 2$** | **From 1: 1, From 2: 4** | **$\min(2, 1 + 2)$** | **$2$** | **`13`** |

---

## 5. Boundary Cases & Failure Modes

- **$maxMoves = 0$:** Can only reach origin node $0$. Distances to all other nodes $> 0$. Returns $1$.
- **Disconnected Graph:** Unreachable major nodes retain $dist[u] = \infty$; remaining moves are clamped to $\max(0, maxMoves - \infty) = 0$.
- **Edge Not Fully Traversed from Either Side:** When $a + b < cnt$, only $a + b$ nodes are reached; capping at $cnt$ is not triggered.
- **Overlapping Edge Penetration:** When $a + b > cnt$, capping $\min(cnt, a + b)$ ensures nodes in the middle are counted once.

---

## 6. Traps & Common Anti-Patterns

- **Explicitly Expanding Subdivision Nodes:** Adding dummy vertices into the graph expands vertex count to $|V| + \sum cnt \approx 3000 + 10^4 \times 10^4 \approx 10^8$, crashing the runtime with Out Of Memory.
- **Double-Counting Meeting Points on Edges:** Simply adding $a + b$ without capping at $cnt$ counts shared nodes twice whenever both endpoints have sufficient remaining moves to meet in the middle.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Graph construction: $\mathcal{O}(|E|)$ edges.
  - Dijkstra algorithm using binary min-heap: $\mathcal{O}(|E| \log |V|)$ where $|V| \le 3000$ and $|E| \le 10^4$.
  - Edge post-processing pass: $\mathcal{O}(|E|)$.
  - Total Time: $\mathcal{O}(|E| \log |V|)$, completing in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - Adjacency list and distance array: $\mathcal{O}(|V| + |E|)$ space ($\approx 500$ KB).
