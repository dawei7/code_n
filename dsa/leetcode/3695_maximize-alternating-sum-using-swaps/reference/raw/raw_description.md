## Description

You are given an integer array `nums`.

You want to maximize the **alternating sum** of `nums`, which is defined as the value obtained by **adding** elements at even indices and **subtracting** elements at odd indices. That is, `nums[0] - nums[1] + nums[2] - nums[3]...`

You are also given a 2D integer array `swaps` where `swaps[i] = [p_i, q_i]`. For each pair `[p_i, q_i]` in `swaps`, you are allowed to swap the elements at indices `p_i` and `q_i`. These swaps can be performed any number of times and in any order.

Return the maximum possible **alternating sum** of `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], swaps = [[0,2],[1,2]]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The maximum alternating sum is achieved when `nums` is `[2, 1, 3]` or `[3, 1, 2]`. As an example, you can obtain `nums = [2, 1, 3]` as follows.

	- Swap `nums[0]` and `nums[2]`. `nums` is now `[3, 2, 1]`.

	- Swap `nums[1]` and `nums[2]`. `nums` is now `[3, 1, 2]`.

	- Swap `nums[0]` and `nums[2]`. `nums` is now `[2, 1, 3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], swaps = [[1,2]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The maximum alternating sum is achieved by not performing any swaps.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1000000000,1,1000000000,1,1000000000], swaps = []</span>

**Output:** <span class="example-io">-2999999997</span>

**Explanation:**

Since we cannot perform any swaps, the maximum alternating sum is achieved by not performing any swaps.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `0 <= swaps.length <= 10^5`

	- `swaps[i] = [p_i, q_i]`

	- `0 <= p_i < q_i <= nums.length - 1`

	- `[p_i, q_i] != [p_j, q_j]`
