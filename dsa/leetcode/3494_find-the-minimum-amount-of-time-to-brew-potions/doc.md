# Find the Minimum Amount of Time to Brew Potions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3494 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/) |

## Problem Description

### Goal

A laboratory has $n$ wizards arranged in a fixed order and $m$ potions that must also be brewed in their given order. Potion $j$ has mana capacity `mana[j]`. It visits every wizard from index $0$ through $n-1$, and wizard $i$ needs `skill[i] * mana[j]` units of time to work on it. A wizard can work on only one potion at a time.

Each potion follows a no-wait rule: when one wizard finishes it, the next wizard must begin that same potion immediately. The start times therefore have to synchronize the whole pipeline; delaying a potion between two wizards is forbidden even when that delay would otherwise avoid a conflict. Determine the earliest time at which every potion has completed the entire sequence of wizards.

### Function Contract

**Inputs**

- `skill`: A list of $n$ positive integers giving each wizard's skill multiplier.
- `mana`: A list of $m$ positive integers giving the potions' mana capacities in required brewing order.

The dimensions satisfy $1\le n,m\le5000$, and every value in either list is between $1$ and $5000$.

**Return value**

Return the minimum time required to finish all $m$ potions.

### Examples

#### Example 1

- **Input:** `skill = [1,5,2,4], mana = [5,1,4,2]`
- **Output:** `110`
- **Explanation:** The four potions can start at times `0`, `52`, `54`, and `86`; the last potion leaves the final wizard at time `110`.

#### Example 2

- **Input:** `skill = [1,1,1], mana = [1,1,1]`
- **Output:** `5`
- **Explanation:** Starting the potions at times `0`, `1`, and `2` keeps the three-wizard pipeline continuously synchronized.

#### Example 3

- **Input:** `skill = [1,2,3,4], mana = [1,2]`
- **Output:** `21`
