# The Number of Weak Characters in the Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1996 |
| Difficulty | Medium |
| Topics | Array, Stack, Greedy, Sorting, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/) |

## Problem Description

### Goal

A game contains $N$ characters, each described by two statistics. For character $i$, `properties[i] = [attack_i, defense_i]` gives its attack and defense levels.

Character $i$ is weak when some other character $j$ is strictly better in both statistics:

$$
\textit{attack}_j>\textit{attack}_i
\quad\text{and}\quad
\textit{defense}_j>\textit{defense}_i.
$$

Equality in either statistic is not enough. Count how many characters have at least one such dominating character.

### Function Contract

**Inputs**

- `properties`: an array of $N$ pairs `[attack, defense]`, where $2 \le N \le 10^5$.
- Every attack and defense value is between $1$ and $10^5$ inclusive.

**Return value**

Return the number of characters dominated in both statistics by at least one other character.

### Examples

**Example 1**

- Input: `properties = [[5, 5], [6, 3], [3, 6]]`
- Output: `0`
- Explanation: Each possible comparison loses in at least one statistic.

**Example 2**

- Input: `properties = [[2, 2], [3, 3]]`
- Output: `1`
- Explanation: The character `[3, 3]` has strictly greater attack and defense than `[2, 2]`.

**Example 3**

- Input: `properties = [[1, 5], [10, 4], [4, 3]]`
- Output: `1`
- Explanation: `[10, 4]` dominates `[4, 3]`, while no character has both statistics above `[1, 5]`.
