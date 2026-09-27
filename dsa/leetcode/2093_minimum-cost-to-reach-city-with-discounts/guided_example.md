# Guided Example: Minimum Cost to Reach City With Discounts

We trace state-augmented shortest path exploration, priority queue Dijkstra relaxation, and optimal discount allocation on a representative transportation network:

- **Number of Cities $n$:** `5`
- **Highway Tolls:**
  - `[0, 1, 4]` (toll 4)
  - `[2, 1, 3]` (toll 3)
  - `[1, 4, 11]` (toll 11)
  - `[3, 2, 3]` (toll 3)
  - `[3, 4, 2]` (toll 2)
- **Discounts Available:** `1`
- **Expected Output:** `9`

---

## 1. Problem Overview & Representative Instance

We are given a network of $n$ cities numbered $0$ to $n - 1$ connected by bidirectional toll highways. We start at city $0$ and wish to reach city $n - 1$ with the minimum possible total toll.
We are equipped with `discounts` discount coupons.
- Each coupon allows us to cut the toll of a single traversed highway in half, rounded down to the nearest integer: $\lfloor \text{toll} / 2 \rfloor$.
- Each highway can receive at most one discount coupon.
- We can use at most `discounts` coupons throughout the entire journey.
- If it is impossible to reach city $n - 1$, we return `-1`.

For our instance ($n = 5, \text{discounts} = 1$):
- Route 1: $0 \to 1 \to 4$.
  - Undiscounted total: $4 + 11 = 15$.
  - With 1 discount on $(1, 4)$: $4 + \lfloor 11/2 \rfloor = 4 + 5 = 9$.
- Route 2: $0 \to 1 \to 2 \to 3 \to 4$.
  - Undiscounted total: $4 + 3 + 3 + 2 = 12$.
  - With 1 discount on $(0, 1)$: $\lfloor 4/2 \rfloor + 3 + 3 + 2 = 2 + 3 + 3 + 2 = 10$.
The optimal journey is Route 1 with cost $9$.

```mermaid
flowchart TD
    accTitle: Layered Dijkstra State Space
    accDescr: 2D state space (city, discounts_used) where each edge offers an undiscounted transition on the same layer and a discounted transition to the next layer.
    subgraph Layer0["Layer 0: 0 Discounts Used"]
        C0_0["(City 0, 0)"] -->|Toll 4| C1_0["(City 1, 0)"]
        C1_0 -->|Toll 11| C4_0["(City 4, 0)"]
        C1_0 -->|Toll 3| C2_0["(City 2, 0)"]
        C2_0 -->|Toll 3| C3_0["(City 3, 0)"]
        C3_0 -->|Toll 2| C4_0
    end

    subgraph Layer1["Layer 1: 1 Discount Used"]
        C1_1["(City 1, 1)"]
        C4_1["(City 4, 1)"]
    end

    C1_0 -.->|Discounted Toll floor(11/2) = 5| C4_1
    C0_0 -.->|Discounted Toll floor(4/2) = 2| C1_1

    classDef l0 fill:#dbeafe,stroke:#1d4ed8,stroke-width:2px;
    classDef l1 fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    class C0_0,C1_0,C2_0,C3_0,C4_0 l0;
    class C1_1,C4_1 l1;
```

---

## 2. Theoretical Invariants & Layered Graph Dijkstra

### Invariant 1: State Augmentation
Because an edge can be traversed with or without a discount coupon, the optimal decision at city $u$ depends on how many discounts $k \in [0, \text{discounts}]$ remain.
We construct an augmented state space:
$$\text{State} = (u, k)$$
where $u \in \{0, \dots, n - 1\}$ is the current city, and $k$ is the number of discounts consumed so far.
The target is to find:
$$\min_{0 \le k \le \text{discounts}} \text{dist}[n - 1][k]$$

### Invariant 2: Non-Negative State Transitions
From state $(u, k)$, traversing an edge $(u, v)$ with toll $w$ generates two candidate transitions:
1. **Regular Transition (No Discount):**
   $$(u, k) \xrightarrow{w} (v, k)$$
