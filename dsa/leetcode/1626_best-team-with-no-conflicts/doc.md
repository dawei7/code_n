# Best Team With No Conflicts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1626 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-team-with-no-conflicts/) |

## Problem Description
### Goal
Choose players for a basketball tournament so that their total score is as large as possible. Player `i` has score `scores[i]` and age `ages[i]`, and any subset of the available players may form the team.

The selected team must contain no conflict: a younger selected player may not have a strictly higher score than an older selected player. Players of the same age never conflict with one another, regardless of their scores. Return the maximum sum of scores among all conflict-free teams.

### Function Contract
**Inputs**

- `scores`: an integer array of length $n$, where $1 \le n \le 1000$ and $1 \le \texttt{scores[i]} \le 10^6$.
- `ages`: an integer array of the same length, where $1 \le \texttt{ages[i]} \le 1000$.
- Entries at the same index describe the same player.

**Return value**

Return the greatest possible sum of selected player scores subject to the no-conflict rule.

### Examples
**Example 1**

- Input: `scores = [1,3,5,10,15], ages = [1,2,3,4,5]`
- Output: `34`

Every player can be selected because scores rise with ages.

**Example 2**

- Input: `scores = [4,5,6,5], ages = [2,1,2,1]`
- Output: `16`

The two players of age 1 with score 5 and the age-2 player with score 6 form an optimal team.

**Example 3**

- Input: `scores = [1,2,3,5], ages = [8,9,10,1]`
- Output: `6`

Choosing the three older players avoids the conflict created by the younger score-5 player.
