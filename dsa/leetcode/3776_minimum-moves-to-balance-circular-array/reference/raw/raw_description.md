## Description

You are given a **circular** array `balance` of length `n`, where `balance[i]` is the net balance of person `i`.

In one move, a person can transfer **exactly** 1 unit of balance to either their left or right neighbor.

Return the **minimum** number of moves required so that every person has a **non-negative** balance. If it is impossible, return `-1`.

**Note**: You are guaranteed that **at most** 1 index has a **negative** balance initially.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">balance = [5,1,-4]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

One optimal sequence of moves is:

	- Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [5, 0, -3]`

	- Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [4, 0, -2]`

	- Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [3, 0, -1]`

	- Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [2, 0, 0]`

Thus, the minimum number of moves required is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">balance = [1,2,-5,2]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

One optimal sequence of moves is:

	- Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [1, 1, -4, 2]`

	- Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [1, 0, -3, 2]`

	- Move 1 unit from `i = 3` to `i = 2`, resulting in `balance = [1, 0, -2, 1]`

	- Move 1 unit from `i = 3` to `i = 2`, resulting in `balance = [1, 0, -1, 0]`

	- Move 1 unit from `i = 0` to `i = 1`, resulting in `balance = [0, 1, -1, 0]`

	- Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [0, 0, 0, 0]`

Thus, the minimum number of moves required is 6.​​​

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">balance = [-3,2]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

**​​​​​​​**It is impossible to make all balances non-negative for `balance = [-3, 2]`, so the answer is -1.

</div>

**Constraints:**

	- `1 <= n == balance.length <= 10^5`

	- `-10^9 <= balance[i] <= 10^9`

	- There is at most one negative value in `balance` initially.
