## Description

You are given an integer array `nums`.

You **must** replace **exactly one** element in the array with **any** integer value in the range `[-10^5, 10^5]` (inclusive).

After performing this single replacement, determine the **maximum possible product** of **any three** elements at **distinct indices** from the modified array.

Return an integer denoting the **maximum product** achievable.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-5,7,0]</span>

**Output:** <span class="example-io">3500000</span>

**Explanation:**

Replacing 0 with -10^5 gives the array `[-5, 7, -10^5]`, which has a product `(-5) * 7 * (-10^5) = 3500000`. The maximum product is 3500000.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-4,-2,-1,-3]</span>

**Output:** <span class="example-io">1200000</span>

**Explanation:**

Two ways to achieve the maximum product include:

	- `[-4, -2, -3]` → replace -2 with 10^5 → product = `(-4) * 10^5 * (-3) = 1200000`.

	- `[-4, -1, -3]` → replace -1 with 10^5 → product = `(-4) * 10^5 * (-3) = 1200000`.

The maximum product is 1200000.</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,10,0]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There is no way to replace an element with another integer and not have a 0 in the array. Hence, the product of all three elements will always be 0, and the maximum product is 0.

</div>

**Constraints:**

	- `3 <= nums.length <= 10^5`

	- `-10^5 <= nums[i] <= 10^5`
