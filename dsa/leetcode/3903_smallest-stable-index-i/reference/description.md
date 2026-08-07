### 1. Description

You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define its **instability score** as $max(nums[0..i]) - min(nums[i..n - 1])$.

In other words:

- `max(nums[0..i])` is the **largest** value among the elements from index 0 to index `i`.

- $min(nums[i..n - 1])$ is the **smallest** value among the elements from index `i` to index $n - 1$.

An index `i` is called **stable** if its instability score is **less than or equal to** `k`.

Return the **smallest** stable index. If no such index exists, return -1.

### 2. Function Contract

**Inputs**

- `nums`: A non-empty array of non-negative integers.
- `k`: The inclusive upper bound for a stable index's instability score.

Both ranges used at index $i$ include $\text{nums}[i]$: the prefix is `nums[0..i]`, and the suffix is $nums[i..n - 1]$.

**Return value**

Return the least index $i$ satisfying

$\max(\texttt{nums}[0..i])-\min(\texttt{nums}[i..n-1])\le \texttt{k}.$

Return `-1` when no index satisfies the inequality.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [5,0,1,4], k = 3

**Output:** 3

**Explanation:**

- At index 0: The maximum in `[5]` is 5, and the minimum in `[5, 0, 1, 4]` is 0, so the instability score is $5 - 0 = 5$.

- At index 1: The maximum in `[5, 0]` is 5, and the minimum in `[0, 1, 4]` is 0, so the instability score is $5 - 0 = 5$.

- At index 2: The maximum in `[5, 0, 1]` is 5, and the minimum in `[1, 4]` is 1, so the instability score is $5 - 1 = 4$.

- At index 3: The maximum in `[5, 0, 1, 4]` is 5, and the minimum in `[4]` is 4, so the instability score is $5 - 4 = 1$.

- This is the first index with an instability score less than or equal to $k = 3$. Thus, the answer is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,2,1], k = 1

**Output:** -1

**Explanation:**

- At index 0, the instability score is $3 - 1 = 2$.

- At index 1, the instability score is $3 - 1 = 2$.

- At index 2, the instability score is $3 - 1 = 2$.

- None of these values is less than or equal to $k = 1$, so the answer is -1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [0], k = 0

**Output:** 0

**Explanation:**

At index 0, the instability score is $0 - 0 = 0$, which is less than or equal to $k = 0$. Therefore, the answer is 0.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $0 \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le 10^{9}$