### 1. Description

You are playing a variation of the game Zuma.

In this variation of Zuma, there is a **single row** of colored balls on a board, where each ball can be colored red `'R'`, yellow `'Y'`, blue `'B'`, green `'G'`, or white `'W'`. You also have several colored balls in your hand.

Your goal is to **clear all** of the balls from the board. On each turn:

- Pick **any** ball from your hand and insert it in between two balls in the row or on either end of the row.

- If there is a group of **three or more consecutive balls** of the **same color**, remove the group of balls from the board.

		- If this removal causes more groups of three or more of the same color to form, then continue removing each group until there are none left.

- If there are no more balls on the board, then you win the game.

- Repeat this process until you either win or do not have any more balls in your hand.

Given a string `board`, representing the row of balls on the board, and a string `hand`, representing the balls in your hand, return *the **minimum** number of balls you have to insert to clear all the balls from the board. If you cannot clear all the balls from the board using the balls in your hand, return *`-1`.

### 2. Function Contract

**Inputs**

- `board`: Input parameter (`str`).
- `hand`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $board = "WRRBBW", hand = "RB"$
- **Output:** `-1`
- **Explanation:** It is impossible to clear all the balls. The best you can do is:
- Insert 'R' so the board becomes WRR<u>R</u>BBW. W<u>RRR</u>BBW -> WBBW.
- Insert 'B' so the board becomes WBB<u>B</u>W. W<u>BBB</u>W -> WW.
There are still balls remaining on the board, and you are out of balls to insert.

#### Example 2

- **Input:** $board = "WWRRBBWW", hand = "WRBRW"$
- **Output:** `2`
- **Explanation:** To make the board empty:
- Insert 'R' so the board becomes WWRR<u>R</u>BBWW. WW<u>RRR</u>BBWW -> WWBBWW.
- Insert 'B' so the board becomes WWBB<u>B</u>WW. WW<u>BBB</u>WW -> <u>WWWW</u> -> empty.
2 balls from your hand were needed to clear the board.

#### Example 3

- **Input:** $board = "G", hand = "GGGGG"$
- **Output:** `2`
- **Explanation:** To make the board empty:
- Insert 'G' so the board becomes G<u>G</u>.
- Insert 'G' so the board becomes GG<u>G</u>. <u>GGG</u> -> empty.
2 balls from your hand were needed to clear the board.

### 4. Constraints

- $1 \le \text{board.length} \le 16$

- $1 \le \text{hand.length} \le 5$

- `board` and `hand` consist of the characters `'R'`, `'Y'`, `'B'`, `'G'`, and `'W'`.

- The initial row of balls on the board will **not** have any groups of three or more consecutive balls of the same color.
