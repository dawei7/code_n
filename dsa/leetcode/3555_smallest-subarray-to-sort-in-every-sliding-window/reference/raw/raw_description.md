## Description

You are given an integer array `nums` and an integer `k`.

For each contiguous <span data-keyword="subarray">subarray</span> of length `k`, determine the **minimum** length of a continuous segment that must be sorted so that the entire window becomes **non‑decreasing**; if the window is already sorted, its required length is zero.

Return an array of length `n − k + 1` where each element corresponds to the answer for its window.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2,4,5], k = 3</span>

**Output:** <span class="example-io">[2,2,0]</span>

**Explanation:**

	- `nums[0...2] = [1, 3, 2]`. Sort `[3, 2]` to get `[1, 2, 3]`, the answer is 2.

	- `nums[1...3] = [3, 2, 4]`. Sort `[3, 2]` to get `[2, 3, 4]`, the answer is 2.

	- `nums[2...4] = [2, 4, 5]` is already sorted, so the answer is 0.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,3,2,1], k = 4</span>

**Output:** <span class="example-io">[4,4]</span>

**Explanation:**

	- `nums[0...3] = [5, 4, 3, 2]`. The whole subarray must be sorted, so the answer is 4.

	- `nums[1...4] = [4, 3, 2, 1]`. The whole subarray must be sorted, so the answer is 4.

</div>

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= k <= nums.length`

	- `1 <= nums[i] <= 10^6`
