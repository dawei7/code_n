### 1. Description

You are given an integer array `nums`.

Split `nums` into two arrays `A` and `B` using the following rule:

- Elements at **prime** indices in `nums` must go into array `A`.

- All other elements must go into array `B`.

Return the **absolute** difference between the sums of the two arrays: $|sum(A) - sum(B)|$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

An empty array has a sum of 0.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,3,4]

**Output:** 1

**Explanation:**

- The only prime index in the array is 2, so $\text{nums}[2] = 4$ is placed in array `A`.

- The remaining elements, $\text{nums}[0] = 2$ and $\text{nums}[1] = 3$ are placed in array `B`.

- $sum(A) = 4$, $sum(B) = 2 + 3 = 5$.

- The absolute difference is $|4 - 5| = 1$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-1,5,7,0]

**Output:** 3

**Explanation:**

- The prime indices in the array are 2 and 3, so $\text{nums}[2] = 7$ and $\text{nums}[3] = 0$ are placed in array `A`.

- The remaining elements, $\text{nums}[0] = -1$ and $\text{nums}[1] = 5$ are placed in array `B`.

- $sum(A) = 7 + 0 = 7$, $sum(B) = -1 + 5 = 4$.

- The absolute difference is $|7 - 4| = 3$.

</div>

### 5. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$