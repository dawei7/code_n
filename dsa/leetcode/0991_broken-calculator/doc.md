# Broken Calculator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 991 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/broken-calculator/) |

## Problem Description

### Goal

A broken calculator initially displays the positive integer `startValue`. It supports only two operations: multiply the displayed number by $2$, or subtract $1$ from it. No other arithmetic keys are available, and each press applies its operation to the value currently shown.

Given `startValue` and another positive integer `target`, return the minimum number of allowed operations required to make the calculator display `target`.

### Function Contract

**Inputs**

- `startValue`: the calculator's initial integer, where $1\le\texttt{startValue}\le10^9$.
- `target`: the desired displayed integer, where $1\le\texttt{target}\le10^9$.

Let $T=\texttt{target}$.

**Return value**

- The minimum number of multiply-by-two and subtract-one operations needed to reach `target`.

### Examples

**Example 1**

- Input: `startValue = 2, target = 3`
- Output: `2`
- Explanation: Double to $4$, then subtract one to reach $3$.

**Example 2**

- Input: `startValue = 5, target = 8`
- Output: `2`
- Explanation: Subtract one to get $4$, then double to get $8$.

**Example 3**

- Input: `startValue = 3, target = 10`
- Output: `3`
- Explanation: The sequence $3\to6\to5\to10$ uses three operations.
