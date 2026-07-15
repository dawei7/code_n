# Divisor Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1025 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/divisor-game/) |

## Problem Description

### Goal

Alice and Bob play a turn-based game, with Alice moving first. The chalkboard initially contains the positive integer `n`.

On a turn, the current player must choose an integer `x` such that $0 < x < n$ and `n % x == 0`, then replace the chalkboard number with `n - x`. A player who has no valid move loses.

Return `true` if and only if Alice wins when both players choose their moves optimally.

### Function Contract

**Inputs**

- `n`: the initial chalkboard number, where $1 \le n \le 1000$.

**Return value**

- `true` exactly when Alice can force a win; otherwise, `false`.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `true`
- Explanation: Alice subtracts `1`, leaving `1`; Bob then has no valid move.

**Example 2**

- Input: `n = 3`
- Output: `false`
- Explanation: Alice's only move subtracts `1`. Bob does the same from `2`, leaving Alice unable to move from `1`.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Classify positions by parity:** The number `1` is losing because it has no positive divisor smaller than itself. More generally, every odd divisor of an odd number is odd. Subtracting any valid divisor from an odd `n` therefore produces an even number.

**Give every even position a winning move:** For every even `n > 1`, `1` is a valid divisor. Subtracting it produces the odd number `n - 1`. Thus an even position can always hand the opponent an odd position.

Starting from the losing odd base case `1`, these two observations inductively classify every positive integer: odd positions can move only to even winning positions, while even positions can move to an odd losing position. Alice wins exactly when the initial `n` is even, so testing `n % 2 == 0` is sufficient.

#### Complexity detail

The algorithm performs one parity test regardless of the value of `n`, so it takes $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Bottom-up game-state dynamic programming:** Mark a number winning if it has a divisor leading to a losing smaller state. This directly models optimal play but costs up to $O(n^2)$ time with a simple divisor scan and $O(n)$ space.
- **Recursive minimax with memoization:** Explore legal subtractions until a losing reply is found. Memoization avoids repeated states, but divisor enumeration is unnecessary once the parity structure is proved.
- **Smallest input:** At `n = 1`, Alice has no legal choice and loses.
- **Even boundary:** At `n = 2`, subtracting `1` wins immediately.
- **Optimal-play requirement:** The result asks whether a forced win exists, not whether every legal first move wins.

</details>
