## Description

You are given a binary array `possible` of length `n`.

Alice and Bob are playing a game that consists of `n` levels. Some of the levels in the game are **impossible** to clear while others can **always** be cleared. In particular, if `possible[i] == 0`, then the `i^th` level is **impossible** to clear for **both** the players. A player gains `1` point on clearing a level and loses `1` point if the player fails to clear it.

At the start of the game, Alice will play some levels in the **given order** starting from the `0^th` level, after which Bob will play for the rest of the levels.

Alice wants to know the **minimum** number of levels she should play to gain more points than Bob, if both players play optimally to **maximize** their points.

Return *the **minimum** number of levels Alice should play to gain more points*. *If this is **not** possible, return* `-1`.

**Note** that each player must play at least `1` level.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">possible = [1,0,1,0]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Let's look at all the levels that Alice can play up to:

	- If Alice plays only level 0 and Bob plays the rest of the levels, Alice has 1 point, while Bob has -1 + 1 - 1 = -1 point.

	- If Alice plays till level 1 and Bob plays the rest of the levels, Alice has 1 - 1 = 0 points, while Bob has 1 - 1 = 0 points.

	- If Alice plays till level 2 and Bob plays the rest of the levels, Alice has 1 - 1 + 1 = 1 point, while Bob has -1 point.

Alice must play a minimum of 1 level to gain more points.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">possible = [1,1,1,1,1]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

Let's look at all the levels that Alice can play up to:

	- If Alice plays only level 0 and Bob plays the rest of the levels, Alice has 1 point, while Bob has 4 points.

	- If Alice plays till level 1 and Bob plays the rest of the levels, Alice has 2 points, while Bob has 3 points.

	- If Alice plays till level 2 and Bob plays the rest of the levels, Alice has 3 points, while Bob has 2 points.

	- If Alice plays till level 3 and Bob plays the rest of the levels, Alice has 4 points, while Bob has 1 point.

Alice must play a minimum of 3 levels to gain more points.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">possible = [0,0]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

The only possible way is for both players to play 1 level each. Alice plays level 0 and loses 1 point. Bob plays level 1 and loses 1 point. As both players have equal points, Alice can't gain more points than Bob.

</div>

**Constraints:**

	- `2 <= n == possible.length <= 10^5`

	- `possible[i]` is either `0` or `1`.
