### 1. Description

We call an array `arr` of length `n` **consecutive** if one of the following holds:

- $\text{arr}[i] - arr[i - 1] = 1$ for *all* $1 \le i < n$.

- $\text{arr}[i] - arr[i - 1] = -1$ for *all* $1 \le i < n$.

The **value** of an array is the sum of its elements.

For example, `[3, 4, 5]` is a consecutive array of value 12 and `[9, 8]` is another of value 17. While `[3, 4, 3]` and `[8, 6]` are not consecutive.

Given an array of integers `nums`, return the *sum* of the **values** of all **consecutive ***non-empty* subsequences.

Since the answer may be very large, return it **modulo** $10^{9} + 7.$

### 2. Function Contract

- Refer to method signature.

### 3. Note

that an array of length 1 is also considered consecutive.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2]

**Output:** 6

**Explanation:**

The consecutive subsequences are: `[1]`, `[2]`, `[1, 2]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,4,2,3]

**Output:** 31

**Explanation:**

The consecutive subsequences are: `[1]`, `[4]`, `[2]`, `[3]`, `[1, 2]`, `[2, 3]`, `[4, 3]`, `[1, 2, 3]`.

</div>

### 5. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$