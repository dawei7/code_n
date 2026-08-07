## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	- Open brackets must be closed by the same type of brackets.

	- Open brackets must be closed in the correct order.

	- Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "()"</span>

**Output:** <span class="example-io">true</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "()[]{}"</span>

**Output:** <span class="example-io">true</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "(]"</span>

**Output:** <span class="example-io">false</span>

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "([])"</span>

**Output:** <span class="example-io">true</span>

</div>

**Example 5:**

<div class="example-block">
**Input:** <span class="example-io">s = "([)]"</span>

**Output:** <span class="example-io">false</span>

</div>

**Constraints:**

	- `1 <= s.length <= 10^4`

	- `s` consists of parentheses only `'()[]{}'`.
