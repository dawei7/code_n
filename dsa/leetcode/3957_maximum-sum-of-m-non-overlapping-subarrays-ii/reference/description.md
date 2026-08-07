### 1. Description

You are given an integer array `nums` of length `n`, and three integers `m`, `l`, and `r`.

Your task is to select **at least** one and **at most** `m` **non-overlapping subarrays** from `nums` such that:

- Each selected **subarray** has a length between `[l, r]` (inclusive).

- The total sum of all selected **subarrays** is **maximized**.

Return the **maximum** total sum you can achieve.

### 2. Function Contract

**Inputs**

- `nums`: The integer array from which subarrays are selected.
- `m`: The maximum number of selected subarrays; at least one must be chosen.
- `l`: The inclusive minimum length of each selected subarray.
- `r`: The inclusive maximum length of each selected subarray.

**Return value**

Return the largest possible total sum of between one and `m` pairwise non-overlapping subarrays, with every selected length between `l` and `r` inclusive.

Let $n = \lvert\texttt{nums}\rvert$ and define

$S = 1 + \sum_{v \in \texttt{nums}} \max(v, 0).$

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [4,1,-5,2], m = 2, l = 1, r = 3

**Output:** 7

**Explanation:**

One optimal strategy is to:

- Select the subarray `[4, 1]` with sum $4 + 1 = 5$ and the subarray `[2]` with sum 2. Both subarrays have length between `[l, r]`.

- The total sum of these subarrays is $5 + 2 = 7$, which is the maximum achievable sum with at most $m = 2$ subarrays.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,0,3,4], m = 2, l = 1, r = 2

**Output:** 8

**Explanation:**

One optimal strategy is to:

- Select the subarray `[1]` with sum `1` and the subarray `[3, 4]` with sum $3 + 4 = 7$. Both subarrays have length between `[l, r]`.

- The total sum of these subarrays is $1 + 7 = 8$, which is the maximum achievable sum with at most $m = 2$ subarrays.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [-1,7,-4], m = 1, l = 2, r = 3

**Output:** 6

**Explanation:**

- Select the subarray `[-1, 7]` from `nums` which has length between `[l, r]`.

- The total sum of this subarray is $-1 + 7 = 6$, which is the maximum achievable sum with at most $m = 1$ subarray.

</div>
#### Example 4

<div class="example-block">
**Input:** nums = [-3,-4,-1], m = 2, l = 1, r = 2

**Output:** -1

**Explanation:**

- All subarrays of `nums` have negative sums. The optimal strategy is to select the subarray `[-1]`, which has length between `[l, r]`.

- The total sum of this subarray is -1, which is the maximum achievable sum with at most $m = 2$ subarrays.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}​​​​​​​$

- $1 \le m \le n$

- $1 \le l \le r \le n$