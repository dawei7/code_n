## Description

You are given three integers `l`, `r`, and `k`.

Consider all possible integers consisting of **exactly** `k` digits, where each digit is chosen independently from the integer range `[l, r]` (inclusive). If 0 is included in the range, leading zeros are allowed.

Return an integer representing the **sum of all such numbers.**​​​​​​​ Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">l = 1, r = 2, k = 2</span>

**Output:** <span class="example-io">66</span>

**Explanation:**

	- All numbers formed using `k = 2` digits in the range `[1, 2]` are `11, 12, 21, 22`.

	- The total sum is `11 + 12 + 21 + 22 = 66`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">l = 0, r = 1, k = 3</span>

**Output:** <span class="example-io">444</span>

**Explanation:**

	- All numbers formed using `k = 3` digits in the range `[0, 1]` are `000, 001, 010, 011, 100, 101, 110, 111`​​​​​​​.

	- These numbers without leading zeros are `0, 1, 10, 11, 100, 101, 110, 111`.

	- The total sum is 444.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">l = 5, r = 5, k = 10</span>

**Output:** <span class="example-io">555555520</span>

**Explanation:**​​​​​​​

	- 5555555555 is the only valid number consisting of `k = 10` digits in the range `[5, 5]`.

	- The total sum is `5555555555 % (10^9 + 7) = 555555520`.

</div>

**Constraints:**

	- `0 <= l <= r <= 9`

	- `1 <= k <= 10^9`
