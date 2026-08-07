## Description

You are given a string `num` which represents a **positive** integer, and an integer `t`.

A number is called **zero-free** if *none* of its digits are 0.

Return a string representing the **smallest** **zero-free** number greater than or equal to `num` such that the **product of its digits** is divisible by `t`. If no such number exists, return `"-1"`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">num = "1234", t = 256</span>

**Output:** <span class="example-io">"1488"</span>

**Explanation:**

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">num = "12355", t = 50</span>

**Output:** <span class="example-io">"12355"</span>

**Explanation:**

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">num = "11111", t = 26</span>

**Output:** <span class="example-io">"-1"</span>

**Explanation:**

No number greater than 11111 has the product of its digits divisible by 26.

</div>

**Constraints:**

	- `2 <= num.length <= 2 * 10^5`

	- `num` consists only of digits in the range `['0', '9']`.

	- `num` does not contain leading zeros.

	- `1 <= t <= 10^14`
