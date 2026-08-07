## Description

You are given an integer array `heights` of size `n`, where `heights[i]` represents the height of the `i^th` block in an exercise routine.

You start on the ground (height 0) and **must** jump onto each block **exactly once** in any order.

	- The **calories burned** for a jump from a block of height `a` to a block of height `b` is `(a - b)^2`.

	- The **calories burned** for the first jump from the ground to the chosen first block `heights[i]` is `(0 - heights[i])^2`.

Return the **maximum** total calories you can burn by selecting an optimal jumping sequence.

**Note:** Once you jump onto the first block, you cannot return to the ground.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">heights = [1,7,9]</span>

**Output:** <span class="example-io">181</span>

**Explanation:**​​​​​​​

The optimal sequence is `[9, 1, 7]`.

	- Initial jump from the ground to `heights[2] = 9`: `(0 - 9)^2 = 81`.

	- Next jump to `heights[0] = 1`: `(9 - 1)^2 = 64`.

	- Final jump to `heights[1] = 7`: `(1 - 7)^2 = 36`.

Total calories burned = `81 + 64 + 36 = 181`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">heights = [5,2,4]</span>

**Output:** <span class="example-io">38</span>

**Explanation:**

The optimal sequence is `[5, 2, 4]`.

	- Initial jump from the ground to `heights[0] = 5`: `(0 - 5)^2 = 25`.

	- Next jump to `heights[1] = 2`: `(5 - 2)^2 = 9`.

	- Final jump to `heights[2] = 4`: `(2 - 4)^2 = 4`.

Total calories burned = `25 + 9 + 4 = 38`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">heights = [3,3]</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

The optimal sequence is `[3, 3]`.

	- Initial jump from the ground to `heights[0] = 3`: `(0 - 3)^2 = 9`.

	- Next jump to `heights[1] = 3`: `(3 - 3)^2 = 0`.

Total calories burned = `9 + 0 = 9`.

</div>

**Constraints:**

	- `1 <= n == heights.length <= 10^5`

	- `1 <= heights[i] <= 10^5`
