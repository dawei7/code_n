## Description

You are given an integer array `nums` of length `n` and an integer array `queries`.

Let `gcdPairs` denote an array obtained by calculating the <span data-keyword="gcd-function">GCD</span> of all possible pairs `(nums[i], nums[j])`, where `0 <= i < j < n`, and then sorting these values in **ascending** order.

For each query `queries[i]`, you need to find the element at index `queries[i]` in `gcdPairs`.

Return an integer array `answer`, where `answer[i]` is the value at `gcdPairs[queries[i]]` for each query.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,4], queries = [0,2,2]</span>

**Output:** <span class="example-io">[1,2,2]</span>

**Explanation:**

`gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1]`.

After sorting in ascending order, `gcdPairs = [1, 1, 2]`.

So, the answer is `[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4,2,1], queries = [5,3,1,0]</span>

**Output:** <span class="example-io">[4,2,1,1]</span>

**Explanation:**

`gcdPairs` sorted in ascending order is `[1, 1, 1, 2, 2, 4]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2], queries = [0,0]</span>

**Output:** <span class="example-io">[2,2]</span>

**Explanation:**

`gcdPairs = [2]`.

</div>

**Constraints:**

	- `2 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 5 * 10^4`

	- `1 <= queries.length <= 10^5`

	- `0 <= queries[i] < n * (n - 1) / 2`
