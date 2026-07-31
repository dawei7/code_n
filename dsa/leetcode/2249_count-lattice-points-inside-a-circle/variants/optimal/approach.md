## General

**Bound the candidates for one circle**

For a circle centered at `(center_x, center_y)` with radius `r`, any covered
lattice point must have both coordinates between the corresponding center
coordinate minus `r` and plus `r`. Enumerate that integer bounding square.

For each candidate `(x, y)`, test the squared-distance relation

$$
(x-\texttt{center\_x})^2+(y-\texttt{center\_y})^2\le r^2.
$$

The non-strict inequality includes circumference points, and squared integers
avoid floating-point square roots. Insert every passing coordinate pair into
one set shared by all circles. The set removes overlap automatically.

Every inserted point satisfies at least one circle inequality. Conversely,
every covered lattice point lies inside its circle's bounding square and
passes that circle's test, so it is inserted. The set size is therefore the
required union count.

## Complexity detail

Circle $i$ has a bounding square with $(2r_i+1)^2=O(r_i^2)$ integer
candidates. Total time is
$O\left(\sum_i r_i^2\right)$ under expected hash-set operations. If $P$ is the
number of distinct candidate points stored in the union, space is $O(P)$.

## Alternatives and edge cases

- **Scan one global bounding rectangle:** Testing every rectangle point against every circle is correct but repeats many circle checks for sparse or elongated inputs.
- **Use Euclidean distance with square roots:** This adds floating-point work and boundary-rounding risk; squared distances are exact.
- **Add each circle's count separately:** Overlapping lattice points would be counted more than once.
- **Circumference points:** Use `<=`, not `<`, because the boundary belongs to the circle.
- **Identical circles:** Their points enter the set again without changing the count.
- **Nested circles:** The inner circle adds no new points, which set union handles naturally.
- **Radius one:** Exactly the center and its four axis-adjacent lattice points are covered.
