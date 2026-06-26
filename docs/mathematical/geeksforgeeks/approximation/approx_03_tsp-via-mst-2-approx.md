# Formal Mathematical Specification: TSP via MST (2-Approximation)

## 1. Definitions and Notation

Let $G = (V, E, w)$ be a complete, undirected, weighted graph representing the network of cities and the distances between them, where:
*   $V = \{v_0, v_1, \dots, v_{n-1}\}$ is the set of vertices (cities), with cardinality $|V| = n \ge 2$.
*   $E = \{\{u, v\} \mid u, v \in V, u \neq v\}$ is the set of undirected edges. Since $G$ is complete, the number of edges is $|E| = \frac{n(n-1)}{2}$.
*   $w: E \to \mathbb{R}^+$ is a weight function mapping each edge to a positive real number, representing the distance between vertices.

### Metric Space Assumptions
The weight function $w$ is assumed to define a metric space over $V$. Specifically, it satisfies the following properties for all $u, v, x \in V$:
1.  **Non-negativity**: $w(u, v) \ge 0$, with $w(u, v) = 0 \iff u = v$.
2.  **Symmetry**: $w(u, v) = w(v, u)$.
3.  **Triangle Inequality**: 
    $$w(u, v) \le w(u, x) + w(x, v)$$

### Spanning Trees and Minimum Spanning Trees
*   A **spanning tree** of $G$ is an acyclic subgraph $T = (V, E_T)$ where $E_T \subseteq E$ and $|E_T| = n - 1$.
*   The weight of a spanning tree $T$ is the sum of its edge weights:
    $$w(T) = \sum_{e \in E_T} w(e)$$
*   A **Minimum Spanning Tree (MST)**, denoted by $T^* = (V, E_{T^*})$, is a spanning tree that minimizes this total weight:
    $$T^* = \arg\min_{T \in \mathcal{T}} w(T)$$
    where $\mathcal{T}$ is the set of all spanning trees of $G$.

### Hamiltonian Cycles and the Traveling Salesman Problem
*   A **Hamiltonian cycle** (or TSP tour) in $G$ is a closed walk that visits every vertex in $V$ exactly once and returns to the starting vertex. Formally, it can be represented as a permutation $\pi$ of the vertex indices $\{0, 1, \dots, n-1\}$, defining the cycle:
    $$H = (v_{\pi(0)}, v_{\pi(1)}, \dots, v_{\pi(n-1)}, v_{\pi(0)})$$
*   The weight of a Hamiltonian cycle $H$ is:
    $$w(H) = \sum_{i=0}^{n-2} w(v_{\pi(i)}, v_{\pi(i+1)}) + w(v_{\pi(n-1)}, v_{\pi(0)})$$
*   The **Optimal TSP Tour**, denoted by $H^*$, is a Hamiltonian cycle of minimum weight:
    $$H^* = \arg\min_{H \in \mathcal{H}} w(H)$$
    where $\mathcal{H}$ is the set of all Hamiltonian cycles in $G$.

---

## 2. Algebraic Characterization and Correctness Proof

The 2-approximation algorithm constructs an approximate TSP tour $H_{approx}$ through three sequential algebraic phases: Minimum Spanning Tree construction, Eulerian multigraph generation, and shortcutting via preorder traversal.

### Phase 1: Minimum Spanning Tree Construction (Prim's Formulation)
Let $S_k \subset V$ denote the set of settled vertices at step $k$, and $E_{T, k}$ denote the set of edges selected up to step $k$.
*   **Initialization ($k=0$)**:
    $$S_0 = \{v_0\}, \quad E_{T, 0} = \emptyset$$
*   **Inductive Step ($k \in \{1, \dots, n-1\}$)**:
    Select an edge $e_k = \{u_k, v_k\}$ that minimizes the cut weight between $S_{k-1}$ and $V \setminus S_{k-1}$:
    $$e_k = \arg\min \{ w(u, v) \mid u \in S_{k-1}, v \in V \setminus S_{k-1} \}$$
    Update the state:
    $$S_k = S_{k-1} \cup \{v_k\}, \quad E_{T, k} = E_{T, k-1} \cup \{e_k\}$$
*   **Termination**: The resulting graph $T^* = (V, E_{T, n-1})$ is an MST of $G$.

