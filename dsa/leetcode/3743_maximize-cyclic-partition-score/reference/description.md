### 1. Description

You are given a **cyclic** array `nums` and an integer `k`.

### 2. Function Contract

**Inputs**

- `nums`: The cyclic array to divide into consecutive parts.
- `k`: The maximum number of subarrays in the partition.

Using fewer than `k` parts is permitted. A one-element part has range `0`.

For complexity notation, let $n=\texttt{nums.length}$ and

$q=\min\left(k,\left\lfloor\frac{n}{2}\right\rfloor\right).$

Only $q$ positive-range parts can matter because each such part needs at least two positions.

**Return value**

Return the maximum sum of subarray ranges over all cyclic partitions containing at most `k` parts.

### 3. Partition

`nums` into **at most** `k`** **subarrays. As `nums` is cyclic, these subarrays may wrap around from the end of the array back to the beginning.

The **range** of a subarray is the difference between its **maximum** and **minimum** values. The **score** of a partition is the sum of subarray **ranges**.

Return the **maximum** possible **score** among all cyclic partitions.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,3], k = 2

**Output:** 3

**Explanation:**

- Partition `nums` into `[2, 3]` and `[3, 1]` (wrapped around).

- The range of `[2, 3]` is $max(2, 3) - min(2, 3) = 3 - 2 = 1$.

- The range of `[3, 1]` is $max(3, 1) - min(3, 1) = 3 - 1 = 2$.

- The score is $1 + 2 = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,3], k = 1

**Output:** 2

**Explanation:**

- Partition `nums` into `[1, 2, 3, 3]`.

- The range of `[1, 2, 3, 3]` is $max(1, 2, 3, 3) - min(1, 2, 3, 3) = 3 - 1 = 2$.

- The score is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,3], k = 4

**Output:** 3

**Explanation:**

Identical to Example 1, we partition `nums` into `[2, 3]` and `[3, 1]`. Note that `nums` may be partitioned into fewer than `k` subarrays.

</div>

### 5. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le \text{nums.length}$