# Number of Ways to Divide a Long Corridor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2147 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [number-of-ways-to-divide-a-long-corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/) |

## Problem Description

### Goal

A 0-indexed string `corridor` describes a line in a library. Each `S`
represents a seat and each `P` represents a decorative plant. Fixed room
dividers already stand immediately before the first character and after the
last character.

At most one additional divider may be installed in each gap between adjacent
characters. The resulting nonoverlapping sections must each contain exactly
two seats and may contain any number of plants. Two divisions differ when at
least one gap contains a divider in one division but not the other.

Return the number of valid divisions modulo $10^9+7$. If no division can give
every section exactly two seats, return `0`.

### Function Contract

**Inputs**

- `corridor`: A string of length $n$, where $1 \leq n \leq 10^5$, containing
  only `S` and `P`.

**Return value**

Return the number of distinct sets of internal divider positions that create
sections with exactly two seats, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `corridor = "SSPPSPS"`
- **Output:** `3`
- **Explanation:** The plants between the second and third seats create three
  possible gaps for the sole internal divider.

#### Example 2

- **Input:** `corridor = "PPSPSP"`
- **Output:** `1`
- **Explanation:** The corridor already contains exactly two seats, so no
  additional divider is installed.

#### Example 3

- **Input:** `corridor = "S"`
- **Output:** `0`
- **Explanation:** One seat cannot form a valid section.