### Phase 2: Doubling Edges and the Eulerian Circuit
Let $2T^*$ denote the directed multigraph obtained by replacing each undirected edge $\{u, v\} \in E_{T^*}$ with two directed edges $(u, v)$ and $(v, u)$. 
*   For every vertex $v \in V$, its in-degree $\deg^-(v)$ and out-degree $\deg^+(v)$ in $2T^*$ are equal to the degree of $v$ in $T^*$:
    $$\deg^-(v) = \deg^+(v) = \deg_{T^*}(v)$$
*   Since $2T^*$ is connected and every vertex has equal in-degree and out-degree, $2T^*$ is Eulerian. It contains an Eulerian circuit $U = (u_0, u_1, \dots, u_{2n-2}, u_0)$ of total weight:
    $$w(U) = \sum_{i=0}^{2n-2} w(u_i, u_{i+1}) = 2 \cdot w(T^*)$$
    where $u_{2n-1} = u_0$.

### Phase 3: Preorder Traversal and Shortcutting
Let $\text{DFS}(T^*, v_0)$ be the sequence of vertices visited during a depth-first search traversal of $T^*$ starting at root $v_0$. We define the shortcutting operator $\mathcal{S}$ which maps the Eulerian walk $U$ to a Hamiltonian cycle $H_{approx}$ by retaining only the first occurrence of each vertex.

Let $H_{approx} = (v_{\sigma(0)}, v_{\sigma(1)}, \dots, v_{\sigma(n-1)}, v_{\sigma(0)})$ be the sequence of unique vertices in the order of their discovery in $\text{DFS}(T^*, v_0)$, where $\sigma(0) = 0$.

### Mathematical Proof of the Approximation Bound

To prove that the algorithm guarantees a 2-approximation, we establish two fundamental lemmas.

#### Lemma 1: Lower Bound of the MST
The weight of the Minimum Spanning Tree $T^*$ is strictly less than the weight of the optimal TSP tour $H^*$:
$$w(T^*) < w(H^*)$$

*Proof:* Let $H^*$ be the optimal Hamiltonian cycle. Removing any single edge $e \in H^*$ yields a spanning path $P$. Since $w(e) > 0$:
$$w(P) = w(H^*) - w(e) < w(H^*)$$
Because $P$ is a spanning tree of $G$, and $T^*$ is the *minimum* spanning tree of $G$, by definition:
$$w(T^*) \le w(P)$$
Combining these inequalities yields:
$$w(T^*) \le w(H^*) - w(e) < w(H^*)$$
$\blacksquare$

#### Lemma 2: Triangle Inequality and Shortcutting
The weight of the shortcutted tour $H_{approx}$ is at most the weight of the Eulerian circuit $U$:
$$w(H_{approx}) \le w(U)$$

*Proof:* The sequence $H_{approx}$ is constructed by replacing subpaths in $U$ of the form $(x, y_1, y_2, \dots, y_k, z)$—where $y_1, \dots, y_k$ are previously visited vertices—with a direct edge $(x, z)$.
By inductive application of the triangle inequality:
$$w(x, z) \le w(x, y_1) + w(y_1, y_2) + \dots + w(y_k, z)$$
Summing this inequality over all shortcuts made to construct $H_{approx}$ from $U$, we obtain:
$$w(H_{approx}) \le w(U)$$
$\blacksquare$

#### Theorem: 2-Approximation Guarantee
The total cost of the tour generated by the algorithm is at most twice the cost of the optimal tour:
$$w(H_{approx}) \le 2 \cdot w(H^*)$$

*Proof:* By combining the results of Lemma 1 and Lemma 2:
$$w(H_{approx}) \le w(U) = 2 \cdot w(T^*) < 2 \cdot w(H^*)$$
Thus, the approximation ratio $\alpha$ satisfies:
$$\alpha = \frac{w(H_{approx})}{w(H^*)} \le 2$$
$\blacksquare$

---

## 3. Complexity Analysis

### Time Complexity Analysis

The computational complexity of the algorithm is determined by three distinct phases: MST construction, tree representation, and depth-first traversal.

```
  [Input: Cost Matrix]
           │
           ▼
┌──────────────────────┐
│ Phase 1: Prim's MST  │  ◄─── O(V^2) using array-based min-set
└───────┬──────────────┘       or O(E log V) = O(V^2 log V) with Heap
        │
        ▼
┌──────────────────────┐
│ Phase 2: Tree Rep.   │  ◄─── O(V) to construct adjacency list
└───────┬──────────────┘
        │
        ▼
┌──────────────────────┐
│ Phase 3: DFS Walk    │  ◄─── O(V) to generate preorder tour
└──────────────────────┘
```

