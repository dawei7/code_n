# Formal Mathematical Specification: Convex Hull (Divide and Conquer)

## 1. Definitions and Notation

Let $P = \{p_1, p_2, \dots, p_n\}$ be a set of $n$ points in the Euclidean plane $\mathbb{R}^2$, where each point $p_i = (x_i, y_i)$. 

*   **Convex Hull:** The convex hull of $P$, denoted $\text{CH}(P)$, is the unique minimal convex polygon such that $P \subseteq \text{CH}(P)$. Formally, $\text{CH}(P) = \{ \sum_{i=1}^n \alpha_i p_i \mid \sum \alpha_i = 1, \alpha_i \ge 0 \}$, the convex combination of all points in $P$.
*   **Orientation Function:** For an ordered triplet of points $(a, b, c)$, we define the orientation function $\Omega: (\mathbb{R}^2)^3 \to \{-1, 0, 1\}$ as:
    $$\Omega(a, b, c) = \text{sgn}((b_x - a_x)(c_y - a_y) - (b_y - a_y)(c_x - a_x))$$
    where $\Omega > 0$ denotes a counter-clockwise turn, $\Omega < 0$ a clockwise turn, and $\Omega = 0$ collinearity.
*   **Tangents:** Given two disjoint convex polygons $L$ and $R$ separated by a vertical line, the **upper tangent** is a line segment $\overline{u_L u_R}$ (where $u_L \in L, u_R \in R$) such that all points in $L \cup R$ lie below or on the line containing $\overline{u_L u_R}$. The **lower tangent** is defined analogously such that all points lie above or on the line.

## 2. Algebraic Characterization

The algorithm relies on the recursive decomposition of the set $P$. Let $P_L$ and $P_R$ be the subsets of $P$ partitioned by the median $x$-coordinate.

### Recurrence Relation
The time complexity $T(n)$ is governed by the Master Theorem. The merge step requires finding the upper and lower tangents. Since the vertices of the convex hulls are stored in cyclic order, finding the tangents via a "walking" procedure (bouncing between $L$ and $R$) takes time proportional to the number of vertices $k$ in the hulls, where $k \le n$. Thus, the merge step is $O(n)$.
$$T(n) = 2T\left(\frac{n}{2}\right) + O(n)$$
By the Master Theorem (Case 2), where $a=2, b=2, f(n)=O(n^1)$, we have:
$$T(n) = \Theta(n \log n)$$

### Merge Invariant
Let $L$ and $R$ be the convex hulls of $P_L$ and $P_R$. The merge step maintains the invariant that the resulting set of vertices $V_{merged}$ satisfies:
$$V_{merged} = (L \setminus \text{interior\_arc}_L) \cup (R \setminus \text{interior\_arc}_R) \cup \{\overline{u_L u_R}, \overline{l_L l_R}\}$$
where $\text{interior\_arc}$ represents the chain of vertices rendered concave or internal by the addition of the new tangent bridges $\overline{u_L u_R}$ (upper) and $\overline{l_L l_R}$ (lower).

## 3. Complexity Analysis

### Time Complexity
The algorithm proceeds in three phases:
1.  **Preprocessing:** Sorting $P$ by $x$-coordinate takes $O(n \log n)$.
2.  **Divide:** The set is partitioned into two subsets of size $n/2$ in $O(1)$ time (given sorted input).
3.  **Conquer:** The merge step involves finding the upper and lower tangents. Because the hulls are convex, the "walking" pointers only move monotonically around the vertices. In the worst case, the pointers traverse the entire perimeter of the hulls, which is $O(n)$.
    Summing the work across the recursion tree:
    $$\sum_{i=0}^{\log n} 2^i \cdot O\left(\frac{n}{2^i}\right) = \sum_{i=0}^{\log n} O(n) = O(n \log n)$$

### Space Complexity
*   **Auxiliary Space:** The recursion stack depth is $\log n$. At each level of the recursion, we store the pointers to the current hulls.
*   **Total Space:** If the algorithm is implemented to return new arrays for each hull, the space complexity is $O(n)$ due to the storage of vertices at each level. However, if the algorithm operates on indices or pointers to the original sorted array, the auxiliary space complexity is $O(\log n)$ to maintain the recursion stack. Thus, the algorithm is $O(n)$ in standard implementations, but $O(\log n)$ is achievable with careful pointer management.