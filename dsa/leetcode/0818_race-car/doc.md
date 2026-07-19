# Race Car

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 818 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/race-car/) |

## Problem Description

### Goal

A car moves along an unbounded number line. It begins at position `0` with speed `1` and accepts a sequence made from two instructions. `A` accelerates: the car first moves by its current signed speed, then doubles that speed. `R` reverses without changing position: a positive speed becomes `-1`, and a negative speed becomes `1`.

Given a positive target position, determine the minimum number of instructions required to land on it exactly. The car may pass the target, travel through negative positions, and reverse more than once; only the final position and instruction count matter.

### Function Contract

**Inputs**

- `target`: a positive destination position.

**Return value**

- The minimum number of accelerate/reverse instructions needed to reach `target` exactly.

### Examples

**Example 1**

- Input: `target = 3`
- Output: `2`
- Explanation: Two accelerations visit positions `1` and `3`.

**Example 2**

- Input: `target = 6`
- Output: `5`
- Explanation: `AAARA` reaches `7`, reverses, then accelerates back to `6`.

**Example 3**

- Input: `target = 4`
- Output: `5`
- Explanation: `AARRA` reaches `3`, turns twice to face forward again, and advances to `4`.
