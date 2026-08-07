## Description

You are given an integer array `nums`.

An array is considered **alternating prime** if:

	- Elements at **even** indices (0-based) are **prime** numbers.

	- Elements at **odd** indices are **non-prime** numbers.

In one operation, you may **increment** any element by 1.

Return the **minimum** number of operations required to transform `nums` into an **alternating prime** array.

A **prime** number is a natural number greater than 1 with only two factors, 1 and itself.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The element at index 0 must be prime. Increment `nums[0] = 1` to 2, using 1 operation.

	- The element at index 1 must be non-prime. Increment `nums[1] = 2` to 4, using 2 operations.

	- The element at index 2 is already prime.

	- The element at index 3 is already non-prime.

Total operations = `1 + 2 = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,6,7,8]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The elements at indices 0 and 2 are already prime.

	- The elements at indices 1 and 3 are already non-prime.

No operations are needed.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- The element at index 0 must be prime. Increment `nums[0] = 4` to 5, using 1 operation.

	- The element at index 1 is already non-prime.

Total operations = 1.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
