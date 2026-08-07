## Description

You are given an array of **positive** integers `nums`.

An array `arr` is called **product equivalent** if `prod(arr) == lcm(arr) * gcd(arr)`, where:

	- `prod(arr)` is the product of all elements of `arr`.

	- `gcd(arr)` is the <span data-keyword="gcd-function">GCD</span> of all elements of `arr`.

	- `lcm(arr)` is the <span data-keyword="lcm-function">LCM</span> of all elements of `arr`.

Return the length of the **longest** **product equivalent** <span data-keyword="subarray-nonempty">subarray</span> of `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1,2,1,1,1]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where `prod([1, 2, 1, 1, 1]) = 2`, `gcd([1, 2, 1, 1, 1]) = 1`, and `lcm([1, 2, 1, 1, 1]) = 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,4,5,6]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The longest product equivalent subarray is `[3, 4, 5].`

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,1,4,5,1]</span>

**Output:** <span class="example-io">5</span>

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 10`
