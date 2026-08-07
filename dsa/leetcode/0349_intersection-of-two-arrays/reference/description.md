### 1. Description

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order**.

### 2. Function Contract

**Inputs**

- `nums1`: The first integer array.
- `nums2`: The second integer array.

**Return value**

Return each distinct integer that appears in both arrays exactly once, in any order.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [1,2,2,1], nums2 = [2,2]$
- **Output:** `[2]`
#### Example 2

- **Input:** $nums1 = [4,9,5], nums2 = [9,4,9,8,4]$
- **Output:** `[9,4]`
- **Explanation:** [4,9] is also accepted.

### 4. Constraints

- $1 \le \text{nums1.length}, \text{nums2.length} \le 1000$

- $0 \le \text{nums1}[i], \text{nums2}[i] \le 1000$