# Triangles Containing the Origin - Optimal Approach

## Algorithm Explanation

Find the total number of triangles with $3$ vertices in $I_{105}$ (non-origin integer points $x^2 + y^2 < 105^2$) that contain the origin $(0, 0)$ strictly in their interior.

### Polar Angle Ray Grouping & Range Sums:
1. **Ray Classification**:
   Group all points $(x, y) \in I_r$ into rays $R_i$ by reduced direction vector $(x/\gcd(|x|,|y|), y/\gcd(|x|,|y|))$.
   Sort rays counter-clockwise by polar angle $\theta_i = \text{atan2}(y, x) \in [0, 2\pi)$. Let $c_i$ be the point count on ray $R_i$.
2. **Origin Enclosure Condition**:
   Three points $P_1, P_2, P_3$ on rays $R_i, R_j, R_k$ (in counter-clockwise order) strictly enclose the origin if and only if:
   - $0 < \theta_j - \theta_i < \pi$
   - $\theta_i + \pi < \theta_k < \theta_j + \pi$
3. **Prefix Sum Acceleration**:
   For each fixed ray $R_i$, $j$ spans over rays in $(\theta_i, \theta_i + \pi)$.
   The valid $k$ range for a pair $(i, j)$ is $(\theta_i + \pi, \theta_j + \pi)$.
   Precomputing prefix sums over $c_j \cdot \text{pref\_counts}[k_{\text{end}}(j)]$ reduces the evaluation to $\mathcal{O}(1)$ per ray $i$, total $\mathcal{O}(m)$ time.
4. **Permutations Division**:
   Dividing the total ordered count by $3$ gives the exact number of unordered triangles.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(r^2 + m)$ where $m$ is the number of distinct rays ($m \approx 10,000$). Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(m)$ - Ray list and prefix sum arrays.
