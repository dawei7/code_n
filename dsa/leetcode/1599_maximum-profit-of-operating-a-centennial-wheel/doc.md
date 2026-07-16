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

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Let $n$ be the number of scheduled arrival groups.

**Simulate every potentially useful service rotation.** Track how many customers are waiting. Before rotation $i+1$, add `customers[i]` when that arrival exists, board `min(4, waiting)`, and subtract those riders from the queue. Continue after the arrival array ends while anyone still waits; those additional paid rotations may increase the attainable profit.

**Maintain cumulative profit and its earliest maximum.** Each rotation changes profit by `boarded * boardingCost - runningCost`. Start the best profit at zero and the answer at `-1`. Update the recorded rotation only when cumulative profit becomes strictly greater than the previous best. This both excludes non-positive histories and preserves the earliest rotation when the same positive maximum occurs more than once.

After each iteration, the waiting count equals all arrived customers not yet boarded, and `profit` equals revenue from everyone boarded so far minus the cost of exactly the rotations performed. Therefore it is the profit obtained by stopping service at that point. Every useful stopping point occurs either during scheduled arrivals or while draining the final queue, and the loop examines all of them. Taking the earliest strictly greatest positive value yields the required answer.

#### Complexity detail

The simulation performs $n$ scheduled rotations plus at most $\lceil W/4 \rceil$ extra rotations for the final waiting count $W$. Since each arrival is at most 50, $W \le 50n$, so the total is $O(n)$. The waiting count, cumulative profit, best profit, and rotation counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Recompute every service prefix:** Simulating from the beginning for every possible stopping rotation is correct but repeats work and can take $O(n^2)$ time.
- **Stop when scheduled arrivals end:** This can miss the optimum because profitable rotations may remain while the final queue is drained.
- **Update on equal profit:** This incorrectly returns a later rotation; the contract asks for the minimum rotation count attaining the maximum.
- A rotation with no boarded customers still incurs `runningCost` while service continues through the arrival schedule.
- If every cumulative profit is zero or negative, return `-1`, not the rotation producing zero.
- Large early arrivals can require many rotations after the final arrival index.

</details>
