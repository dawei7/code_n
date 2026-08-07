## Description

You are given an integer array `nums`.

Partition the array into **three** (possibly empty) <span data-keyword="subsequence-array">subsequences</span> `A`, `B`, and `C` such that every element of `nums` belongs to **exactly** one subsequence.

Your goal is to **maximize** the value of: `XOR(A) + AND(B) + XOR(C)`

where:

	- `XOR(arr)` denotes the bitwise XOR of all elements in `arr`. If `arr` is empty, its value is defined as 0.

	- `AND(arr)` denotes the bitwise AND of all elements in `arr`. If `arr` is empty, its value is defined as 0.

Return the **maximum** value achievable.

**Note:** If multiple partitions result in the same **maximum** sum, you can consider any one of them.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

One optimal partition is:

	- `A = [3], XOR(A) = 3`

	- `B = [2], AND(B) = 2`

	- `C = [], XOR(C) = 0`

The maximum value of: `XOR(A) + AND(B) + XOR(C) = 3 + 2 + 0 = 5`. Thus, the answer is 5.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

One optimal partition is:

	- `A = [1], XOR(A) = 1`

	- `B = [2], AND(B) = 2`

	- `C = [3], XOR(C) = 3`

The maximum value of: `XOR(A) + AND(B) + XOR(C) = 1 + 2 + 3 = 6`. Thus, the answer is 6.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,6,7]</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

One optimal partition is:

	- `A = [7], XOR(A) = 7`

	- `B = [2,3], AND(B) = 2`

	- `C = [6], XOR(C) = 6`

The maximum value of: `XOR(A) + AND(B) + XOR(C) = 7 + 2 + 6 = 15`. Thus, the answer is 15.

</div>

**Constraints:**

	- `1 <= nums.length <= 19`

	- `1 <= nums[i] <= 10^9`
