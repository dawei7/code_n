## Description

You are given an integer array `nums` and two **distinct** integers `target1` and `target2`.

A **partition** of `nums` splits it into one or more **contiguous, non-empty** blocks that cover the entire array without overlap.

A partition is **valid** if the **bitwise XOR** of elements in its blocks **alternates** between `target1` and `target2`, starting with `target1`.

Formally, for blocks `b1`, `b2`, …:

	- `XOR(b1) = target1`

	- `XOR(b2) = target2` (if it exists)

	- `XOR(b3) = target1`, and so on.

Return the number of valid partitions of `nums`, modulo `10^9 + 7`.

**Note:** A single block is valid if its **XOR** equals `target1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,1,4], target1 = 1, target2 = 5</span>

**Output:** <span class="example-io">1</span>

**Explanation:**​​​​​​​

	- The XOR of `[2, 3]` is 1, which matches `target1`.

	- The XOR of the remaining block `[1, 4]` is 5, which matches `target2`.

	- This is the only valid alternating partition, so the answer is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,0], target1 = 1, target2 = 0</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- **​​​​​​​**The XOR of `[1, 0, 0]` is 1, which matches `target1`.

	- The XOR of `[1]` and `[0, 0]` are 1 and 0, matching `target1` and `target2`.

	- The XOR of `[1, 0]` and `[0]` are 1 and 0, matching `target1` and `target2`.

	- Thus, the answer is 3.​​​​​​​

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7], target1 = 1, target2 = 7</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The XOR of `[7]` is 7, which does not match `target1`, so no valid partition exists.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i], target1, target2 <= 10^5`

	- `target1 != target2`
