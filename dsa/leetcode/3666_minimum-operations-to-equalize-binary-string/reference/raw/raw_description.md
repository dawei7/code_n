## Description

You are given a binary string `s`, and an integer `k`.

In one operation, you must choose **exactly** `k` **different** indices and **flip** each `'0'` to `'1'` and each `'1'` to `'0'`.

Return the **minimum** number of operations required to make all characters in the string equal to `'1'`. If it is not possible, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "110", k = 1</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- There is one `'0'` in `s`.

	- Since `k = 1`, we can flip it directly in one operation.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "0101", k = 3</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One optimal set of operations choosing `k = 3` indices in each operation is:

	- **Operation 1**: Flip indices `[0, 1, 3]`. `s` changes from `"0101"` to `"1000"`.

	- **Operation 2**: Flip indices `[1, 2, 3]`. `s` changes from `"1000"` to `"1111"`.

Thus, the minimum number of operations is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "101", k = 2</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

Since `k = 2` and `s` has only one `'0'`, it is impossible to flip exactly `k` indices to make all `'1'`. Hence, the answer is -1.

</div>

**Constraints:**

	- `1 <= s.length <= 10^​​​​​​​5`

	- `s[i]` is either `'0'` or `'1'`.

	- `1 <= k <= s.length`
