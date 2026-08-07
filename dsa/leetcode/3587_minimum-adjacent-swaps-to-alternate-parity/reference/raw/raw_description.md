## Description

You are given an array `nums` of **distinct** integers.

In one operation, you can swap any two **adjacent** elements in the array.

An arrangement of the array is considered **valid** if the parity of adjacent elements **alternates**, meaning every pair of neighboring elements consists of one even and one odd number.

Return the **minimum** number of adjacent swaps required to transform `nums` into any valid arrangement.

If it is impossible to rearrange `nums` such that no two adjacent elements have the same parity, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,4,6,5,7]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

Swapping 5 and 6, the array becomes `[2,4,5,6,7]`

Swapping 5 and 4, the array becomes `[2,5,4,6,7]`

Swapping 6 and 7, the array becomes `[2,5,4,7,6]`. The array is now a valid arrangement. Thus, the answer is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,4,5,7]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

By swapping 4 and 5, the array becomes `[2,5,4,7]`, which is a valid arrangement. Thus, the answer is 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The array is already a valid arrangement. Thus, no operations are needed.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,5,6,8]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

No valid arrangement is possible. Thus, the answer is -1.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- All elements in `nums` are **distinct**.
