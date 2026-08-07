## Description

You are given a <span data-keyword="binary-array">binary array</span> `nums`.

You can do the following operation on the array **any** number of times (possibly zero):

	- Choose **any** index `i` from the array and **flip** **all** the elements from index `i` to the end of the array.

**Flipping** an element means changing its value from 0 to 1, and from 1 to 0.

Return the **minimum** number of operations required to make all elements in `nums` equal to 1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1,1,0,1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

We can do the following operations:

	- Choose the index `i = 1`<span class="example-io">. The resulting array will be `nums = [0,<u>**0**</u>,<u>**0**</u>,<u>**1**</u>,<u>**0**</u>]`.</span>

	- Choose the index `i = 0`<span class="example-io">. The resulting array will be `nums = [<u>**1**</u>,<u>**1**</u>,<u>**1**</u>,<u>**0**</u>,<u>**1**</u>]`.</span>

	- Choose the index `i = 4`<span class="example-io">. The resulting array will be `nums = [1,1,1,0,<u>**0**</u>]`.</span>

	- Choose the index `i = 3`<span class="example-io">. The resulting array will be `nums = [1,1,1,<u>**1**</u>,<u>**1**</u>]`.</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,0,0]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

We can do the following operation:

	- Choose the index `i = 1`<span class="example-io">. The resulting array will be `nums = [1,<u>**1**</u>,<u>**1**</u>,<u>**1**</u>]`.</span>

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 1`
