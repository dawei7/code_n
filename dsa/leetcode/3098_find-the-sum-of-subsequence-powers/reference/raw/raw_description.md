## Description

You are given an integer array `nums` of length `n`, and a **positive** integer `k`.

The **power** of a <span data-keyword="subsequence-array">subsequence</span> is defined as the **minimum** absolute difference between **any** two elements in the subsequence.

Return *the **sum** of **powers** of **all** subsequences of *`nums`* which have length* ***equal to*** `k`.

Since the answer may be large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4], k = 3</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

There are 4 subsequences in `nums` which have length 3: `[1,2,3]`, `[1,3,4]`, `[1,2,4]`, and `[2,3,4]`. The sum of powers is `|2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2], k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The only subsequence in `nums` which has length 2 is `[2,2]`. The sum of powers is `|2 - 2| = 0`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,-1], k = 2</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

There are 3 subsequences in `nums` which have length 2: `[4,3]`, `[4,-1]`, and `[3,-1]`. The sum of powers is `|4 - 3| + |4 - (-1)| + |3 - (-1)| = 10`.

</div>

**Constraints:**

	- `2 <= n == nums.length <= 50`

	- `-10^8 <= nums[i] <= 10^8 `

	- `2 <= k <= n`
