# Minimum Hours of Training to Win a Competition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2383 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/) |

## Problem Description

### Goal

You enter a competition with positive initial amounts of energy and experience. Two arrays describe the energy and experience of $n$ opponents, whom you must face in the given order. To defeat an opponent, your current energy and current experience must both be strictly greater than that opponent's corresponding values.

After each victory, your energy decreases by the opponent's energy, while your experience increases by the opponent's experience. Before the competition begins, each hour of training can increase either your initial energy or your initial experience by exactly one. Determine the minimum total number of training hours that guarantees you can defeat every opponent in order.

### Function Contract

**Inputs**

- `initialEnergy`: Your positive starting energy.
- `initialExperience`: Your positive starting experience.
- `energy`: A list of $n$ opponents' energy values.
- `experience`: A list of the same $n$ opponents' experience values.

Here $1 \le n \le 100$, and every initial or opponent value lies between 1 and 100 inclusive.

**Return value**

- Return the minimum number of one-point training hours needed before the competition.

**Competition rules**

- Both current statistics must be strictly greater than the current opponent's values.
- A victory subtracts that opponent's energy and adds that opponent's experience.
- Training occurs only before the first opponent, but its added points remain part of the evolving statistics.

### Examples

**Example 1**

- Input: `initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]`
- Output: `8`
- Explanation: Six energy hours and two experience hours provide enough strength to win all four encounters in order.

**Example 2**

- Input: `initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]`
- Output: `0`
- Explanation: Both starting statistics are already strictly greater than the only opponent's values.
