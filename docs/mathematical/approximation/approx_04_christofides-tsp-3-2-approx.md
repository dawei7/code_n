# Formal Mathematical Specification: Christofides TSP (1.5-Approximation)

## 1. Definitions and Notation

Let $G = (V, E, w)$ be a complete, undirected, weighted graph where:
*   $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices representing the cities, with $|V| = n$.
*   $E = \{\{u, v\} \mid u, v \in V, u \neq v\}$ is the set of edges, with $|E| = \frac{n(n-1)}{2}$.
*   $w: E \to \mathbb{R}_{\ge 0}$ is a symmetric weight function assigning a non-negative real cost to each edge. For convenience, we write $w(u, v)$ instead of $w(\{u, v\})$.

### The Metric Property
The weight function $w$ satisfies the **triangle inequality** (metric property):
$$\forall u, v, z \in V, \quad w(u, z) \le w(u, v) + w(v, z)$$

### Subgraphs and Trees
*   **Spanning Tree:** A subgraph $T = (V, E_T)$ of $G$ that is connected and acyclic.
*   **Minimum Spanning Tree (MST):** A spanning tree $T$ that minimizes the total edge weight:
    $$w(T) = \sum_{e \in E_T} w(e)$$
*   **Induced Subgraph:** For a subset of vertices $U \subseteq V$, the induced subgraph $G[U] = (U, E_U, w|_{E_U})$ contains only the vertices in $U$ and the edges in $E$ whose endpoints both belong to $U$.

