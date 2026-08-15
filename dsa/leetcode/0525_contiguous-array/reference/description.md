### 1. Description

Given a binary array `nums`, return *the maximum length of a contiguous subarray with an equal number of *`0`* and *`1`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [0,1]`
- **Output:** `2`
- **Explanation:** [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

#### Example 2

- **Input:** `nums = [0,1,0]`
- **Output:** `2`
- **Explanation:** [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

#### Example 3

- **Input:** `nums = [0,1,1,1,1,1,0,0,0]`
- **Output:** `6`
- **Explanation:** [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $\text{nums}[i]$ is either `0` or `1`.
