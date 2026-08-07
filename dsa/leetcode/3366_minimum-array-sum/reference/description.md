## Description

You are given an integer array `nums` and three integers `k`, `op1`, and `op2`.

You can perform the following operations on `nums`:

- **Operation 1**: Choose an index `i` and divide $\text{nums}[i]$ by 2, **rounding up** to the nearest whole number. You can perform this operation at most `op1` times, and not more than **once** per index.

- **Operation 2**: Choose an index `i` and subtract `k` from $\text{nums}[i]$, but only if $\text{nums}[i]$ is greater than or equal to `k`. You can perform this operation at most `op2` times, and not more than **once** per index.

**Note:** Both operations can be applied to the same index, but at most once each.

Return the **minimum** possible **sum** of all elements in `nums` after performing any number of operations.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1

**Output:** 23

**Explanation:**

- Apply Operation 2 to $\text{nums}[1] = 8$, making $\text{nums}[1] = 5$.

- Apply Operation 1 to $\text{nums}[3] = 19$, making $\text{nums}[3] = 10$.

- The resulting array becomes `[2, 5, 3, 10, 3]`, which has the minimum possible sum of 23 after applying the operations.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,4,3], k = 3, op1 = 2, op2 = 1

**Output:** 3

**Explanation:**

- Apply Operation 1 to $\text{nums}[0] = 2$, making $\text{nums}[0] = 1$.

- Apply Operation 1 to $\text{nums}[1] = 4$, making $\text{nums}[1] = 2$.

- Apply Operation 2 to $\text{nums}[2] = 3$, making $\text{nums}[2] = 0$.

- The resulting array becomes `[1, 2, 0]`, which has the minimum possible sum of 3 after applying the operations.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $0 \le \text{nums}[i] \le 10^{5}$

- $0 \le k \le 10^{5}$

- $0 \le op1, op2 \le \text{nums.length}$