### Matchings and Circuits
*   **Perfect Matching:** Given a graph $H = (V_H, E_H)$, a matching $M \subseteq E_H$ is perfect if every vertex $v \in V_H$ is incident to exactly one edge in $M$. This requires $|V_H|$ to be even.
*   **Minimum-Weight Perfect Matching (MWPM):** A perfect matching $M$ on $H$ that minimizes $\sum_{e \in M} w(e)$.
*   **Multigraph:** A graph $H' = (V, E_{H'})$ where $E_{H'}$ is a multiset of edges, allowing multiple edges between the same pair of vertices. We denote multiset union by $\uplus$.
*   **Eulerian Circuit:** A closed walk in a multigraph that traverses every edge in the multiset exactly once.
*   **Hamiltonian Cycle (TSP Tour):** A closed walk in $G$ that visits every vertex in $V$ exactly once and returns to the starting vertex. Let $\mathcal{H}$ denote the set of all Hamiltonian cycles in $G$.
*   **Optimal TSP Tour:** A Hamiltonian cycle $H^* \in \mathcal{H}$ such that:
    $$w(H^*) = \min_{H \in \mathcal{H}} w(H)$$

---

## 2. Algebraic Characterization

The Christofides algorithm constructs a Hamiltonian cycle $H$ through a sequence of graph-theoretic transformations.

```
                  [ Input Graph G ]
                          │
                          ▼
               [ Step 1: Compute MST T ]
                          │
                          ▼
         [ Step 2: Identify Odd-Degree Vertices O ]
                          │
                          ▼
       [ Step 3: Compute MWPM M on Induced Subgraph G[O] ]
                          │
                          ▼
         [ Step 4: Form Multigraph H' = T ⊎ M ]
                          │
                          ▼
            [ Step 5: Find Eulerian Circuit C ]
                          │
                          ▼
            [ Step 6: Shortcut C to Tour H ]
```

### Step 1: Minimum Spanning Tree Construction
We compute an MST $T = (V, E_T)$ of $G$. 
$$\text{Minimize } \sum_{e \in E_T} w(e) \quad \text{subject to } (V, E_T) \text{ being a spanning tree.}$$

#### Lemma 1 (MST Lower Bound)
The weight of the MST $T$ is strictly less than the weight of the optimal TSP tour $H^*$:
$$w(T) < w(H^*)$$

*Proof:* Let $H^*$ be the optimal Hamiltonian cycle. Removing any single edge from $H^*$ yields a spanning path $P$. Since a spanning path is a spanning tree, and $T$ is the *minimum* spanning tree, we have:
$$w(T) \le w(P) < w(H^*)$$
The strict inequality holds because edge weights are non-negative, and $H^*$ contains at least one edge not in $P$ with weight $w(e) \ge 0$.

### Step 2: Odd-Degree Vertex Selection
Let $O \subseteq V$ be the set of vertices with odd degrees in $T$:
$$O = \{ v \in V \mid \deg_T(v) \equiv 1 \pmod 2 \}$$

#### Lemma 2 (Handshaking Lemma Corollary)
The cardinality of $O$ is even: $|O| \equiv 0 \pmod 2$.

*Proof:* By the Handshaking Lemma, the sum of degrees of all vertices in any graph is even:
$$\sum_{v \in V} \deg_T(v) = 2|E_T|$$
We partition the sum into vertices of even and odd degrees:
$$\sum_{v \in V} \deg_T(v) = \sum_{v \in O} \deg_T(v) + \sum_{v \notin O} \deg_T(v) \equiv 0 \pmod 2$$
Since $\sum_{v \notin O} \deg_T(v)$ is a sum of even numbers, it is even. Thus, $\sum_{v \in O} \deg_T(v)$ must be even. Because every term in $\sum_{v \in O} \deg_T(v)$ is odd, the number of terms $|O|$ must be even.

### Step 3: Minimum-Weight Perfect Matching (MWPM)
We construct the induced subgraph $G[O]$ and compute a Minimum-Weight Perfect Matching $M$ on $G[O]$.

#### Lemma 3 (Matching Upper Bound)
The weight of the minimum-weight perfect matching $M$ on $G[O]$ is bounded by half the weight of the optimal TSP tour $H^*$:
$$w(M) \le \frac{1}{2} w(H^*)$$

*Proof:* Let $H^*$ be the optimal Hamiltonian cycle on $G$. We construct a cycle $H^*_O$ on the vertex set $O$ by traversing $H^*$ and shortcutting past any vertices not in $O$. By the triangle inequality, shortcutting does not increase the total weight:
$$w(H^*_O) \le w(H^*)$$
Since $|O|$ is even, the cycle $H^*_O$ consists of an even number of edges. We can partition the edges of $H^*_O$ into two disjoint perfect matchings, $M_1$ and $M_2$, such that:
$$E(H^*_O) = M_1 \cup M_2 \quad \text{and} \quad M_1 \cap M_2 = \emptyset$$
Thus, the sum of their weights is:
$$w(M_1) + w(M_2) = w(H^*_O) \le w(H^*)$$
Since $M$ is the *minimum*-weight perfect matching on $G[O]$, its weight must be less than or equal to the weight of both $M_1$ and $M_2$:
$$w(M) \le \min(w(M_1), w(M_2))$$
Therefore:
$$2 w(M) \le w(M_1) + w(M_2) \le w(H^*) \implies w(M) \le \frac{1}{2} w(H^*)$$

### Step 4: Multigraph Union
We define the multigraph $H' = (V, E_{H'})$ where $E_{H'} = E_T \uplus M$.

#### Lemma 4 (Eulerian Property)
Every vertex in $H'$ has an even degree, and $H'$ is connected.

*Proof:* For any vertex $v \in V$, its degree in $H'$ is:
$$\deg_{H'}(v) = \deg_T(v) + \deg_M(v)$$
*   If $v \in O$, then $\deg_T(v)$ is odd, and $\deg_M(v) = 1$. Thus, $\deg_{H'}(v)$ is even.
*   If $v \notin O$, then $\deg_T(v)$ is even, and $\deg_M(v) = 0$. Thus, $\deg_{H'}(v)$ is even.

Since $T$ is a spanning tree, it connects all vertices in $V$. Adding the matching edges $M$ preserves connectivity. Since $H'$ is connected and all its vertices have even degrees, $H'$ contains an Eulerian circuit.

### Step 5: Eulerian Circuit and Shortcutting
Let $C = (u_1, u_2, \dots, u_m, u_1)$ be an Eulerian circuit in $H'$, where $m = |E_T| + |M| = n - 1 + \frac{|O|}{2}$.
We construct a Hamiltonian cycle $H = (v_1, v_2, \dots, v_n, v_1)$ by traversing $C$ from start to finish and skipping any vertex that has already been visited.

Let $\sigma: C \to H$ represent this shortcutting operator. By the triangle inequality, for any sequence of vertices skipped:
$$w(v_i, v_{i+1}) \le \sum_{j=a}^{b} w(u_j, u_{j+1})$$
where $u_a = v_i$ and $u_{b+1} = v_{i+1}$. Summing over the entire cycle yields:
$$w(H) \le w(C)$$

### Step 6: Approximation Ratio Proof
Combining the bounds from the previous steps:
$$w(H) \le w(C) = w(T) + w(M)$$
Applying Lemma 1 ($w(T) < w(H^*)$) and Lemma 3 ($w(M) \le \frac{1}{2} w(H^*)$):
$$w(H) < w(H^*) + \frac{1}{2} w(H^*) = 1.5 \cdot w(H^*)$$
This completes the proof that the algorithm guarantees a $1.5$-approximation.

---

## 3. Complexity Analysis

### Time Complexity

The overall time complexity of the Christofides algorithm is dominated by the Minimum-Weight Perfect Matching step.

#### 1. Minimum Spanning Tree (Prim's Algorithm)
Using an adjacency matrix representation for a complete graph $G$:
*   Finding the minimum weight edge at each step takes $O(V)$ time.
*   Repeating this for $V - 1$ vertices yields:
    $$T_{\text{MST}}(V) = \sum_{i=1}^{V-1} O(V) = O(V^2)$$

#### 2. Odd-Degree Vertex Identification
Scanning the degrees of the vertices in $T$ to construct the set $O$:
$$T_{\text{odd}}(V) = O(V)$$

#### 3. Minimum-Weight Perfect Matching (MWPM)
*   **Exact Formulation (Edmonds' Blossom Algorithm):**
    To guarantee the $1.5$-approximation ratio, we must find the exact minimum-weight perfect matching on the complete graph $G[O]$. Edmonds' Blossom Algorithm adapted for weighted graphs runs in:
    $$T_{\text{MWPM}}(|O|) = O(|O|^3) \le O(V^3)$$
*   **Heuristic Approximation (Greedy Matching):**
    The provided Python implementation uses a greedy matching heuristic (repeatedly picking the cheapest edge between unmatched odd vertices). This heuristic runs in $O(|O|^2 \log |O|)$ or $O(V^2)$ but **does not** guarantee the $1.5$-approximation ratio in all metric spaces. For a mathematically rigorous guarantee, the $O(V^3)$ Blossom algorithm is required.

#### 4. Eulerian Circuit (Hierholzer's Algorithm)
Hierholzer's algorithm finds an Eulerian circuit by traversing each edge in $H'$ exactly once.
*   Number of vertices: $|V| = n$.
*   Number of edges in $H'$: $|E_{H'}| = |E_T| + |M| = (n - 1) + \frac{|O|}{2} < 1.5n$.
*   Using an adjacency list with efficient edge removal, the time complexity is:
    $$T_{\text{Euler}}(V) = O(|V| + |E_{H'}|) = O(V)$$

#### 5. Shortcutting
Traversing the Eulerian circuit of length $O(V)$ and skipping duplicates using a lookup table (hash set or boolean array) of size $V$:
$$T_{\text{shortcut}}(V) = O(V)$$

#### Total Time Complexity
Summing the components:
$$T_{\text{total}}(V) = T_{\text{MST}}(V) + T_{\text{odd}}(V) + T_{\text{MWPM}}(V) + T_{\text{Euler}}(V) + T_{\text{shortcut}}(V)$$
$$T_{\text{total}}(V) = O(V^2) + O(V) + O(V^3) + O(V) + O(V) = O(V^3)$$

---

### Space Complexity

The space complexity is analyzed in terms of auxiliary space and total space.

#### 1. Input Representation
The input cost matrix requires storing $n \times n$ distances:
$$S_{\text{input}}(V) = \Theta(V^2)$$

#### 2. Auxiliary Space
*   **MST Representation:** The parent array and degree tracking array require $O(V)$ space.
*   **Odd-Degree Set $O$:** Storing the indices of odd-degree vertices requires $O(V)$ space.
*   **Multigraph $H'$:** The adjacency list representation of $H'$ contains $V$ vertices and at most $1.5V$ edges, requiring $O(V)$ space.
*   **Eulerian Circuit Stack:** The recursion stack or explicit stack for Hierholzer's algorithm stores at most $|E_{H'}| + 1$ vertices:
    $$S_{\text{stack}}(V) = O(V)$$
*   **Shortcutting State:** A boolean array or hash set of size $V$ to track visited vertices:
    $$S_{\text{visited}}(V) = O(V)$$

#### Total Space Complexity
*   **Auxiliary Space:** $O(V)$
*   **Total Space (including input matrix):** $O(V^2)$