## Description

Given two integers `n` and `k`, split the number `n` into exactly `k` positive integers such that the **product** of these integers is equal to `n`.

Return *any* *one* split in which the **maximum** difference between any two numbers is **minimized**. You may return the result in *any order*.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 100, k = 2</span>

**Output:** <span class="example-io">[10,10]</span>

**Explanation:**

The split `[10, 10]` yields `10 * 10 = 100` and a max-min difference of 0, which is minimal.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 44, k = 3</span>

**Output:** <span class="example-io">[2,2,11]</span>

**Explanation:**

	- Split `[1, 1, 44]` yields a difference of 43

	- Split `[1, 2, 22]` yields a difference of 21

	- Split `[1, 4, 11]` yields a difference of 10

	- Split `[2, 2, 11]` yields a difference of 9

Therefore, `[2, 2, 11]` is the optimal split with the smallest difference 9.

</div>

**Constraints:**

	- `4 <= n <= 10^<span style="font-size: 10.8333px;">5</span>`

	- `2 <= k <= 5`

	- `k` is strictly less than the total number of positive divisors of `n`.
