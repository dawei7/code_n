# Path Sum: Four Ways - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In the $5 \times 5$ matrix below, the minimal path sum from the top left to the bottom right by moving in all four directions (**up**, **down**, **left**, **right**) has a sum of $2297$:

$$
\begin{pmatrix}
\mathbf{131} & 673 & \mathbf{234} & \mathbf{103} & \mathbf{18} \\
\mathbf{201} & \mathbf{96} & \mathbf{342} & 965 & \mathbf{150} \\
630 & 803 & 746 & \mathbf{422} & \mathbf{111} \\
537 & 699 & 497 & \mathbf{121} & 956 \\
805 & 732 & 524 & \mathbf{37} & \mathbf{331}
\end{pmatrix}
$$

Let $\mathbf{T}$ denote the $80 \times 80$ integer matrix given in `matrix.txt`.
A valid 4-way path starts at top-left $(0, 0)$ and reaches bottom-right $(R-1, C-1)$ using orthogonal steps $(\Delta r, \Delta c) \in \{(-1, 0), (1, 0), (0, -1), (0, 1)\}$.

The objective is to find the **minimal path sum**:

$$
S_{\text{min}} = \min_{\mathbf{P}: (0,0) \rightsquigarrow (R-1, C-1)} \left( T_{0, 0} + \sum_{(u, v) \in \mathbf{P}} T_{v_r, v_c} \right)
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Standard Dynamic Programming Failure
Standard topological dynamic programming fails because bidirectional transitions (cycles) exist between adjacent cells when moving in 4 directions.

### Dijkstra's Shortest Path on a Grid Graph
1. We construct a directed grid graph $G = (V, E)$ with $|V| = 80 \times 80 = 6400$ nodes, where each directed edge $(u, v)$ has non-negative weight $w(u, v) = T_{v_r, v_c}$.
2. Using **Dijkstra's Algorithm with a Binary Min-Heap (`heapq`)**, the optimal shortest path is discovered in $\mathcal{O}(|V| \log |V|)$ time in $\approx 0.02$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Grid Graph Orthogonal Adjacency

| Current Cell $(r, c)$ | Neighbor $(nr, nc)$ | Direction | Edge Cost $w(u, v)$ | In-Bounds Condition |
| :---: | :---: | :---: | :---: | :---: |
| $(r, c)$ | $(r - 1, c)$ | **Up** | $T_{r-1, c}$ | $r > 0$ |
| $(r, c)$ | $(r + 1, c)$ | **Down** | $T_{r+1, c}$ | $r < R - 1$ |
| $(r, c)$ | $(r, c - 1)$ | **Left** | $T_{r, c-1}$ | $c > 0$ |
| $(r, c)$ | $(r, c + 1)$ | **Right** | $T_{r, c+1}$ | $c < C - 1$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Dijkstra Min-Heap Pipeline
1. Initialize distance dictionary $\text{dist} = \{(0, 0): T[0][0]\}$.
2. Min-heap priority queue $\text{pq} = [(T[0][0], 0, 0)]$.
3. While $\text{pq}$ is not empty:
   - Pop $(d, r, c)$ with smallest tentative distance.
   - If $(r, c) == (R-1, C-1)$, return $d$.
   - If $d > \text{dist}[(r, c)]$, continue (stale entry).
   - For $(\Delta r, \Delta c) \in \{(-1, 0), (1, 0), (0, -1), (0, 1)\}$:
     - Let $nr = r + \Delta r, nc = c + \Delta c$.
     - If $0 \le nr < R$ and $0 \le nc < C$:
       - $\text{new\_d} = d + T[nr][nc]$.
       - If $\text{new\_d} < \text{dist}[(nr, nc)]$:
         - $\text{dist}[(nr, nc)] = \text{new\_d}$.
         - Push $(\text{new\_d}, nr, nc)$ onto $\text{pq}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $5 \times 5$ Sample Matrix
- Path: $(0,0) \to (1,0) \to (1,1) \to (0,1) \dots \to (4,4)$.
- Cell sequence: $131 \to 201 \to 96 \to 342 \to 234 \to 103 \to 18 \to 150 \to 111 \to 422 \to 121 \to 37 \to 331$.
- Path sum:

$$
S = 131 + 201 + 96 + 342 + 234 + 103 + 18 + 150 + 111 + 422 + 121 + 37 + 331 = \mathbf{2297}
$$

- Matches problem statement sample! $\checkmark$

### Example 2: Target $80 \times 80$ Matrix
- Running Dijkstra's algorithm on `matrix.txt`:

$$
S_{\text{min}} = \mathbf{425\,185}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read `matrix.txt` into 2D integer array | $\mathcal{O}(R \cdot C)$ |
| **Stage 2** | **Heap Init** | `pq = [(grid[0][0], 0, 0)]` | $\mathcal{O}(1)$ |
| **Stage 3** | **Pop Min Node** | `d, r, c = heapq.heappop(pq)` | $\mathcal{O}(\log |V|)$ |
| **Stage 4** | **4-Way Relaxation** | Explore $\{(-1,0), (1,0), (0,-1), (0,1)\}$ | $4$ edges/node |
| **Stage 5** | **Target Return** | If `(r, c) == (R-1, C-1): return d` $\implies 425185$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(|V| \log |V|)$ where $|V| = 6400$ | $\approx 0.02$ seconds |
| **Space Complexity** | $\mathcal{O}(|V|)$ | Distance map and min-heap $\approx 500$ KB |
| **Dynamic Execution** | $100\%$ Inline | 4-way Dijkstra priority queue expansion |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `matrix.txt` relative to package location without relying on external working directories.
2. **Non-Negative Edge Weights**: Every cell value $T_{r, c} \ge 0$, guaranteeing the correctness of greedy Dijkstra selection without negative weight cycles.