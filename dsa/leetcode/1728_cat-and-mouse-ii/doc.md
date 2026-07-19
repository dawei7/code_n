# Cat and Mouse II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1728 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Matrix, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cat-and-mouse-ii/) |

## Problem Description

### Goal

Cat and Mouse play on a rectangular grid containing floor cells `.`, impassable walls `#`, one mouse `M`, one cat `C`, and one food cell `F`. Mouse moves first, and the players then alternate turns. On a turn, the current player may stay in place or jump from zero up to that player's maximum distance in one of the four cardinal directions. A jump cannot leave the grid or cross a wall, although Mouse is allowed to jump over Cat.

Cat wins immediately by occupying Mouse's cell or reaching the food first. Mouse wins immediately by reaching the food first. If Mouse cannot reach the food within 1000 turns, Cat wins. Given `catJump` and `mouseJump`, return whether Mouse can force a win when both players choose their moves optimally.

### Function Contract

**Inputs**

- `grid`: an array of `rows` equal-length strings, where $1 \le \texttt{rows},\texttt{cols} \le 8$. Every character is `.`, `#`, `M`, `C`, or `F`, and exactly one each of `M`, `C`, and `F` appears.
- `catJump`: Cat's maximum jump length, where $1 \le \texttt{catJump} \le 8$.
- `mouseJump`: Mouse's maximum jump length, where $1 \le \texttt{mouseJump} \le 8$.

Let $V$ be the number of non-wall cells and let $D$ be the maximum number of legal destinations, including staying, available from any cell to either player.

**Return value**

- Return `True` if Mouse has a strategy that guarantees reaching the food within 1000 turns; otherwise return `False`.

### Examples

**Example 1**

- Input: `grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2`
- Output: `True`
- Explanation: Mouse can force a route to the food before Cat can catch it or reach the food.

**Example 2**

- Input: `grid = ["M.C...F"], catJump = 1, mouseJump = 4`
- Output: `True`
- Explanation: Mouse can jump beyond Cat and land on the food on its first turn.

**Example 3**

- Input: `grid = ["M.C...F"], catJump = 1, mouseJump = 3`
- Output: `False`
- Explanation: Mouse cannot reach the food immediately, and Cat can prevent a forced win.
