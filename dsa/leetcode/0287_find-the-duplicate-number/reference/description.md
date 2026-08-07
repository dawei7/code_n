## Description

Given an array of integers `nums` containing $n + 1$ integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and using only constant extra space.
### Function Contract

**Inputs**

- `nums`: An array of `n + 1` integers from `[1,n]` containing exactly one distinct repeated value.

**Return value**

Return the value that occurs more than once.

### Examples
#### Example 1

- **Input:** `nums = [1,3,4,2,2]`
- **Output:** `2`
#### Example 2

- **Input:** `nums = [3,1,3,4,2]`
- **Output:** `3`
#### Example 3

- **Input:** `nums = [3,3,3,3,3]`
- **Output:** `3`
### Constraints

- $1 \le n \le 10^{5}$

- $\text{nums.length} = n + 1$

- $1 \le \text{nums}[i] \le n$

- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

**Follow up:**

- How can we prove that at least one duplicate number must exist in `nums`?

- Can you solve the problem in linear runtime complexity?