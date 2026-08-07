## Description

You are given an integer array `nums` of length `n` and a **positive** integer `k`.

The **power** of an array of integers is defined as the number of <span data-keyword="subsequence-array">subsequences</span> with their sum **equal** to `k`.

Return *the **sum** of **power** of all subsequences of* `nums`*.*

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [1,2,3], k = 3 </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 6 </span>

**Explanation:**

There are `5` subsequences of nums with non-zero power:

	- The subsequence `[<u>**1**</u>,<u>**2**</u>,<u>**3**</u>]` has `2` subsequences with `sum == 3`: `[1,2,<u>3</u>]` and `[<u>1</u>,<u>2</u>,3]`.

	- The subsequence `[<u>**1**</u>,2,<u>**3**</u>]` has `1` subsequence with `sum == 3`: `[1,2,<u>3</u>]`.

	- The subsequence `[1,<u>**2**</u>,<u>**3**</u>]` has `1` subsequence with `sum == 3`: `[1,2,<u>3</u>]`.

	- The subsequence `[<u>**1**</u>,<u>**2**</u>,3]` has `1` subsequence with `sum == 3`: `[<u>1</u>,<u>2</u>,3]`.

	- The subsequence `[1,2,<u>**3**</u>]` has `1` subsequence with `sum == 3`: `[1,2,<u>3</u>]`.

Hence the answer is `2 + 1 + 1 + 1 + 1 = 6`.

</div>

**Example 2:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [2,3,3], k = 5 </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 4 </span>

**Explanation:**

There are `3` subsequences of nums with non-zero power:

	- The subsequence `[<u>**2**</u>,<u>**3**</u>,<u>**3**</u>]` has 2 subsequences with `sum == 5`: `[<u>2</u>,3,<u>3</u>]` and `[<u>2</u>,<u>3</u>,3]`.

	- The subsequence `[<u>**2**</u>,3,<u>**3**</u>]` has 1 subsequence with `sum == 5`: `[<u>2</u>,3,<u>3</u>]`.

	- The subsequence `[<u>**2**</u>,<u>**3**</u>,3]` has 1 subsequence with `sum == 5`: `[<u>2</u>,<u>3</u>,3]`.

Hence the answer is `2 + 1 + 1 = 4`.

</div>

**Example 3:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [1,2,3], k = 7 </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 0 </span>

**Explanation: **There exists no subsequence with sum `7`. Hence all subsequences of nums have `power = 0`.

</div>

**Constraints:**

	- `1 <= n <= 100`

	- `1 <= nums[i] <= 10^4`

	- `1 <= k <= 100`
