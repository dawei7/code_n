### 1. Description

Given an integer array `nums`, return the number of subarrays of length 3 such that the sum of the first and third numbers equals *exactly* half of the second number.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,1,4,1]

- **Output:** 1

- **Explanation:** Only the subarray `[1,4,1]` contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

#### Example 2

- **Input:** nums = [1,1,1]

- **Output:** 0

- **Explanation:** `[1,1,1]` is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

### 4. Constraints

- $3 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$
