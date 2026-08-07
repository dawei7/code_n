## Description

You are given an integer array `nums` of length `n`.

The **score** of an index `i` is defined as the number of indices `j` such that:

	- `i < j < n`, and

	- `nums[i]` and `nums[j]` have different parity (one is even and the other is odd).

Return an integer array `answer` of length `n`, where `answer[i]` is the score of index `i`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">[2,1,1,0]</span>

**Explanation:**

	- `nums[0] = 1`, which is odd. Thus, the indices `j = 1` and `j = 3` satisfy the conditions, so the score of index 0 is 2.

	- `nums[1] = 2`, which is even. Thus, the index `j = 2` satisfies the conditions, so the score of index 1 is 1.

	- `nums[2] = 3`, which is odd. Thus, the index `j = 3` satisfies the conditions, so the score of index 2 is 1.

	- `nums[3] = 4`, which is even. Thus, no index satisfies the conditions, so the score of index 3 is 0.

Thus, the `answer = [2, 1, 1, 0]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">[0]</span>

**Explanation:**

There is only one element in `nums`. Thus, the score of index 0 is 0.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
