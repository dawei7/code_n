# Last Stone Weight

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1046 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/last-stone-weight/) |

## Problem Description

### Goal

The array `stones` gives the weight of every stone in a game. On each turn, choose the two heaviest stones. Let their weights be $x$ and $y$, with $x \le y$, and smash them together.

If $x=y$, both stones are destroyed. If $x\ne y$, the stone weighing $x$ is destroyed and the other stone's weight becomes `y - x`. Continue until at most one stone remains. Return its weight, or return `0` when every stone has been destroyed.

### Function Contract

**Inputs**

- `stones`: the $N$ positive stone weights, where $1 \le N \le 30$ and $1 \le \texttt{stones[i]} \le 1000$.

**Return value**

- The weight of the only remaining stone after repeatedly smashing the two heaviest, or `0` if no stone remains.

### Examples

**Example 1**

- Input: `stones = [2,7,4,1,8,1]`
- Output: `1`
- Explanation: The successive heaviest pairs produce differences `1`, `2`, and `1`; an equal pair is then destroyed, leaving weight `1`.

**Example 2**

- Input: `stones = [1]`
- Output: `1`
