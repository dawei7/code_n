### 1. Description

You are given an integer array `nums` and an integer `k`.

Your task is to partition `nums` into **exactly** `k` subarrays and return an integer denoting the **minimum possible score** among all valid partitions.

The **score** of a partition is the **sum** of the **values** of all its subarrays.

The **value** of a subarray is defined as $sumArr * (sumArr + 1) / 2$, where `sumArr` is the sum of its elements.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers, kept in its original order.
- `k`: The exact number of nonempty contiguous subarrays in the partition.

Let $N = \lvert\texttt{nums}\rvert$ and $K = \texttt{k}$. A partition places $K-1$ cuts between adjacent elements, so every element belongs to exactly one subarray and no subarray is empty.

**Return value**

Return the minimum integer score over all partitions of `nums` into exactly $K$ subarrays. Each subarray contributes the triangular number determined by the sum of its elements.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [5,1,2,1], k = 2

**Output:** 25

**Explanation:**

- We must partition the array into $k = 2$ subarrays. One optimal partition is `[5]` and `[1, 2, 1]`.

- The first subarray has $sumArr = 5$ and $value = 5 × 6 / 2 = 15$.

- The second subarray has $sumArr = 1 + 2 + 1 = 4$ and $value = 4 × 5 / 2 = 10$.

- The score of this partition is $15 + 10 = 25$, which is the minimum possible score.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,4], k = 1

**Output:** 55

**Explanation:**

- Since we must partition the array into $k = 1$ subarray, all elements belong to the same subarray: `[1, 2, 3, 4]`.

- This subarray has $sumArr = 1 + 2 + 3 + 4 = 10$ and $value = 10 × 11 / 2 = 55$.​​​​​​​

- The score of this partition is 55, which is the minimum possible score.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,1,1], k = 3

**Output:** 3

**Explanation:**

- We must partition the array into $k = 3$ subarrays. The only valid partition is `[1], [1], [1]`.

- Each subarray has $sumArr = 1$ and $value = 1 × 2 / 2 = 1$.

- The score of this partition is $1 + 1 + 1 = 3$, which is the minimum possible score.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{4}$

- $1 \le k \le \text{nums.length}$