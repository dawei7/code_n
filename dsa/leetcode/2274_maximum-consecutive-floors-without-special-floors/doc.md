# Maximum Consecutive Floors Without Special Floors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2274 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/) |

## Problem Description
### Goal
Alice has rented every floor of a building from `bottom` through `top`,
inclusive, for her company. Some of those rented floors are designated as
special floors used only for relaxation. The distinct floor numbers of all
such locations are listed in `special`.

Among the rented floors, find the greatest possible length of a consecutive
interval that contains no special floor. A valid interval may lie below the
lowest special floor, between two special floors, or above the highest special
floor. Its endpoints must remain within the inclusive rented range.

Return the number of floors in the longest such interval. If every rented
floor is special, return zero.

### Function Contract
**Inputs**

- `bottom`: the lowest rented floor, with $1 \le \texttt{bottom}$
- `top`: the highest rented floor, with $\texttt{bottom} \le \texttt{top} \le 10^9$
- `special`: between 1 and $10^5$ distinct floor numbers, each in the inclusive
  interval from `bottom` through `top`

Let $m=\lvert\texttt{special}\rvert$.

**Return value**

The maximum number of consecutive rented floors containing no special floor.

### Examples
**Example 1**

- Input: `bottom = 2, top = 9, special = [4, 6]`
- Output: `3`

The longest special-free interval is floors 7 through 9.

**Example 2**

- Input: `bottom = 6, top = 8, special = [7, 6, 8]`
- Output: `0`

Every rented floor is special.

**Example 3**

- Input: `bottom = 2, top = 10, special = [2, 3, 9]`
- Output: `5`

Floors 4 through 8 form the longest special-free interval.
