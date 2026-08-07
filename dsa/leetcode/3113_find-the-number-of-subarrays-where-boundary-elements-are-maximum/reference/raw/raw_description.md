## Description

You are given an array of **positive** integers `nums`.

Return the number of <span data-keyword="subarray-nonempty">subarrays</span> of `nums`, where the **first** and the **last** elements of the subarray are *equal* to the **largest** element in the subarray.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,3,3,2]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

	- subarray `[**<u>1</u>**,4,3,3,2]`, with its largest element 1. The first element is 1 and the last element is also 1.

	- subarray `[1,<u>**4**</u>,3,3,2]`, with its largest element 4. The first element is 4 and the last element is also 4.

	- subarray `[1,4,<u>**3**</u>,3,2]`, with its largest element 3. The first element is 3 and the last element is also 3.

	- subarray `[1,4,3,<u>**3**</u>,2]`, with its largest element 3. The first element is 3 and the last element is also 3.

	- subarray `[1,4,3,3,<u>**2**</u>]`, with its largest element 2. The first element is 2 and the last element is also 2.

	- subarray `[1,4,<u>**3,3**</u>,2]`, with its largest element 3. The first element is 3 and the last element is also 3.

Hence, we return 6.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,3,3]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

	- subarray `[<u>**3**</u>,3,3]`, with its largest element 3. The first element is 3 and the last element is also 3.

	- subarray `[3,**<u>3</u>**,3]`, with its largest element 3. The first element is 3 and the last element is also 3.

	- subarray `[3,3,<u>**3**</u>]`, with its largest element 3. The first element is 3 and the last element is also 3.

	- subarray `[**<u>3,3</u>**,3]`, with its largest element 3. The first element is 3 and the last element is also 3.

	- subarray `[3,<u>**3,3**</u>]`, with its largest element 3. The first element is 3 and the last element is also 3.

	- subarray `[<u>**3,3,3**</u>]`, with its largest element 3. The first element is 3 and the last element is also 3.

Hence, we return 6.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

There is a single subarray of `nums` which is `[**<u>1</u>**]`, with its largest element 1. The first element is 1 and the last element is also 1.

Hence, we return 1.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`
