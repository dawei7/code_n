# Guided Example: Cheapest Flights Within K Stops

We trace the step-by-step hop-constrained shortest path formulation ($k \text{ stops} \iff k + 1 \text{ flights}$), Bellman-Ford dynamic programming edge relaxation, synchronous state snapshotting ($backup = dist.copy()$) preventing intra-iteration chaining, distance relaxation updates ($dist[v] = \min(dist[v], backup[u] + cost)$), and unreachable node detection ($-1$) on representative flight network graphs:

- **Input:**
  - City count: $n = 3$
  - Flight routes: $flights = [[0, 1, 100], \; [1, 2, 100], \; [0, 2, 500]]$
  - Source: $src = 0$
  - Destination: $dst = 2$
  - Maximum stops: $k = 1$
- **Required output:** `200`
  - Flight network constraints & mechanics:
    - Each flight $[u, v, p]$ connects city $u$ to city $v$ with ticket cost $p$.
    - A stop is an intermediate city between $src$ and $dst$.
    - Taking at most $k$ stops means using at most:
      $$
      \text{max\_edges} = k + 1 \text{ flight segments}
      $$
    - For $src = 0, dst = 2, k = 1$:
      - Max flights allowed: $1 + 1 = 2$.
      - Path 1 (Direct, 0 stops): $0 \to 2$ with cost $500$ (1 flight).
      - Path 2 (1 stop at city 1): $0 \to 1 \to 2$ with cost $100 + 100 = 200$ (2 flights).
      - Path 2 uses exactly 1 stop ($1 \le k$) and has lower cost ($200 < 500$).
      - Cheapest valid price is **200**.
- **Bounded-Hop Bellman-Ford & Snapshot Invariant:**
  - **The Step-Limited Distance Vector:**
    - Standard Dijkstra's algorithm finds unconstrained shortest paths, which might use $> k + 1$ edges.
    - Instead, Bellman-Ford with exactly $k + 1$ rounds computes the exact minimum cost using $\le m$ edges after round $m$.
  - **The Anti-Chaining Snapshot Invariant ($backup$):**
    - In round $m$, an edge $u \to v$ must only extend paths that used at most $m - 1$ edges:
      $$
      dist^{(m)}[v] = \min\Big(dist^{(m - 1)}[v], \;\; \min_{(u, v) \in E} (dist^{(m - 1)}[u] + cost(u, v))\Big)
      $$
    - To prevent a single relaxation round from updating $u$ and then immediately using the new value of $u$ to update $v$ (which would simulate 2 hops in a single round!), we take an immutable snapshot:
      $$
      backup = dist.copy()
      $$
    - All relaxations in that round read exclusively from $backup[u]$:
      $$
      dist[v] \leftarrow \min(dist[v], \; backup[u] + p)
      $$
- **Step-by-Step Worked Execution Trace on the 3-City Network ($k = 1$):**
  - Cities: $0, 1, 2$. Source: $src = 0$, Destination: $dst = 2$.
  - Maximum allowed flight rounds: $k + 1 = 1 + 1 = \mathbf{2} \text{ rounds}$.
  - Initialize distance array:
    $$
    dist = [0, \; \infty, \; \infty]
    $$
  - **Round 1 (At most 1 flight segment):**
    - Create snapshot:
      $$
      backup = [0, \; \infty, \; \infty]
      $$
    - **Flight 1: $0 \to 1$ (Cost 100):**
      - $backup[0] = 0 \ne \infty$.
      - $dist[1] \leftarrow \min(\infty, 0 + 100) = \mathbf{100}$.
    - **Flight 2: $1 \to 2$ (Cost 100):**
      - Read from snapshot: $backup[1] = \infty$.
      - City 1 was unreachable in zero hops $\implies$ no update to $dist[2]$.
    - **Flight 3: $0 \to 2$ (Cost 500):**
      - $backup[0] = 0 \ne \infty$.
      - $dist[2] \leftarrow \min(\infty, 0 + 500) = \mathbf{500}$.
    - State at end of Round 1:
      $$
      dist = [0, \; 100, \; 500]
      $$
      *(Direct flights from source evaluated; city 2 reachable for 500)*.
  - **Round 2 (At most 2 flight segments):**
    - Create snapshot:
      $$
      backup = [0, \; 100, \; 500]
      $$
    - **Flight 1: $0 \to 1$ (Cost 100):**
      - $dist[1] \leftarrow \min(100, 0 + 100) = 100$.
    - **Flight 2: $1 \to 2$ (Cost 100):**
      - Read from snapshot: $backup[1] = 100 \ne \infty$.
      - Path candidate: $backup[1] + 100 = 100 + 100 = 200$.
      - Relax distance to city 2:
        $$
        dist[2] \leftarrow \min(500, 200) = \mathbf{200}
        $$
    - **Flight 3: $0 \to 2$ (Cost 500):**
      - $dist[2] \leftarrow \min(200, 0 + 500) = 200$.
    - State at end of Round 2:
      $$
      dist = [0, \; 100, \; 200]
      $$
  - **Output Result:**
    - Destination distance:
      $$
      ans = dist[dst] = dist[2] = \mathbf{200}
      $$
