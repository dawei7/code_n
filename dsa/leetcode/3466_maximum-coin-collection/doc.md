# Maximum Coin Collection

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3466 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-coin-collection/) |

## Problem Description

### Goal

Mario travels forward along a two-lane freeway. At mile `i`, driving in lane 1 changes his coin total by `lane1[i]`, while driving in lane 2 changes it by `lane2[i]`; positive values award coins and negative values charge a toll. He may enter at any mile and leave after any later visited mile, but the trip must include at least one mile and all visited indices must be contiguous.

Mario enters in lane 1 and may switch between the two lanes at most twice while moving forward. A switch may happen immediately after entering, so the first visited mile can effectively be in lane 2, and it may also happen just before he exits. Return the largest total obtainable over every valid entry point, exit point, and sequence of no more than two lane switches.

### Function Contract

**Inputs**

- `lane1`: Coin changes for successive miles in lane 1.
- `lane2`: Coin changes for the same successive miles in lane 2.

Let $n=\lvert\texttt{lane1}\rvert=\lvert\texttt{lane2}\rvert$. The constraints are $1\le n\le10^5$ and $-10^9\le\texttt{lane1[i]},\texttt{lane2[i]}\le10^9$.

**Return value**

Return the maximum coin total of a nonempty contiguous trip using at most two switches.

### Examples

#### Example 1

- **Input:** `lane1 = [1,-2,-10,3], lane2 = [-5,10,0,1]`
- **Output:** `14`

Drive the first mile in lane 1, switch to lane 2 for the next two miles, and switch back to lane 1 for the last mile, collecting `1 + 10 + 0 + 3`.

#### Example 2

- **Input:** `lane1 = [-5,-4,-3], lane2 = [-1,2,3]`
- **Output:** `5`

Enter at mile 1, switch immediately to lane 2, and collect `2 + 3`.

#### Example 3

- **Input:** `lane1 = [-10], lane2 = [-2]`
- **Output:** `-2`

The trip cannot be empty, so Mario switches immediately and accepts the smaller one-mile loss.
