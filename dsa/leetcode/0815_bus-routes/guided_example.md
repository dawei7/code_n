# Guided Example: Bus Routes

We trace the step-by-step stop-to-bus inverted index construction ($stop \to [bus_i]$), dual visited set tracking ($vis\_bus, vis\_stop$), breadth-first search (BFS) level-order expansion on hypergraph transit networks, transfer point discovery, and minimum bus ride count derivation on representative transit route maps:

- **Input:**
  $$
  routes = [[1, 2, 7], \; [3, 6, 7]], \quad source = 1, \quad target = 6
  $$
- **Required output:** `2`
  - Bus transit network rules:
    - Each route array represents a circular bus line visiting its listed stops indefinitely.
    - Riding a single bus allows traveling between any two stops on that bus's route for a cost of **1 bus**.
    - Switching to another bus at an intersection stop incurs $+1$ bus ride.
    - Objective: Find the **minimum number of buses** to take from $source$ to $target$. Return -1 if unreachable.
    - For $routes = [[1, 2, 7], [3, 6, 7]]$ with $source = 1, target = 6$:
      - Bus 0 serves stops $\{1, 2, 7\}$.
      - Bus 1 serves stops $\{3, 6, 7\}$.
      - We board Bus 0 at stop 1 and ride to intersection stop 7 (1 bus taken).
      - At stop 7, we transfer to Bus 1 and ride directly to stop 6 (2 buses taken).
      - Total buses: **2**.
- **Hypergraph Modeling & Dual-Visited BFS Invariant:**
  - **The Stop-Bus Hypergraph:**
    - A naive graph with edges between every pair of stops on the same route would have $\mathcal{O}(L^2)$ edges per route, leading to quadratic blowup on routes with thousands of stops.
    - Instead, model the network as a bipartite hypergraph:
      - Stops are nodes.
      - Buses are hyperedges connecting all stops on their route.
    - Build an inverted index:
      $$
      g[stop] = \{ bus \mid stop \in routes[bus] \}
      $$
  - **Dual Visited Sets ($vis\_bus, vis\_stop$):**
    - Once a bus line is boarded and all its stops are enqueued, boarding that bus line again in a later turn can never yield a shorter path!
    - Tracking visited **buses** ($vis\_bus$) guarantees that each bus route is traversed **at most once**, strictly bounding queue operations to $\mathcal{O}(\sum |routes[i]|)$.
    - Tracking visited **stops** ($vis\_stop$) prevents redundant queue entries.
- **Step-by-Step Worked Execution Trace on $source = 1, target = 6$:**
  - Inverted stop map:
    - Stop 1: $[0]$
    - Stop 2: $[0]$
    - Stop 3: $[1]$
    - Stop 6: $[1]$
    - Stop 7: $[0, 1]$ (Transfer hub!)
  - Initialize:
    - $q = [(1, 0)]$ (Queue holding $(stop, bus\_count)$)
    - $vis\_bus = \emptyset$
    - $vis\_stop = \{1\}$
  - **Level 0 (Start at Stop 1):**
    - Dequeue $(1, 0)$.
    - Stop 1 connects to bus lines: $g[1] = [0]$.
    - **Inspect Bus 0:**
      - Bus 0 not in $vis\_bus \implies$ mark visited: $vis\_bus.\text{add}(0)$.
      - All stops on Bus 0 ($routes[0] = [1, 2, 7]$):
        - Stop 1: already in $vis\_stop$.
        - Stop 2: new stop!
          - $vis\_stop.\text{add}(2)$
          - Enqueue: $q.\text{append}((2, 0 + 1)) \to (2, 1)$.
        - Stop 7: new stop!
          - $vis\_stop.\text{add}(7)$
          - Enqueue: $q.\text{append}((7, 0 + 1)) \to (7, 1)$.
    - Queue after Level 0:
      $$
      q = [(2, 1), \; (7, 1)]
      $$
  - **Level 1 (Stops reachable with 1 bus):**
    - **Process $(2, 1)$:**
      - Stop 2 is not target ($2 \ne 6$).
      - Bus lines at stop 2: $g[2] = [0]$.
      - Bus 0 is already in $vis\_bus \implies$ skip!
    - **Process $(7, 1)$:**
      - Stop 7 is not target ($7 \ne 6$).
      - Bus lines at stop 7: $g[7] = [0, 1]$.
      - Bus 0: already in $vis\_bus \implies$ skip.
      - **Inspect Bus 1:**
        - Bus 1 not in $vis\_bus \implies$ mark visited: $vis\_bus.\text{add}(1)$.
        - All stops on Bus 1 ($routes[1] = [3, 6, 7]$):
          - Stop 3: new stop!
            - $vis\_stop.\text{add}(3)$
            - Enqueue: $q.\text{append}((3, 1 + 1)) \to (3, 2)$.
          - Stop 6: new stop!
            - $vis\_stop.\text{add}(6)$
            - Enqueue: $q.\text{append}((6, 1 + 1)) \to (6, 2)$.
          - Stop 7: already in $vis\_stop$.
    - Queue after Level 1:
      $$
      q = [(3, 2), \; (6, 2)]
      $$
  - **Level 2 (Stops reachable with 2 buses):**
    - **Process $(3, 2)$:**
      - Stop 3 is not target ($3 \ne 6$).
      - Bus 1 already visited $\implies$ skip.
    - **Process $(6, 2)$:**
      - Target matched:
        $$
        stop == target \iff 6 == 6 \implies \mathbf{Destination\ Reached!}
        $$
      - Return current bus count:
        $$
        ans = \mathbf{2}
        $$
