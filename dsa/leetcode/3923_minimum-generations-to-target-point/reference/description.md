## Description

An initial list `points` contains distinct points in three-dimensional integer space, and `target` names another point.

Generation $0$ is exactly the initial list. To form generation $k\ge1$, take every pair of points with different coordinate triples that appeared in generations $0$ through $k-1$. For

$$
a=(x_1,y_1,z_1)
\quad\text{and}\quad
b=(x_2,y_2,z_2),
$$

the pair produces the coordinate-wise floored midpoint

$$
\left(
\left\lfloor\frac{x_1+x_2}{2}\right\rfloor,
\left\lfloor\frac{y_1+y_2}{2}\right\rfloor,
\left\lfloor\frac{z_1+z_2}{2}\right\rfloor
\right).
$$

All points of one generation are produced simultaneously from the points available before that generation. Only after generation $k$ is complete may its points participate in generation $k+1$ or later.

Return the earliest generation containing `target`. An initially present target has answer `0`; return `-1` when the process can never produce it.

**Notes**

- Flooring always rounds down to the nearest integer.
- A valid pair must contain two different coordinate triples. A point cannot be paired with itself, and two occurrences with identical coordinates would not constitute distinct points.
