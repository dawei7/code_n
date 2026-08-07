## Description

You are given an integer array `nums` of length `n` and an integer `maxVal`.

You **may** change any element in `nums` to any positive integer **less than or equal** to `maxVal`. Each such change costs 1.

Two integers are **co-prime** if their <span data-keyword="gcd-function">**greatest common divisor (GCD)**</span> is 1.

After all modifications, you **must** choose an index `i` such that, `nums[i]` is **co-prime** with every other element `nums[j]`.

Let:

	- `selectedValue` be the final value of `nums[i]` after modifications.

	- `modificationCost` be the total number of elements changed.

The score is defined as `score = selectedValue - modificationCost`.

Return the **maximum** possible score.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,4,6], maxVal = 5</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Change `nums[2]` from 6 to 5, which costs 1. Choose `nums[2] = 5`, since it is co-prime with 3 and 4.

	- `selectedValue = 5`

	- `modificationCost = 1`

	- The score is `5 - 1 = 4`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], maxVal = 4</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

No modifications are required. Choose `nums[2] = 3`, since it is co-prime with 1 and 2.

	- `selectedValue = 3`

	- `modificationCost = 0`

	- The score is `3 - 0 = 3`

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2], maxVal = 1</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Change `nums[0]` from 2 to 1, which costs 1. Choose `nums[1] = 2`, since it is co-prime with 1.

	- `selectedValue = 2`

	- `modificationCost = 1`

	- The score is ​​​​​​​`2 - 1 = 1`

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `1 <= maxVal <= 10^​​​​​​​5`
