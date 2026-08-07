## Description

You are given an integer array `weights` and two integers `w1` and `w2` representing the **maximum** capacities of two bags.

Each item may be placed in **at most** one bag such that:

	- Bag 1 holds **at most** `w1` total weight.

	- Bag 2 holds **at most** `w2` total weight.

Return the **maximum** total weight that can be packed into the two bags.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">weights = [1,4,3,2], w1 = 5, w2 = 4</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

	- Bag 1: Place `weights[2] = 3` and `weights[3] = 2` as `3 + 2 = 5 <= w1`

	- Bag 2: Place `weights[1] = 4` as `4 <= w2`

	- Total weight: `5 + 4 = 9`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">weights = [3,6,4,8], w1 = 9, w2 = 7</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

	- Bag 1: Place `weights[3] = 8` as `8 <= w1`

	- Bag 2: Place `weights[0] = 3` and `weights[2] = 4` as `3 + 4 = 7 <= w2`

	- Total weight: `8 + 7 = 15`

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">weights = [5,7], w1 = 2, w2 = 3</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No weight fits in either bag, thus the answer is 0.

</div>

**Constraints:**

	- `1 <= weights.length <= 100`

	- `1 <= weights[i] <= 100`

	- `1 <= w1, w2 <= 300`
