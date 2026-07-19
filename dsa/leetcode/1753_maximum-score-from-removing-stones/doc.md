# Maximum Score From Removing Stones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1753 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-from-removing-stones/) |

## Problem Description

### Goal

You are playing a solitaire game with exactly three nonempty piles containing `a`, `b`, and `c` stones. On each turn, choose two different piles that are both nonempty, remove one stone from each chosen pile, and increase the score by one.

The game ends when fewer than two piles remain nonempty, because no legal pair can then be chosen. Decide how to choose the piles on every turn so that the final score is as large as possible, and return that maximum score.

### Function Contract

**Inputs**

- `a`, `b`, and `c`: the three initial pile sizes, each satisfying $1 \le a,b,c \le 10^5$.

Let $S=a+b+c$ and $M=\max(a,b,c)$.

**Return value**

- Return the maximum number of turns, equivalently the maximum score, obtainable before fewer than two piles are nonempty.

### Examples

**Example 1**

- Input: `a = 2, b = 4, c = 6`
- Output: `6`
- Explanation: All twelve stones can be consumed in six cross-pile pairs.

**Example 2**

- Input: `a = 4, b = 4, c = 6`
- Output: `7`
- Explanation: The fourteen stones can be paired completely across seven turns.

**Example 3**

- Input: `a = 1, b = 8, c = 8`
- Output: `8`
- Explanation: Pair the two size-eight piles until both are empty; the remaining single stone cannot form another move.
