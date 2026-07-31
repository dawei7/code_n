# Check if Two Chessboard Squares Have the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3274 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Check if Two Chessboard Squares Have the Same Color](https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/) |

## Problem Description

### Goal

Two strings identify squares on a standard $8 \times 8$ chessboard. Each coordinate contains a lowercase letter from `a` through `h` for its column, followed by a digit from `1` through `8` for its row. Both coordinates are guaranteed to name valid squares.

Chessboard colors alternate between neighboring squares along both rows and columns. Determine whether the two given squares therefore have the same color. Return `true` when their colors match and `false` when one square is black and the other is white.

### Function Contract

**Inputs**

- `coordinate1`: A valid two-character chessboard coordinate.
- `coordinate2`: A second valid two-character chessboard coordinate.

Each coordinate has a file in `a` through `h` and a rank in `1` through `8`.

**Return value**

Return a boolean indicating whether the two named squares have the same color.

### Examples

**Example 1**

- Input: `coordinate1 = "a1", coordinate2 = "c3"`
- Output: `true`
- Explanation: Both squares are black.

**Example 2**

- Input: `coordinate1 = "a1", coordinate2 = "h3"`
- Output: `false`
- Explanation: The two squares have different colors.

**Example 3**

- Input: `coordinate1 = "h8", coordinate2 = "a1"`
- Output: `true`
- Explanation: Moving seven columns and seven rows preserves the color.
