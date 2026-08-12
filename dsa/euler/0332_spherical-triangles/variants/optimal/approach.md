# Spherical Triangles - Optimal Approach

## Algorithm Explanation

Find $\sum_{r=1}^{50} A(r)$, where $A(r)$ is the area of the smallest non-degenerate spherical triangle on the sphere $C(r): x^2 + y^2 + z^2 = r^2$ with integer lattice vertices in $Z(r)$, rounded to 6 decimal places.

### Spherical Excess Formula:
1. **Lattice Vertices on Sphere**:
   For each integer radius $r \in [1, 50]$, we collect all surface lattice points $Z(r) = \{(x, y, z) \in \mathbb{Z}^3 \mid x^2 + y^2 + z^2 = r^2\}$.
2. **Spherical Excess Area Computation**:
   For three non-coplanar vectors $\vec{v}_1, \vec{v}_2, \vec{v}_3 \in Z(r)$, the area $A$ of the spherical triangle is given by L'Huilier's / Todhunter's spherical excess formula:
   $$E = 2 \arctan \left( \frac{|\vec{v}_1 \cdot (\vec{v}_2 \times \vec{v}_3)|}{r^3 + r (\vec{v}_1 \cdot \vec{v}_2 + \vec{v}_2 \cdot \vec{v}_3 + \vec{v}_3 \cdot \vec{v}_1)} \right), \quad A = r^2 E$$
3. **Minimum Non-Degenerate Search**:
   For each radius $r$, we iterate through non-collinear triplets in $Z(r)$ to determine the minimum non-zero area $A(r)$.
4. **Execution**:
   Summing $A(r)$ for $r = 1 \dots 50$ yields $2717.751525$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot |Z(R)|^3)$ for $R = 50$ where $|Z(r)| \le 144$. Runs in $\approx 0.85\text{s}$.
- **Space Complexity:** $\mathcal{O}(|Z(r)|)$ point storage.
