## Description

You are given two integers, `l` and `r`, represented as strings, and an integer `b`. Return the count of integers in the inclusive range `[l, r]` whose digits are in **non-decreasing** order when represented in base `b`.

An integer is considered to have **non-decreasing** digits if, when read from left to right (from the most significant digit to the least significant digit), each digit is greater than or equal to the previous one.

Since the answer may be too large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">l = "23", r = "28", b = 8</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The numbers from 23 to 28 in base 8 are: 27, 30, 31, 32, 33, and 34.

	- Out of these, 27, 33, and 34 have non-decreasing digits. Hence, the output is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">l = "2", r = "7", b = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- The numbers from 2 to 7 in base 2 are: 10, 11, 100, 101, 110, and 111.

	- Out of these, 11 and 111 have non-decreasing digits. Hence, the output is 2.

</div>

**Constraints:**

	- `<font face="monospace">1 <= l.length <= r.length <= 100</font>`

	- `2 <= b <= 10`

	- `l` and `r` consist only of digits.

	- The value represented by `l` is less than or equal to the value represented by `r`.

	- `l` and `r` do not contain leading zeros.
