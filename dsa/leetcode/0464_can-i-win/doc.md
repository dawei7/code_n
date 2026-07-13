# Can I Win

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 464 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Bit Manipulation, Memoization, Game Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/can-i-win/) |

## Problem Description
### Goal
Two players alternate selecting unused integers from `1` through `maxChoosableInteger`, with the first player moving first. Each selected value is added to a shared running total and then becomes unavailable for the rest of the game.

The player whose choice first makes the total reach or exceed `desiredTotal` wins immediately. Assuming optimal play, return whether the first player can force a win against every response. If the sum of all available integers cannot reach the target, return `False`; if the target is already nonpositive, no selection is needed. The result concerns strategy, not one fixed play sequence.

### Function Contract
**Inputs**

- `maxChoosableInteger`: the available integers are `1` through this value, and each may be chosen once
- `desiredTotal`: the running-total threshold that immediately wins the game

**Return value**

- `True` if the first player has a strategy that wins against every opponent response; otherwise `False`

### Examples
**Example 1**

- Input: `maxChoosableInteger = 10, desiredTotal = 11`
- Output: `False`

**Example 2**

- Input: `maxChoosableInteger = 10, desiredTotal = 0`
- Output: `True`

**Example 3**

- Input: `maxChoosableInteger = 10, desiredTotal = 1`
- Output: `True`

### Required Complexity

- **Time:** $O(m \cdot 2^m)$
- **Space:** $O(2^m)$

<details>
<summary>Approach</summary>

#### General

**Reject or accept arithmetic boundary cases first**

If the target is nonpositive, the first player has already met it. If the sum $1 + \ldots + m$ is below the target, neither player can ever reach it, so the first player cannot win. If the target is at most `m`, the first player chooses it immediately.

**Represent the game state by used choices**

Use one bit per available integer. A set bit means that number has already been chosen. The remaining target is determined by this mask because the running total equals the sum of its chosen numbers, so the same mask always describes the same future game regardless of move order.

**A state wins when one move defeats every continuation**

For each unused choice, the current player wins if that number reaches the remaining target immediately. Otherwise make the choice and evaluate the opponent's resulting state. If the opponent cannot force a win there, the current choice is winning. Only when every legal choice gives the opponent a winning state is the current state losing.

**Memoize shared subgames**

Different move orders can reach the same used-number mask. Cache the win/loss result for that mask so its entire game tree is solved once. This converts repeated permutations of choices into one evaluation per subset while preserving the minimax quantifiers.

#### Complexity detail

There are at most $2^{m}$ masks, and each state examines up to `m` choices, giving $O(m \cdot 2^m)$ time. Cached state results use $O(2^m)$ space, and recursion depth is at most `m`.

#### Alternatives and edge cases

- **Bottom-up subset game DP:** evaluates masks in reverse population order with the same asymptotic bounds but more bookkeeping.
- **Tuple of remaining numbers:** can memoize equivalent subgames but copies and hashes larger state objects than a bitmask.
- **Unmemoized minimax:** recomputes the same subset after different move orders and can grow factorially.
- **Unreachable target:** when the sum of all choices is too small, return `False` before search.
- **Immediate target:** a target no larger than the maximum choice is won in one move.
- **Exact exhaustion:** if all numbers are used without reaching the target, the player to move has no winning choice.
- **Optimal opposition:** finding one plausible sequence is insufficient; a winning move must survive every opponent response encoded by the recursive losing state.

</details>
