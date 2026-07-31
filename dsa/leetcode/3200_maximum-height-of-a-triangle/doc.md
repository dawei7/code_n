# Maximum Height of a Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3200 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-height-of-a-triangle/) |

## Problem Description

### Goal

You have `red` red balls and `blue` blue balls. Build a triangle one complete row at a time: row $1$ contains one ball, row $2$ contains two balls, row $3$ contains three balls, and row $i$ must contain exactly $i$ balls.

Every ball in one row must have the same color. Adjacent rows must use different colors, so row colors alternate throughout the triangle. You may choose either red or blue for the top row, and unused balls are allowed.

Return the greatest height, meaning the largest number of complete rows that can be built without using more balls of either color than are available.

### Function Contract

**Inputs**

- `red`: The available number of red balls.
- `blue`: The available number of blue balls.

Both values are integers in $[1,100]$.

**Return value**

- The maximum attainable triangle height when the first row may use either color.

### Examples

**Example 1**

- Input: `red = 2, blue = 4`
- Output: `3`
- Explanation: Red rows of sizes $1$ and $3$ would need four balls, so the valid height-three arrangement instead starts with blue and uses row colors blue, red, blue.

**Example 2**

- Input: `red = 2, blue = 1`
- Output: `2`
- Explanation: A one-ball blue row followed by a two-ball red row uses both piles exactly.

**Example 3**

- Input: `red = 1, blue = 1`
- Output: `1`
- Explanation: Either color can fill the first row, but neither pile can fill a second row of two balls.

**Example 4**

- Input: `red = 10, blue = 1`
- Output: `2`
- Explanation: Starting with blue permits rows of sizes one and two; the next blue row would require three balls.
