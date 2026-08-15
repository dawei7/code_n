# Pass the Pillow

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2582 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Pass the Pillow](https://leetcode.com/problems/pass-the-pillow/) |

## Problem Description

### Goal

There are `n` people standing in a line, numbered from $1$ through $n$. At time zero, person `1` holds a pillow.

Once per second, the current holder passes the pillow to the adjacent person in the current direction. Passing begins toward increasing labels. Whenever the pillow reaches either end of the line, the direction reverses, so no pass goes beyond person `1` or person `n`.

Return the label of the person holding the pillow after exactly `time` seconds.

### Function Contract

**Inputs**

- `n`: The number of people in the line.
- `time`: The number of one-second passes to perform.

The constraints are $2 \leq n \leq 1000$ and $1 \leq \texttt{time} \leq 1000$.

**Return value**

- The label of the person holding the pillow after exactly `time` seconds.

### Examples

#### Example 1

- **Input:** `n = 4, time = 5`
- **Output:** `2`
- **Explanation:** The holders are `1 -> 2 -> 3 -> 4 -> 3 -> 2`.

#### Example 2

- **Input:** `n = 3, time = 2`
- **Output:** `3`
- **Explanation:** After two passes, the pillow has just reached the right endpoint.
