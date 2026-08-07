## Description

You are given two integers `n` and `m`.

You have to select a multiset of **<span data-keyword="prime-number">prime numbers</span>** from the **first** `m` prime numbers such that the sum of the selected primes is **exactly** `n`. You may use each prime number **multiple** times.

Return the **minimum** number of prime numbers needed to sum up to `n`, or -1 if it is not possible.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 10, m = 2</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The first 2 primes are [2, 3]. The sum 10 can be formed as 2 + 2 + 3 + 3, requiring 4 primes.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 15, m = 5</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The first 5 primes are [2, 3, 5, 7, 11]. The sum 15 can be formed as 5 + 5 + 5, requiring 3 primes.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 7, m = 6</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The first 6 primes are [2, 3, 5, 7, 11, 13]. The sum 7 can be formed directly by prime 7, requiring only 1 prime.

</div>

**Constraints:**

	- `1 <= n <= 1000`

	- `1 <= m <= 1000`
