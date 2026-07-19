# Paint House

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 256 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-house/) |

## Problem Description
### Goal
Houses stand in a row, and each row of `costs` gives the price of painting that house red, blue, or green. Choose exactly one color for every house, with the restriction that adjacent houses cannot receive the same color.

Return the minimum total cost across all valid color assignments. A locally cheapest color may need to be avoided because of the neighboring choice, and the same color can be reused after at least one differently colored house. The function returns only the optimal cost, not the chosen color sequence. When there are no houses, return `0`.

### Function Contract
**Inputs**

- `costs`: one `[red, blue, green]` cost row per house

**Return value**

The minimum valid total cost, or zero for no houses.

### Examples
**Example 1**

- Input: `costs = [[17,2,17],[16,16,5],[14,3,19]]`
- Output: `10`

**Example 2**

- Input: `costs = [[7,6,2]]`
- Output: `2`

**Example 3**

- Input: `costs = []`
- Output: `0`
