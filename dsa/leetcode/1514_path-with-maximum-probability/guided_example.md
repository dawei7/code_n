# Guided Example: Path With Maximum Probability

## 1. Instance & Teaching Goal

We are given an undirected network containing $n = 3$ nodes and $3$ weighted communication links:
$$\text{edges} = [[0, 1], [1, 2], [0, 2]]$$
with transmission success probabilities:
$$\text{succProb} = [0.5, 0.5, 0.2]$$
We seek the optimal trajectory from $\text{start} = 0$ to $\text{end} = 2$.

Our teaching goal is to find the path that maximizes the joint product of edge success probabilities. We explain why the multiplicative nature of independent edge survival probabilities ($p \in [0, 1]$) satisfies the optimal substructure and greedy choice properties of Dijkstra's algorithm, demonstrating max-heap relaxation without logarithmic conversion.

## 2. Conceptual Foundation & Invariants

Let $G = (V, E)$ be an undirected graph where each edge $e = (u, v)$ has traversal success probability $P(e) \in [0, 1]$.
1. **Multiplicative Path Probability**:
   For a simple path $\pi = (v_0, v_1, \dots, v_k)$, the probability of traversing the entire path without failure is the product of individual link probabilities:
   $$\mathcal{P}(\pi) = \prod_{i=1}^{k} P(v_{i-1}, v_i)$$
2. **Monotonicity and Shortest Path Isomorphism**:
   Because each $P(e) \le 1$, multiplying by an edge probability never increases the total probability:
   $$\mathcal{P}(\pi \mathbin{\Vert} e) = \mathcal{P}(\pi) \cdot P(e) \le \mathcal{P}(\pi)$$
   Taking the negative logarithm transforms products into non-negative additive costs:
   $$-\log(\mathcal{P}(\pi)) = \sum_{i=1}^{k} -\log(P(v_{i-1}, v_i))$$
   Since $P(e) \in [0, 1]$, $-\log(P(e)) \ge 0$.
   Maximizing the product $\prod P(e)$ is mathematically isomorphic to minimizing the non-negative additive cost $\sum -\log P(e)$, allowing direct application of Dijkstra's algorithm.
3. **Max-Priority Queue Mechanics**:
   Rather than performing floating-point logarithms, we maintain a max-priority queue directly over probabilities:
   - Initial state: $\text{prob}[\text{start}] = 1.0$, and $\text{prob}[u] = 0.0$ for all $u \ne \text{start}$.
   - Priority queue stores pairs $(w, u)$, extracting the unvisited node with maximal tentative probability $w$.
   - **Relaxation Step**: For each neighbor $v$ of $u$ connected via edge probability $p$:
     $$\text{new\_prob} = w \cdot p$$
     If $\text{new\_prob} > \text{prob}[v]$, we update $\text{prob}[v] \leftarrow \text{new\_prob}$ and push $(\text{new\_prob}, v)$ into the priority queue.

```text
+-------------------------------------------------------------------------------+
|                    MULTIPLICATIVE DIJKSTRA STATE EXPLORATION                  |
|                                                                               |
|            (0.5)                   (0.5)                                      |
|      [0] ---------> [1] -------------------> [2]                              |
|       |                                       ^                               |
|       +---------------------------------------+                               |
|                         (0.2)                                                 |
|                                                                               |
|  Path A: 0 -> 2            Probability = 0.20                                 |
|  Path B: 0 -> 1 -> 2       Probability = 0.5 * 0.5 = 0.25 (Optimal)           |
+-------------------------------------------------------------------------------+
```

The algorithm maintains the following state variables:

| State Variable | Domain | Initial Value | Transition / Role |
|---|---|---|---|
| `best_prob` | Array of size $n$ | $\text{best\_prob}[\text{start}]=1.0$, else $0.0$ | Highest confirmed or tentative probability to reach each vertex. |
| `max_heap` | Priority queue of pairs | $[(1.0, \text{start})]$ | Orders vertices by decreasing candidate probability. |
| `active_node` | Integer $\in [0, n-1]$ | $\text{start}$ | Vertex currently extracted from top of heap. |
| `curr_prob` | Float $\in [0.0, 1.0]$ | $1.0$ | Extracted probability associated with `active_node`. |

> [!IMPORTANT]
> **Submultiplicative Invariant**: Because edge probabilities satisfy $p \in [0, 1]$, path probabilities decrease monotonically as more edges are appended. Once a node is popped with the maximal tentative probability in the priority queue, no alternative route through unvisited vertices can achieve a higher probability.