- **Strict Stop Limit Rejection Trace ($k = 0$ on same graph):**
  - Only $k + 1 = 1$ round executes.
  - Path $0 \to 1 \to 2$ cannot be evaluated because city 1 was not reachable before the round.
  - Only direct flight $0 \to 2$ is considered.
  - Returns **`500`**.
- **Completely Unreachable Destination Trace:**
  - If no path exists from $src$ to $dst$ within $k + 1$ hops:
  - $dist[dst]$ remains $\infty$ (`0x3F3F3F3F`).
  - Returns **`-1`**.

This instance demonstrates dynamic programming over path-length filtrations and synchronous Jacobi relaxation on weighted directed graphs, mathematically proves why $k+1$ iterations of Bellman-Ford compute the exact minimum over the restricted walk space $\mathcal{W}_{\le k+1}(src, dst)$, and derives $O(K \cdot |E|)$ runtime and $O(V)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given flight routes, source $src$, destination $dst$, and maximum stops $k$:
Find the **cheapest price** to reach $dst$ using **at most $k$ stops** ($k + 1$ flights).
Return `-1` if unreachable.

```text
Flights:
  0 -> 1 (cost 100)
  1 -> 2 (cost 100)
  0 -> 2 (cost 500)

src = 0, dst = 2, k = 1 stop (max 2 flights)

Round 1 (max 1 flight):
  dist[1] = 100
  dist[2] = 500

Round 2 (max 2 flights):
  dist[2] = min(500, dist[1] + 100) = 100 + 100 = 200

Result: 200
```

### The Invariant of the Synchronous Snapshot
- Exactly $k + 1$ rounds of edge relaxations must be run.
- Taking `backup = dist.copy()` before each round guarantees that each flight uses prices from $\le m - 1$ hops, preventing chaining multiple flights in a single iteration.

---

## 2. Conceptual Foundation & Invariants

### 1. Bounded Edge Recurrence:
$$
dist^{(m)}[v] = \min\left( dist^{(m - 1)}[v], \; \min_{(u, v) \in E} (dist^{(m - 1)}[u] + cost(u, v)) \right)
$$

### 2. Termination & Unreachability:
$$
\text{Total Rounds} = k + 1
$$
$$
ans = \begin{cases} dist[dst] & dist[dst] < \infty \\ -1 & dist[dst] = \infty \end{cases}
$$

> **Tropical Matrix Power Invariant.** In the min-plus semiring $(\mathbb{R} \cup \{\infty\}, \min, +)$, the $m$-hop distance vector is given by the matrix-vector product $dist^{(m)} = dist^{(0)} \otimes A^m$, where exactly $k+1$ powers of the adjacency matrix $A$ bound the walk length without cycle distortion.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Initialize
- $dist = [0, \infty, \infty]$.

---

### Step 2: Round 1 (1 Flight)
- $0 \to 1 \implies dist[1] = 100$.
- $0 \to 2 \implies dist[2] = 500$.
- $1 \to 2$ cannot be used because $backup[1] = \infty$.
- $dist = [0, 100, 500]$.

---

### Step 3: Round 2 (2 Flights)
- $backup[1] = 100$.
- $1 \to 2 \implies dist[2] = \min(500, 100 + 100) = 200$.
- $dist = [0, 100, 200]$.

---

### Step 4: Output
$$
\mathbf{200}
$$

---

## 4. Complete Execution Trace

| Round $m$ | Max Flights | Snapshot $backup$ | Edge Relaxed | Updated $dist$ |
|:---:|:---:|:---:|:---:|:---:|
| Initial | $0$ | — | — | `[0, inf, inf]` |
| $1$ | $1$ | `[0, inf, inf]` | $0 \to 1 (100), 0 \to 2 (500)$ | `[0, 100, 500]` |
| **$2$** | **$2$** | **`[0, 100, 500]`** | **$1 \to 2 (100+100=200)$** | **`[0, 100, 200]`** |
| **Final** | — | — | **$dist[2] = 200$** | **`200`** |

---

## 5. Boundary Cases & Failure Modes

- **Direct Flight Only ($k = 0$):** Executes only 1 round $\implies$ only direct flights are eligible.
- **Unreachable ($dist[dst] == \infty$):** No valid route within $k$ stops $\implies$ returns -1.
- **Cycles in Graph:** Bounded rounds naturally prevent infinite negative or positive cycling.
- **Source Equals Destination:** $dist[src] = 0$.

---

## 6. Traps & Common Anti-Patterns

- **Relaxing In-Place without a Backup Array:** If you update `dist[t]` in-place without `backup = dist.copy()`, an edge relaxed earlier in the loop can be used immediately by another edge later in the *same* round. This effectively allows $\ge 2$ flights in a single round, violating the $k$-stops limit!
- **Using Standard Dijkstra Without Hop Tracking:** Standard Dijkstra terminates early based on price, potentially picking a cheaper path that uses too many stops, and abandoning valid paths with fewer stops.
- **Off-By-One on Stop Count:** $k$ stops means at most **$k + 1$ flights** (outer loop must run $k + 1$ times).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Outer loop runs $k + 1$ times ($k \le N$).
  - Inner loop iterates over all $E$ flights: $\mathcal{O}(E)$.
  - Total Time: strictly $\mathcal{O}(K \cdot E)$ where $K \le 100, E \le 10^4$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for $dist$ and $backup$ arrays.
