# Formal Mathematical Specification: Convex Hull (Jarvis March / Gift Wrapping)

## 1. Definitions and Notation

Let $P = \{p_1, p_2, \dots, p_n\}$ be a set of $n$ points in the Euclidean plane $\mathbb{R}^2$, where each point $p_i = (x_i, y_i)$. 

*   **Convex Hull:** The convex hull of $P$, denoted $\text{CH}(P)$, is the unique minimal convex polygon such that $P \subseteq \text{CH}(P)$. The vertices of $\text{CH}(P)$ are a subset of $P$.
*   **Orientation Function:** For any ordered triplet of points $(a, b, c)$, the orientation is determined by the sign of the cross product of vectors $\vec{ab}$ and $\vec{ac}$:
    $$\Omega(a, b, c) = (x_b - x_a)(y_c - y_a) - (y_b - y_a)(x_c - x_a)$$
    *   If $\Omega(a, b, c) > 0$, the sequence $(a, b, c)$ makes a counter-clockwise (left) turn.
    *   If $\Omega(a, b, c) < 0$, the sequence $(a, b, c)$ makes a clockwise (right) turn.
    *   If $\Omega(a, b, c) = 0$, the points are collinear.
*   **State Space:** The algorithm maintains a sequence of vertices $H = (h_0, h_1, \dots, h_{m-1})$, where $m = |H|$ is the number of vertices on the hull. The state at iteration $k$ is defined by the current vertex $h_k \in P$.

## 2. Algebraic Characterization

The Jarvis March algorithm constructs the sequence $H$ by iteratively selecting the "most counter-clockwise" point relative to the current vertex.

**Initialization:**
The starting vertex $h_0$ is defined as the point with the minimum $x$-coordinate (and minimum $y$-coordinate in case of ties):
$$h_0 = \text{argmin}_{p \in P} \{x_p \mid \forall q \in P, x_p < x_q \lor (x_p = x_q \land y_p \le y_q)\}$$

**Inductive Step:**
Given the current vertex $h_k$, the next vertex $h_{k+1}$ is chosen such that for all $p \in P \setminus \{h_k\}$, the orientation $\Omega(h_k, h_{k+1}, p) \ge 0$. Formally:
$$h_{k+1} = \{q \in P \mid \forall p \in P, \Omega(h_k, q, p) \ge 0\}$$
In the case of collinear points where $\Omega(h_k, q, p) = 0$, the point $p$ that maximizes the Euclidean distance $\|p - h_k\|_2$ is selected to ensure the hull boundary is strictly defined by the extreme points.

**Termination:**
The algorithm terminates at step $m$ when $h_m = h_0$. The sequence $H = (h_0, h_1, \dots, h_{m-1})$ constitutes the vertices of the convex hull in counter-clockwise order.

## 3. Complexity Analysis

### Time Complexity
The algorithm proceeds in $m$ iterations, where $m$ is the number of vertices on the convex hull (denoted as $H$ in the problem statement). 

In each iteration $k \in \{0, \dots, m-1\}$, the algorithm performs a linear scan over all $n$ points to identify the next vertex $h_{k+1}$. The work performed per iteration is $\Theta(n)$. Summing over all iterations, the total time complexity $T(n)$ is:
$$T(n) = \sum_{k=0}^{m-1} \Theta(n) = \Theta(n \cdot m)$$
Since $m \le n$, the worst-case complexity is $O(n^2)$, occurring when all points lie on the convex hull (e.g., points distributed on a circle). The best-case complexity is $\Omega(n)$, occurring when $m$ is constant. Thus, the algorithm is output-sensitive with complexity $O(n \cdot H)$.

### Space Complexity
*   **Auxiliary Space:** The algorithm maintains a constant number of pointers and variables (`leftmost`, `cur`, `candidate`, `cross`) to track the current state. Thus, the auxiliary space complexity is $O(1)$.
*   **Total Space:** The algorithm stores the resulting hull vertices. If the output is considered part of the space requirement, the space complexity is $O(H)$. Excluding the output, the space complexity remains $O(1)$.