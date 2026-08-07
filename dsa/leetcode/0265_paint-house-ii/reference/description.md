## Description

There are a row of `n` houses, each house can be painted with one of the `k` colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an `n x k` cost matrix costs.

- For example, $\text{costs}[0][0]$ is the cost of painting house `0` with color `0`; $\text{costs}[1][2]$ is the cost of painting house `1` with color `2`, and so on...

Return *the minimum cost to paint all houses*.
### Function Contract

**Inputs**

- `costs`: An `n x k` matrix in which $\text{costs}[i][j]$ is the price of painting house `i` with color `j`.

**Return value**

Return the minimum cost of painting all `n` houses so that adjacent houses have different colors.

### Examples

#### Example 1

- **Input:** $costs = [[1,5,3],[2,9,4]]$
- **Output:** `5`
- **Explanation:**
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
#### Example 2

- **Input:** $costs = [[1,3],[2,4]]$
- **Output:** `5`
### Constraints

- $\text{costs.length} = n$

- $\text{costs}[i].length = k$

- $1 \le n \le 100$

- $2 \le k \le 20$

- $1 \le \text{costs}[i][j] \le 20$

**Follow up:** Could you solve it in `O(nk)` runtime?