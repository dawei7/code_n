## Description

You are given an integer array `nums` and a **positive** integer `k`.
A <span data-keyword="subsequence-array">subsequence</span> `sub` of `nums` with length `x` is called **valid** if it satisfies:

	- `(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.`

Return the length of the **longest** **valid** subsequence of `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5], k = 2</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The longest valid subsequence is `[1, 2, 3, 4, 5]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,2,3,1,4], k = 3</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The longest valid subsequence is `[1, 4, 1, 4]`.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^3`

	- `1 <= nums[i] <= 10^7`

	- `1 <= k <= 10^3`
