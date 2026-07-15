# Stone Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1406 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/stone-game-iii/) |

## Problem Description

### Goal

Stones are arranged in a row, and `stoneValue[i]` is the possibly negative value of one stone. Alice and Bob alternate turns, with Alice moving first. On a turn, the player removes the first one, two, or three remaining stones and adds their values to their score.

The game ends after every stone has been taken. Both players choose moves optimally. Return `"Alice"` when Alice's final score is greater, `"Bob"` when Bob's is greater, and `"Tie"` when the scores are equal.

### Function Contract

**Inputs**

- `stoneValue`: an array of $n$ integers, where $1 \le n \le 5 \times 10^4$ and $-1000 \le \texttt{stoneValue[i]} \le 1000$.

**Return value**

- `"Alice"`, `"Bob"`, or `"Tie"` according to optimal play and final scores.

### Examples

**Example 1**

- Input: `stoneValue = [1,2,3,7]`
- Output: `"Bob"`

**Example 2**

- Input: `stoneValue = [1,2,3,-9]`
- Output: `"Alice"`

**Example 3**

- Input: `stoneValue = [1,2,3,6]`
- Output: `"Tie"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Measure the advantage of the player to move.** Let `difference[i]` be the greatest score difference current player minus opponent achievable from the suffix beginning at `i`.

If the current player takes one through three stones, accumulate their values as `taken`. Roles swap on the remaining suffix, where `difference[next]` is the next player's advantage. The current move therefore produces `taken - difference[next]`. Store the maximum of the legal choices. The empty suffix has difference zero.

Backward evaluation makes every required later state available. The recurrence tests every legal first move, and subtraction incorporates the opponent's optimal response, so induction over suffix length proves each state is the true optimal advantage. The sign of `difference[0]` directly identifies Alice, Bob, or a tie.

#### Complexity detail

Each of the $n$ suffix states tests at most three moves, giving $O(n)$ time. The difference table uses $O(n)$ space. Because only the next three states are needed, a rolling implementation can reduce auxiliary space to $O(1)$, but the table keeps the recurrence explicit.

#### Alternatives and edge cases

- **Absolute-score DP with suffix totals:** Compute the current player's best score as suffix total minus the opponent's best remainder. It is equivalent, but recomputing every suffix total makes it $O(n^2)$.
- **Minimax without memoization:** Exploring every take sequence repeats suffix states and takes exponential time.
- **Negative stones:** A player must take at least one stone while any remain, so choosing fewer negative values can matter.
- **Take all remaining:** When at most three stones remain, any legal prefix length through the full suffix is considered.
- **Tie:** A zero optimal difference must return `"Tie"`, not either player's name.
- **Greedy local sum:** Taking the largest immediate one-, two-, or three-stone sum can lose because it ignores the opponent's suffix.

</details>
