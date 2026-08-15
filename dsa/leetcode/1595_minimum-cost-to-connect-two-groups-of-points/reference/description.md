### 1. Description

You are given two groups of points where the first group has $\text{size}_{1}$ points, the second group has $\text{size}_{2}$ points, and $\text{size}_{1} \ge \text{size}_{2}$.

The `cost` of the connection between any two points are given in an $\text{size}_{1} x \text{size}_{2}$ matrix where $\text{cost}[i][j]$ is the cost of connecting point `i` of the first group and point `j` of the second group. The groups are connected if **each point in both groups is connected to one or more points in the opposite group**. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

Return *the minimum cost it takes to connect the two groups*.

### 2. Function Contract

**Inputs**

- `cost`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

![](images/ex1.jpg)

- **Input:** $cost = [[15, 96], [36, 2]]$
- **Output:** `17`
**Explanation**: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

#### Example 2

![](images/ex2.jpg)

- **Input:** $cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]$
- **Output:** `4`
**Explanation**: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.

#### Example 3

- **Input:** $cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]$
- **Output:** `10`

### 4. Constraints

- $\text{size}_{1} = \text{cost.length}$

- $\text{size}_{2} = \text{cost}[i].length$

- $1 \le \text{size}_{1}, \text{size}_{2} \le 12$

- $\text{size}_{1} \ge \text{size}_{2}$

- $0 \le \text{cost}[i][j] \le 100$
