### 1. Description

You are given an integer array `nums` and an integer `k`.

Return the **minimum** length of a **subarray** whose sum of the **distinct** values present in that subarray (each value counted once) is **at least** `k`. If no such subarray exists, return -1.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The inclusive lower bound required for the distinct-value sum.

A subarray must contain consecutive elements and cannot be empty. If a value occurs several times in the selected interval, it is still included only once in the sum.

**Return value**

Return the smallest positive subarray length whose set of values sums to at least `k`. Return `-1` if every subarray has a smaller distinct-value sum.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,2,3,1], k = 4

**Output:** 2

**Explanation:**

The subarray `[2, 3]` has distinct elements `{2, 3}` whose sum is $2 + 3 = 5$, which is ​​​​​​​at least $k = 4$. Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,2,3,4], k = 5

**Output:** 2

**Explanation:**

The subarray `[3, 2]` has distinct elements `{3, 2}` whose sum is $3 + 2 = 5$, which is ​​​​​​​at least $k = 5$. Thus, the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,5,4], k = 5

**Output:** 1

**Explanation:**

The subarray `[5]` has distinct elements `{5}` whose sum is `5`, which is at least $k = 5$. Thus, the answer is 1.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le 10^{9}$