### 1. Description

You are given an integer array `nums` and two integers `cost1` and `cost2`. You are allowed to perform **either** of the following operations **any** number of times:

- Choose an index `i` from `nums` and **increase** $\text{nums}[i]$ by `1` for a cost of `cost1`.

- Choose two **different** indices `i`, `j`, from `nums` and **increase** $\text{nums}[i]$ and $\text{nums}[j]$ by `1` for a cost of `cost2`.

Return the **minimum** **cost** required to make all elements in the array **equal***. *

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [4,1], cost1 = 5, cost2 = 2

**Output:** 15

**Explanation: **

The following operations can be performed to make the values equal:

- Increase $\text{nums}[1]$ by 1 for a cost of 5. `nums` becomes `[4,2]`.

- Increase $\text{nums}[1]$ by 1 for a cost of 5. `nums` becomes `[4,3]`.

- Increase $\text{nums}[1]$ by 1 for a cost of 5. `nums` becomes `[4,4]`.

The total cost is 15.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,3,3,3,5], cost1 = 2, cost2 = 1

**Output:** 6

**Explanation: **

The following operations can be performed to make the values equal:

- Increase $\text{nums}[0]$ and $\text{nums}[1]$ by 1 for a cost of 1. `nums` becomes `[3,4,3,3,5]`.

- Increase $\text{nums}[0]$ and $\text{nums}[2]$ by 1 for a cost of 1. `nums` becomes `[4,4,4,3,5]`.

- Increase $\text{nums}[0]$ and $\text{nums}[3]$ by 1 for a cost of 1. `nums` becomes `[5,4,4,4,5]`.

- Increase $\text{nums}[1]$ and $\text{nums}[2]$ by 1 for a cost of 1. `nums` becomes `[5,5,5,4,5]`.

- Increase $\text{nums}[3]$ by 1 for a cost of 2. `nums` becomes `[5,5,5,5,5]`.

The total cost is 6.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [3,5,3], cost1 = 1, cost2 = 3

**Output:** 4

**Explanation:**

The following operations can be performed to make the values equal:

- Increase $\text{nums}[0]$ by 1 for a cost of 1. `nums` becomes `[4,5,3]`.

- Increase $\text{nums}[0]$ by 1 for a cost of 1. `nums` becomes `[5,5,3]`.

- Increase $\text{nums}[2]$ by 1 for a cost of 1. `nums` becomes `[5,5,4]`.

- Increase $\text{nums}[2]$ by 1 for a cost of 1. `nums` becomes `[5,5,5]`.

The total cost is 4.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{6}$

- $1 \le cost1 \le 10^{6}$

- $1 \le cost2 \le 10^{6}$