# Super Washing Machines

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 517 |
| Difficulty | Hard |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/super-washing-machines/) |

## Problem Description
### Goal
A line of washing machines contains `machines[i]` dresses at position `i`. During one move, choose any number of machines simultaneously; each chosen machine passes one dress to one adjacent machine, while unchosen machines send nothing.

Return the minimum number of simultaneous moves needed to leave every machine with the same number of dresses, or `-1` when equalization is impossible. Dresses are conserved, so a total not divisible by the number of machines cannot succeed. A machine may receive and send across different moves, and counting individual dress transfers is not the same as counting simultaneous rounds.

### Function Contract
**Inputs**

- `machines`: a nonempty array where each value is the dresses currently held by one machine

**Return value**

- The minimum simultaneous moves needed to give every machine the same load, or `-1` if the total cannot be divided evenly

### Examples
**Example 1**

- Input: `machines = [1, 0, 5]`
- Output: `3`

**Example 2**

- Input: `machines = [0, 3, 0]`
- Output: `2`

**Example 3**

- Input: `machines = [0, 2, 0]`
- Output: `-1`
