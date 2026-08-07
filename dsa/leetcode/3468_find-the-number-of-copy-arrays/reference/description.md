## Description

You are given an array `original` of length `n` and a 2D array `bounds` of length `n x 2`, where $\text{bounds}[i] = [u_{i}, v_{i}]$.

You need to find the number of **possible** arrays `copy` of length `n` such that:

- $(\text{copy}[i] - copy[i - 1]) = (\text{original}[i] - original[i - 1])$ for $1 \le i \le n - 1$.

- $u_{i} \le \text{copy}[i] \le v_{i}$ for $0 \le i \le n - 1$.

Return the number of such arrays.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]

**Output:** 2

**Explanation:**

The possible arrays are:

- `[1, 2, 3, 4]`

- `[2, 3, 4, 5]`

</div>
#### Example 2

<div class="example-block">
**Input:** original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]

**Output:** 4

**Explanation:**

The possible arrays are:

- `[1, 2, 3, 4]`

- `[2, 3, 4, 5]`

- `[3, 4, 5, 6]`

- `[4, 5, 6, 7]`

</div>
#### Example 3

<div class="example-block">
**Input:** original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]

**Output:** 0

**Explanation:**

No array is possible.

</div>
### Constraints

- $2 \le n = \text{original.length} \le 10^{5}$

- $1 \le \text{original}[i] \le 10^{9}$

- $\text{bounds.length} = n$

- $\text{bounds}[i].length = 2$

- $1 \le \text{bounds}[i][0] \le \text{bounds}[i][1] \le 10^{9}$