# Bulb Switcher

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 319 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bulb-switcher/) |

## Problem Description
### Goal
There are `n` bulbs numbered from `1` through `n`, all initially off. During round `i`, toggle every bulb whose position is a multiple of `i`: off becomes on and on becomes off. Perform rounds `1` through `n` in order.

Return the number of bulbs that remain on after the final round. A bulb is toggled once for each positive divisor of its position, so only positions with an odd number of divisors finish on. The input `0` has no bulbs or rounds and returns `0`; the task asks for the count rather than the final boolean state of each bulb.

### Function Contract
**Inputs**

- `n`: the number of bulbs and rounds

**Return value**

The number of bulbs left on after all rounds.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `1`

**Example 2**

- Input: `n = 0`
- Output: `0`

**Example 3**

- Input: `n = 1`
- Output: `1`
