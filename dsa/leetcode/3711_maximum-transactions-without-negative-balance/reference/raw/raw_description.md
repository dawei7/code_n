## Description

You are given an integer array `transactions`, where `transactions[i]` represents the amount of the `i^th` transaction:

	- A positive value means money is **received**.

	- A negative value means money is **sent**.

The account starts with a balance of 0, and the balance **must never become negative**. Transactions must be considered in the given order, but you are allowed to skip some transactions.

Return an integer denoting the **maximum number of transactions** that can be performed without the balance ever going negative.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">transactions = [2,-5,3,-1,-2]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

One optimal sequence is `[2, 3, -1, -2]`, balance: `0 → 2 → 5 → 4 → 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">transactions = [-1,-2,-3]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

All transactions are negative. Including any would make the balance negative.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">transactions = [3,-2,3,-2,1,-1]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

All transactions can be taken in order, balance: `0 → 3 → 1 → 4 → 2 → 3 → 2`.

</div>

**Constraints:**

	- `1 <= transactions.length <= 10^5`

	- `-10^9 <= transactions[i] <= 10^9`
