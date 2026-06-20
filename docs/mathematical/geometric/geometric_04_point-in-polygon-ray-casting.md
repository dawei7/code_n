# Formal Mathematical Specification: Point in Polygon (Ray-Casting)

## 1. Definitions and Notation

Let $\mathcal{P}$ be a simple polygon defined by an ordered sequence of $V$ vertices in the Euclidean plane $\mathbb{R}^2$, denoted as $\mathcal{P} = \{v_0, v_1, \dots, v_{V-1}\}$, where $v_i = (x_i, y_i)$. The edges of the polygon are the line segments $e_i = \overline{v_i v_{i+1}}$ for $0 \le i < V$, with indices taken modulo $V$.

Let $P = (x_p, y_p) \in \mathbb{R}^2$ be the test point. We define the ray $\mathcal{R}$ originating at $P$ as the set of points:
$$\mathcal{R} = \{ (x, y) \in \mathbb{R}^2 \mid x \ge x_p, y = y_p \}$$

We define the intersection set $\mathcal{I}$ as the collection of points where the ray $\mathcal{R}$ intersects the boundary $\partial\mathcal{P} = \bigcup_{i=0}^{V-1} e_i$:
$$\mathcal{I} = \mathcal{R} \cap \partial\mathcal{P}$$

The goal is to determine the membership of $P$ relative to the interior $\text{int}(\mathcal{P})$ and boundary $\partial\mathcal{P}$.

## 2. Algebraic Characterization

The algorithm relies on the Jordan Curve Theorem, which states that a simple closed curve divides the plane into exactly two regions: an interior and an exterior. The Ray-Casting algorithm utilizes the parity of the intersection count to determine the region.

### 2.1. Intersection Condition
For an edge $e_i$ defined by endpoints $v_i = (x_i, y_i)$ and $v_{i+1} = (x_{i+1}, y_{i+1})$, the ray $\mathcal{R}$ intersects $e_i$ if and only if:
1. The $y$-coordinate of $P$ lies strictly between the $y$-coordinates of the edge endpoints: $(y_i > y_p) \neq (y_{i+1} > y_p)$.
2. The $x$-coordinate of the intersection point $x_{int}$ satisfies $x_{int} > x_p$.

Using linear interpolation, the $x$-coordinate of the intersection point on the line segment $e_i$ at height $y_p$ is given by:
$$x_{int} = x_i + (x_{i+1} - x_i) \frac{y_p - y_i}{y_{i+1} - y_i}$$

### 2.2. The Even-Odd Rule
Let $\chi(e_i)$ be an indicator function such that $\chi(e_i) = 1$ if the ray $\mathcal{R}$ intersects $e_i$, and $\chi(e_i) = 0$ otherwise. The point $P$ is in the interior $\text{int}(\mathcal{P})$ if and only if:
$$\left( \sum_{i=0}^{V-1} \chi(e_i) \right) \equiv 1 \pmod 2$$

### 2.3. Boundary Condition
The point $P$ lies on the boundary $\partial\mathcal{P}$ if there exists at least one $i \in \{0, \dots, V-1\}$ such that $P \in e_i$. This is satisfied if $P$ is collinear with $v_i$ and $v_{i+1}$ and lies within the bounding box of the segment:
$$\min(x_i, x_{i+1}) \le x_p \le \max(x_i, x_{i+1}) \land \min(y_i, y_{i+1}) \le y_p \le \max(y_i, y_{i+1})$$
$$\text{and } (x_{i+1} - x_i)(y_p - y_i) = (y_{i+1} - y_i)(x_p - x_i)$$

## 3. Complexity Analysis

### 3.1. Time Complexity
The algorithm iterates through the set of edges $E = \{e_0, e_1, \dots, e_{V-1}\}$. For each edge $e_i$, the algorithm performs a constant number of arithmetic operations (comparisons, additions, and multiplications) to evaluate the intersection condition and the boundary condition.

Let $T(V)$ be the total time complexity. Since each edge is processed exactly once:
$$T(V) = \sum_{i=0}^{V-1} O(1) = O(V)$$
Thus, the algorithm is linear with respect to the number of vertices $V$.

### 3.2. Space Complexity
The algorithm maintains a constant number of scalar variables: the current vertex indices $i$ and $j$, the coordinates of the test point $P$, and a boolean flag `inside`. No auxiliary data structures proportional to the input size are allocated.

The total space complexity is:
$$S(V) = O(1)$$
This represents optimal auxiliary space usage, as the algorithm operates in-place relative to the input polygon representation.