2. **Discounted Transition (Spend 1 Coupon, if $k < \text{discounts}$):**
   $$(u, k) \xrightarrow{\lfloor w / 2 \rfloor} (v, k + 1)$$

Since all edge weights $w \ge 0$, all transition costs are strictly non-negative ($w \ge 0$ and $\lfloor w / 2 \rfloor \ge 0$). Therefore, Dijkstra's algorithm with a min-priority queue guarantees that the first time any state $(u, k)$ is popped from the heap, its recorded distance is optimal.

| State Vector | Components | Invariant Property |
|---|---|---|
| Heap Entry | $(\text{cost}, u, k)$ | Min-heap ordered by cumulative toll $\text{cost}$ |
| Distance Table | $\text{dist}[u][k]$ | Minimum toll to reach city $u$ using exactly $k$ discounts |
| Target State | $(n - 1, k)$ | First extraction of any $(n - 1, k)$ terminates search |

---

## 3. Step-by-Step Worked Execution

We trace Dijkstra's algorithm on the sample network ($n = 5, \text{discounts} = 1$):
- Distance table $\text{dist}[u][k]$ initialized to $\infty$.
- Seed heap with start state: $(0, 0, 0)$ (cost $0$, city $0$, $0$ discounts used).

---

### Step 1: Pop $(0, 0, 0)$
- City $0$ with $k = 0$ discounts.
- Neighbors of $0$: city $1$ with toll $4$.
  - Regular move: push $(0 + 4, 1, 0) = (4, 1, 0)$.
  - Discounted move ($k < 1$): push $(0 + \lfloor 4/2 \rfloor, 1, 1) = (2, 1, 1)$.
- Heap state: `[(2, 1, 1), (4, 1, 0)]`.

---

### Step 2: Pop $(2, 1, 1)$
- City $1$ with $k = 1$ discount consumed.
- $k = 1 = \text{discounts}$, so no further discounts can be spent from this branch!
- Neighbors of $1$:
  - Edge $(1, 4, 11)$: regular push $(2 + 11, 4, 1) = (13, 4, 1)$.
  - Edge $(1, 2, 3)$: regular push $(2 + 3, 2, 1) = (5, 2, 1)$.
- Heap state: `[(4, 1, 0), (5, 2, 1), (13, 4, 1)]`.

---

### Step 3: Pop $(4, 1, 0)$
- City $1$ with $k = 0$ discounts consumed.
- Neighbors of $1$:
  - Edge $(1, 4, 11)$:
    - Regular move: push $(4 + 11, 4, 0) = (15, 4, 0)$.
    - Discounted move ($k < 1$): push $(4 + \lfloor 11/2 \rfloor, 4, 1) = (4 + 5, 4, 1) = (9, 4, 1)$.
  - Edge $(1, 2, 3)$:
    - Regular move: push $(4 + 3, 2, 0) = (7, 2, 0)$.
    - Discounted move: push $(4 + \lfloor 3/2 \rfloor, 2, 1) = (4 + 1, 2, 1) = (5, 2, 1)$ (already reached with cost 5).
- Heap state: `[(5, 2, 1), (7, 2, 0), (9, 4, 1), (13, 4, 1), (15, 4, 0)]`.

---

### Step 4: Pop $(5, 2, 1)$
- City $2$ with $k = 1$ discount.
- Neighbors of $2$:
  - Edge $(2, 3, 3)$: regular push $(5 + 3, 3, 1) = (8, 3, 1)$.
- Heap state: `[(7, 2, 0), (8, 3, 1), (9, 4, 1), (13, 4, 1), (15, 4, 0)]`.

---

### Step 5: Pop $(7, 2, 0)$
- City $2$ with $k = 0$ discounts.
- Neighbors of $2$:
  - Edge $(2, 3, 3)$:
    - Regular push: $(7 + 3, 3, 0) = (10, 3, 0)$.
    - Discounted push: $(7 + 1, 3, 1) = (8, 3, 1)$.

---

### Step 6: Pop $(8, 3, 1)$
- City $3$ with $k = 1$ discount.
- Neighbors of $3$:
  - Edge $(3, 4, 2)$: regular push $(8 + 2, 4, 1) = (10, 4, 1)$.

