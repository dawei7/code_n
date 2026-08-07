## Description

Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.
### Function Contract

**Inputs**

- `nums`: A non-empty integer array.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return the maximum sum among all non-empty contiguous subarrays of `nums`.

### Examples
#### Example 1

- **Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`
- **Output:** `6`
- **Explanation:** The subarray [4,-1,2,1] has the largest sum 6.
#### Example 2

- **Input:** `nums = [1]`
- **Output:** `1`
- **Explanation:** The subarray [1] has the largest sum 1.
#### Example 3

- **Input:** `nums = [5,4,-1,7,8]`
- **Output:** `23`
- **Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.