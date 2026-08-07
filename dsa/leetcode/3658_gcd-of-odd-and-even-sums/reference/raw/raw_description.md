## Description

You are given an integer `n`. Your task is to compute the **GCD** (greatest common divisor) of two values:

	- `sumOdd`: the sum of the smallest `n` positive odd numbers.

	- `sumEven`: the sum of the smallest `n` positive even numbers.

Return the GCD of `sumOdd` and `sumEven`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Sum of the first 4 odd numbers `sumOdd = 1 + 3 + 5 + 7 = 16`

	- Sum of the first 4 even numbers `sumEven = 2 + 4 + 6 + 8 = 20`

Hence, `GCD(sumOdd, sumEven) = GCD(16, 20) = 4`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- Sum of the first 5 odd numbers `sumOdd = 1 + 3 + 5 + 7 + 9 = 25`

	- Sum of the first 5 even numbers `sumEven = 2 + 4 + 6 + 8 + 10 = 30`

Hence, `GCD(sumOdd, sumEven) = GCD(25, 30) = 5`.

</div>

**Constraints:**

	- `1 <= n <= 10​​​​​​​00`
