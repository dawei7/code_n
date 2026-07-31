# Calculate Score After Performing Instructions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3522 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-score-after-performing-instructions/) |

## Problem Description

### Goal

Two arrays describe a program of $n$ indexed instructions. Execution begins at index `0` with score `0`. An `"add"` instruction adds the corresponding entry of `values` to the score and continues at the next index. A `"jump"` instruction changes the current index by its corresponding value without changing the score.

Execution stops as soon as the next index lies outside $[0,n)$ or the program attempts to visit an instruction that has already been executed. A repeated instruction is not executed a second time. Return the score accumulated before termination.

### Function Contract

**Inputs**

- `instructions`: A list of $n$ strings, each equal to `"add"` or `"jump"`.
- `values`: A list of $n$ integers. For an add instruction the value changes the score; for a jump instruction it is the relative index offset.

The arrays have equal length, with $1 \le n \le 10^5$, and every value lies between $-10^5$ and $10^5$ inclusive.

**Return value**

Return the integer score when execution first leaves the array or would revisit an executed index.

### Examples

**Example 1**

- Input: `instructions = ["jump", "add", "add", "jump", "add", "jump"]`, `values = [2, 1, 3, 1, -2, -3]`
- Output: `1`
- Explanation: The path is `0 -> 2 -> 3 -> 4 -> 5 -> 2`; values `3` and `-2` are added before the attempted revisit of index `2`.

**Example 2**

- Input: `instructions = ["jump", "add", "add"]`, `values = [3, 1, 1]`
- Output: `0`
- Explanation: The first jump lands at index `3`, which is out of bounds.

**Example 3**

- Input: `instructions = ["jump"]`, `values = [0]`
- Output: `0`
- Explanation: The jump targets index `0` again, so execution stops before a second execution.
