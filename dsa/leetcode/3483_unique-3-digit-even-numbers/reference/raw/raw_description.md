## Description

You are given an array of digits called `digits`. Your task is to determine the number of **distinct** three-digit even numbers that can be formed using these digits.

**Note**: Each *copy* of a digit can only be used **once per number**, and there may **not** be leading zeros.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">digits = [1,2,3,4]</span>

**Output:** <span class="example-io">12</span>

**Explanation:** The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">digits = [0,2,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:** The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">digits = [6,6,6]</span>

**Output:** <span class="example-io">1</span>

**Explanation:** Only 666 can be formed.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">digits = [1,3,5]</span>

**Output:** <span class="example-io">0</span>

**Explanation:** No even 3-digit numbers can be formed.

</div>

**Constraints:**

	- `3 <= digits.length <= 10`

	- `0 <= digits[i] <= 9`
