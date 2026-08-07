## Description

You are given two integer arrays of size 2: `d = [d_1, d_2]` and `r = [r_1, r_2]`.

Two delivery drones are tasked with completing a specific number of deliveries. Drone `i` must complete `d_i` deliveries.

Each delivery takes **exactly** one hour and **only one** drone can make a delivery at any given hour.

Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone `i` must recharge every `r_i` hours (i.e. at hours that are multiples of `r_i`).

Return an integer denoting the **minimum** total time (in hours) required to complete all deliveries.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">d = [3,1], r = [2,3]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- The first drone delivers at hours 1, 3, 5 (recharges at hours 2, 4).

	- The second drone delivers at hour 2 (recharges at hour 3).

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">d = [1,3], r = [2,2]</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

	- The first drone delivers at hour 3 (recharges at hours 2, 4, 6).

	- The second drone delivers at hours 1, 5, 7 (recharges at hours 2, 4, 6).

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">d = [2,1], r = [3,4]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The first drone delivers at hours 1, 2 (recharges at hour 3).

	- The second drone delivers at hour 3.

</div>

**Constraints:**

	- `d = [d_1, d_2]`

	- `1 <= d_i <= 10^9`

	- `r = [r_1, r_2]`

	- `2 <= r_i <= 3 * 10^4`
