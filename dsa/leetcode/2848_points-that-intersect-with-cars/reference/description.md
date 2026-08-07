### 1. Description

You are given a **0-indexed** 2D integer array `nums` representing the coordinates of the cars parking on a number line. For any index `i`, $\text{nums}[i] = [\text{start}_{i}, \text{end}_{i}]$ where $\text{start}_{i}$ is the starting point of the $$i^{\text{th}}$$ car and $\text{end}_{i}$ is the ending point of the $$i^{\text{th}}$$ car.

Return *the number of integer points on the line that are covered with **any part** of a car.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [[3,6],[1,5],[4,7]]`
- **Output:** `7`
- **Explanation:** All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
#### Example 2

- **Input:** `nums = [[1,3],[5,8]]`
- **Output:** `7`
- **Explanation:** Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $\text{nums}[i].length = 2$

- $1 \le \text{start}_{i} \le \text{end}_{i} \le 100$