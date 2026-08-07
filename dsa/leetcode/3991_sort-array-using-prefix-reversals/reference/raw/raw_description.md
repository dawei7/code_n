## Description

You are given an integer array `nums` of length `n`, where `nums` is a <span data-keyword="permutation-array">permutation</span> of the integers in the range `[0, n - 1]`.

You are also given an integer array `pre`, where each `pre[i]` is a valid <span data-keyword="array-prefix">prefix</span> length.

In one operation, you may choose any length `x` from `pre` and reverse the first `x` elements of `nums`.

For example, applying a prefix reversal of length `3` on `[4, 1, 2, 3]` results in `[2, 1, 4, 3]`.

Return the minimum number of operations required to sort `nums` in ascending order. If it is impossible to sort `nums`, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,0,1], pre = [2,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Reverse `pre[1] = 3` elements to get `nums = [1, 0, 2]`.

	- Then reverse `pre[0] = 2` elements to get `nums = [0, 1, 2]`.

	- Thus, the minimum number of prefix reversal required is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,2], pre = [1,3]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

It is impossible to sort the array using the given prefix lengths, so the answer is -1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1], pre = [2]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

Since `nums` is already sorted, no prefix reversals are needed. Thus, the answer is 0.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 8`

	- `0 <= nums[i] <= n - 1`

	- `1 <= pre.length <= n`

	- `1 <= pre[i] <= n`

	- `​​​​​​​nums` is a permutation of integers from 0 to `n - 1`.

	- `pre` consists of **unique** integers.
