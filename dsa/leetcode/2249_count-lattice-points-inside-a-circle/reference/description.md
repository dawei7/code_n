### 1. Description

Given a 2D integer array `circles` where $\text{circles}[i] = [x_{i}, y_{i}, r_{i}]$ represents the center $(x_{i}, y_{i})$ and radius $r_{i}$ of the $$i^{\text{th}}$$ circle drawn on a grid, return *the **number of lattice points** **that are present inside **at least one** circle*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

- A **lattice point** is a point with integer coordinates.

- Points that lie **on the circumference of a circle** are also considered to be inside it.

### 4. Examples

#### Example 1

![](images/exa-11.png)

- **Input:** $circles = [[2,2,1]]$
- **Output:** `5`
- **Explanation:**
The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.
#### Example 2

![](images/exa-22.png)

- **Input:** $circles = [[2,2,2],[3,4,1]]$
- **Output:** `16`
- **Explanation:**
The figure above shows the given circles.
There are exactly 16 lattice points which are present inside at least one circle.
Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).

### 5. Constraints

- $1 \le \text{circles.length} \le 200$

- $\text{circles}[i].length = 3$

- $1 \le x_{i}, y_{i} \le 100$

- $1 \le r_{i} \le min(x_{i}, y_{i})$