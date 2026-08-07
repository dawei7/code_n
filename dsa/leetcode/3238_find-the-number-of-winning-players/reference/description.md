## Description

You are given an integer `n` representing the number of players in a game and a 2D array `pick` where $\text{pick}[i] = [x_{i}, y_{i}]$ represents that the player $x_{i}$ picked a ball of color $y_{i}$.

Player `i` **wins** the game if they pick **strictly more** than `i` balls of the **same** color. In other words,

- Player 0 wins if they pick any ball.

- Player 1 wins if they pick at least two balls of the *same* color.

- ...

- Player `i` wins if they pick at least $i + 1$ balls of the *same* color.

Return the number of players who **win** the game.

**Note** that *multiple* players can win the game.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]

**Output:** 2

**Explanation:**

Player 0 and player 1 win the game, while players 2 and 3 do not win.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]

**Output:** 0

**Explanation:**

No player wins the game.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]

**Output:** 1

**Explanation:**

Player 2 wins the game by picking 3 balls with color 4.

</div>
### Constraints

- $2 \le n \le 10$

- $1 \le \text{pick.length} \le 100$

- $\text{pick}[i].length = 2$

- $0 \le x_{i} \le n - 1$

- $0 \le y_{i} \le 10$