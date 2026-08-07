## Description

You are given an integer array `nums`.

You want to construct an array `result` by repeatedly performing the following operation until `nums` becomes empty:

	- Choose an integer `k` such that `1 <= k <= len(nums)`.

	- Compute the **MEX** of the first `k` elements of `nums`.

	- Append this **MEX** to `result`.

	- Remove the first `k` elements from `nums`.

Return the **lexicographically maximum** array `result` that can be obtained after performing the operations.

The **MEX** of an array is the **smallest non-negative** integer not present in the array.

An array `a` is **lexicographically greater** than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is greater than the corresponding element in `b`. If the first `min(a.length, b.length)` elements do not differ, then the longer array is the **lexicographically greater** one.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1,0]</span>

**Output:** <span class="example-io">[2,1]</span>

**Explanation:**

	- Take the first `k = 2` elements `[0, 1]` which has MEX = 2. Current `result = [2]`.

	- Remaining array `[0]` has MEX = 1. Thus, the final `result = [2, 1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,2]</span>

**Output:** <span class="example-io">[3]</span>

**Explanation:**

	- Take the first `k = 3` elements `[1, 0, 2]` which has MEX = 3.

	- `<span class="example-io">nums</span>` is now empty. Thus, the final `result = [3]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1]</span>

**Output:** <span class="example-io">[0,0]</span>

**Explanation:**​​​​​​​

	- Take `k = 1`, first element `[3]` has MEX = 0. Current `result = [0]`.

	- Remaining array `[1]` has MEX = 0. Thus, the final `result = [0, 0]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`
