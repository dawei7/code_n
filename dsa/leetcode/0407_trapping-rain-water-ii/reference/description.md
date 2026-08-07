## Description

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return *the volume of water it can trap after raining*.
### Function Contract

**Inputs**

- `heightMap`: The rectangular nonnegative elevation matrix.

**Return value**

Return the number of unit cubes of water trapped above the terrain after levels stabilize.

### Examples
#### Example 1

![](images/trap1-3d.jpg)

- **Input:** $heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]$
- **Output:** `4`
- **Explanation:** After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
#### Example 2

![](images/trap2-3d.jpg)

- **Input:** $heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]$
- **Output:** `10`
### Constraints

- $m = \text{heightMap.length}$

- $n = \text{heightMap}[i].length$

- $1 \le m, n \le 200$

- $0 \le \text{heightMap}[i][j] \le 2 * 10^{4}$