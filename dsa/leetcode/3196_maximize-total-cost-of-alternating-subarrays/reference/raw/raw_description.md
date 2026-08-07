## Description

You are given an integer array `nums` with length `n`.

The **cost** of a <span data-keyword="subarray-nonempty">subarray</span> `nums[l..r]`, where `0 <= l <= r < n`, is defined as:

`cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)^r − l`

Your task is to **split** `nums` into subarrays such that the **total** **cost** of the subarrays is **maximized**, ensuring each element belongs to **exactly one** subarray.

Formally, if `nums` is split into `k` subarrays, where `k > 1`, at indices `i_1, i_2, ..., i_k − 1`, where `0 <= i_1 < i_2 < ... < i_k - 1 < n - 1`, then the total cost will be:

`cost(0, i_1) + cost(i_1 + 1, i_2) + ... + cost(i_k − 1 + 1, n − 1)`

Return an integer denoting the *maximum total cost* of the subarrays after splitting the array optimally.

**Note:** If `nums` is not split into subarrays, i.e. `k = 1`, the total cost is simply `cost(0, n - 1)`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-2,3,4]</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

One way to maximize the total cost is by splitting `[1, -2, 3, 4]` into subarrays `[1, -2, 3]` and `[4]`. The total cost will be `(1 + 2 + 3) + 4 = 10`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-1,1,-1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

One way to maximize the total cost is by splitting `[1, -1, 1, -1]` into subarrays `[1, -1]` and `[1, -1]`. The total cost will be `(1 + 1) + (1 + 1) = 4`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0]</span>

**Output:** 0

**Explanation:**

We cannot split the array further, so the answer is 0.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Selecting the whole array gives a total cost of `1 + 1 = 2`, which is the maximum.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`
