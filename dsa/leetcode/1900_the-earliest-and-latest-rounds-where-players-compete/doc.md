# The Earliest and Latest Rounds Where Players Compete

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1900 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [The Earliest and Latest Rounds Where Players Compete](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/) |

## Problem Description

### Goal

Players numbered $1$ through $n$ stand in their original order. In every round, the first remaining player faces the last, the second faces the second-last, and so on. An unpaired middle player advances automatically. Winners are then reordered by their original player numbers before the next round.

`firstPlayer` and `secondPlayer` defeat every other opponent, so both remain until they face each other. For a match between any two other players, either winner may be chosen. Across every possible assignment of those results, return the earliest and latest round in which the two distinguished players can meet.

### Function Contract

**Inputs**

- `n`: the initial number of players, where $2 \le n \le 28$.
- `firstPlayer` and `secondPlayer`: distinct original player numbers satisfying $1 \le \texttt{firstPlayer} < \texttt{secondPlayer} \le n$.

**Return value**

Return `[earliest, latest]`, the minimum and maximum possible one-based round numbers in which the distinguished players compete.

### Examples

**Example 1**

- Input: `n = 11, firstPlayer = 2, secondPlayer = 4`
- Output: `[3, 4]`
- Explanation: Choosing different winners in unrelated matches can make the two players meet in round three or postpone their meeting until round four.

**Example 2**

- Input: `n = 5, firstPlayer = 1, secondPlayer = 5`
- Output: `[1, 1]`
- Explanation: The first and last players are paired immediately, so no other outcome can change their meeting round.

**Example 3**

- Input: `n = 5, firstPlayer = 1, secondPlayer = 3`
- Output: `[2, 3]`
