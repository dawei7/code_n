# Formal Mathematical Specification: Quickhull (Convex Hull)

## 1. Definitions and Notation

Let $S = \{p_1, p_2, \dots, p_n\}$ be a set of $n$ points in the Euclidean plane $\mathbb{R}^2$, where each point $p_i = (x_i, y_i)$. 

*   **Convex Hull:** The convex hull of $S$, denoted $\text{CH}(S)$, is the unique minimal convex set $K \subseteq \mathbb{R}^2$ such that $S \subseteq K$. Equivalently, $\text{CH}(S)$ is the intersection of all convex sets containing $S$.
*   **Orientation Function:** For an ordered triplet of points $(A, B, P)$, we define the orientation function $\Omega: (\mathbb{R}^2)^3 \to \mathbb{R}$ as the determinant:
    $$\Omega(A, B, P) = \det \begin{pmatrix} x_A & y_A & 1 \\ x_B & y_B & 1 \\ x_P & y_P & 1 \end{pmatrix} = (x_B - x_A)(y_P - y_A) - (y_B - y_A)(x_P - x_A)$$
    The sign of $\Omega$ determines the side of the directed line $\vec{AB}$ on which $P$ lies:
    *   $\Omega > 0$: $P$ is to the left of $\vec{AB}$.
    *   $\Omega < 0$: $P$ is to the right of $\vec{AB}$.
    *   $\Omega = 0$: $P$ is collinear with $AB$.
*   **Distance Function:** The perpendicular distance $d(P, \vec{AB})$ from point $P$ to the line passing through $A$ and $B$ is proportional to $|\Omega(A, B, P)|$:
    $$d(P, \vec{AB}) = \frac{|\Omega(A, B, P)|}{\|B - A\|_2}$$

## 2. Algebraic Characterization

The Quickhull algorithm relies on the property that extreme points in a given direction must belong to the convex hull.

**Initial Partition:**
Let $p_{min} = \arg \min_{p \in S} x_p$ and $p_{max} = \arg \max_{p \in S} x_p$. The set $S$ is partitioned into two subsets based on the orientation relative to the directed line $\vec{p_{min}p_{max}}$:
$$S_1 = \{p \in S \mid \Omega(p_{min}, p_{max}, p) > 0\}, \quad S_2 = \{p \in S \mid \Omega(p_{min}, p_{max}, p) < 0\}$$

**Recursive Step:**
For a directed line segment $\vec{AB}$ and a set of points $S_{sub}$ lying to one side, we define the furthest point $P_{far}$ as:
$$P_{far} = \arg \max_{p \in S_{sub}} \Omega(A, B, p)$$
The algorithm then recursively processes the two new sets defined by the triangle $\triangle ABP_{far}$:
1. $S_{left} = \{p \in S_{sub} \mid \Omega(A, P_{far}, p) > 0\}$
2. $S_{right} = \{p \in S_{sub} \mid \Omega(P_{far}, B, p) > 0\}$

**Invariant:**
At each recursive step, the points $A$ and $B$ are vertices of $\text{CH}(S)$. Any point $P$ such that $\Omega(A, B, P) \leq 0$ (relative to the outward-facing normal of the current hull edge) is strictly contained within the convex polygon formed by the current hull and is thus excluded from further consideration.

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the recurrence relation:
$$T(n) = T(k) + T(n - k - 2) + O(n)$$
where $n$ is the number of points and $k$ is the number of points remaining in the recursive sub-problems.

*   **Average Case:** If the point $P_{far}$ is chosen such that the points are partitioned into roughly equal subsets ($k \approx n/2$), the recurrence becomes $T(n) = 2T(n/2) + O(n)$. By the Master Theorem, $T(n) = O(n \log n)$.
*   **Worst Case:** If the points are distributed such that the partition is highly unbalanced (e.g., $k=0$ or $k=n-1$ at each step), the recurrence becomes $T(n) = T(n-1) + O(n)$, which yields $T(n) = O(n^2)$. This occurs when points are distributed on a circle or a convex curve.

### Space Complexity
*   **Auxiliary Space:** The algorithm requires $O(n)$ space to store the input points. The recursion stack depth $D$ depends on the partitioning. In the average case, $D = O(\log n)$. In the worst case, $D = O(n)$.
*   **Total Space:** The algorithm operates in $O(n)$ total space, as the points are passed by reference and the hull is constructed incrementally. The auxiliary stack space is $O(\log n)$ on average and $O(n)$ in the worst case.