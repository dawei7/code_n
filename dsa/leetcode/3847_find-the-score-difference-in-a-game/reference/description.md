## Description

You are given an integer array `nums`, where $\text{nums}[i]$ represents the points scored in the $$i^{\text{th}}$$ game.

There are **exactly **two players. Initially, the first player is **active** and the second player is **inactive**.

The following rules apply **sequentially** for each game `i`:

- If $\text{nums}[i]$ is odd, the active and inactive players swap roles.

- In every 6th game (that is, game indices `5, 11, 17, ...`), the active and inactive players swap roles.

- The active player plays the $$i^{\text{th}}$$ game and gains $\text{nums}[i]$ points.

Return the **score difference**, defined as the first player's **total** score **minus** the second player's **total** score.
### Function Contract

**Inputs**

- `nums`: A nonempty array in which $\text{nums}[i]$ is the positive point value of zero-indexed game $i$.

The active-player state persists between games. An odd point value toggles that state first. A game whose one-based number $i+1$ is divisible by $6$ toggles it second. Therefore, an odd-valued sixth game performs two swaps and leaves the same player active as before that game's rules began.

Let $S_1$ and $S_2$ be the accumulated scores of the first and second players. Exactly one of them receives $\text{nums}[i]$ in each game, after the two swap conditions have been evaluated in the required order.

**Return value**

Return the signed integer difference

$S_1-S_2.$

The result may be negative when the second player finishes with more points.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 0

**Explanation:**​​​​​​​

- Game 0: Since the points are odd, the second player becomes active and gains $\text{nums}[0] = 1$ point.

- Game 1: No swap occurs. The second player gains $\text{nums}[1] = 2$ points.

- Game 2: Since the points are odd, the first player becomes active and gains $\text{nums}[2] = 3$ points.

- The score difference is $3 - 3 = 0$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,4,2,1,2,1]

**Output:** 4

**Explanation:**

- Games 0 to 2: The first player gains $2 + 4 + 2 = 8$ points.

- Game 3: Since the points are odd, the second player is now active and gains $\text{nums}[3] = 1$ point.

- Game 4: The second player gains $\text{nums}[4] = 2$ points.

- Game 5: Since the points are odd, the players swap roles. Then, because this is the 6th game, the players swap again. The second player gains $\text{nums}[5] = 1$ point.

- The score difference is $8 - 4 = 4$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1]

**Output:** -1

**Explanation:**

- Game 0: Since the points are odd, the second player is now active and gains $\text{nums}[0] = 1$ point.

- The score difference is $0 - 1 = -1$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 1000$