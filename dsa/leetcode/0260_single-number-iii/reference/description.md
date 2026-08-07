## Description

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in **any order**.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
### Function Contract

**Inputs**

- `nums`: An integer array with exactly two singleton values; all other values occur twice.

**Return value**

Return the two singleton values in either order.

### Examples
#### Example 1

- **Input:** `nums = [1,2,1,3,2,5]`
- **Output:** `[3,5]`
- **Explanation:** [5, 3] is also a valid answer.
#### Example 2

- **Input:** `nums = [-1,0]`
- **Output:** `[-1,0]`
#### Example 3

- **Input:** `nums = [0,1]`
- **Output:** `[1,0]`
### Constraints

- $2 \le \text{nums.length} \le 3 * 10^{4}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

- Each integer in `nums` will appear twice, only two integers will appear once.