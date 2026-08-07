## Description

You are given two integer arrays `costs` and `capacity`, both of length `n`, where `costs[i]` represents the purchase cost of the `i^th` machine and `capacity[i]` represents its performance capacity.

You are also given an integer `budget`.

You may select **at most two distinct** machines such that the **total cost** of the selected machines is **strictly less** than `budget`.

Return the **maximum** achievable total capacity of the selected machines.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

	- Choose two machines with `costs[0] = 4` and `costs[3] = 3`.

	- The total cost is `4 + 3 = 7`, which is strictly less than `budget = 8`.

	- The maximum total capacity is `capacity[0] + capacity[3] = 1 + 7 = 8`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">costs = [3,5,7,4], capacity = [2,4,3,6], budget = 7</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- Choose one machine with `costs[3] = 4`.

	- The total cost is 4, which is strictly less than `budget = 7`.

	- The maximum total capacity is `capacity[3] = 6`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">costs = [2,2,2], capacity = [3,5,4], budget = 5</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

	- Choose two machines with `costs[1] = 2` and `costs[2] = 2`.

	- The total cost is `2 + 2 = 4`, which is strictly less than `budget = 5`.

	- The maximum total capacity is `capacity[1] + capacity[2] = 5 + 4 = 9`.

</div>

**Constraints:**

	- `1 <= n == costs.length == capacity.length <= 10^5`

	- `1 <= costs[i], capacity[i] <= 10^5`

	- `1 <= budget <= 2 * 10^5`
