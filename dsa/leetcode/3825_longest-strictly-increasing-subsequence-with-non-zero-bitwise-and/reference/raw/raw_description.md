## Description

You are given an integer array `nums`.

Return the length of the **longest strictly increasing <span data-keyword="subsequence-array-nonempty">subsequence</span>** in `nums` whose bitwise **AND** is **non-zero**. If no such **subsequence** exists, return 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,7]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One longest strictly increasing subsequence is `[5, 7]`. The bitwise AND is `5 AND 7 = 5`, which is non-zero.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,6]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The longest strictly increasing subsequence is `[2, 3, 6]`. The bitwise AND is `2 AND 3 AND 6 = 2`, which is non-zero.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

One longest strictly increasing subsequence is `[1]`. The bitwise AND is 1, which is non-zero.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`​​​​​​​
