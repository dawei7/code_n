## Description

You are given an integer `n` representing the number of players in a game and a 2D array `pick` where `pick[i] = [x_i, y_i]` represents that the player `x_i` picked a ball of color `y_i`.

Player `i` **wins** the game if they pick **strictly more** than `i` balls of the **same** color. In other words,

	- Player 0 wins if they pick any ball.

	- Player 1 wins if they pick at least two balls of the *same* color.

	- ...

	- Player `i` wins if they pick at least `i + 1` balls of the *same* color.

Return the number of players who **win** the game.

**Note** that *multiple* players can win the game.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Player 0 and player 1 win the game, while players 2 and 3 do not win.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No player wins the game.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Player 2 wins the game by picking 3 balls with color 4.

</div>

**Constraints:**

	- `2 <= n <= 10`

	- `1 <= pick.length <= 100`

	- `pick[i].length == 2`

	- `0 <= x_i <= n - 1 `

	- `0 <= y_i <= 10`
