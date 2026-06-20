# Formal Mathematical Specification: Line Segment Intersection

## 1. Definitions and Notation

Let the Euclidean plane be defined as $\mathbb{R}^2$. A line segment $S$ is defined by an ordered pair of distinct points $(P_i, P_j) \in (\mathbb{Z}^2)^2$. We consider two segments:
$S_1 = (\mathbf{p}_1, \mathbf{p}_2)$ and $S_2 = (\mathbf{p}_3, \mathbf{p}_4)$, where $\mathbf{p}_k = (x_k, y_k)$.

We define the orientation function $\text{orient}: (\mathbb{Z}^2)^3 \to \{-1, 0, 1\}$ as the sign of the determinant of the matrix representing the vectors $\vec{AB}$ and $\vec{AC}$:
$$\text{orient}(\mathbf{a}, \mathbf{b}, \mathbf{c}) = \text{sgn}\left( (x_b - x_a)(y_c - y_a) - (y_b - y_a)(x_c - x_a) \right)$$
where $\text{sgn}(z)$ is the signum function:
$$\text{sgn}(z) = \begin{cases} 1 & \text{if } z > 0 \\ -1 & \text{if } z < 0 \\ 0 & \text{if } z = 0 \end{cases}$$

The intersection predicate $\mathcal{I}(S_1, S_2)$ is a boolean function mapping $(\mathbb{Z}^2)^4 \to \{ \text{True, False} \}$.

## 2. Algebraic Characterization

The intersection of two segments $S_1$ and $S_2$ is defined by the existence of a point $\mathbf{p}$ such that $\mathbf{p} \in S_1 \cap S_2$. Geometrically, this occurs if and only if the endpoints of one segment lie on opposite sides of the line containing the other segment, or if the segments are collinear and overlap.

Let $o_1 = \text{orient}(\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_3)$, $o_2 = \text{orient}(\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_4)$, $o_3 = \text{orient}(\mathbf{p}_3, \mathbf{p}_4, \mathbf{p}_1)$, and $o_4 = \text{orient}(\mathbf{p}_3, \mathbf{p}_4, \mathbf{p}_2)$.

The segments intersect if and only if:
1. **General Case:** The segments straddle each other:
   $$(o_1 \cdot o_2 < 0) \land (o_3 \cdot o_4 < 0)$$
2. **Collinear/Tangential Case:** One endpoint lies on the other segment:
   $$\exists k \in \{1, 2, 3, 4\} \text{ such that } o_i = 0 \text{ and } \mathbf{p}_k \in \text{BoundingBox}(S_j)$$
   where $\text{BoundingBox}((A, B)) = \{ (x, y) \in \mathbb{R}^2 \mid \min(x_A, x_B) \le x \le \max(x_A, x_B) \land \min(y_A, y_B) \le y \le \max(y_A, y_B) \}$.

Formally, the algorithm returns $\text{True}$ if:
$$\mathcal{I}(S_1, S_2) \iff ((o_1 \cdot o_2 < 0) \land (o_3 \cdot o_4 < 0)) \lor \bigvee_{i=1}^4 \text{is\_on\_segment}(S_i)$$
where $\text{is\_on\_segment}$ evaluates the collinearity and bounding box condition for each endpoint.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of a fixed sequence of arithmetic operations:
1. **Orientation Calculations:** Four calls to the `orient` function. Each call involves 2 subtractions, 2 multiplications, and 1 subtraction, totaling $O(1)$ arithmetic operations.
2. **Comparison and Logic:** A constant number of comparisons ($<, =, \le$) and logical conjunctions/disjunctions.
3. **Bounding Box Checks:** Up to four checks, each involving 4 comparisons and 2 logical conjunctions, totaling $O(1)$.

Since the number of operations $N_{ops}$ is independent of the coordinate values (assuming fixed-width integer arithmetic) and the number of segments is fixed at two, the total time complexity is:
$$T(n) = \Theta(1)$$

### Space Complexity
The algorithm requires storage for four coordinate pairs $(\mathbf{p}_1, \dots, \mathbf{p}_4)$ and four orientation scalars $(o_1, \dots, o_4)$. 
- Input storage: $O(1)$ (fixed size).
- Auxiliary storage: $O(1)$ (a constant number of integer variables).

Thus, the total space complexity is:
$$S(n) = \Theta(1)$$