### 1. Description

Given an array `nums`, return the number of subsequences with an odd sum of elements.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,1,1]

**Output:** 4

**Explanation:**

The odd-sum subsequences are: `[<u>**1**</u>, 1, 1]`, `[1, <u>**1**</u>, 1],` `[1, 1, <u>**1**</u>]`, `[<u>**1, 1, 1**</u>]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,2]

**Output:** 4

**Explanation:**

The odd-sum subsequences are: `[<u>**1**</u>, 2, 2]`, `[<u>**1, 2**</u>, 2],` `[<u>**1**</u>, 2, **<u>2</u>**]`, `[<u>**1, 2, 2**</u>]`.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$