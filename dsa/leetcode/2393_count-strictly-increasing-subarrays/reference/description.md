## Description

You are given an array `nums` consisting of **positive** integers.

Return *the number of **subarrays** of *`nums`* that are in **strictly increasing** order.*

A **subarray** is a **contiguous** part of an array.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

- **Input:** `nums = [1,3,5,4,4,6]`
- **Output:** `10`
- **Explanation:** The strictly increasing subarrays are the following:
- Subarrays of length 1: [1], [3], [5], [4], [4], [6].
- Subarrays of length 2: [1,3], [3,5], [4,6].
- Subarrays of length 3: [1,3,5].
The total number of subarrays is 6 + 3 + 1 = 10.
#### Example 2

- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `15`
- **Explanation:** Every subarray is strictly increasing. There are 15 possible subarrays that we can take.
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{6}$