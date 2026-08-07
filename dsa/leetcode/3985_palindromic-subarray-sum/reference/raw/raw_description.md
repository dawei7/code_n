## Description

You are given an integer array `nums`.

Return the maximum possible sum of a <span data-keyword="subarray-nonempty">subarray</span> of `nums` that is a <span data-keyword="palindrome-array">palindrome</span>.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,10]</span>

**Output:** <span class="example-io">20</span>

**Explanation:**

The whole array `[10,10]` is a palindrome. Therefore, the maximum sum is `10 + 10 = 20`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,2,1,5,6]</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

The contiguous subarray `[1,2,3,2,1]` is a palindrome. Its sum is `1 + 2 + 3 + 2 + 1 = 9` and it is the maximum sum.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,1,2,1,7,3,4,3,4]</span>

**Output:** <span class="example-io">18</span>

**Explanation:**

The contiguous subarray `[7,1,2,1,7]` is a palindrome. Its sum is `7 + 1 + 2 + 1 + 7 = 18` and it is the maximum sum.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

No subarray with length greater than 1 is a palindrome. The largest element in the array is 5. Therefore, the answer is 5.

</div>

**Example 5:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1000]</span>

**Output:** <span class="example-io">1000</span>

**Explanation:**

The subarray with only one element is a palindrome. Therefore, the answer is 1000.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^​​​​​​​9`
