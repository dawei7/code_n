## Description

You are given an integer array `nums`, where `nums[i]` represents the points scored in the `i^th` game.

There are **exactly **two players. Initially, the first player is **active** and the second player is **inactive**.

The following rules apply **sequentially** for each game `i`:

	- If `nums[i]` is odd, the active and inactive players swap roles.

	- In every 6th game (that is, game indices `5, 11, 17, ...`), the active and inactive players swap roles.

	- The active player plays the `i^th` game and gains `nums[i]` points.

Return the **score difference**, defined as the first player's **total** score **minus** the second player's **total** score.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**​​​​​​​

	- Game 0: Since the points are odd, the second player becomes active and gains `nums[0] = 1` point.

	- Game 1: No swap occurs. The second player gains `nums[1] = 2` points.

	- Game 2: Since the points are odd, the first player becomes active and gains `nums[2] = 3` points.

	- The score difference is `3 - 3 = 0`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,4,2,1,2,1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Games 0 to 2: The first player gains `2 + 4 + 2 = 8` points.

	- Game 3: Since the points are odd, the second player is now active and gains `nums[3] = 1` point.

	- Game 4: The second player gains `nums[4] = 2` points.

	- Game 5: Since the points are odd, the players swap roles. Then, because this is the 6th game, the players swap again. The second player gains `nums[5] = 1` point.

	- The score difference is `8 - 4 = 4`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

	- Game 0: Since the points are odd, the second player is now active and gains `nums[0] = 1` point.

	- The score difference is `0 - 1 = -1`.

</div>

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`
