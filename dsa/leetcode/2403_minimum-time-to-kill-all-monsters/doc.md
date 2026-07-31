# Minimum Time to Kill All Monsters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2403 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-kill-all-monsters/) |

## Problem Description

### Goal

Each monster has a positive power requirement. You begin with zero mana and a
daily mana gain of 1. At the start of every day, add the current gain to your
stored mana. After that addition, you may defeat one surviving monster whose
power is no greater than the available mana.

Defeating a monster resets mana to zero and increases the daily gain by one.
You may choose both the order of the monsters and the day on which each is
defeated. Return the minimum total number of days required to defeat every
monster.

### Function Contract

**Inputs**

- `power`: A list of $n$ monster powers, where
  $1 \le n \le 17$ and $1 \le \texttt{power[i]} \le 10^9$.

**Return value**

Return the minimum number of days until all monsters are defeated, assuming
mana starts at zero, gain starts at one, a kill resets mana to zero, and each
kill permanently increases gain by one.

### Examples

**Example 1**

- Input: `power = [3,1,4]`
- Output: `4`
- Explanation: Kill power 1 after one day, power 4 after two more days at gain
  2, and power 3 after one day at gain 3.

**Example 2**

- Input: `power = [1,1,4]`
- Output: `4`
- Explanation: The two power-1 monsters take one day each; the last monster
  takes two days at gain 3.

**Example 3**

- Input: `power = [1,2,4,9]`
- Output: `6`
- Explanation: One optimal order is 1, 2, 9, 4, requiring respectively
  1, 1, 3, and 1 days.
