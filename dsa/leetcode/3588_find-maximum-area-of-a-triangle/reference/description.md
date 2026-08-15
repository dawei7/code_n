### 1. Description

You are given a 2D array `coords` of size `n x 2`, representing the coordinates of `n` points in an infinite Cartesian plane.

Find **twice** the **maximum** area of a triangle with its corners at *any* three elements from `coords`, such that at least one side of this triangle is **parallel** to the x-axis or y-axis. Formally, if the maximum area of such a triangle is `A`, return $2 * A$.

If no such triangle exists, return -1.

### 2. Function Contract

**Inputs**

- `coords`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Note

that a triangle *cannot* have zero area.

### 4. Examples

#### Example 1

- **Input:** coords = [[1,1],[1,2],[3,2],[3,3]]

- **Output:** 2

- **Explanation:** ![](images/image-20250420010047-1.png)

The triangle shown in the image has a base 1 and height 2. Hence its area is $1/2 * base * height = 1$.

#### Example 2

- **Input:** coords = [[1,1],[2,2],[3,3]]

- **Output:** -1

- **Explanation:** The only possible triangle has corners `(1, 1)`, `(2, 2)`, and `(3, 3)`. None of its sides are parallel to the x-axis or the y-axis.

### 5. Constraints

- $1 \le n = \text{coords.length} \le 10^{5}$

- $1 \le \text{coords}[i][0], \text{coords}[i][1] \le 10^{6}$

- All $\text{coords}[i]$ are **unique**.
