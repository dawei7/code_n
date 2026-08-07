## Description

You are given an integer array `nums` and an integer `k`.

Rotate only the **non-negative** elements of the array to the **left** by `k` positions, in a cyclic manner.

All **negative** elements must stay in their original positions and must not move.

After rotation, place the **non-negative** elements back into the array in the new order, filling only the positions that originally contained **non-negative** values and **skipping all negative** positions.

Return the resulting array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-2,3,-4], k = 3</span>

**Output:** <span class="example-io">[3,-2,1,-4]</span>

**Explanation:**​​​​​​​

	- The non-negative elements, in order, are `[1, 3]`.

	- Left rotation with `k = 3` results in:

		<li>`[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]`

	</li>
	- Placing them back into the non-negative indices results in `[3, -2, 1, -4]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-3,-2,7], k = 1</span>

**Output:** <span class="example-io">[-3,-2,7]</span>

**Explanation:**

	- The non-negative elements, in order, are `[7]`.

	- Left rotation with `k = 1` results in `[7]`.

	- Placing them back into the non-negative indices results in `[-3, -2, 7]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,-9,6], k = 2</span>

**Output:** <span class="example-io">[6,5,-9,4]</span>

**Explanation:**

	- The non-negative elements, in order, are `[5, 4, 6]`.

	- Left rotation with `k = 2` results in `[6, 5, 4]`.

	- Placing them back into the non-negative indices results in `[6, 5, -9, 4]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^5 <= nums[i] <= 10^5`

	- `0 <= k <= 10^5`
