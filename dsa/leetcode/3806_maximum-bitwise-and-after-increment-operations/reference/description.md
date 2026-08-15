### 1. Description

You are given an integer array `nums` and two integers `k` and `m`.

You may perform **at most** `k` operations. In one operation, you may choose any index `i` and **increase** $\text{nums}[i]$ by 1.

Return an integer denoting the **maximum** possible **bitwise AND** of any **subset** of size `m` after performing up to `k` operations optimally.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The maximum total number of unit-increment operations.
- `m`: The exact number of indices whose final values participate in the bitwise AND.

Let $N=\lvert\texttt{nums}\rvert$. Operations may be distributed among indices in any way, and fewer than `k` operations may be used. Only the final values at the chosen `m` distinct indices affect the returned AND.

**Return value**

Return the greatest integer that can equal the bitwise AND of some size-`m` subset after no more than `k` increments.

### 3. Examples

#### Example 1

- **Input:** nums = [3,1,2], k = 8, m = 2

- **Output:** 6

- **Explanation:** 

- We need a subset of size $m = 2$. Choose indices `[0, 2]`.

- Increase $\text{nums}[0] = 3$ to 6 using 3 operations, and increase $\text{nums}[2] = 2$ to 6 using 4 operations.

- The total number of operations used is 7, which is not greater than $k = 8$.

- The two chosen values become `[6, 6]`, and their bitwise AND is `6`, which is the maximum possible.

#### Example 2

- **Input:** nums = [1,2,8,4], k = 7, m = 3

- **Output:** 4

- **Explanation:** 

- We need a subset of size $m = 3$. Choose indices `[0, 1, 3]`.

- Increase $\text{nums}[0] = 1$ to 4 using 3 operations, increase $\text{nums}[1] = 2$ to 4 using 2 operations, and keep $\text{nums}[3] = 4$.

- The total number of operations used is 5, which is not greater than $k = 7$.

- The three chosen values become `[4, 4, 4]`, and their bitwise AND is 4, which is the maximum possible.​​​​​​​

#### Example 3

- **Input:** nums = [1,1], k = 3, m = 2

- **Output:** 2

- **Explanation:** 

- We need a subset of size $m = 2$. Choose indices `[0, 1]`.

- Increase both values from 1 to 2 using 1 operation each.

- The total number of operations used is 2, which is not greater than $k = 3$.

- The two chosen values become `[2, 2]`, and their bitwise AND is 2, which is the maximum possible.

### 4. Constraints

- $1 \le n = \text{nums.length} \le 5 * 10^{4}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le 10^{9}$

- $1 \le m \le n$
