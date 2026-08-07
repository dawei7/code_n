## Description

You are given a binary string `s` consisting only of characters `'0'` and `'1'`.

A string is **balanced** if it contains an **equal** number of `'0'`s and `'1'`s.

You can perform **at most one** swap between any two characters in `s`. Then, you select a **balanced** <span data-keyword="substring">substring</span> from `s`.

Return an integer representing the **maximum** length of the **balanced** substring you can select.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "100001"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Swap `"10<u>**0**</u>00<u>**1**</u>"`. The string becomes `"101000"`.

	- Select the substring `"<u>**1010**</u>00"`, which is balanced because it has two `'0'`s and two `'1'`s.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "111"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- Choose not to perform any swaps.

	- Select the empty substring, which is balanced because it has zero `'0'`s and zero `'1'`s.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists only of the characters `'0'` and `'1'`.
