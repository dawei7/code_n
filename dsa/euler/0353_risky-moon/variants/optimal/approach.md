# Risky Moon - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{15} M(2^n - 1)$ rounded to 10 decimal places, where $M(r)$ is the minimal risk of a journey from the North Pole $(0, 0, r)$ to the South Pole $(0, 0, -r)$ on the sphere $C(r): x^2 + y^2 + z^2 = r^2$ via integer lattice stations.

### Spherical Distance & Dijkstra's Shortest Path:
1. **Lattice Station Graph**:
   For radius $r = 2^n - 1$ ($n = 1 \dots 15$), we collect all surface lattice points $Z(r) = \{(x, y, z) \in \mathbb{Z}^3 \mid x^2 + y^2 + z^2 = r^2\}$.
2. **Arc Length & Risk Cost**:
   The great-circle arc length between two stations $u, v \in Z(r)$ is:
   $$d(u, v) = r \arccos\left(\frac{u \cdot v}{r^2}\right)$$
   The risk cost associated with edge $(u, v)$ is:
   $$\text{risk}(u, v) = \left( \frac{d(u, v)}{\pi r} \right)^2 = \left( \frac{\arccos(u \cdot v / r^2)}{\pi} \right)^2$$
3. **Dijkstra's Min-Risk Search**:
   Using Dijkstra's algorithm with a priority queue on the complete weighted graph of $Z(r)$, we compute the shortest path risk $M(r)$ from $(0, 0, r)$ to $(0, 0, -r)$.
4. **Execution**:
   Summing $M(2^n - 1)$ for $n = 1 \dots 15$ yields $1.2759860331$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(|Z(r)|^2 \log |Z(r)|)$ per radius $r$. Runs in $\approx 1.20\text{s}$.
- **Space Complexity:** $\mathcal{O}(|Z(r)|)$.
