# Divide Players Into Teams of Equal Skill

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2491 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) |

## Problem Description

### Goal

An even-length array `skill` gives the positive skill level of every player. Divide all $n$ players into exactly $n/2$ disjoint teams, with two players on each team, so that every team's two skill levels have the same sum.

The chemistry of one team is the product of its two skill levels. If an equal-sum division exists, return the sum of the chemistry values across all teams. If every possible division leaves teams with different total skills, return `-1`.

### Function Contract

**Inputs**

- `skill`: An even-length list of positive player skill levels.

Let $n = \lvert\texttt{skill}\rvert$. The constraints satisfy $2 \le n \le 10^5$, $n$ is even, and $1 \le \texttt{skill[i]} \le 1000$.

**Return value**

Return the total chemistry of a division into equal-skill pairs, or `-1` when no such complete pairing exists.

### Examples

**Example 1**

- Input: `skill = [3, 2, 5, 1, 3, 4]`
- Output: `22`
- Explanation: Pairs `(1, 5)`, `(2, 4)`, and `(3, 3)` all sum to `6`; their chemistry totals `5 + 8 + 9 = 22`.

**Example 2**

- Input: `skill = [3, 4]`
- Output: `12`
- Explanation: The only two players form one team, whose chemistry is `3 * 4`.

**Example 3**

- Input: `skill = [1, 1, 2, 3]`
- Output: `-1`
- Explanation: The four players cannot be paired so that both teams have the same total skill.
