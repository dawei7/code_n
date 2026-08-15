# Minimum Amount of Time to Fill Cups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2335 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/) |

## Problem Description

### Goal

A dispenser provides cold, warm, and hot water. In one second, it can fill one
cup of any type, or it can fill two cups simultaneously when they require
different water types.

The three entries of `amount` state how many cold, warm, and hot cups remain to
be filled. Determine the minimum number of seconds needed to fill every
requested cup while respecting the rule that a simultaneous pair must use two
different types.

### Function Contract

**Inputs**

- `amount`: Exactly three nonnegative integers for cold, warm, and hot cups,
  with each entry in $[0,100]$.

**Return value**

The minimum number of seconds required to reduce all three requested counts to
zero.

### Examples

#### Example 1

- **Input:** `amount = [1,4,2]`
- **Output:** `4`
- **Explanation:** Three seconds can each pair a warm cup with another type, and
  one final warm cup takes the fourth second.

#### Example 2

- **Input:** `amount = [5,4,4]`
- **Output:** `7`
- **Explanation:** Thirteen cups require at least seven seconds, and the three
  types can be paired so that seven seconds suffice.

#### Example 3

- **Input:** `amount = [5,0,0]`
- **Output:** `5`
- **Explanation:** With only one water type requested, every cup must be filled
  separately.
