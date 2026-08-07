## Description

You are given two **0-indexed** integer arrays `<font face="monospace">player1</font>` and `player2`, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of `n` turns, and the number of pins in each turn is exactly 10.

Assume a player hits `x_i` pins in the i^th turn. The value of the i^th turn for the player is:

	- `2x_i` if the player hits 10 pins **in either (i - 1)^th or (i - 2)^th turn**.

	- Otherwise, it is `x_i`.

The **score** of the player is the sum of the values of their `n` turns.

Return

	- 1 if the score of player 1 is more than the score of player 2,

	- 2 if the score of player 2 is more than the score of player 1, and

	- 0 in case of a draw.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">player1 = [5,10,3,2], player2 = [6,5,7,3]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25.

The score of player 2 is 6 + 5 + 7 + 3 = 21.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">player1 = [3,5,7,6], player2 = [8,10,10,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The score of player 1 is 3 + 5 + 7 + 6 = 21.

The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">player1 = [2,3], player2 = [4,1]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The score of player1 is 2 + 3 = 5.

The score of player2 is 4 + 1 = 5.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73.

The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.

</div>

**Constraints:**

	- `n == player1.length == player2.length`

	- `1 <= n <= 1000`

	- `0 <= player1[i], player2[i] <= 10`
