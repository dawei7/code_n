# Stone Game IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1510 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-iv/) |

## Problem Description
### Goal

Alice and Bob play a turn-based game on one pile containing $n$ stones, with Alice moving first. On each turn, the current player must remove a non-zero square number of stones: $1,4,9,16,\ldots$, provided that many stones remain.

A player who has no legal move loses. Given the positive initial pile size, determine whether Alice can force a win when both players choose their moves optimally.

### Function Contract
**Inputs**

- `n`: The initial number of stones, satisfying $1 \leq n \leq 10^5$.
- A legal move from a pile of size $s$ removes $k^2$ stones for some positive integer $k$ with $k^2 \leq s$.
- Both players know the full game state and play optimally; there is no randomness or hidden information.

**Return value**

Return `True` exactly when Alice has a strategy that wins from the initial state `n`; otherwise return `False`.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `True`
- Explanation: Alice removes the one stone, leaving Bob with no move.

**Example 2**

- Input: `n = 2`
- Output: `False`
- Explanation: The only move leaves one stone, which Bob removes.

**Example 3**

- Input: `n = 4`
- Output: `True`
- Explanation: Alice removes all four stones in one square-number move.

### Required Complexity

- **Time:** $O(n\sqrt{n})$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Classify states by whether they can reach a losing state**

Define `winning[s]` to mean that the player whose turn begins with $s$ stones can force a win. The empty state is losing because it offers no move, so `winning[0] = False`.

For any positive $s$, the current player may choose a square $q \leq s$ and hand the opponent state $s-q$. If at least one such destination is losing, choosing it guarantees victory, so $s$ is winning. If every legal destination is winning for the opponent, no move avoids defeat and $s$ is losing. This gives the recurrence

$$
\textit{winning}[s] = \bigvee_{q=k^2\leq s} \neg\textit{winning}[s-q].
$$

**Evaluate the recurrence from small piles upward**

Every transition decreases the pile, so when processing `s` in ascending order, all destination states are already known. Precompute the positive squares through $n$. For each pile size, scan legal squares and mark the state winning as soon as one reaches a losing state; otherwise leave it losing.

A byte array stores one Boolean state per pile compactly. The early exit is an implementation improvement, while the worst-case bound still accounts for examining all $\lfloor\sqrt{s}\rfloor$ legal moves at a losing state.

**Why the table models optimal play**

The base state correctly labels a player with no move as losing. Assume every state below $s$ is classified correctly. If the recurrence finds a losing child, the current player can choose that move and force the opponent into a state from which no winning strategy exists. Conversely, if all children are winning, the opponent has a winning response after every possible move, so the current player must lose. Strong induction therefore proves every table entry, including `winning[n]`.

#### Complexity detail

State $s$ has $\lfloor\sqrt{s}\rfloor$ possible square removals. Summing this over all states through $n$ gives

$$
\sum_{s=1}^{n} O(\sqrt{s}) = O(n\sqrt{n}).
$$

Precomputing the square list takes $O(\sqrt n)$ time and space, which is dominated by the $n+1$ Boolean state table. Total auxiliary space is therefore $O(n)$.

#### Alternatives and edge cases

- **Top-down memoized minimax:** recursively evaluate only reached states and cache them. It has the same asymptotic bounds, but a long chain of one-stone moves can exceed the language's recursion limit.
- **Unmemoized recursion:** directly mirrors the game tree but revisits the same pile sizes exponentially many times.
- **Test every removal for squareness:** checking all integers from 1 through each pile size yields a correct but unnecessarily quadratic transition search.
- **Perfect-square pile:** Alice removes the entire pile immediately and wins.
- **One stone:** the only move reaches the losing empty state.
- **Losing state:** every square removal must lead to a winning state; checking only one preferred square is insufficient.
- **No parity shortcut:** both winning and losing states occur among odd and even pile sizes, so parity alone cannot decide the game.
- **Optimal play:** the question asks whether a forced win exists, not whether some arbitrary sequence lets Alice win.
- **Upper bound:** iterative storage avoids recursion-depth failure at $n=10^5$.

</details>
