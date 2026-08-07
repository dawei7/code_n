## Description

You are given an integer array `digitSum` of length `n`.

An array `arr` of length `n` is considered **valid** if:

	- `0 <= arr[i] <= 5000`

	- it is **non-decreasing**.

	- the **sum of the digits** of `arr[i]` **equals** `digitSum[i]`.

Return an integer denoting the number of **distinct valid arrays**. Since the answer may be large, return it modulo `10^9 + 7`.

An array is said to be **non-decreasing** if each element is greater than or equal to the previous element, if it exists.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">digitSum = [25,1]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

Numbers whose sum of digits is 25 are 799, 889, 898, 979, 988, and 997.

The only number whose sum of digits is 1 that can appear after these values while keeping the array non-decreasing is 1000.

Thus, the valid arrays are `[799, 1000]`, `[889, 1000]`, `[898, 1000]`, `[979, 1000]`, `[988, 1000]`, and `[997, 1000]`.

Hence, the answer is 6.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">digitSum = [1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The valid arrays are `[1]`, `[10]`, `[100]`, and `[1000]`.

Thus, the answer is 4.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">digitSum = [2,49,23]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There is no integer in the range [0, 5000] whose sum of digits is 49. Thus, the answer is 0.

</div>

**Constraints:**

	- `1 <= digitSum.length <= 1000`

	- `0 <= digitSum[i] <= 50`
