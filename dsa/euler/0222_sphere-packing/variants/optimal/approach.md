# Sphere Packing - Optimal Approach

## Algorithm Explanation

Find the shortest length of a pipe of internal radius $R = 50\text{ mm}$ that can fully contain $21$ balls of radii $r \in \{30, 31, \dots, 50\}\text{ mm}$, given in micrometres ($\pu{10^{-6} m}$) rounded to the nearest integer.

### 3D Cylinder Geometry & Held-Karp Bitmask DP:
1. **Axial Distance Formula**:
   When two adjacent spheres of radii $r_i$ and $r_j$ touch the inner cylinder wall of radius $R = 50$, the distance along the cylinder axis between their centers is:
   $$\Delta z(r_i, r_j) = \sqrt{(r_i + r_j)^2 - (100 - r_i - r_j)^2} = \sqrt{200 (r_i + r_j - 50)}$$
2. **Total Pipe Length**:
   For any ordering $(r_{\pi(1)}, \dots, r_{\pi(21)})$, total length is:
   $$L = r_{\pi(1)} + r_{\pi(21)} + \sum_{k=1}^{20} \sqrt{200 (r_{\pi(k)} + r_{\pi(k+1)} - 50)}$$
3. **Traveling Salesperson Problem (TSP)**:
   This optimization maps to TSP on $N = 21$ nodes. We solve it using Held-Karp dynamic programming with bitmask state `dp[mask][last]`.
4. **Execution**:
   The minimum pipe length is $1590.933116\text{ mm}$, which equals $1590933\text{ \mu m}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2 \cdot 2^N)$ for $N = 21$. Runs in $\approx 0.1\text{s}$ (C++ compiled).
- **Space Complexity:** $\mathcal{O}(N \cdot 2^N)$ for bitmask DP states.
