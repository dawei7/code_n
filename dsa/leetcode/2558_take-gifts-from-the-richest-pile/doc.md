# Take Gifts From the Richest Pile

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2558 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) |

## Problem Description

### Goal

The integer array `gifts` records how many gifts are held in several piles. During each second, choose a pile containing the maximum current number of gifts. If several piles tie for the maximum, any one of them may be selected.

For the chosen pile, leave behind exactly the floor of the square root of its previous size; all other piles remain unchanged. Perform this operation for exactly `k` seconds, then return the total number of gifts remaining across every pile.

### Function Contract

**Inputs**

- `gifts`: A list of $n$ positive pile sizes, where $1 \le n \le 10^3$ and $1 \le \texttt{gifts[i]} \le 10^9$.
- `k`: The exact number of operations to perform, where $1 \le k \le 10^3$.

**Return value**

- The sum of all pile sizes after exactly `k` richest-pile reductions.

### Examples

**Example 1**

- Input: `gifts = [25, 64, 9, 4, 100], k = 4`
- Output: `29`
- Explanation: The selected values become `100 -> 10`, `64 -> 8`, `25 -> 5`, and then `10 -> 3`. The remaining piles are `[5, 8, 9, 4, 3]`.

**Example 2**

- Input: `gifts = [1, 1, 1, 1], k = 4`
- Output: `4`
- Explanation: Reducing a pile of size `1` leaves it at `1`, so no operation changes the total.

**Example 3**

- Input: `gifts = [10], k = 1`
- Output: `3`
- Explanation: The only pile becomes $\lfloor\sqrt{10}\rfloor=3$.
