## Description

You are given an integer array `nums`.

Your task is to find two **distinct** indices `i` and `j` such that the product `nums[i] * nums[j]` is **maximized,** and the binary representations of `nums[i]` and `nums[j]` do not share any common set bits.

Return the **maximum** possible product of such a pair. If no such pair exists, return 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5,6,7]</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

The best pair is 3 (011) and 4 (100). They share no set bits and `3 * 4 = 12`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,6,4]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

Every pair of numbers has at least one common set bit. Hence, the answer is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [64,8,32]</span>

**Output:** <span class="example-io">2048</span>

**Explanation:**

No pair of numbers share a common bit, so the answer is the product of the two maximum elements, 64 and 32 (`64 * 32 = 2048`).

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`
