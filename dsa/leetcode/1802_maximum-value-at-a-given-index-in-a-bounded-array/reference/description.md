### 1. Description

You are given three positive integers: `n`, `index`, and `maxSum`. You want to construct an array `nums` (**0-indexed**)** **that satisfies the following conditions:

- $\text{nums.length} = n$

- $\text{nums}[i]$ is a **positive** integer where $0 \le i < n$.

- $abs(\text{nums}[i] - nums[i+1]) \le 1$ where $0 \le i < n-1$.

- The sum of all the elements of `nums` does not exceed `maxSum`.

- $\text{nums}[index]$ is **maximized**.

Return $\text{nums}[index]$* of the constructed array*.

Note that `abs(x)` equals `x` if $x \ge 0$, and `-x` otherwise.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $n = 4, index = 2, maxSum = 6$
- **Output:** `2`
- **Explanation:** nums = [1,2,<u>**2**</u>,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
#### Example 2

- **Input:** $n = 6, index = 1, maxSum = 10$
- **Output:** `3`

### 4. Constraints

- $1 \le n \le maxSum \le 10^{9}$

- $0 \le index < n$