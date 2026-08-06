## Description

You are given an **0-indexed** integer array `prices` where `prices[i]` denotes the number of coins needed to purchase the `(i + 1)^th` fruit.

The fruit market has the following reward for each fruit:

<ul>
	<li>If you purchase the `(i + 1)^th` fruit at `prices[i]` coins, you can get any number of the next `i` fruits for free.</li>
</ul>

**Note** that even if you **can** take fruit `j` for free, you can still purchase it for `prices[j - 1]` coins to receive its reward.

Return the **minimum** number of coins needed to acquire all the fruits.
