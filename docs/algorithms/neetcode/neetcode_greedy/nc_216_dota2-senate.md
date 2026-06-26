## Problem Description & Examples
### Goal
In the world of Dota2, there are two senate factions: Radiant and Dire. The Dota2 senate consists of representatives from both parties, and the voting alternates round by round.

Each senator has one of two rights:
- **Ban one senator's right**: A senator can make another senator lose all rights in this and all following rounds.
- **Announce the victory**: If a senator finds that all senators who have voting rights are from the same party, they can announce the victory.

Given a string `senate` representing each senator's faction, return `"Radiant"` or `"Dire"`.

### Function Contract
**Inputs**

- `senate`: str

**Return value**

str - 'Radiant' or 'Dire'

### Examples
**Example 1**

- Input: `senate = "RDD"`
- Output: `"Dire"`

**Example 2**

- Input: `senate = 'DRD'`
- Output: `'Dire'`

**Example 3**

- Input: `senate = 'RD'`
- Output: `'Radiant'`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
