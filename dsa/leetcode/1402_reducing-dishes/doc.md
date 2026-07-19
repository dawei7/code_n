# Reducing Dishes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1402 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/reducing-dishes/) |

## Problem Description

### Goal

A chef has several dishes, and `satisfaction[i]` is the satisfaction value of one dish. The chef may discard any dishes and may arrange the selected dishes in any order before cooking them. Every selected dish takes one unit of time.

If a dish with satisfaction $s$ finishes at time $t$, it contributes $t \cdot s$ to the like-time coefficient. Cooking starts at time one for the first selected dish. Return the maximum total like-time coefficient possible; selecting no dishes is allowed and gives zero.

### Function Contract

**Inputs**

- `satisfaction`: an array of $n$ integers, where $1 \le n \le 500$ and $-1000 \le \texttt{satisfaction[i]} \le 1000$.

**Return value**

- The greatest sum of completion-time-weighted satisfaction over any chosen subset and ordering.

### Examples

**Example 1**

- Input: `satisfaction = [-1,-8,0,5,-9]`
- Output: `14`

**Example 2**

- Input: `satisfaction = [4,3,2]`
- Output: `20`

**Example 3**

- Input: `satisfaction = [-1,-4,-5]`
- Output: `0`
