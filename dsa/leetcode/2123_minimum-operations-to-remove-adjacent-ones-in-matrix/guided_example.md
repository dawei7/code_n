# Guided Example: Minimum Operations to Remove Adjacent Ones in Matrix

We trace the step-by-step execution of the bipartite graph modeling and augmenting-path maximum matching approach on a representative problem instance:

- **Input Matrix (`grid`):**
  $$\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$$
- **Expected Output:** `3`

This instance illustrates how removing adjacent pairs of identical values reduces to finding a Minimum Vertex Cover on a 2D grid graph, how checkerboard parity establishes bipartiteness, and how Kőnig's theorem equates minimum operations to maximum bipartite matching.

---

## 1. Problem Overview & Representative Instance

We are given a 0-indexed $m \times n$ binary matrix `grid`. In a single operation, we may change any cell with value $1$ to $0$. We must determine the minimum number of operations required so that no two $1$s are horizontally or vertically adjacent.

Consider our representative $3 \times 3$ matrix:
- Row 0: `[1, 1, 0]` with $1$s at $(0, 0)$ and $(0, 1)$.
- Row 1: `[0, 1, 1]` with $1$s at $(1, 1)$ and $(1, 2)$.
- Row 2: `[1, 1, 1]` with $1$s at $(2, 0)$, $(2, 1)$, and $(2, 2)$.

Adjacent $1$s create conflict edges that must be resolved. Flipping a cell to $0$ removes that cell and resolves all conflict edges incident to it. This formulation is precisely the Minimum Vertex Cover problem on the adjacency conflict graph.

---

## 2. Mathematical & Algorithmic Principles

### Bipartite Parity Decomposition
Every grid graph possesses a natural 2-coloring determined by the coordinate sum parity:

$$\pi(r, c) = (r + c) \bmod 2$$

Any adjacent neighbors $(r', c')$ have $|r - r'| + |c - c'| = 1$, which strictly inverts the parity:

$$\pi(r', c') = 1 - \pi(r, c)$$

Thus, the conflict graph $G = (V, E)$ is strictly bipartite:
- $L = \{ (r, c) \mid \text{grid}[r][c] = 1 \land (r + c) \equiv 0 \pmod 2 \}$ (Even parity set)
- $R = \{ (r, c) \mid \text{grid}[r][c] = 1 \land (r + c) \equiv 1 \pmod 2 \}$ (Odd parity set)
- Every conflict edge connects a cell in $L$ to a cell in $R$.

### Kőnig's Duality Theorem
In any bipartite graph $G$, the size of the minimum vertex cover $\tau(G)$ equals the size of the maximum matching $\nu(G)$:

$$\tau(G) = \nu(G)$$

