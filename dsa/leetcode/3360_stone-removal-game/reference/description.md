### 1. Description

Alice and Bob are playing a game where they take turns removing stones from a pile, with *Alice going first*.

- Alice starts by removing **exactly** 10 stones on her first turn.

- For each subsequent turn, each player removes **exactly** 1 fewer** **stone** **than the previous opponent.

The player who cannot make a move loses the game.

Given a positive integer `n`, return `true` if Alice wins the game and `false` otherwise.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 12

**Output:** true

**Explanation:**

- Alice removes 10 stones on her first turn, leaving 2 stones for Bob.

- Bob cannot remove 9 stones, so Alice wins.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 1

**Output:** false

**Explanation:**

- Alice cannot remove 10 stones, so Alice loses.

</div>

### 4. Constraints

- $1 \le n \le 50$