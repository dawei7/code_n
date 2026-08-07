## Description

You are given a <span data-keyword="circular-array">circular array</span> `balance` of length `n`, where `balance[i]` is the net balance of person `i`.

In one move, a person can transfer **exactly** 1 unit of balance to either their left or right neighbor.

Return the **minimum** number of moves required so that every person has a **non-negative** balance. If it is impossible, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">balance = [-1,2,-1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One optimal sequence of moves is:

	- Move 1 unit from `i = 1` to `i = 0`, resulting in `balance = [0, 1, -1]`

	- Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [0, 0, 0]`

Thus, the minimum number of moves required is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">balance = [4,-1,-2]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

One optimal sequence of moves is:

	- Move 1 unit from `i = 0` to `i = 1`, resulting in `balance = [3, 0, -2]`

	- Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [2, 0, -1]`

	- Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [1, 0, 0]`

Thus, the minimum number of moves required is 3.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">balance = [-3,-3,5]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

It is impossible to make all balances non-negative for `balance = [-3, -3, 5]`, so the answer is -1.

</div>

**Constraints:**

	- `1 <= n == balance.length <= 1000`

	- `-10^5 <= balance[i] <= 10^5`
