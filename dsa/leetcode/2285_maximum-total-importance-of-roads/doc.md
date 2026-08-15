# Maximum Total Importance of Roads

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2285 |
| Difficulty | Medium |
| Topics | Greedy, Graph Theory, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-importance-of-roads/) |

## Problem Description

### Goal

A country has $n$ cities numbered from 0 through $n-1$. Each pair
`roads[i] = [a_i, b_i]` describes one bidirectional road between distinct
cities, and no road is repeated.

Assign the distinct values $1,2,\ldots,n$ to the cities, using every value
exactly once. A road's importance is the sum of the two values assigned to its
endpoints. Return the maximum possible sum of importance over all roads after
choosing the assignment optimally.

### Function Contract

**Inputs**

- `n`: The number of cities.
- `roads`: An array of distinct undirected endpoint pairs.

Here, $2 \le n \le 5 \cdot 10^4$, there are between 1 and
$5 \cdot 10^4$ roads, and every endpoint is in $[0,n-1]$.

**Return value**

The greatest total road importance attainable by assigning the values from 1
through $n$ bijectively to the cities.

### Examples

#### Example 1

- **Input:** `n = 5`, `roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]`
- **Output:** `43`

#### Example 2

- **Input:** `n = 5`, `roads = [[0, 3], [2, 4], [1, 3]]`
- **Output:** `20`

#### Example 3

- **Input:** `n = 2`, `roads = [[0, 1]]`
- **Output:** `3`
