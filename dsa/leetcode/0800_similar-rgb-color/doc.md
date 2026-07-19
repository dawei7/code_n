# Similar RGB Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 800 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/similar-rgb-color/) |

## Problem Description

### Goal

Given a lowercase RGB color `#RRGGBB`, find the most similar color that can be written in three-digit shorthand. A shorthand color `#RGB` expands to `#RRGGBB`, so each red, green, and blue byte must consist of one repeated hexadecimal digit.

Similarity is the negative sum of the squared numerical differences between corresponding RGB channels. Return the shorthand-expressible color with maximum similarity in lowercase six-digit form. Optimize the three channels together under that definition; an exact shorthand channel remains unchanged.

### Function Contract

**Inputs**

- `color`: a lowercase string in the form `#RRGGBB`.

**Return value**

- The lowercase `#RRGGBB` form of the shorthand-expressible color with maximum similarity to `color`.

### Examples

**Example 1**

- Input: `color = "#09f166"`
- Output: `"#11ee66"`
- Explanation: The closest repeated-digit values to hexadecimal `09`, `f1`, and `66` are `11`, `ee`, and `66`.

**Example 2**

- Input: `color = "#4e3fe1"`
- Output: `"#5544dd"`
- Explanation: Each RGB channel is independently rounded to its nearest shorthand value.

**Example 3**

- Input: `color = "#abcdef"`
- Output: `"#aaccee"`
- Explanation: The nearest repeated-digit values are `aa`, `cc`, and `ee`.
