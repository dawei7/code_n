## Description

You are given a string array `numbers` that represents phone numbers. Return `true` if no phone number is a prefix of any other phone number; otherwise, return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">numbers = ["1","2","4","3"]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

No number is a prefix of another number, so the output is `true`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">numbers = ["001","007","15","00153"]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

The string `"001"` is a prefix of the string `"00153"`. Thus, the output is `false`.

</div>

**Constraints:**

	- `2 <= numbers.length <= 50`

	- `1 <= numbers[i].length <= 50`

	- All numbers contain only digits `'0'` to `'9'`.
