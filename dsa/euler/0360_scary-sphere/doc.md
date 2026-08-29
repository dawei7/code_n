# Scary Sphere

Given two points $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ in three-dimensional space, the Manhattan distance between those points is defined as:

$$
d_1 = |x_1 - x_2| + |y_1 - y_2| + |z_1 - z_2|
$$

Let $C(r)$ be a sphere with radius $r$ and center at the origin $O(0, 0, 0)$.

Let $I(r)$ be the set of all points with integer coordinates on the surface of $C(r)$.

Let $S(r)$ be the sum of the Manhattan distances of all elements of $I(r)$ to the origin $O$.

For example, $S(45) = 34518$.

Find $S(10^{10})$.
