### 1. Description

You are given a 2D integer array `points`, where $\text{points}[i] = [x_{i}, y_{i}]$ represents the coordinates of the $$i^{\text{th}}$$ point on the Cartesian plane.

The **Manhattan distance** between two points $\text{points}[i] = [x_{i}, y_{i}]$ and $\text{points}[j] = [x_{j}, y_{j}]$ is $|x_{i} - x_{j}| + |y_{i} - y_{j}|$.

Split the `n` points into **exactly two non-empty** groups. The **partition factor** of a split is the **minimum** Manhattan distance among all unordered pairs of points that lie in the same group.

Return the **maximum** possible **partition factor** over all valid splits.

Note: A group of size 1 contributes no intra-group pairs. When $n = 2$ (both groups size 1), there are no intra-group pairs, so define the partition factor as 0.

### 2. Function Contract

**Inputs**

- `points`: An array of Cartesian coordinates, with each entry containing exactly $[x_{i}, y_{i}]$.

Every point must be assigned to one of exactly two non-empty groups. Pair order does not matter, and only pairs whose two endpoints are in the same group contribute to that split's minimum.

**Return value**

Return the maximum, over all valid two-group assignments, of the minimum intra-group Manhattan distance. Apply the special value from the Note when neither group contains a pair.

### 3. Examples

#### Example 1

- **Input:** points = [[0,0],[0,2],[2,0],[2,2]]

- **Output:** 4

- **Explanation:** We split the points into two groups: ${[0, 0], [2, 2]}$ and ${[0, 2], [2, 0]}$.

- In the first group, the only pair has Manhattan distance $|0 - 2| + |0 - 2| = 4$.

- In the second group, the only pair also has Manhattan distance $|0 - 2| + |2 - 0| = 4$.

The partition factor of this split is $min(4, 4) = 4$, which is maximal.

#### Example 2

- **Input:** points = [[0,0],[0,1],[10,0]]

- **Output:** 11

- **Explanation:** ​​​​​​​**

We split the points into two groups: ${[0, 1], [10, 0]}$ and ${[0, 0]}$.

- In the first group, the only pair has Manhattan distance $|0 - 10| + |1 - 0| = 11$.

- The second group is a singleton, so it contributes no pairs.

The partition factor of this split is `11`, which is maximal.

### 4. Constraints

- $2 \le \text{points.length} \le 500$

- $\text{points}[i] = [x_{i}, y_{i}]$

- $-10^{8} \le x_{i}, y_{i} \le 10^{8}$
