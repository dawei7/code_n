# Number of Laser Beams in a Bank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2125 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/) |

## Problem Description

### Goal

The binary strings in `bank` form an $m \times n$ floor plan. A `1` marks a
security device and a `0` marks an empty cell.

One laser beam connects each pair of devices placed on two distinct rows
$r_1<r_2$ exactly when every row strictly between them contains no security
device. Empty rows therefore do not create beams or block them, while any
nonempty intermediate row prevents all device pairs across it from connecting.
Beams are independent: sharing a device does not merge or remove them.

Return the total number of qualifying device pairs across the entire bank.

### Function Contract

**Inputs**

- `bank`: A nonempty list of equal-length binary strings.

Let $m=\lvert\texttt{bank}\rvert$, $n=\lvert\texttt{bank}[0]\rvert$, and
$S=mn$ be the number of cells.

**Return value**

Return the total number of laser beams between devices satisfying the
no-nonempty-intermediate-row condition.

### Examples

#### Example 1

- **Input:** `bank = ["011001", "000000", "010100", "001000"]`
- **Output:** `8`

The three devices in row zero connect to both devices in row two, contributing
six beams. Those two devices connect to the one device in row three,
contributing two more.

#### Example 2

- **Input:** `bank = ["000", "111", "000"]`
- **Output:** `0`

Only one row contains devices, so no pair can use distinct rows.
