# Categorize Box According to Criteria

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2525 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/categorize-box-according-to-criteria/) |

## Problem Description

### Goal

Four integers describe a box: `length`, `width`, and `height` are its dimensions, while `mass` is its mass. The box is **Bulky** when at least one dimension is at least $10^4$, or when its volume `length * width * height` is at least $10^9$. It is **Heavy** when its mass is at least $100$.

Return `"Both"` if both properties hold, `"Neither"` if neither holds, `"Bulky"` if only the bulky condition holds, or `"Heavy"` if only the heavy condition holds.

### Function Contract

**Inputs**

- `length`: The box's first dimension.
- `width`: The box's second dimension.
- `height`: The box's third dimension.
- `mass`: The box's mass.

Each dimension is between $1$ and $10^5$, inclusive, and `mass` is between $1$ and $10^3$, inclusive.

**Return value**

Return exactly one of `"Both"`, `"Neither"`, `"Bulky"`, or `"Heavy"` according to the two independent criteria.

### Examples

#### Example 1

- **Input:** `length = 1000, width = 35, height = 700, mass = 300`
- **Output:** `"Heavy"`
- **Explanation:** No dimension and not the volume reaches a bulky threshold, while the mass is at least `100`.

#### Example 2

- **Input:** `length = 200, width = 50, height = 800, mass = 50`
- **Output:** `"Neither"`
- **Explanation:** Its dimensions, volume, and mass all remain below their respective thresholds.
