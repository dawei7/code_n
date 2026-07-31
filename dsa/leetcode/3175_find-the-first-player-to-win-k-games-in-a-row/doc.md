# Find The First Player to win K Games in a Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3175 |
| Difficulty | Medium |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/) |

## Problem Description
### Goal
A competition has $n$ players, numbered from $0$ through $n-1$. The array `skills` gives each player's skill level, and every skill value is unique. Initially, the players stand in a queue in their index order.

During each game, the first two players compete and the one with the higher skill level wins. The winner remains at the beginning of the queue, while the loser moves to its end. A player's consecutive-win count ends as soon as another player defeats them.

The competition winner is the first player to complete a run of $k$ games in a row. Return that player's index in the original `skills` array. The value of $k$ may be much larger than the number of players, so the process must be resolved without simulating an unbounded number of repeated queue rotations.

### Function Contract
**Inputs**

- `skills`: A list of $n$ unique integers, where `skills[i]` is the skill level of player $i$ and the list order is the initial queue order.
- `k`: The positive number of consecutive games a player must win.

The constraints are $2 \le n \le 10^5$, $1 \le k \le 10^9$, and $1 \le \texttt{skills[i]} \le 10^6$.

**Return value**

Return the initial index of the first player to win $k$ games in a row.

### Examples
**Example 1**

- Input: `skills = [4, 2, 6, 3, 9], k = 2`
- Output: `2`

Player $0$ first beats player $1$, then player $2$ defeats player $0$. Player $2$ next beats player $3$, completing two consecutive wins before player $4$ reaches the front.

**Example 2**

- Input: `skills = [2, 5, 4], k = 3`
- Output: `1`

Player $1$ defeats player $0$, then player $2$, and then player $0$ again, so player $1$ is the first to reach three consecutive wins.
