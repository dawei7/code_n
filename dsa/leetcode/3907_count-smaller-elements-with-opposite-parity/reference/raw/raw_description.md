## Description

You are given an integer array `nums` of length `n`.

The **score** of an index `i` is defined as the number of indices `j` such that:

	- `i < j < n`

	- `nums[j] < nums[i]`

	- `nums[i]` and `nums[j]` have different parity (one is even and the other is odd).

Return an integer array `answer` of length `n`, where `answer[i]` is the score of index `i`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,2,4,1,3]</span>

**Output:** <span class="example-io">[2,1,2,0,0]</span>

**Explanation:**

	- For `i = 0`, the elements `nums[1] = 2` and `nums[2] = 4` are smaller and have different parity.

	- For `i = 1`, the element `nums[3] = 1` is smaller and has different parity.

	- For `i = 2`, the elements `nums[3] = 1` and `nums[4] = 3` are smaller and have different parity.

	- No valid elements exist for the remaining indices.

Thus, the `answer = [2, 1, 2, 0, 0]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4,1]</span>

**Output:** <span class="example-io">[1,1,0]</span>

**Explanation:**​​​​​​​

For `i = 0` and `i = 1`, the element `nums[2] = 1` is smaller and has different parity. Thus, the `answer = [1, 1, 0]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7]</span>

**Output:** <span class="example-io">[0]</span>

**Explanation:**

No elements exist to the right of index 0, so its score is 0. Thus, the `answer = [0]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`​​​​​​​
