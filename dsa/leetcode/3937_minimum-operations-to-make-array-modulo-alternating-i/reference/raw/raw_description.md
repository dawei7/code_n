## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase** or **decrease** any element of `nums` by 1.

An array is called **modulo alternating** if there exist two **distinct** integers `x` and `y` (`0 <= x, y < k`) such that:

	- For every **even** index `i`, `nums[i] % k == x`

	- For every **odd** index `i`, `nums[i] % k == y`

Return the **minimum** number of operations required to make `nums` **modulo alternating**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,2,8], k = 3</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Let's choose `x = 1` for even indices and `y = 2` for odd indices.

	- Perform the following operations:

		<li>Increment `nums[1] = 4` by 1, giving `nums = [1, 5, 2, 8]`.

		- Decrement `nums[2] = 2` by 1, giving `nums = [1, 5, 1, 8]`.

	</li>
	- Now, for even indices, `nums[i] % k = 1`, and for odd indices, `nums[i] % k = 2`.

	- Thus, the total number of operations required is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1], k = 3</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Incrementing `nums[1]` by 1 gives `nums = [1, 2, 1]`, which satisfies the condition with `x = 1` and `y = 2`.

	- Thus, the total number of operations required is 1.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 10^9`

	- `2 <= k <= 100`
