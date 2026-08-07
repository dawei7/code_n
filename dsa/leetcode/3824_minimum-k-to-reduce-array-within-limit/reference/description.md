### 1. Description

You are given a **positive** integer array `nums`.

For a positive integer `k`, define `nonPositive(nums, k)` as the **minimum** number of **operations** needed to make every element of `nums` **non-positive**. In one operation, you can choose an index `i` and reduce $\text{nums}[i]$ by `k`.

Return an integer denoting the **minimum** value of `k` such that $nonPositive(nums, k) \le k^{2}$.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $N = \lvert\texttt{nums}\rvert$, let $V = \max(\texttt{nums})$, and define

$H = \max\left(V, \left\lceil\sqrt{N}\right\rceil\right).$

**Return value**

Return the minimum positive `k` whose minimum required operation count is at most $k^2$. Reaching exactly zero is sufficient because zero is non-positive, and reducing an element below zero is also allowed.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,7,5]

**Output:** 3

**Explanation:**

When $k = 3$, $nonPositive(nums, k) = 6 \le k^{2}$.

- Reduce $\text{nums}[0] = 3$ one time. $\text{nums}[0]$ becomes $3 - 3 = 0$.

- Reduce $\text{nums}[1] = 7$ three times. $\text{nums}[1]$ becomes $7 - 3 - 3 - 3 = -2$.

- Reduce $\text{nums}[2] = 5$ two times. $\text{nums}[2]$ becomes $5 - 3 - 3 = -1$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1]

**Output:** 1

**Explanation:**

When $k = 1$, $nonPositive(nums, k) = 1 \le k^{2}$.

- Reduce $\text{nums}[0] = 1$ one time. $\text{nums}[0]$ becomes $1 - 1 = 0$.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$