### 1. Description

You are given an integer array `nums` and an integer `m`.

Return the **maximum** product of the first and last elements of any **subsequence** of `nums` of size `m`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `m`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [-1,-9,2,3,-2,-3,1], m = 1

- **Output:** 81

- **Explanation:** The subsequence `[-9]` has the largest product of the first and last elements: $-9 * -9 = 81$. Therefore, the answer is 81.

#### Example 2

- **Input:** nums = [1,3,-5,5,6,-4], m = 3

- **Output:** 20

- **Explanation:** The subsequence `[-5, 6, -4]` has the largest product of the first and last elements.

#### Example 3

- **Input:** nums = [2,-1,2,-6,5,2,-5,7], m = 2

- **Output:** 35

- **Explanation:** The subsequence `[5, 7]` has the largest product of the first and last elements.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $1 \le m \le \text{nums.length}$
