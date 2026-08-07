## Description

You are given an integer array `nums` and an integer `k`.

An array is considered **balanced** if the value of its **maximum** element is **at most** `k` times the **minimum** element.

You may remove **any** number of elements from `nums`​​​​​​​ without making it **empty**.

Return the **minimum** number of elements to remove so that the remaining array is balanced.

**Note:** An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,1,5], k = 2

**Output:** 1

**Explanation:**

- Remove $\text{nums}[2] = 5$ to get `nums = [2, 1]`.

- Now $max = 2$, $min = 1$ and $max \le min * k$ as $2 \le 1 * 2$. Thus, the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,6,2,9], k = 3

**Output:** 2

**Explanation:**

- Remove $\text{nums}[0] = 1$ and $\text{nums}[3] = 9$ to get `nums = [6, 2]`.

- Now $max = 6$, $min = 2$ and $max \le min * k$ as $6 \le 2 * 3$. Thus, the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [4,6], k = 2

**Output:** 0

**Explanation:**

- Since `nums` is already balanced as $6 \le 4 * 2$, no elements need to be removed.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le 10^{5}$