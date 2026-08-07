## Description

You are given an integer array `cost` of size `n`. You are currently at position `n` (at the end of the line) in a line of `n + 1` people (numbered from 0 to `n`).

You wish to move forward in the line, but each person in front of you charges a specific amount to **swap** places. The cost to swap with person `i` is given by `cost[i]`.

You are allowed to swap places with people as follows:

	- If they are in front of you, you **must** pay them `cost[i]` to swap with them.

	- If they are behind you, they can swap with you for free.

Return an array `answer` of size `n`, where `answer[i]` is the **minimum** total cost to reach each position `i` in the line<font face="monospace">.</font>

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">cost = [5,3,4,1,3,2]</span>

**Output:** <span class="example-io">[5,3,3,1,1,1]</span>

**Explanation:**

We can get to each position in the following way:

	- `i = 0`. We can swap with person 0 for a cost of 5.

	- <span class="example-io">`<font face="monospace">i = </font>1`. We can swap with person 1 for a cost of 3.</span>

	- <span class="example-io">`i = 2`. We can swap with person 1 for a cost of 3, then swap with person 2 for free.</span>

	- <span class="example-io">`i = 3`. We can swap with person 3 for a cost of 1.</span>

	- <span class="example-io">`i = 4`. We can swap with person 3 for a cost of 1, then swap with person 4 for free.</span>

	- <span class="example-io">`i = 5`. We can swap with person 3 for a cost of 1, then swap with person 5 for free.</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">cost = [1,2,4,6,7]</span>

**Output:** <span class="example-io">[1,1,1,1,1]</span>

**Explanation:**

We can swap with person 0 for a cost of <span class="example-io">1, then we will be able to reach any position `i` for free.</span>

</div>

**Constraints:**

	- `1 <= n == cost.length <= 100`

	- `1 <= cost[i] <= 100`
