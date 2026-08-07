## Description

You are given an integer array `nums`.

From any index `i`, you can jump to another index `j` under the following rules:

	- Jump to index `j` where `j > i` is allowed only if `nums[j] < nums[i]`.

	- Jump to index `j` where `j < i` is allowed only if `nums[j] > nums[i]`.

For each index `i`, find the **maximum** **value** in `nums` that can be reached by following **any** sequence of valid jumps starting at `i`.

Return an array `ans` where `ans[i]` is the **maximum** **value** reachable starting from index `i`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,3]</span>

**Output:** <span class="example-io">[2,2,3]</span>

**Explanation:**

	- For `i = 0`: No jump increases the value.

	- For `i = 1`: Jump to `j = 0` as `nums[j] = 2` is greater than `nums[i]`.

	- For `i = 2`: Since `nums[2] = 3` is the maximum value in `nums`, no jump increases the value.

Thus, `ans = [2, 2, 3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,1]</span>

**Output:** <span class="example-io">[3,3,3]</span>

**Explanation:**

	- For `i = 0`: Jump forward to `j = 2` as `nums[j] = 1` is less than `nums[i] = 2`, then from `i = 2` jump to `j = 1` as `nums[j] = 3` is greater than `nums[2]`.

	- For `i = 1`: Since `nums[1] = 3` is the maximum value in `nums`, no jump increases the value.

	- For `i = 2`: Jump to `j = 1` as `nums[j] = 3` is greater than `nums[2] = 1`.

Thus, `ans = [3, 3, 3]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9​​​​​​​`
