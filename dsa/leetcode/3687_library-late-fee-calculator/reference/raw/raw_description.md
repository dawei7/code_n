## Description

You are given an integer array `daysLate` where `daysLate[i]` indicates how many days late the `i^th` book was returned.

The penalty is calculated as follows:

	- If `daysLate[i] == 1`, penalty is 1.

	- If `2 <= daysLate[i] <= 5`, penalty is `2 * daysLate[i]`.

	- If `daysLate[i] > 5`, penalty is `3 * daysLate[i]`.

Return the total penalty for all books.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">daysLate = [5,1,7]</span>

**Output:** <span class="example-io">32</span>

**Explanation:**

	- `daysLate[0] = 5`: Penalty is `2 * daysLate[0] = 2 * 5 = 10`.

	- `daysLate[1] = 1`: Penalty is `1`.

	- `daysLate[2] = 7`: Penalty is `3 * daysLate[2] = 3 * 7 = 21`.

	- Thus, the total penalty is `10 + 1 + 21 = 32`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">daysLate = [1,1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- `daysLate[0] = 1`: Penalty is `1`.

	- `daysLate[1] = 1`: Penalty is `1`.

	- Thus, the total penalty is `1 + 1 = 2`.

</div>

**Constraints:**

	- `1 <= daysLate.length <= 100`

	- `1 <= daysLate[i] <= 100`