Instead of solving the NP-hard general vertex cover problem, we find the maximum cardinality matching in polynomial time using augmenting path algorithms (Kuhn's DFS or Hopcroft-Karp).

| Parity Set | Coordinates $(r, c)$ in Instance | Total Nodes |
|---|---|---|
| Even Set $L$ | $(0, 0)$, $(1, 1)$, $(2, 0)$, $(2, 2)$ | $4$ |
| Odd Set $R$ | $(0, 1)$, $(1, 2)$, $(2, 1)$ | $3$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Graph Construction
- Even set $L = \{(0, 0), (1, 1), (2, 0), (2, 2)\}$
- Odd set $R = \{(0, 1), (1, 2), (2, 1)\}$
- Incident conflict edges:
  - From $(0, 0) \in L$: neighbor $(0, 1) \in R$.
  - From $(1, 1) \in L$: neighbors $(0, 1)$, $(1, 2)$, $(2, 1) \in R$.
  - From $(2, 0) \in L$: neighbor $(2, 1) \in R$.
  - From $(2, 2) \in L$: neighbors $(1, 2)$, $(2, 1) \in R$.

### Kuhn's Augmenting Path Search
We search for augmenting paths from each unassigned vertex in $L$:

#### Step 1: Augment from $(0, 0) \in L$
- Neighbor $(0, 1) \in R$ is currently unmatched.
- Create matching edge: $(0, 0) \longleftrightarrow (0, 1)$.
- Current matching size: $1$.

#### Step 2: Augment from $(1, 1) \in L$
- Neighbor $(0, 1)$ is already matched to $(0, 0)$.
- Next neighbor $(1, 2) \in R$ is unmatched!
- Create matching edge: $(1, 1) \longleftrightarrow (1, 2)$.
- Current matching size: $2$.

#### Step 3: Augment from $(2, 0) \in L$
- Neighbor $(2, 1) \in R$ is unmatched!
- Create matching edge: $(2, 0) \longleftrightarrow (2, 1)$.
- Current matching size: $3$.

#### Step 4: Augment from $(2, 2) \in L$
- Neighbor $(1, 2)$ is matched to $(1, 1)$. We test if $(1, 1)$ can be rerouted:
  - $(1, 1)$ can try $(0, 1)$, but $(0, 1)$ is matched to $(0, 0)$, which has no other neighbors.
  - $(1, 1)$ can try $(2, 1)$, but $(2, 1)$ is matched to $(2, 0)$, which has no other neighbors.
- Neighbor $(2, 1)$ is matched to $(2, 0)$, which cannot be rerouted.
- No augmenting path exists for $(2, 2)$.
- Matching remains at size $3$.

### Termination and Duality Result
All vertices in $L$ have been processed.
- Maximum Bipartite Matching: $\nu(G) = 3$.
- By Kőnig's Theorem, the minimum vertex cover size is $\tau(G) = 3$.
- Minimum flip operations: $3$.
(Flipping the three odd cells $(0, 1)$, $(1, 2)$, and $(2, 1)$ to $0$ completely isolates all remaining $1$s).

---

## 4. Comprehensive State Trace

The state of the bipartite matching across successive node evaluations is detailed below:

| Vertex from $L$ Evaluated | Adjacent Candidates in $R$ | Augmenting Path Discovered | Matching Edge Added | Current Matching Set | Total Matching Size |
|---|---|---|---|---|---|
| $(0, 0)$ | $(0, 1)$ | $(0, 0) \to (0, 1)$ | $(0, 0) \leftrightarrow (0, 1)$ | $\{((0,0), (0,1))\}$ | $1$ |
| $(1, 1)$ | $(0, 1), (1, 2), (2, 1)$ | $(1, 1) \to (1, 2)$ | $(1, 1) \leftrightarrow (1, 2)$ | $\{((0,0), (0,1)), ((1,1), (1,2))\}$ | $2$ |
| $(2, 0)$ | $(2, 1)$ | $(2, 0) \to (2, 1)$ | $(2, 0) \leftrightarrow (2, 1)$ | $\{((0,0), (0,1)), ((1,1), (1,2)), ((2,0), (2,1))\}$ | $3$ |
| $(2, 2)$ | $(1, 2), (2, 1)$ | None (all in $R$ saturated) | None | Unchanged | $3$ |

Final minimum vertex cover operations: $3$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** A set of flip operations eliminates all adjacent pairs if and only if for every edge $(u, v) \in E$, at least one endpoint is flipped to $0$. This matches the definition of a Vertex Cover on graph $G$. Because the grid coordinates $(r, c)$ ensure that all edges connect cells of opposite parity $(r + c) \bmod 2$, the graph is bipartite with no odd cycles. By Kőnig's Theorem, in any bipartite graph the size of the minimum vertex cover is identical to the maximum number of mutually disjoint edges (maximum matching). Augmenting path algorithms provably terminate at an optimal maximum matching.

**Completeness.** Every cell containing $1$ is assigned a vertex, and all horizontal and vertical adjacencies between $1$s are represented as edges. Because every valid augmenting path increases matching cardinality by $1$ and the algorithm halts only when no augmenting path exists from any unmatched node in $L$, Berge's Lemma guarantees that the final matching is maximal.

---

## 6. Edge Cases & Anti-Patterns

- **No Adjacent Ones:** If no two $1$s are adjacent, the edge set $E = \emptyset$. The maximum matching is $0$, correctly returning $0$ operations.
- **Checkerboard Configuration:** If $1$s are already placed in a checkerboard pattern (all in $L$ or all in $R$), no edges exist, requiring $0$ flips.
- **Isolated Ones:** Cells with value $1$ surrounded entirely by $0$s have degree $0$ and never participate in matching or cover requirements.
- **Anti-Pattern — Greedy Local Flipping:** Greedily flipping the cell with the highest degree can produce suboptimal solutions on bipartite graphs where symmetric cross-edges create subtle bottlenecks. Maximum matching resolves the global optimal cover in polynomial time.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(V \cdot E)$, where $V \le m \cdot n$ is the number of cells with $1$ and $E \le 2mn$ is the number of adjacent pairs. Kuhn's algorithm performs at most $|L| \le V$ augmenting path DFS searches, each taking $\mathcal{O}(E)$ time. (Using Hopcroft-Karp yields $\mathcal{O}(E \sqrt{V})$).
- **Auxiliary Space Complexity:** $\mathcal{O}(V + E)$ to store the adjacency list representation, the visited tracking array, and the match partner lookup tables.
