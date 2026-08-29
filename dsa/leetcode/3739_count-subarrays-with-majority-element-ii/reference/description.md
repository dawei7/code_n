### 1. Description

You are given an integer array `nums` and an integer `target`.

Return the number of **subarrays** of `nums` in which `target` is the **majority element**.

The **majority element** of a subarray is the element that appears **strictly more than half** of the times in that subarray.

### 2. Function Contract

**Inputs**

- `nums`: The integer array whose non-empty contiguous subarrays are examined.
- `target`: The value that must be a strict majority in a counted subarray.

For a subarray of length $L$, let $f$ be the number of positions whose value equals `target`. The subarray is counted precisely when $2f > L$.

**Return value**

Return the total number of subarrays for which `target` satisfies that strict-majority condition. The count can be as large as $n(n+1)/2$, which exceeds a 32-bit signed integer when $n$ is near its upper bound.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,2,3], target = 2

- **Output:** 5

- **Explanation:** Valid subarrays with $target = 2$ as the majority element:

- $nums[1..1] = [2]$

- $nums[2..2] = [2]$

- $nums[1..2] = [2,2]$

- $nums[0..2] = [1,2,2]$

- $nums[1..3] = [2,2,3]$

So there are 5 such subarrays.

#### Example 2

- **Input:** nums = [1,1,1,1], target = 1

- **Output:** 10

- **Explanation:** 

****All 10 subarrays have 1 as the majority element.

#### Example 3

- **Input:** nums = [1,2,3], target = 4

- **Output:** 0

- **Explanation:** $target = 4$ does not appear in `nums` at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^5$

- $1 \le \text{nums}[i] \le 10^9$

- $1 \le target \le 10^{9}$
