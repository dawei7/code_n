### 1. Description

You are given an integer array `nums`.

A **subarray** is called **balanced** if the number of **distinct even** numbers in the subarray is equal to the number of **distinct odd** numbers.

Return the length of the **longest** balanced subarray.

### 2. Function Contract

**Inputs**

- `nums`: The positive integer array whose contiguous subarrays are considered.

Repeated occurrences count only once within their parity group: balance compares the number of distinct even values with the number of distinct odd values, not the number of elements of each parity.

**Return value**

Return the length of the longest balanced subarray. Return `0` if no non-empty subarray is balanced.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,5,4,3]

**Output:** 4

**Explanation:**

- The longest balanced subarray is `[2, 5, 4, 3]`.

- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,2,2,5,4]

**Output:** 5

**Explanation:**

- The longest balanced subarray is `[3, 2, 2, 5, 4]`.

- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[3, 5]`. Thus, the answer is 5.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,2]

**Output:** 3

**Explanation:**

- The longest balanced subarray is `[2, 3, 2]`.

- It has 1 distinct even number `[2]` and 1 distinct odd number `[3]`. Thus, the answer is 3.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 1500$

- $1 \le \text{nums}[i] \le 10^{5}$