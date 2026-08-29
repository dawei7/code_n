### 1. Description

You are given an array `start` where $start = [startX, startY]$ represents your initial position `(startX, startY)` in a 2D space. You are also given the array `target` where $target = [targetX, targetY]$ represents your target position `(targetX, targetY)`.

The **cost** of going from a position `(x1, y1)` to any other position in the space `(x2, y2)` is $|x2 - x1| + |y2 - y1|$.

There are also some **special roads**. You are given a 2D array `specialRoads` where $\text{specialRoads}[i] = [\text{x1}_{i}, \text{y1}_{i}, \text{x2}_{i}, \text{y2}_{i}, \text{cost}_{i}]$ indicates that the $i^{\text{th}}$ special road goes in **one direction** from $(\text{x1}_{i}, \text{y1}_{i})$ to $(\text{x2}_{i}, \text{y2}_{i})$ with a cost equal to $\text{cost}_{i}$. You can use each special road any number of times.

Return the **minimum** cost required to go from `(startX, startY)` to `(targetX, targetY)`.

### 2. Function Contract

**Inputs**

- `start`: Input parameter (`List[int]`).
- `target`: Input parameter (`List[int]`).
- `specialRoads`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]

- **Output:** 5

- **Explanation:** 

- (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.

- (1,2) to (3,3). Use $\text{specialRoads}[0]$ with the cost 2.

- (3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1.

- (3,4) to (4,5). Use $\text{specialRoads}[1]$ with the cost 1.

So the total cost is 1 + 2 + 1 + 1 = 5.

#### Example 2

- **Input:** start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]

- **Output:** 7

- **Explanation:** It is optimal not to use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.

Note that the $\text{specialRoads}[0]$ is directed from (5,7) to (3,2).

#### Example 3

- **Input:** start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]

- **Output:** 8

- **Explanation:** 

- (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.

- (1,2) to (7,4). Use $\text{specialRoads}[1]$ with the cost 4.

- (7,4) to (10,4) with a cost of |10 - 7| + |4 - 4| = 3.

### 4. Constraints

- $\text{start.length} = \text{target.length} = 2$

- $1 \le startX \le targetX \le 10^{5}$

- $1 \le startY \le targetY \le 10^{5}$

- $1 \le \text{specialRoads.length} \le 200$

- $\text{specialRoads}[i].length = 5$

- $startX \le \text{x1}_{i}, \text{x2}_{i} \le targetX$

- $startY \le \text{y1}_{i}, \text{y2}_{i} \le targetY$

- $1 \le \text{cost}_{i} \le 10^{5}$
