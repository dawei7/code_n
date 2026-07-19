# Maximum Profit of Operating a Centennial Wheel

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1599 |
| Difficulty | Medium |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/) |

## Problem Description
### Goal
You operate a Centennial Wheel with four gondolas, each able to board at most four customers when it reaches the ground. One counterclockwise rotation costs `runningCost`. Each customer pays `boardingCost` when boarding and exits after that gondola completes its trip back to the ground.

Array `customers` gives arrivals over time: `customers[i]` people arrive immediately before rotation $i+1$. Waiting customers must board whenever space is available, with at most four boarding per rotation; any excess remains for the next rotation. You may stop serving at any time, even before everyone boards. Once service stops, later rotations needed to unload riders are free and add no new boarding revenue. Return the smallest number of paid service rotations at which cumulative profit is maximized, or `-1` if profit is never positive.

### Function Contract
**Inputs**

- `customers`: an array of $n$ arrival counts with $1 \le n \le 10^5$ and $0 \le \texttt{customers[i]} \le 50$.
- `boardingCost`: the payment from each boarded customer, with $1 \le \texttt{boardingCost} \le 100$.
- `runningCost`: the cost of each service rotation, with $1 \le \texttt{runningCost} \le 100$.

**Return value**

Return the earliest positive-profit rotation count that attains the maximum cumulative profit, or `-1` when no service prefix has positive profit.

### Examples
**Example 1**

- Input: `customers = [8, 3]`, `boardingCost = 5`, `runningCost = 6`
- Output: `3`

**Example 2**

- Input: `customers = [10, 9, 6]`, `boardingCost = 6`, `runningCost = 4`
- Output: `7`

**Example 3**

- Input: `customers = [3, 4, 0, 5, 1]`, `boardingCost = 1`, `runningCost = 92`
- Output: `-1`
