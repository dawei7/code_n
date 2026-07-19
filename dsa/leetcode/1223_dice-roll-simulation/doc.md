# Dice Roll Simulation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1223 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/dice-roll-simulation/) |

## Problem Description

### Goal

A die simulator produces a sequence of `n` rolls, each with a value from `1` through `6`. The six-element array `rollMax` limits consecutive repetitions: face $i+1$ may appear at most `rollMax[i]` times in a row.

Return the number of distinct roll sequences that satisfy every face's consecutive-occurrence limit. Because the count can be large, return it modulo $M=10^9+7$.

### Function Contract

**Inputs**

- `n`: The number of rolls in a sequence, where $1\le n\le5000$.
- `roll_max`: Six consecutive-run limits corresponding to faces `1` through `6`; each value lies from `1` through `15`. This is the app-local form of LeetCode's `rollMax` parameter.

Define the total number of run-length states as

$$
R=\sum_{f=0}^{5}\texttt{roll\_max[f]}.
$$

**Return value**

- The number of valid length-`n` roll sequences, reduced modulo $M$.

### Examples

**Example 1**

- Input: `n = 2`, `roll_max = [1,1,2,2,2,3]`
- Output: `34`

Of the `36` two-roll sequences, `11` and `22` violate their limits.

**Example 2**

- Input: `n = 2`, `roll_max = [1,1,1,1,1,1]`
- Output: `30`

The second roll must differ from the first, giving `6 * 5` choices.

**Example 3**

- Input: `n = 3`, `roll_max = [1,1,1,2,2,3]`
- Output: `181`
