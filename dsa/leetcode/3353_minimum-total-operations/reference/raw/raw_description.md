## Description

Given an array of integers `<font face="monospace">nums</font>`, you can perform *any* number of operations on this array.

In each **operation**, you can:

	- Choose a **prefix** of the array.

	- Choose an integer `<font face="monospace">k</font>`<font face="monospace"> </font>(which can be negative) and add `<font face="monospace">k</font>` to each element in the chosen prefix.

A **prefix** of an array is a subarray that starts from the beginning of the array and extends to any point within it.

Return the **minimum** number of operations required to make all elements in `arr` equal.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- **Operation 1**: Choose the prefix `[1, 4]` of length 2 and add -2 to each element of the prefix. The array becomes `[-1, 2, 2]`.

	- **Operation 2**: Choose the prefix `[-1]` of length 1 and add 3 to it. The array becomes `[2, 2, 2]`.

	- Thus, the minimum number of required operations is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,10,10]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- All elements are already equal, so no operations are needed.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`
