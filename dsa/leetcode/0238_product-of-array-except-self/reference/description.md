## Description

Given an integer array `nums`, return *an array* `answer` *such that* $\text{answer}[i]$ *is equal to the product of all the elements of* `nums` *except* $\text{nums}[i]$.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.
### Function Contract

**Inputs**

- `nums`: An integer array containing at least two elements.

**Return value**

Return an equally sized array whose element `i` is the product of all $\text{nums}[j]$ for $j \ne i$.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,4]`
- **Output:** `[24,12,8,6]`
#### Example 2

- **Input:** `nums = [-1,1,0,-3,3]`
- **Output:** `[0,0,9,0,0]`
### Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $-30 \le \text{nums}[i] \le 30$

- The input is generated such that $\text{answer}[i]$ is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)