## Description

You are given five integers `cost1`, `cost2`, `costBoth`, `need1`, and `need2`.

There are three types of items available:

	- An item of **type 1** costs `cost1` and contributes 1 unit to the type 1 requirement only.

	- An item of **type 2** costs `cost2` and contributes 1 unit to the type 2 requirement only.

	- An item of **type 3** costs `costBoth` and contributes 1 unit to **both** type 1 and type 2 requirements.

You must collect enough items so that the total contribution toward type 1 is **at least** `need1` and the total contribution toward type 2 is **at least** `need2`.

Return an integer representing the **minimum** possible total cost to achieve these requirements.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

After buying three type 3 items, which cost `3 * 1 = 3`, the total contribution to type 1 is 3 (`>= need1 = 3`) and to type 2 is 3 (`>= need2 = 2`).<br data-end="229" data-start="226" />
Any other valid combination would cost more, so the minimum total cost is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3</span>

**Output:** <span class="example-io">22</span>

**Explanation:**

We buy `need1 = 2` items of type 1 and `need2 = 3` items of type 2: `2 * 5 + 3 * 4 = 10 + 12 = 22`.

Any other valid combination would cost more, so the minimum total cost is 22.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

Since no items are required (`need1 = need2 = 0`), we buy nothing and pay 0.

</div>

**Constraints:**

	- `1 <= cost1, cost2, costBoth <= 10^6`

	- `0 <= need1, need2 <= 10^9`
