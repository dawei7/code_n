## Description

You are given an integer array `coins` representing coins of different denominations and an integer `k`.

You have an infinite number of coins of each denomination. However, you are **not allowed** to combine coins of different denominations.

Return the `k^th` **smallest** amount that can be made using these coins.

**Example 1:**

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:** <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">coins = [3,6,9], k = 3</span>

**Output:** <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> 9</span>

**Explanation:** The given coins can make the following amounts:

Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.

Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.

Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.

All of the coins combined produce: 3, 6, <u>**9**</u>, 12, 15, etc.

</div>

**Example 2:**

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:**<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> coins = [5,2], k = 7</span>

**Output:**<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> 12 </span>

**Explanation:** The given coins can make the following amounts:

Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.

Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.

All of the coins combined produce: 2, 4, 5, 6, 8, 10, <u>**12**</u>, 14, 15, etc.

</div>

**Constraints:**

	- `1 <= coins.length <= 15`

	- `1 <= coins[i] <= 25`

	- `1 <= k <= 2 * 10^9`

	- `coins` contains pairwise distinct integers.
