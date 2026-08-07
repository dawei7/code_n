### 1. Description

You are given an integer array `nums` containing **distinct** positive integers and an integer `target`.

Determine if you can partition `nums` into two **non-empty** **disjoint** **subsets**, with each element belonging to **exactly one** subset, such that the product of the elements in each subset is equal to `target`.

Return `true` if such a partition exists and `false` otherwise.

A **subset** of an array is a selection of elements of the array.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,1,6,8,4], target = 24

**Output:** true

**Explanation:** The subsets `[3, 8]` and `[1, 6, 4]` each have a product of 24. Hence, the output is true.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,5,3,7], target = 15

**Output:** false

**Explanation:** There is no way to partition `nums` into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.

</div>

### 4. Constraints

- $3 \le \text{nums.length} \le 12$

- $1 \le target \le 10^{15}$

- $1 \le \text{nums}[i] \le 100$

- All elements of `nums` are **distinct**.