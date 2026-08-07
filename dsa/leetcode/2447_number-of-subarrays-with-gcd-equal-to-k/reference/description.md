### 1. Description

Given an integer array `nums` and an integer `k`, return *the number of **subarrays** of *`nums`* where the greatest common divisor of the subarray's elements is *`k`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

The **greatest common divisor of an array** is the largest integer that evenly divides all the array elements.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [9,3,1,2,6,3], k = 3`
- **Output:** `4`
- **Explanation:** The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,<u>**3**</u>,1,2,6,3]
- [9,3,1,2,6,<u>**3**</u>]
- [<u>**9,3**</u>,1,2,6,3]
- [9,3,1,2,<u>**6,3**</u>]
#### Example 2

- **Input:** `nums = [4], k = 7`
- **Output:** `0`
- **Explanation:** There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i], k \le 10^{9}$