- **Immediate Source Equals Target Trace ($source == target$):**
  - If $source == target$, zero buses are needed $\implies$ returns **`0`**.
- **Disconnected Route Groups Trace ($source$ and $target$ in separate components):**
  - Queue empties without reaching $target \implies$ returns **`-1`**.

This instance demonstrates shortest-path distance on hypergraph incidence structures and bipartite BFS with duality visited pruning, mathematically proves why marking hyperedges visited strictly eliminates quadratic clique expansions, and derives $O(\sum |routes[i]|)$ execution time and $O(\sum |routes[i]|)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given bus routes and start/destination stops:
Find the **minimum number of buses** to travel from $source$ to $target$.
Return -1 if impossible.

```text
routes:
  Bus 0: [ 1, 2, 7 ]
  Bus 1: [ 3, 6, 7 ]

source = 1, target = 6

Step 1: Board Bus 0 at stop 1 -> can reach { 1, 2, 7 } with 1 bus.
Step 2: Transfer at stop 7 to Bus 1 -> can reach { 3, 6, 7 } with 2 buses.
Target 6 reached!

Result: 2
```

### The Invariant of the Dual-Visited BFS
- We must track visited **buses** ($vis\_bus$) in addition to visited **stops** ($vis\_stop$).
- Marking each bus route visited as soon as it is boarded ensures that each bus line is explored at most once.
- This prevents $O(S^2)$ clique expansion and guarantees linear runtime.

---

## 2. Conceptual Foundation & Invariants

### 1. Inverted Stop-to-Bus Index:
$$
g[stop] = \{ i \mid stop \in routes[i] \}
$$

### 2. Hypergraph Breadth-First Search:
$$
\text{Pop } (u, c) \implies \forall bus \in g[u] \setminus vis\_bus:
$$
$$
vis\_bus \leftarrow vis\_bus \cup \{bus\}
$$
$$
\forall v \in routes[bus] \setminus vis\_stop: \; q.\text{append}((v, c + 1))
$$

> **Hypergraph Incidence Invariant.** The bus route system is a bipartite graph $G = (V_{stops} \sqcup V_{buses}, E)$. The minimum number of buses corresponds to half the unweighted shortest-path distance in the bipartite incidence graph.

---

## 3. Step-by-Step Worked Execution

We trace $routes = [[1, 2, 7], [3, 6, 7]], source = 1, target = 6$:

---

### Step 1: Initialize
- $q = [(1, 0)]$.
- $vis\_stop = \{1\}$.

---

### Step 2: Pop $(1, 0)$
- Board Bus 0 $\implies$ enqueue $(2, 1)$ and $(7, 1)$.

---

### Step 3: Pop $(2, 1)$
- Bus 0 already visited $\implies$ no new stops.

---

### Step 4: Pop $(7, 1)$
- Board Bus 1 $\implies$ enqueue $(3, 2)$ and $(6, 2)$.

---

### Step 5: Pop $(6, 2)$
- Stop $6 == target \implies$ return **`2`**.

---

## 4. Complete Execution Trace

| Dequeued Element | Current Bus Count | Candidate Bus Lines | Newly Boarded Bus | Stops Added to Queue |
|:---:|:---:|:---:|:---:|:---:|
| $(1, 0)$ | $0$ | Bus $0$ | Bus $0$ | $(2, 1), (7, 1)$ |
| $(2, 1)$ | $1$ | Bus $0$ (Visited) | None | None |
| $(7, 1)$ | $1$ | Bus $0$ (Visited), Bus $1$ | **Bus $1$** | $(3, 2), (6, 2)$ |
| $(3, 2)$ | $2$ | Bus $1$ (Visited) | None | None |
| **$(6, 2)$** | **$2$** | **Target Reached!** | — | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **$source == target$:** Already at destination $\implies 0$ buses.
- **Source or Target Not in Any Route:** Cannot board or arrive $\implies -1$.
- **Disconnected Routes:** No transfer path exists $\implies -1$.
- **Single Route Contains Both ($[1, 6]$):** 1 bus needed $\implies 1$.

---

## 6. Traps & Common Anti-Patterns

- **Building Complete Stop-to-Stop Graph ($O(N \cdot L^2)$):** If a route has 500 stops, generating all edges between stops creates $\approx 125,000$ edges per route, causing Memory and Time Limit Exceeded. Traversing via the inverted index `g[stop]` directly maintains linear time.
- **Not Tracking Visited Buses:** If only stops are tracked, the same long bus route might be re-scanned repeatedly from multiple intersection stops. Marking `vis_bus` ensures each bus route is traversed once.
- **Missing Immediate $source == target$ Check:** Always check $source == target$ at the entry point to return 0.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Inverted index construction: $\mathcal{O}(\sum |routes[i]|)$.
  - BFS visits each bus at most once and each stop at most once: $\mathcal{O}(\sum |routes[i]|)$.
  - Total Time: strictly linear in input size $\mathcal{O}(\sum |routes[i]|)$ where $\sum |routes[i]| \le 10^5$. Completes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\sum |routes[i]|)$ memory for the inverted index, queue, and visited sets.
