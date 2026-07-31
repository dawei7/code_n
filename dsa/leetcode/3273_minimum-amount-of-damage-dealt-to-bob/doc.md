# Minimum Amount of Damage Dealt to Bob

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3273 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/) |

## Problem Description

### Goal

Bob faces `n` enemies. While enemy `i` remains alive, it deals `damage[i]` points to Bob at the beginning of every second. After all surviving enemies attack, Bob chooses one living enemy and removes `power` points from its health.

Bob may keep attacking the same enemy or switch targets. An enemy stops contributing only after the attack that reduces its health to zero or below, so it still deals damage during its final second. Determine the smallest total damage Bob can receive before every enemy is defeated.

### Function Contract

**Inputs**

- `power`: Bob's fixed attack damage per second, where $1 \le \texttt{power} \le 10^4$.
- `damage`: A positive integer list of length $n$ containing each enemy's damage rate.
- `health`: A positive integer list of the same length containing each enemy's initial health.

The common length satisfies $1 \le n \le 10^5$, and every damage and health value is at most $10^4$.

**Return value**

- The minimum total damage dealt to Bob before all enemies die.

### Examples

**Example 1**

- Input: `power = 4, damage = [1,2,3,4], health = [4,5,6,8]`
- Output: `39`

One optimal defeat order is enemy 3, enemy 2, enemy 0, then enemy 1.

**Example 2**

- Input: `power = 1, damage = [1,1,1,1], health = [1,2,3,4]`
- Output: `20`

With equal rates, defeating enemies in increasing required attack time is optimal.

**Example 3**

- Input: `power = 8, damage = [40], health = [59]`
- Output: `320`

The lone enemy attacks for $\lceil 59/8 \rceil = 8$ seconds.