#### 1. MST Construction (Prim's Algorithm)
Let $V$ be the set of vertices and $E$ be the set of edges. In a complete graph, $|E| = \Theta(V^2)$.
*   **Naive Implementation (as shown in the Python code)**:
    The outer loop runs $V-1$ times. Inside, it performs a nested search over all pairs $(u, v) \in V \times V$ to find the minimum weight edge crossing the cut. The work done is:
    $$T_{\text{naive}}(V) = \sum_{k=1}^{V-1} \sum_{u=1}^{V} \sum_{v=1}^{V} \mathcal{O}(1) = \sum_{k=1}^{V-1} \mathcal{O}(V^2) = \Theta(V^3)$$
*   **Standard Array-Based Prim's**:
    By maintaining a $key$ array storing the minimum weight from any vertex in the MST to a vertex outside the MST, we can find the minimum vertex in $O(V)$ and update keys in $O(V)$.
    $$T_{\text{array}}(V) = \sum_{k=1}^{V} \left( \mathcal{O}(V) + \mathcal{O}(V) \right) = \Theta(V^2)$$
*   **Binary Heap-Based Prim's**:
    Using a binary heap to extract the minimum weight edge, extracting the minimum takes $O(\log V)$ and updating the keys takes $O(\log V)$ per edge.
    $$T_{\text{heap}}(V) = \mathcal{O}(V \log V + E \log V)$$
    Since the graph is complete ($E = \Theta(V^2)$):
    $$T_{\text{heap}}(V) = \mathcal{O}(V^2 \log V)$$

#### 2. Tree Representation
Converting the parent array representation of the MST into an adjacency list of children requires iterating over the parent array of size $V$:
$$T_{\text{tree}}(V) = \Theta(V)$$

#### 3. Depth-First Search (DFS) Traversal
The DFS visits each vertex exactly once and traverses each edge of the tree $T^*$ exactly twice (once down, once up). Since $T^*$ has $V-1$ edges:
$$T_{\text{dfs}}(V) = \Theta(V + (V-1)) = \Theta(V)$$

#### 4. Tour Cost Accumulation
Summing the weights of the edges in the final Hamiltonian cycle of length $V$ takes:
$$T_{\text{cost}}(V) = \Theta(V)$$

#### Total Time Complexity
The total time complexity is dominated by the MST construction phase. Depending on the implementation of Prim's algorithm:
*   **Naive Implementation**: $\Theta(V^3)$
*   **Binary Heap Implementation**: $\Theta(V^2 \log V)$
*   **Array-Based Implementation (Optimal for dense graphs)**: $\Theta(V^2)$

---

### Space Complexity Analysis

The space complexity is analyzed in terms of auxiliary space (memory allocated by the algorithm excluding the input) and total space.

#### 1. Auxiliary Space
The auxiliary memory is consumed by the following data structures:
*   `in_mst`: A boolean tracking array of size $V \implies \Theta(V)$ bits.
*   `parent`: An integer array of size $V$ storing the MST structure $\implies \Theta(V)$ words.
*   `children`: An adjacency list representing the directed tree, containing $V$ list heads and $V-1$ total nodes $\implies \Theta(V)$ words.
*   `tour`: An array storing the preorder traversal sequence of size $V \implies \Theta(V)$ words.
*   **Recursion Stack**: The execution stack during the DFS traversal has a maximum depth equal to the height of the tree $T^*$. In the worst-case (a degenerate line graph), the depth is $V$, requiring $\Theta(V)$ stack frames.

Summing these components:
$$\text{Space}_{\text{auxiliary}}(V) = \Theta(V) + \Theta(V) + \Theta(V) + \Theta(V) + \mathcal{O}(V) = \Theta(V)$$

#### 2. Total Space
The total space complexity includes the input representation. The input is an adjacency matrix of size $V \times V$ representing the complete graph:
$$\text{Space}_{\text{input}}(V) = \Theta(V^2)$$
Thus, the total space complexity is:
$$\text{Space}_{\text{total}}(V) = \text{Space}_{\text{input}}(V) + \text{Space}_{\text{auxiliary}}(V) = \Theta(V^2)$$