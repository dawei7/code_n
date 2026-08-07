### 1. Description

You are given an integer array `nums` of odd length `n`.

Return `true` if the middle element of `nums` appears **exactly** once in the array. Otherwise return `false`.

### 2. Function Contract

`solve(nums) -> bool`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: An odd-length integer array. Its middle element is `nums[n // 2]` in the original order.

**Output**

Return `true` if `nums[n // 2]` has total frequency exactly one in `nums`; otherwise return `false`. The odd-length guarantee means the middle position always exists and is unique, including when $n = 1$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** true

**Explanation:**

The middle element of `nums` is 2, which appears exactly once.

Thus, the answer is `true`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,2]

**Output:** false

**Explanation:**

The middle element of `nums` is 2, which appears twice.

Thus, the answer is `false`.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 100$

- `n` is odd.

- $1 \le \text{nums}[i] \le 100$