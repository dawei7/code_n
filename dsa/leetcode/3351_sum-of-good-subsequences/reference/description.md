### 1. Description

You are given an integer array `nums`. A **good **subsequence is defined as a subsequence of `nums` where the absolute difference between any **two** consecutive elements in the subsequence is **exactly** 1.

Return the **sum** of all *possible* **good subsequences** of `nums`.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that a subsequence of size 1 is considered good by definition.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1]

**Output:** 14

**Explanation:**

- Good subsequences are: `[1]`, `[2]`, `[1]`, `[1,2]`, `[2,1]`, `[1,2,1]`.

- The sum of elements in these subsequences is 14.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,4,5]

**Output:** 40

**Explanation:**

- Good subsequences are: `[3]`, `[4]`, `[5]`, `[3,4]`, `[4,5]`, `[3,4,5]`.

- The sum of elements in these subsequences is 40.

</div>

### 5. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{5}$