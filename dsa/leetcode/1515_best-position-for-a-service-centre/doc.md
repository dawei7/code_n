# Best Position for a Service Centre

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1515 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/best-position-for-a-service-centre/) |

## Problem Description
### Goal

A delivery company knows the Cartesian coordinates of all customers in a city. It may place one service centre at any real-valued point in the plane, not only at an existing customer position or an integer coordinate.

Choose the centre so that the sum of its Euclidean distances to every customer is as small as possible, and return that minimum total. An answer within $10^{-5}$ of the true value is accepted.

### Function Contract
**Inputs**

Let $n$ be the number of customer positions and $I$ the fixed number of ternary-search iterations used per coordinate.

- `positions`: A list of $n$ coordinate pairs `[x_i, y_i]`, where $1 \leq n \leq 50$.
- Each coordinate is an integer in the inclusive range from 0 through 100.
- The service centre may use arbitrary real coordinates.

**Return value**

Return the minimum possible value of

$$
\sum_{i=1}^{n}\sqrt{(x-x_i)^2+(y-y_i)^2}
$$

over all real centre positions $(x,y)$.

### Examples
**Example 1**

- Input: `positions = [[0, 1], [1, 0], [1, 2], [2, 1]]`
- Output: `4.0`
- Explanation: Placing the centre at `(1, 1)` gives distance 1 to each customer.

**Example 2**

- Input: `positions = [[1, 1], [3, 3]]`
- Output: `2.82843`
- Explanation: Every point on the segment between the two customers has the same minimum total, equal to their separation.

**Example 3**

- Input: `positions = [[1, 1]]`
- Output: `0.0`
