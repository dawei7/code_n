# Find Indices of Stable Mountains

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3285 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Find Indices of Stable Mountains](https://leetcode.com/problems/find-indices-of-stable-mountains/) |

## Problem Description

### Goal

Mountains are arranged in a row, and `height[i]` records the height of mountain $i$. A mountain is stable when the mountain immediately before it has height strictly greater than `threshold`.

Mountain `0` has no predecessor and is never stable. For every later index, only `height[i - 1]` determines stability; the current mountain's own height is irrelevant. Return all stable indices in any order.

### Function Contract

**Inputs**

- `height`: A list of $n$ mountain heights, each from `1` through `100`, with $2 \le n \le 100$.
- `threshold`: The strict comparison threshold, from `1` through `100`.

**Return value**

Return every index $i$ from `1` through `n - 1` for which `height[i - 1] > threshold`. The canonical implementation returns them in ascending order.

### Examples

#### Example 1

- **Input:** `height = [1, 2, 3, 4, 5], threshold = 2`
- **Output:** `[3, 4]`
- **Explanation:** The predecessors at indices `2` and `3` exceed `2`.

#### Example 2

- **Input:** `height = [10, 1, 10, 1, 10], threshold = 3`
- **Output:** `[1, 3]`

#### Example 3

- **Input:** `height = [10, 1, 10, 1, 10], threshold = 10`
- **Output:** `[]`
- **Explanation:** Equality with the threshold is not sufficient.
