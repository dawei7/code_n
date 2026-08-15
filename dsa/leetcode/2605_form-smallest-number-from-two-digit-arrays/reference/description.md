### 1. Description

Given two arrays of **unique** digits `nums1` and `nums2`, return *the **smallest** number that contains **at least** one digit from each array*.

### 2. Function Contract

**Inputs**

- `nums1`: Input parameter (`List[int]`).
- `nums2`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [4,1,3], nums2 = [5,7]$
- **Output:** `15`
- **Explanation:** The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

#### Example 2

- **Input:** $nums1 = [3,5,2,6], nums2 = [3,1,7]$
- **Output:** `3`
- **Explanation:** The number 3 contains the digit 3 which exists in both arrays.

### 4. Constraints

- $1 \le \text{nums1.length}, \text{nums2.length} \le 9$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 9$

- All digits in each array are **unique**.
