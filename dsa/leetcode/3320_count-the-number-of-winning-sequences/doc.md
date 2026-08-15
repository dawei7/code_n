# Count The Number of Winning Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3320 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-winning-sequences/) |

## Problem Description

### Goal

Alice and Bob play $n$ simultaneous battle rounds. In each round they summon Fire (`F`), Water (`W`), or Earth (`E`). Water defeats Fire, Earth defeats Water, and Fire defeats Earth. The winner of a round receives one point; matching creatures give neither player a point.

The string `s` fixes Alice's entire sequence. Count the distinct length-$n$ sequences Bob can choose such that he never uses the same creature in two consecutive rounds and finishes with strictly more points than Alice. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: Alice's sequence of 1 to 1000 characters, each equal to `F`, `W`, or `E`.

**Return value**

Return, modulo $1{,}000{,}000{,}007$, the number of Bob sequences satisfying the adjacent-move restriction and ending with a strictly positive score advantage.

### Examples

#### Example 1

- **Input:** `s = "FFF"`
- **Output:** `3`

The winning legal sequences are `WFW`, `FWF`, and `WEW`; sequences with adjacent repeated moves are forbidden.

#### Example 2

- **Input:** `s = "FWEFW"`
- **Output:** `18`

#### Example 3

- **Input:** `s = "F"`
- **Output:** `1`

Only Water gives Bob a positive score in the single round.
