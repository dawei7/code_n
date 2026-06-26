# Formal Mathematical Specification: Convex Hull (Graham Scan)

## 1. Definitions and Notation

Let $P = \{p_1, p_2, \dots, p_N\}$ be a set of $N$ points in the Euclidean plane $\mathbb{R}^2$, where each point $p_i = (x_i, y_i)$. 

*   **Convex Hull:** The convex hull of $P$, denoted $\text{CH}(P)$, is the unique minimal convex set $C \subseteq \mathbb{R}^2$ such that $P \subseteq C$. The vertices of $\text{CH}(P)$ are a subset of $P$.
*   **Anchor Point:** Let $p_0 \in P$ be the point such that $y_0 = \min_{i} \{y_i\}$, with ties broken by $x_0 = \min \{x_i\}$.
*   **Polar Angle:** For any $p_i \in P \setminus \{p_0\}$, let $\theta_i = \operatorname{atan2}(y_i - y_0, x_i - x_0)$ be the polar angle relative to $p_0$.
*   **Cross Product:** For an ordered triplet of points $(A, B, C)$, the orientation is determined by the sign of the cross product of vectors $\vec{AB}$ and $\vec{BC}$:
    $$\text{CCW}(A, B, C) = (x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A)$$
    *   $\text{CCW} > 0$: Left turn (Counter-clockwise).
    *   $\text{CCW} < 0$: Right turn (Clockwise).
    *   $\text{CCW} = 0$: Collinear.
*   **State Space:** The algorithm maintains a stack $S = (s_0, s_1, \dots, s_k)$, where $s_i \in P$ and $k$ is the current index of the stack top.

## 2. Algebraic Characterization

The Graham Scan constructs the boundary of $\text{CH}(P)$ by maintaining a sequence of points that satisfy the convexity constraint.

**Ordering:**
The set $P \setminus \{p_0\}$ is sorted into a sequence $Q = (q_1, q_2, \dots, q_{N-1})$ such that for any $i < j$, $\theta_i < \theta_j$, or if $\theta_i = \theta_j$, then $\|\vec{p_0 q_i}\| < \|\vec{p_0 q_j}\|$.

**Loop Invariant:**
At each iteration $m \in \{1, \dots, N-1\}$, the stack $S$ contains the vertices of the convex hull of the set $\{p_0, q_1, \dots, q_m\}$ in counter-clockwise order. 

**Transition Rule:**
For a new point $q_m$, the algorithm maintains the invariant by ensuring that for the top two elements of the stack $s_{k-1}, s_k$ and the new point $q_m$:
$$\text{CCW}(s_{k-1}, s_k, q_m) > 0$$
If $\text{CCW}(s_{k-1}, s_k, q_m) \leq 0$, the point $s_k$ is removed (popped) from $S$. This operation is repeated until the condition holds or $|S| < 2$. The point $q_m$ is then pushed onto $S$.

**Correctness:**
The algorithm terminates when $m = N-1$. Since $p_0$ is the bottom-most point, it is guaranteed to be a vertex of $\text{CH}(P)$. The sorting by polar angle ensures that the points are visited in a monotonic angular sweep, and the CCW condition ensures that the boundary remains strictly convex.

## 3. Complexity Analysis

### Time Complexity
The total time complexity $T(N)$ is the sum of the preprocessing phase and the scanning phase:

1.  **Finding the Anchor:** $T_{anchor} = O(N)$ to perform a linear scan for the minimum coordinate.
2.  **Sorting:** $T_{sort} = O(N \log N)$ to sort the remaining $N-1$ points based on the polar angle $\theta$.
3.  **Scanning:** The scanning phase involves a single loop over $N-1$ points. Each point $q_i$ is pushed onto the stack exactly once. A point is popped from the stack at most once. Thus, the total number of stack operations is $O(N)$.

$$T(N) = O(N) + O(N \log N) + O(N) = O(N \log N)$$

### Space Complexity
1.  **Auxiliary Space:** The algorithm requires $O(N)$ space to store the sorted list of points $Q$.
2.  **Stack Space:** The stack $S$ stores at most $N$ vertices in the worst case (e.g., all points lie on the convex hull).

$$S(N) = O(N) + O(N) = O(N)$$

The algorithm is optimal in the algebraic decision tree model, as the problem of finding the convex hull has a lower bound of $\Omega(N \log N)$ due to its reduction from the sorting problem.