## Description

Given an array of integers `nums` and an integer `k`, return the number of subarrays of `nums` where the bitwise `AND` of the elements of the subarray equals `k`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,1,1], k = 1

**Output:** 6

**Explanation:**

All subarrays contain only 1's.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,1,2], k = 1

**Output:** 3

**Explanation:**

Subarrays having an `AND` value of 1 are: `[<u>**1**</u>,1,2]`, `[1,<u>**1**</u>,2]`, `[<u>**1,1**</u>,2]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3], k = 2

**Output:** 2

**Explanation:**

Subarrays having an `AND` value of 2 are: `[1,**<u>2</u>**,3]`, `[1,<u>**2,3**</u>]`.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i], k \le 10^{9}$