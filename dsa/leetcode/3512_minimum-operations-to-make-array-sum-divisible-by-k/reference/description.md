### 1. Description

You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times:

- Select an index `i` and replace $\text{nums}[i]$ with $\text{nums}[i] - 1$.

Return the **minimum** number of operations required to make the sum of the array divisible by `k`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,9,7], k = 5

**Output:** 4

**Explanation:**

- Perform 4 operations on $\text{nums}[1] = 9$. Now, `nums = [3, 5, 7]`.

- The sum is 15, which is divisible by 5.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,1,3], k = 4

**Output:** 0

**Explanation:**

- The sum is 8, which is already divisible by 4. Hence, no operations are needed.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [3,2], k = 6

**Output:** 5

**Explanation:**

- Perform 3 operations on $\text{nums}[0] = 3$ and 2 operations on $\text{nums}[1] = 2$. Now, `nums = [0, 0]`.

- The sum is 0, which is divisible by 6.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 1000$

- $1 \le k \le 100$