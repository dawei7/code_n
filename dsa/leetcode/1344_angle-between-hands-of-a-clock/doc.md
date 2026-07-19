# Angle Between Hands of a Clock

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1344 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/angle-between-hands-of-a-clock/) |

## Problem Description

### Goal

An analog clock is showing the time described by an integer `hour` and an integer `minutes`. The hour hand moves continuously as the minutes advance; it is not restricted to the numbered hour marks. The minute hand points to the position for the given whole minute.

Return the smaller angle, measured in degrees, between the two hands. Either direction around the clock may describe an angle between them, so the requested result is never greater than $180$ degrees. Floating-point answers within $10^{-5}$ of the exact value are accepted.

### Function Contract

**Inputs**

- `hour`: an integer from $1$ through $12$.
- `minutes`: an integer from $0$ through $59$.

**Return value**

- Return the smaller nonnegative angle in degrees between the hour and minute hands.

### Examples

**Example 1**

- Input: `hour = 12, minutes = 30`
- Output: `165.0`
- Explanation: The minute hand is at $180$ degrees while the hour hand has advanced to $15$ degrees.

**Example 2**

- Input: `hour = 3, minutes = 30`
- Output: `75.0`

**Example 3**

- Input: `hour = 3, minutes = 15`
- Output: `7.5`
