# Maximum Area of Longest Diagonal Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3000 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/) |

## Problem Description

### Goal

You are given a list of rectangles. Each row contains the positive integer
length and width of one rectangle.

Choose a rectangle with the longest diagonal and return its area. When several
rectangles have the same longest diagonal, choose the one with the greatest
area among them.

For a rectangle with sides $a$ and $b$, its diagonal length is
$\sqrt{a^2+b^2}$ and its area is $ab$. The returned value is the selected
rectangle's integer area, not its diagonal length or its dimensions.

### Function Contract

**Inputs**

- `dimensions`: rows of the form `[length, width]`

Let $N=\lvert\texttt{dimensions}\rvert$. The contract guarantees
$1\le N\le100$, every row has exactly two entries, and every side length is
between 1 and 100 inclusive.

**Return value**

Return the area of the rectangle selected by diagonal length and then area.

### Examples

#### Example 1

- **Input:** `dimensions = [[9,3],[8,6]]`
- **Output:** `48`

The squared diagonals are 90 and 100, so the second rectangle is selected.

#### Example 2

- **Input:** `dimensions = [[3,4],[4,3]]`
- **Output:** `12`

Both diagonals have length 5 and both areas are 12.
