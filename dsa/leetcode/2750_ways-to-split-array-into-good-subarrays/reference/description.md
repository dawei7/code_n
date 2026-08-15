### 1. Description

You are given a binary array `nums`.

A subarray of an array is **good** if it contains **exactly** **one** element with the value `1`.

Return *an integer denoting the number of ways to split the array *`nums`* into **good** subarrays*. As the number may be too large, return it **modulo** $10^{9} + 7$.

A subarray is a contiguous **non-empty** sequence of elements within an array.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [0,1,0,0,1]`
- **Output:** `3`
- **Explanation:** There are 3 ways to split nums into good subarrays:
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]

#### Example 2

- **Input:** `nums = [0,1,0]`
- **Output:** `1`
- **Explanation:** There is 1 way to split nums into good subarrays:
- [0,1,0]

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 1$
