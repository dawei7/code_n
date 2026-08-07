### 1. Description

You are given two integers, `x` and `y`, which represent your current location on a Cartesian grid: `(x, y)`. You are also given an array `points` where each $\text{points}[i] = [a_{i}, b_{i}]$ represents that a point exists at $(a_{i}, b_{i})$. A point is **valid** if it shares the same x-coordinate or the same y-coordinate as your location.

Return *the index **(0-indexed)** of the **valid** point with the smallest **Manhattan distance** from your current location*. If there are multiple, return *the valid point with the **smallest** index*. If there are no valid points, return `-1`.

The **Manhattan distance** between two points $(x_{1}, y_{1})$ and $(x_{2}, y_{2})$ is $abs(x_{1} - x_{2}) + abs(y_{1} - y_{2})$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]$
- **Output:** `2`
- **Explanation:** Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.
#### Example 2

- **Input:** $x = 3, y = 4, points = [[3,4]]$
- **Output:** `0`
- **Explanation:** The answer is allowed to be on the same location as your current location.
#### Example 3

- **Input:** $x = 3, y = 4, points = [[2,3]]$
- **Output:** `-1`
- **Explanation:** There are no valid points.

### 4. Constraints

- $1 \le \text{points.length} \le 10^{4}$

- $\text{points}[i].length = 2$

- $1 \le x, y, a_{i}, b_{i} \le 10^{4}$