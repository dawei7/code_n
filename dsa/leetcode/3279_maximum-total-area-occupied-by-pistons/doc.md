# Maximum Total Area Occupied by Pistons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3279 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Simulation, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Total Area Occupied by Pistons](https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/) |

## Problem Description

### Goal

Several pistons move vertically between positions `0` and `height`. The current position of a piston is also the area beneath it. `positions[i]` gives its initial position, while `directions[i]` is `U` for upward motion or `D` for downward motion.

During every second, each piston moves one unit in its current direction. Reaching either endpoint reverses its direction for subsequent motion, so every piston repeatedly travels from bottom to top and back. Endpoint directions are interpreted through this immediate reflection: a piston at an endpoint next moves into the valid interval.

At any integer time, the total occupied area is the sum of all piston positions. Return the greatest total that occurs over the continuing periodic motion, including the initial state.

### Function Contract

**Inputs**

- `height`: The common maximum position, with $1 \le \texttt{height} \le 10^6$.
- `positions`: Initial piston positions, each between `0` and `height` inclusive.
- `directions`: A same-length string containing only `U` and `D`.

Let $n$ be the number of pistons, where $1 \le n \le 10^5$.

**Return value**

Return the maximum possible sum of all piston positions at one integer time.

### Examples

**Example 1**

- Input: `height = 5, positions = [2, 5], directions = "UD"`
- Output: `7`
- Explanation: The initial total is already the maximum.

**Example 2**

- Input: `height = 6, positions = [0, 0, 6, 3], directions = "UUDU"`
- Output: `15`
- Explanation: After three seconds the positions are `[3, 3, 3, 6]`.

**Example 3**

- Input: `height = 4, positions = [0], directions = "D"`
- Output: `4`
- Explanation: Reflection at the bottom sends the piston upward, and it eventually reaches the top.
