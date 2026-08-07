## Description

You have `n` data centers and need to upgrade their servers.

You are given four arrays `count`, `upgrade`, `sell`, and `money` of length `n`, which show:

	- The number of servers

	- The cost of upgrading a single server

	- The money you get by selling a server

	- The money you initially have

for each data center respectively.

Return an array `answer`, where for each data center, the corresponding element in `answer` represents the **maximum** number of servers that can be upgraded.

Note that the money from one data center **cannot** be used for another data center.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">count = [4,3], upgrade = [3,5], sell = [4,2], money = [8,9]</span>

**Output:** <span class="example-io">[3,2]</span>

**Explanation:**

For the first data center, if we sell one server, we'll have `8 + 4 = 12` units of money and we can upgrade the remaining 3 servers.

For the second data center, if we sell one server, we'll have `9 + 2 = 11` units of money and we can upgrade the remaining 2 servers.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">count = [1], upgrade = [2], sell = [1], money = [1]</span>

**Output:** <span class="example-io">[0]</span>

</div>

**Constraints:**

	- `1 <= count.length == upgrade.length == sell.length == money.length <= 10^5`

	- `1 <= count[i], upgrade[i], sell[i], money[i] <= 10^5`
