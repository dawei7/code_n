### 1. Description

Given two integer arrays `nums1` and `nums2`, return *the maximum length of a subarray that appears in **both** arrays*.

### 2. Function Contract

**Inputs**

- `nums1`: Input parameter (`List[int]`).
- `nums2`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]$
- **Output:** `3`
- **Explanation:** The repeated subarray with maximum length is [3,2,1].

#### Example 2

- **Input:** $nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]$
- **Output:** `5`
- **Explanation:** The repeated subarray with maximum length is [0,0,0,0,0].

### 4. Constraints

- $1 \le \text{nums1.length}, \text{nums2.length} \le 1000$

- $0 \le \text{nums1}[i], \text{nums2}[i] \le 100$
