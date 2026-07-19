# Minimum Operations to Convert Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2059 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-convert-number/) |

## Problem Description

### Goal

An integer `x` begins at `start`. While its current value lies from $0$ through $1000$, choose any distinct operand from `nums` and replace `x` with `x + operand`, `x - operand`, or `x ^ operand`, where `^` is bitwise XOR. Operands may be reused in any order and any number of times.

An operation may produce a value outside the allowed range, and that operation can successfully reach `goal`; however, no later operation may be applied from an out-of-range result. Return the fewest operations needed to reach `goal`, or `-1` if no legal sequence does so.

### Function Contract

**Inputs**

- `nums`: an array of $m$ distinct integers, where $1 \le m \le 1000$ and each value lies from $-10^9$ through $10^9$.
- `start`: the initial value, satisfying $0 \le start \le 1000$.
- `goal`: a target from $-10^9$ through $10^9$, distinct from `start`.

Let $R$ be the number of reachable values in the expandable range $[0,1000]$, so $R\le1001$.

**Return value**

- Return the minimum number of permitted operations that converts `start` to `goal`, or `-1` if conversion is impossible.

### Examples

**Example 1**

- Input: `nums = [2,4,12], start = 2, goal = 12`
- Output: `2`
- Explanation: One shortest sequence is `2 + 12 = 14`, followed by `14 - 2 = 12`.

**Example 2**

- Input: `nums = [3,5,7], start = 0, goal = -4`
- Output: `2`
- Explanation: `0 + 3 = 3`, then `3 - 7 = -4`; the final out-of-range result is allowed.

**Example 3**

- Input: `nums = [2,8,16], start = 0, goal = 1`
- Output: `-1`
