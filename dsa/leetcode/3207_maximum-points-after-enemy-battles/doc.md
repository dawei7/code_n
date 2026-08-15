# Maximum Points After Enemy Battles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3207 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-points-after-enemy-battles/) |

## Problem Description

### Goal

`enemyEnergies` gives the energy values of several enemies. Initially, every enemy is unmarked, the score is zero, and the available energy is `currentEnergy`.

Any unmarked enemy may be used repeatedly to gain one point whenever the current energy is at least that enemy's value; doing so subtracts its value from the current energy but does not mark it. Separately, once at least one point has been earned, an unmarked enemy may be marked to add its energy value to the current energy. Marking an enemy does not spend a point, but that enemy can no longer be selected by either operation.

Perform either operation any number of times in any valid order. Return the largest final point total.

### Function Contract

**Inputs**

- `enemyEnergies`: A nonempty list of enemy energy values, with $1 \le \lvert\texttt{enemyEnergies}\rvert \le 10^5$ and $1 \le \texttt{enemyEnergies}[i] \le 10^9$.
- `currentEnergy`: The initial energy, where $0 \le \texttt{currentEnergy} \le 10^9$.

Let $n=\lvert\texttt{enemyEnergies}\rvert$.

**Return value**

- The maximum number of points obtainable through valid scoring and marking operations.

### Examples

#### Example 1

- **Input:** `enemyEnergies = [3,2,2], currentEnergy = 2`
- **Output:** `3`
- **Explanation:** Score once against a value-`2` enemy, mark the value-`3` enemy for energy, score again, mark the other value-`2` enemy, and score a third time using the still-unmarked minimum enemy.

#### Example 2

- **Input:** `enemyEnergies = [2], currentEnergy = 10`
- **Output:** `5`
- **Explanation:** The only enemy can remain unmarked while its energy cost is paid five times.
