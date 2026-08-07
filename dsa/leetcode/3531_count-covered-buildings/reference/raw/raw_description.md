## Description

You are given a positive integer `n`, representing an `n x n` city. You are also given a 2D grid `buildings`, where `buildings[i] = [x, y]` denotes a **unique** building located at coordinates `[x, y]`.

A building is **covered** if there is at least one building in all **four** directions: left, right, above, and below.

Return the number of **covered** buildings.

**Example 1:**

![](images/telegram-cloud-photo-size-5-6212982906394101085-m.jpg)

<div class="example-block">
**Input:** <span class="example-io">n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Only building `[2,2]` is covered as it has at least one building:

		<li>above (`[1,2]`)

		- below (`[3,2]`)

		- left (`[2,1]`)

		- right (`[2,3]`)

	</li>
	- Thus, the count of covered buildings is 1.

</div>

**Example 2:**

![](images/telegram-cloud-photo-size-5-6212982906394101086-m.jpg)

<div class="example-block">
**Input:** <span class="example-io">n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- No building has at least one building in all four directions.

</div>

**Example 3:**

![](images/telegram-cloud-photo-size-5-6248862251436067566-x.jpg)

<div class="example-block">
**Input:** <span class="example-io">n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Only building `[3,3]` is covered as it has at least one building:

		<li>above (`[1,3]`)

		- below (`[5,3]`)

		- left (`[3,2]`)

		- right (`[3,5]`)

	</li>
	- Thus, the count of covered buildings is 1.

</div>

**Constraints:**

	- `2 <= n <= 10^5`

	- `1 <= buildings.length <= 10^5 `

	- `buildings[i] = [x, y]`

	- `1 <= x, y <= n`

	- All coordinates of `buildings` are **unique**.
