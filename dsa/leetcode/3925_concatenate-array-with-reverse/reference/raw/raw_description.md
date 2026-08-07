## Description

You are given an integer array `nums` of length `n`.

Construct a new array `ans` of length `2 * n` such that the first `n` elements are the same as `nums`, and the next `n` elements are the elements of `nums` in reverse order.

Formally, for `0 <= i <= n - 1`:

	- `ans[i] = nums[i]`

	- `ans[i + n] = nums[n - i - 1]`

Return an integer array `ans`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">[1,2,3,3,2,1]</span>

**Explanation:**

The first `n` elements of `ans` are the same as `nums`.

For the next `n = 3` elements, each element is taken from `nums` in reverse order:

	- `ans[3] = nums[2] = 3`

	- `ans[4] = nums[1] = 2`

	- `ans[5] = nums[0] = 1`

Thus, `ans = [1, 2, 3, 3, 2, 1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">[1,1]</span>

**Explanation:**

The array remains the same when reversed. Thus, `ans = [1, 1]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
