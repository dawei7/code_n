### 1. Description

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a **subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

### 2. Function Contract

**Inputs**

- `target`: The positive lower bound for the subarray sum.
- `nums`: An array of positive integers.

**Return value**

Return the smallest length of a contiguous, nonempty subarray whose sum is at least `target`, or `0` if none exists.

### 3. Examples

#### Example 1

- **Input:** $target = 7, nums = [2,3,1,2,4,3]$
- **Output:** `2`
- **Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

#### Example 2

- **Input:** $target = 4, nums = [1,4,4]$
- **Output:** `1`

#### Example 3

- **Input:** $target = 11, nums = [1,1,1,1,1,1,1,1]$
- **Output:** `0`

### 4. Constraints

- $1 \le target \le 10^{9}$

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{4}$

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.