```mermaid
flowchart TD
    accTitle: Maximum Probability Dijkstra Flow
    accDescr: Flowchart illustrating max-heap priority queue extraction and probability relaxation for neighbors.
    A["Initialize best_prob array with 0.0, start = 1.0"] --> B["Push (1.0, start_node) to max_heap"]
    B --> C{"Is max_heap empty?"}
    C -->|Yes| END["Return best_prob[end_node] (0.0 if unreachable)"]
    C -->|No| D["Pop (curr_prob, u) with largest probability"]
    D --> E{"curr_prob < best_prob[u] ?"}
    E -->|Yes (Stale)| C
    E -->|No| F{"Is u == end_node ?"}
    F -->|Yes| G["Early Exit: Return curr_prob"]
    F -->|No| H["Iterate neighbors v with edge probability p"]
    H --> I{"curr_prob * p > best_prob[v] ?"}
    I -->|Yes| J["best_prob[v] = curr_prob * p, push to max_heap"]
    I -->|No| H
    J --> H
    H -->|All neighbors relaxed| C
```

## 3. Step-by-Step Worked Execution

We walk through the instance: $n = 3$, edges connecting $(0, 1)$ with $p=0.5$, $(1, 2)$ with $p=0.5$, and $(0, 2)$ with $p=0.2$, running from $\text{start} = 0$ to $\text{end} = 2$.

### Initialization

- `best_prob` table initialized to $[1.0, 0.0, 0.0]$.
- Max-heap initialized with $[(1.0, \text{Node } 0)]$.

---

### Iteration 1: Extract Node 0

- Pop highest entry: $\text{curr\_prob} = 1.0$, node $u = 0$.
- Validation: $1.0 == \text{best\_prob}[0]$ (valid entry).
- Relax neighbors of Node 0:
  - **Neighbor 1** (edge probability $0.5$):
    - Candidate probability: $1.0 \times 0.5 = 0.5$.
    - Comparison: $0.5 > \text{best\_prob}[1] = 0.0$.
    - Update: $\text{best\_prob}[1] \leftarrow 0.5$.
    - Push $(0.5, 1)$ to heap.
  - **Neighbor 2** (edge probability $0.2$):
    - Candidate probability: $1.0 \times 0.2 = 0.2$.
    - Comparison: $0.2 > \text{best\_prob}[2] = 0.0$.
    - Update: $\text{best\_prob}[2] \leftarrow 0.2$.
    - Push $(0.2, 2)$ to heap.
- Heap after Iteration 1: $[(0.5, 1), (0.2, 2)]$.

---

### Iteration 2: Extract Node 1

- Pop highest entry: $\text{curr\_prob} = 0.5$, node $u = 1$.
- Validation: $0.5 == \text{best\_prob}[1]$ (valid entry).
- Relax neighbors of Node 1:
  - **Neighbor 0** (edge probability $0.5$):
    - Candidate probability: $0.5 \times 0.5 = 0.25$.
    - Comparison: $0.25 \le \text{best\_prob}[0] = 1.0$ (no update).
  - **Neighbor 2** (edge probability $0.5$):
    - Candidate probability: $0.5 \times 0.5 = 0.25$.
    - Comparison: $0.25 > \text{best\_prob}[2] = 0.2$.
    - Update: $\text{best\_prob}[2] \leftarrow 0.25$.
    - Push $(0.25, 2)$ to heap.
- Heap after Iteration 2: $[(0.25, 2), (0.2, 2)]$.

---

### Iteration 3: Extract Node 2

- Pop highest entry: $\text{curr\_prob} = 0.25$, node $u = 2$.
- Target reached! Node $2$ is the designated `end_node`.
- Since max-priority queue extraction guarantees optimal prefix closure, $\text{best\_prob}[2] = 0.25$ is the maximum possible path probability.
- Early return: output $0.25000$.

## 4. Complete Execution Trace

We collect the complete state mutations across all heap events in the trace table below.

