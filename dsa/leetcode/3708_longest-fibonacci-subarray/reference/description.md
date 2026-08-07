### 1. Description

You are given an array of **positive** integers `nums`.

A **Fibonacci** array is a contiguous sequence whose third and subsequent terms each equal the sum of the two preceding terms.

Return the length of the longest **Fibonacci** **subarray** in `nums`.

### 2. Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers.

A subarray `nums[left..right]` is contiguous. When it contains at least three values, each index $k$ with $left + 2 \le k \le right$ must satisfy $\text{nums}[k] = nums[k - 1] + nums[k - 2]$.

**Return value**

Return the greatest length of any Fibonacci subarray in `nums`.

### 3. Note

Subarrays of length 1 or 2 are always **Fibonacci**.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,1,1,1,2,3,5,1]

**Output:** 5

**Explanation:**

The longest Fibonacci subarray is $nums[2..6] = [1, 1, 2, 3, 5]$.

`[1, 1, 2, 3, 5]` is Fibonacci because $1 + 1 = 2$, $1 + 2 = 3$, and $2 + 3 = 5$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,2,7,9,16]

**Output:** 5

**Explanation:**

The longest Fibonacci subarray is $nums[0..4] = [5, 2, 7, 9, 16]$.

`[5, 2, 7, 9, 16]` is Fibonacci because $5 + 2 = 7$, $2 + 7 = 9$, and $7 + 9 = 16$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1000000000,1000000000,1000000000]

**Output:** 2

**Explanation:**

The longest Fibonacci subarray is $nums[1..2] = [1000000000, 1000000000]$.

`[1000000000, 1000000000]` is Fibonacci because its length is 2.

</div>

### 5. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$