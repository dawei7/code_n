## Description

You are given `m` `arrays`, where each array is sorted in **ascending order**.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference $|a - b|$.

Return *the maximum distance*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $arrays = [[1,2,3],[4,5],[1,2,3]]$
- **Output:** `4`
- **Explanation:** One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
#### Example 2

- **Input:** $arrays = [[1],[1]]$
- **Output:** `0`
### Constraints

- $m = \text{arrays.length}$

- $2 \le m \le 10^{5}$

- $1 \le \text{arrays}[i].length \le 500$

- $-10^{4} \le \text{arrays}[i][j] \le 10^{4}$

- $\text{arrays}[i]$ is sorted in **ascending order**.

- There will be at most $10^{5}$ integers in all the arrays.