---

### Step 7: Pop $(9, 4, 1)$
- Extracted state: city $4$ with cost $9$!
- Destination reached: city $4 = n - 1$.
- Because Dijkstra pops states in non-decreasing order of cost, $9$ is guaranteed to be the global minimum cost!
- Search terminates immediately. Return $9$.

---

## 4. Complete Execution Trace & Heap Extraction Table

Below is the state progression trace across the priority queue extractions:

| Heap Extraction Step | Popped Cost | Current City $u$ | Discounts Used $k$ | Destination Reached? | New Transitions Pushed to Heap |
|---|---|---|---|---|---|
| Step 1 | $0$ | $0$ | $0$ | No | $(4, 1, 0)$, $(2, 1, 1)$ |
| Step 2 | $2$ | $1$ | $1$ | No | $(5, 2, 1)$, $(13, 4, 1)$ |
| Step 3 | $4$ | $1$ | $0$ | No | $(7, 2, 0)$, **$(9, 4, 1)$**, $(15, 4, 0)$ |
| Step 4 | $5$ | $2$ | $1$ | No | $(8, 3, 1)$ |
| Step 5 | $7$ | $2$ | $0$ | No | $(10, 3, 0)$, $(8, 3, 1)$ |
| Step 6 | $8$ | $3$ | $1$ | No | $(10, 4, 1)$ |
| **Step 7 (Final)** | **$9$** | **$4$ ($n - 1$)** | **$1$** | **Yes!** | **Target reached; return 9** |

---

## 5. Algorithmic Correctness & Soundness

1. **Optimality of Layered Graph Dijkstra:**
   The state space is a Directed Acyclic Graph (DAG) with respect to the discount counter $k$, since $k$ can only increase.
   Because all edge costs ($w$ and $\lfloor w / 2 \rfloor$) are non-negative, Dijkstra's algorithm maintains the invariant that once a node $(u, k)$ is popped from the priority queue, no shorter path to $(u, k)$ can ever be discovered.
2. **Floor Division Compliance:**
   The specification states that the toll is halved and rounded down. Using integer division $\lfloor w / 2 \rfloor$ adheres strictly to this rule.
3. **Disconnection Detection:**
   If the priority queue becomes empty without ever popping a state with $u = n - 1$, then no path exists connecting city $0$ to city $n - 1$ within the discount budget. Emitting $-1$ is correct and sound.

---

## 6. Edge Cases, Pitfalls & Structural Traps

- **Zero Discounts Available ($\text{discounts} = 0$):**
  When discounts is 0, the algorithm only executes regular transitions on layer 0, reducing identically to standard Dijkstra shortest path.
- **More Discounts Than Highway Edges:**
  Having `discounts = 20` on a path of length 3 is harmless: the discount counter increments at each discounted edge, but unused coupons do not alter the correctness.
- **Revisiting States with Higher Cost:**
  Maintaining `dist[u][k]` and pruning any popped tuple with $\text{cost} > \text{dist}[u][k]$ prevents redundant relaxations and infinite cycles.

---

## 7. Complexity Analysis

- **Time Complexity:**
  - The augmented graph has $|V'| = n \cdot (\text{discounts} + 1)$ states.
  - Each highway edge $(u, v)$ induces at most $2 \cdot (\text{discounts} + 1)$ directed transitions.
  - Total edges: $|E'| = 2 \cdot m \cdot (\text{discounts} + 1)$.
  - Dijkstra's algorithm runs in $\mathcal{O}(|E'| \log |V'|) = \mathcal{O}(m \cdot d \log(n \cdot d))$ time, where $d = \text{discounts}$. For $n \le 1000, m \le 2000, d \le 30$, this takes $\approx 6 \times 10^4 \log(3 \times 10^4)$ operations, executing in under $0.05$ seconds.
- **Auxiliary Space Complexity:**
  - The distance table and adjacency graph require $\mathcal{O}(n \cdot d + m)$ memory.
  - Total auxiliary space: $\mathcal{O}(n \cdot d + m)$ working memory.