| Step | Operation | Node $u$ | Popped Probability | Stale Check | Neighbor $v$ | Edge $P$ | New Prob $w \cdot P$ | Prior `best_prob[v]` | Heap Update |
|---|---|---|---|---|---|---|---|---|---|
| Init | Seed | $0$ | — | — | — | — | — | — | Push $(1.0, 0)$ |
| 1 | Pop top | $0$ | $1.000$ | Valid ($1.00 \ge 1.00$) | $1$ | $0.5$ | $0.500$ | $0.000$ | Update $1 \to 0.50$, push $(0.50, 1)$ |
| 1 | Relax | $0$ | $1.000$ | Valid | $2$ | $0.2$ | $0.200$ | $0.000$ | Update $2 \to 0.20$, push $(0.20, 2)$ |
| 2 | Pop top | $1$ | $0.500$ | Valid ($0.50 \ge 0.50$) | $0$ | $0.5$ | $0.250$ | $1.000$ | Pruned ($0.25 \le 1.00$) |
| 2 | Relax | $1$ | $0.500$ | Valid | $2$ | $0.5$ | $0.250$ | $0.200$ | Update $2 \to 0.25$, push $(0.25, 2)$ |
| 3 | Pop top | $2$ | $0.250$ | Valid ($0.25 \ge 0.25$) | — | — | — | — | **Destination Reached: Return $0.25$** |

### Path Comparison Summary

The graph contains two candidate simple paths from $0$ to $2$:
1. Direct Path $0 \to 2$:
   $$\mathcal{P}(0 \to 2) = 0.20000$$
2. Two-Hop Path $0 \to 1 \to 2$:
   $$\mathcal{P}(0 \to 1 \to 2) = 0.5 \times 0.5 = 0.25000$$
The two-hop route achieves higher reliability ($0.25 > 0.20$), correctly selected by the algorithm.

## 5. Algorithmic Correctness

### Soundness

By taking the transformation $c(e) = -\log(P(e))$, each edge weight satisfies $c(e) \ge 0$.
The problem of maximizing $\prod P(e)$ is strictly equivalent to minimizing $\sum c(e)$.
Because all transformed edge weights are non-negative, Dijkstra's algorithm is guaranteed to be sound.
When working directly in probability space, the submultiplicative property ($w \cdot p \le w$ for $p \le 1$) ensures that the extracted vertex from the max-heap has reached its globally maximal probability. Any path through other frontier nodes in the heap has a starting probability $w' \le w$, and further multiplications by $p' \le 1$ cannot exceed $w$. Therefore, the probability returned is sound.

### Completeness

If a path from `start` to `end` exists with non-zero probability, breadth-first traversal via the priority queue explores all connected components having positive edge probabilities.
If `end` is disconnected from `start`, the priority queue exhausts without ever reaching `end`, and `best_prob[end]` remains $0.0$, matching the disconnected graph specification.

## 6. Traps This Instance Exposes

- **Additive Shortest Path Confusion**: Adding probabilities ($w + p$) instead of multiplying ($w \cdot p$), which misinterprets independent event probabilities as additive distance metrics.
- **Logarithmic Zero Singularity**: Computing $\log(0)$ on edges where $P(e) = 0$, producing negative infinity runtime errors. Direct probability multiplication natively handles $0$ as an absorbing element ($w \times 0 = 0$).
- **Min-Heap Inversion Trap**: Using standard min-heap logic without negating probabilities. Standard Dijkstra extracts the smallest values, whereas finding the maximum probability requires a max-priority queue (or pushing negated values $-w$).
- **Precision Underflow in Deep Graphs**: In extremely long paths, multiplying many small floating-point values can underflow to $0.0$. However, because $P(e) \le 1$ and we seek the *maximum* probability path, paths that underflow to $0$ are strictly suboptimal compared to shorter, higher-probability alternatives.

## 7. Complexity Derivation

### Time Complexity

Let $V = n$ denote the number of vertices and $E = |\text{edges}|$ denote the number of undirected edges.
- **Adjacency List Construction**: Building the graph takes $\mathcal{O}(V + E)$ time.
- **Priority Queue Operations**:
  - Each node is pushed and popped at most once per incoming relaxation, leading to at most $\mathcal{O}(E)$ push operations.
  - Each heap operation takes $\mathcal{O}(\log V)$ time.
  - Relaxing all adjacent edges across the graph takes $\mathcal{O}(E \log V)$ time.
- Total time complexity is strictly:
  $$\mathcal{O}(E \log V)$$
- With $V \le 10^4$ and $E \le 2 \times 10^4$, $E \log_2 V \approx 20,000 \times 14 \approx 2.8 \times 10^5$ operations, executing within $15$ milliseconds.

### Auxiliary Space Complexity

- **Adjacency List**: Stores $2E$ directed edge entries: $\mathcal{O}(V + E)$.
- **Probability Table**: Stores $V$ floating-point values: $\mathcal{O}(V)$.
- **Priority Queue**: Holds at most $\mathcal{O}(E)$ items: $\mathcal{O}(E)$.
- Total auxiliary space is $\mathcal{O}(V + E)$.
