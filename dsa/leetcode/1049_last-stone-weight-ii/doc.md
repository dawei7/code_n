# Last Stone Weight II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1049 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/last-stone-weight-ii/) |

## Problem Description

### Goal

The array `stones` gives the weight of each stone. On every turn, choose any two stones with weights $x$ and $y$, where $x \le y$, and smash them together.

If $x=y$, both stones are destroyed. Otherwise the stone weighing $x$ is destroyed and the other stone's weight becomes `y - x`. Continue until at most one stone remains. Among every possible sequence of choices, return the smallest achievable remaining weight, or return `0` if all stones can be destroyed.

### Function Contract

**Inputs**

- `stones`: the $N$ positive weights, where $1 \le N \le 30$ and $1 \le \texttt{stones[i]} \le 100$; their total is $S=\sum_{i=0}^{N-1}\texttt{stones[i]}$.

**Return value**

- The minimum possible weight of the final stone after choosing smash pairs optimally, or `0` when no stone remains.

### Examples

**Example 1**

- Input: `stones = [2,7,4,1,8,1]`
- Output: `1`
- Explanation: Suitable pair choices reduce the multiset until a stone of weight `1` remains, and zero is impossible.

**Example 2**

- Input: `stones = [31,26,33,21,40]`
- Output: `5`
