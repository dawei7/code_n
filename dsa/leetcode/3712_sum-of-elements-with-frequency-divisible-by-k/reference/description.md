## Description

You are given an integer array `nums` and an integer `k`.

Return an integer denoting the **sum** of all elements in `nums` whose **frequency** is divisible by `k`, or 0 if there are no such elements.

**Note:** An element is included in the sum **exactly** as many times as it appears in the array if its total frequency is divisible by `k`.
### Function Contract

**Inputs**

- `nums`: An array of positive integers.
- `k`: The positive frequency divisor.

Frequency is computed over the complete array and independently for each distinct value.

**Return value**

Return the sum of every occurrence whose value's total frequency is divisible by `k`, or `0` when no frequency passes that test.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,2,3,3,3,3,4], k = 2

**Output:** 16

**Explanation:**

- The number 1 appears once (odd frequency).

- The number 2 appears twice (even frequency).

- The number 3 appears four times (even frequency).

- The number 4 appears once (odd frequency).

So, the total sum is $2 + 2 + 3 + 3 + 3 + 3 = 16$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,4,5], k = 2

**Output:** 0

**Explanation:**

There are no elements that appear an even number of times, so the total sum is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [4,4,4,1,2,3], k = 3

**Output:** 12

**Explanation:**

- The number 1 appears once.

- The number 2 appears once.

- The number 3 appears once.

- The number 4 appears three times.

So, the total sum is $4 + 4 + 4 = 12$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$

- $1 \le k \le 100$