## Description

You are given a string `num` consisting of only digits. A string of digits is called **balanced **if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return `true` if `num` is **balanced**, otherwise return `false`.

**Example 1:**

<div class="example-block">
**Input:** num<span class="example-io"> = "1234"</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

	- The sum of digits at even indices is `1 + 3 == 4`, and the sum of digits at odd indices is `2 + 4 == 6`.

	- Since 4 is not equal to 6, `num` is not balanced.

</div>

**Example 2:**

<div class="example-block">
**Input:** num<span class="example-io"> = "24123"</span>

**Output:** true

**Explanation:**

	- The sum of digits at even indices is `2 + 1 + 3 == 6`, and the sum of digits at odd indices is `4 + 2 == 6`.

	- Since both are equal the `num` is balanced.

</div>

**Constraints:**

	- `2 <= num.length <= 100`

	- `<font face="monospace">num</font>` consists of digits only
