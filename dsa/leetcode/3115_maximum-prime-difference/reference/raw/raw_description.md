## Description

You are given an integer array `nums`.

Return an integer that is the **maximum** distance between the **indices** of two (not necessarily different) prime numbers in `nums`*.*

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,2,9,5,3]</span>

**Output:** <span class="example-io">3</span>

**Explanation:** `nums[1]`, `nums[3]`, and `nums[4]` are prime. So the answer is `|4 - 1| = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,8,2,8]</span>

**Output:** <span class="example-io">0</span>

**Explanation:** `nums[2]` is prime. Because there is just one prime number, the answer is `|2 - 2| = 0`.

</div>

**Constraints:**

	- `1 <= nums.length <= 3 * 10^5`

	- `1 <= nums[i] <= 100`

	- The input is generated such that the number of prime numbers in the `nums` is at least one.
