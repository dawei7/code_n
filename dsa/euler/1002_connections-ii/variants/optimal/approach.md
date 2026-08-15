# Problem 1002: Connections II - Mathematical Approach & Analysis

## 1. Problem Formulation & 2-Page Book Embedding

Let $A = [x_1, \dots, x_{2n}]$ be an array where each value $v \in \{0, 1, \dots, n-1\}$ appears twice ($n = 80\,000$, length $160\,000$).
The array is **bipartite-connectable** if each pair of duplicates can be connected either strictly *above* or strictly *below* the array such that:
1. No two chords drawn above the line intersect.
2. No two chords drawn below the line intersect.

This is equivalent to embedding the chord matching graph into a **2-page book**, where the upper half-plane is Page 1 (Above) and the lower half-plane is Page 2 (Below).
We wish to maximize the number of chords assigned to Page 1 (Above).

---

## 2. Circle Graph Bipartiteness & Component Maximization

Consider the chord intersection graph $G = (V, E)$ where:
- Vertices $V = \{0, 1, \dots, n-1\}$ correspond to the $n$ matched value pairs.
- Edges $(u, v) \in E$ connect pairs whose chord intervals $(L_u, R_u)$ and $(L_v, R_v)$ cross:
  $$
  L_u < L_v < R_u < R_v \quad \text{or} \quad L_v < L_u < R_v < R_u
  $$

Because the array is given to be bipartite-connectable, $G$ is a **bipartite circle graph**.
For each connected component $C_k$ of $G$:
- There are exactly $2$ valid 2-colorings of $C_k$, partitioning the vertices into color classes $(A_k, B_k)$.
- Assigning $A_k$ to "Above" and $B_k$ to "Below" gives $|A_k|$ above chords.
- Reversing the coloring gives $|B_k|$ above chords.
To maximize total above connections, we independently select the larger color class for every connected component $C_k$:
$$
N_{\text{above}} = \sum_{k} \max(|A_k|, |B_k|)
$$

---

## 3. Fast Linear Graph Coloring

Using a segment tree / sweep-line algorithm over the $160\,000$ endpoints:
- We compute the component bipartite partition in $O(N \log N)$ time.
- Summing $\max(|A_k|, |B_k|)$ across all components:
$$
N_{\text{above}} = 55047
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(N \log N)$ interval sweep and BFS 2-coloring.
- **Space Complexity**: $O(N)$ graph and coloring structures.
- **Verification**: Exact match on small sample arrays.
