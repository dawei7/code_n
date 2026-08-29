# Irregular Star Polygons - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Given $n$ equally spaced vertices on a circle, an $n$-star polygon is an undirected Hamiltonian cycle in the complete graph $K_n$.
There are $\frac{(n-1)!}{2}$ such distinct star polygons.
For each star polygon $S$, let $I(S)$ be the number of distinct self-intersection points of its edges inside the open disk (points with multiple concurrent edges counted once).
Let $T(n) = \sum_S I(S)$.
Given:
- $T(5) = 20$
- $T(8) = 14640$

Find $\sum_{n=3}^{60} T(n) \bmod (10^9 + 7)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Explicit Hamiltonian Cycle Enumeration
- For $n = 60$, the number of Hamiltonian cycles is $\frac{59!}{2} \approx 6.9 \times 10^{79}$.
- Enumerating individual polygons is completely intractable.

---

## 3. Core Intuition & Mathematical Structure

### Linearity of Expectation & Concurrency Multiplicities
By linearity of expectation, the sum $T(n) = \sum_S I(S)$ is rewritten over all potential interior intersection points $P$:

$$
T(n) = \sum_{P \in \mathcal{P}_n} \mathbb{P}(P \in S)
$$

where $\mathbb{P}(P \in S)$ is the number of star polygons containing at least 2 of the $k(P)$ chords passing through $P$.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Hamiltonian Cycles Containing Disjoint Edges
Any set of $j$ concurrent chords meeting at an interior point $P$ consists of $j$ pairwise vertex-disjoint edges (a matching of size $j$).
Contracting the $j$ edges in $K_n$ results in $n - j$ vertices.
The number of undirected Hamiltonian cycles containing all $j$ fixed edges is:

$$
H(n, j) = (n - j - 1)! \cdot 2^{j - 1}
$$

### Inclusion-Exclusion for "At Least Two" Chords
The indicator polynomial for $\ge 2$ events under elementary symmetric sums is:

$$
\mathbb{I}(m \ge 2) = \sum_{j=2}^k (-1)^{j - 2} (j - 1) \binom{k}{j}
$$

Thus, the number of star polygons containing at least 2 of the $k$ chords is:

$$
N(n, k) = \sum_{j=2}^k (-1)^{j - 2} (j - 1) \binom{k}{j} H(n, j) \pmod{10^9 + 7}
$$

### Geometry & DSU Point Clustering
All $\binom{n}{2}$ chords are generated with exact complex endpoints $\omega_k = e^{2\pi i k / n}$.
Intersecting chord pairs $(C_1, C_2)$ are evaluated at:

$$
z = \frac{\omega_a \omega_b (\omega_c + \omega_d) - \omega_c \omega_d (\omega_a + \omega_b)}{\omega_a \omega_b - \omega_c \omega_d}
$$

A 1D sorted scan with Disjoint Set Union (DSU) clusters identical intersection points with tolerance $\epsilon = 10^{-7}$.
For a cluster containing $C$ intersecting chord pairs, its concurrency is:

$$
k = \frac{1 + \sqrt{1 + 8C}}{2}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $n = 5$:
1. $n = 5$ has $\binom{5}{4} = 5$ intersection points, each having $k = 2$ chords.
2. For $k = 2$:

$$
N(5, 2) = (-1)^0 (1) \binom{2}{2} H(5, 2) = 1 \cdot 1 \cdot (5 - 2 - 1)! 2^1 = 2! \cdot 2 = 4
$$

3. Total $T(5) = 5 \times 4 = \mathbf{20}$. (Matches problem statement! $\checkmark$)

### Walkthrough for $n = 8$:
- Concurrency distribution: $40$ points with $k=2$, $8$ points with $k=3$, $1$ point (center) with $k=4$.
- Evaluating $\sum \text{count} \times N(8, k)$ gives $T(8) = \mathbf{14640}$. (Matches problem statement! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Chord Generation** | Generate all chords $(u, v)$ for regular $n$-gon | $\mathcal{O}(n^2)$ |
| **Stage 2** | **Complex Intersections** | Calculate all interior intersection coordinates $z$ | $\mathcal{O}(n^4)$ |
| **Stage 3** | **DSU Clustering** | Group identical intersection points into connected components | $\mathcal{O}(M \log M)$ |
| **Stage 4** | **Inclusion-Exclusion Sum** | Evaluate $N(n, k)$ for each cluster and accumulate modulo $10^9 + 7$ | $\mathcal{O}(k)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\sum_{n=3}^{60} n^4) \approx 2.0\text{ s}$ | Real-time computation |
| **Space Complexity** | $\mathcal{O}(M) \le 5\text{ MB}$ | Minimal memory footprint |
| **Implementation Standard** | C DLL + Pure Python Fallback | Zero external dependencies |

### Critical Invariants Handled:
1. **Pascal Triangle Precomputation**: Precomputing $\binom{k}{j} \pmod M$ prevents 64-bit integer overflow when $k = 30$.
2. **Distinct Endpoints Check**: Restricts intersections strictly to chord pairs sharing no boundary vertices ($|z| < 1$).
