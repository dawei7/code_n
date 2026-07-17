# Stone Game VII

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1690 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-vii/) |

## Problem Description
### Goal

Alice and Bob play with a row of $n$ stones whose positive values appear in `stones` from left to right. Alice moves first, and the players alternate turns. A move removes exactly one endpoint: either the current leftmost stone or the current rightmost stone. The moving player then earns the sum of the values that remain in the row, rather than the value of the removed stone.

Play continues until the row is empty. Alice chooses moves to maximize the final difference between her score and Bob's, while Bob chooses moves to minimize that same difference; both play optimally. Return Alice's final score minus Bob's final score. The last removal earns zero points because no stones remain afterward.

### Function Contract
**Inputs**

- `stones`: a list of $n$ positive integers in their left-to-right order, where $2 \le n \le 1000$ and each value is at most $1000$

**Return value**

Alice's score minus Bob's score when both players choose optimally.

### Examples
**Example 1**

- Input: `stones = [5, 3, 1, 4, 2]`
- Output: `6`

Alice can finish with 18 points against Bob's 12. Every turn accounts for the sum after the chosen endpoint has been removed.

**Example 2**

- Input: `stones = [7, 90, 5, 1, 100, 10, 10, 2]`
- Output: `122`

**Example 3**

- Input: `stones = [1, 2]`
- Output: `2`

Alice removes the value `1`, scores the remaining value `2`, and Bob's final removal scores zero.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Describe a position by its current player's advantage**

After several endpoint removals, the remaining stones always form one interval. For an interval from `left` through `right`, let its state value be the greatest score advantage the player about to move can force over the other player. This definition absorbs both Alice's maximizing turns and Bob's minimizing turns: after the move, the opponent becomes the current player and can earn their own optimal advantage.

If the left endpoint is removed, the immediate score is the sum from `left + 1` through `right`. The opponent then controls that smaller interval, so subtract the opponent's stored advantage. Removing the right endpoint is symmetric. Therefore the current state is the larger of

$$
\begin{aligned}
\operatorname{sum}(\texttt{left}+1,\texttt{right})-\operatorname{dp}(\texttt{left}+1,\texttt{right}),\\
\operatorname{sum}(\texttt{left},\texttt{right}-1)-\operatorname{dp}(\texttt{left},\texttt{right}-1).
\end{aligned}
$$

A one-stone interval has value zero because its only move leaves an empty row. Building intervals from shorter to longer makes both successor states available. Prefix sums provide every remaining-interval sum in constant time.

**Compress adjacent interval lengths into one array**

Store the previous interval length in `advantage[left]`. For a new interval ending at `right`, the left-removal transition reads `advantage[left + 1]`, while the right-removal transition reads the old `advantage[left]`. Process `left` in ascending order: updating one cell cannot overwrite the still-needed old value at the next cell. Once all lengths have been processed, `advantage[0]` is the optimal difference for the whole row.

Each transition considers every legal first move. It combines the points earned now with the negated optimal advantage of the exact position left to the opponent, so induction on interval length establishes that every stored value is the correct minimax difference.

#### Complexity detail

There are $O(n^2)$ intervals and each transition uses constant-time prefix-sum queries, giving $O(n^2)$ time. The prefix sums and one rolling DP row each use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Two-dimensional interval table:** storing every `dp[left][right]` makes the recurrence visually direct but uses $O(n^2)$ space without improving the $O(n^2)$ time bound.
- **Recompute each remaining sum:** summing an interval inside every transition is correct but raises the running time to $O(n^3)$.
- **Recursive minimax without memoization:** exploring both endpoint choices repeatedly takes exponential time because the same intervals recur along many play sequences.
- **Greedy endpoint removal:** choosing the larger or smaller endpoint ignores how that removal changes both the immediate remaining sum and the opponent's future choices.
- **Two stones:** Alice removes the smaller endpoint so that the larger value remains as her score; Bob's last move scores zero.
- **Equal values:** ties between the two transitions are harmless; either endpoint produces the same optimal state value.
- **Update direction:** the rolling array must be updated from smaller to larger left indices so `advantage[left + 1]` still represents the previous interval length.

</details>
