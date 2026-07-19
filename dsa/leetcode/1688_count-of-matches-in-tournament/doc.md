# Count of Matches in Tournament

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1688 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-matches-in-tournament/) |

## Problem Description
### Goal

A single-elimination tournament begins with `n` teams. In a round with an even number of teams, every team is paired, half as many matches are played, and one winner from each match advances. In a round with an odd number, one team advances without playing while all other teams are paired; the winners and the team receiving the bye form the next round.

Rounds continue until only one team remains and becomes the champion. Return the total number of matches played across every round. A bye neither plays a match nor eliminates a team, and the identity of the team receiving it does not affect the requested count.

### Function Contract
**Inputs**

- `n`: the initial number of teams, with $1 \le n \le 200$

**Return value**

The total number of matches required to leave exactly one tournament winner.

### Examples
**Example 1**

- Input: `n = 7`
- Output: `6`

The three rounds play 3, 2, and 1 matches.

**Example 2**

- Input: `n = 14`
- Output: `13`

The rounds play 7, 3, 2, and 1 matches.

**Example 3**

- Input: `n = 1`
- Output: `0`

The sole team is already the winner, so no match is necessary.
