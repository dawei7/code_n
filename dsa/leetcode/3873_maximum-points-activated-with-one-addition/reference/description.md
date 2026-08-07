## Description

You are given a 2D integer array `points`, where $\text{points}[i] = [x_{i}, y_{i}]$ represents the coordinates of the $$i^{\text{th}}$$ point. All coordinates in `points` are **distinct**.

If a point is **activated**, then all points that have the **same** x-coordinate **or** y-coordinate become **activated** as well.

Activation continues until no additional points can be activated.

You may add **one additional** point at any integer coordinate `(x, y)` not already present in `points`. Activation begins by **activating** this **newly added point**.

Return an integer denoting the **maximum** number of points that can be activated, including the newly added point.
### Function Contract

**Inputs**

- `points`: Distinct coordinate pairs representing the existing points.

Two existing points are directly connected when their x-coordinates are equal or their y-coordinates are equal. Activation reaches an entire connected component under the transitive closure of this relation. The added coordinate must contain integers and must differ from every existing coordinate pair; either individual coordinate may still equal an existing x- or y-coordinate.

Let $n=\lvert\texttt{points}\rvert$.

**Return value**

Return the largest number of activated points achievable after adding and initially activating one valid point. Include the newly added point in the count.

### Examples
#### Example 1

<div class="example-block">
**Input:** points = [[1,1],[1,2],[2,2]]

**Output:** 4

**Explanation:**

Adding and activating a point such as `(1, 3)` causes activations:

- `(1, 3)` shares $x = 1$ with `(1, 1)` and `(1, 2)` -> `(1, 1)` and `(1, 2)` become activated.

- `(1, 2)` shares $y = 2$ with `(2, 2)` -> `(2, 2)` becomes activated.

Thus, the activated points are `(1, 3)`, `(1, 1)`, `(1, 2)`, `(2, 2)`, so 4 points in total. We can show this is the maximum activated.

</div>
#### Example 2

<div class="example-block">
**Input:** points = [[2,2],[1,1],[3,3]]

**Output:** 3

**Explanation:**

Adding and activating a point such as `(1, 2)` causes activations:

- `(1, 2)` shares $x = 1$ with `(1, 1)` -> `(1, 1)` becomes activated.

- `(1, 2)` shares $y = 2$ with `(2, 2)` -> `(2, 2)` becomes activated.

Thus, the activated points are `(1, 2)`, `(1, 1)`, `(2, 2)`, so 3 points in total. We can show this is the maximum activated.

</div>
#### Example 3

<div class="example-block">
**Input:** points = [[2,3],[2,2],[1,1],[4,5]]

**Output:** 4

**Explanation:**

Adding and activating a point such as `(2, 1)` causes activations:

- `(2, 1)` shares $x = 2$ with `(2, 3)` and `(2, 2)` -> `(2, 3)` and `(2, 2)` become activated.

- `(2, 1)` shares $y = 1$ with `(1, 1)` -> `(1, 1)` becomes activated.

Thus, the activated points are `(2, 1)`, `(2, 3)`, `(2, 2)`, `(1, 1)`, so 4 points in total.

</div>
### Constraints

- $1 \le \text{points.length} \le 10^{5}$

- $\text{points}[i] = [x_{i}, y_{i}]$

- $-10^{9} \le x_{i}, y_{i} \le 10^{9}$

- `points` contains all **distinct** coordinates.