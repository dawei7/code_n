### 1. Description

Given an array `nums` and an integer `target`, return *the maximum number of **non-empty** **non-overlapping** subarrays such that the sum of values in each subarray is equal to* `target`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `target`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,1,1,1,1], target = 2`
- **Output:** `2`
- **Explanation:** There are 2 non-overlapping subarrays [**1,1**,1,**1,1**] with sum equals to target(2).

#### Example 2

- **Input:** `nums = [-1,3,5,1,4,2,-9], target = 6`
- **Output:** `2`
- **Explanation:** There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

- $0 \le target \le 10^{6}$
