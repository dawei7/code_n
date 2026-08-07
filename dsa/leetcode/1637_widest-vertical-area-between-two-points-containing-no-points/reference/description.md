### 1. Description

Given `n` `points` on a 2D plane where $\text{points}[i] = [x_{i}, y_{i}]$, Return* the **widest vertical area** between two points such that no points are inside the area.*

A **vertical area** is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The **widest vertical area** is the one with the maximum width.

Note that points **on the edge** of a vertical area **are not** considered included in the area.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/points3.png)

​

- **Input:** $points = [[8,7],[9,9],[7,4],[9,7]]$
- **Output:** `1`
- **Explanation:** Both the red and the blue area are optimal.
#### Example 2

- **Input:** $points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]$
- **Output:** `3`

### 4. Constraints

- $n = \text{points.length}$

- $2 \le n \le 10^{5}$

- $\text{points}[i].length = 2$

- $0 \le x_{i}, y_{i} \le 10^{9}$