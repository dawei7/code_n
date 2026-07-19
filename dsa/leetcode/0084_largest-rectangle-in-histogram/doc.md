# Largest Rectangle in Histogram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 84 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) |

## Problem Description
### Goal
The array `heights` describes adjacent histogram bars, each with unit width and a nonnegative height. Choose one contiguous span of bars and place an axis-aligned rectangle on the common baseline entirely beneath that span.

The rectangle's width is the number of selected bars, and its height cannot exceed the shortest selected bar. Return the greatest possible area over every span and allowable height. Zero-height bars may split useful regions, and a rectangle may consist of a single bar.

### Function Contract
**Inputs**

- `heights`: a nonempty list of nonnegative bar heights

**Return value**

The maximum rectangular area as an integer.

### Examples
**Example 1**

- Input: `heights = [2,1,5,6,2,3]`
- Output: `10`

**Example 2**

- Input: `heights = [2,4]`
- Output: `4`

**Example 3**

- Input: `heights = [0]`
- Output: `0`
