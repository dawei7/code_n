# Minimum Time to Make Rope Colorful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1578 |
| Difficulty | Medium |
| Topics | Array, String, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) |

## Problem Description
### Goal

A rope holds $N$ balloons in a row. The character `colors[i]` gives the color of balloon `i`, and `neededTime[i]` gives the number of seconds required to remove that same balloon from the rope.

The rope is colorful when no two balloons that remain adjacent have the same color. Removing a balloon closes the gap, so balloons that were separated by removed positions may become neighbors afterward.

Choose any balloons to remove and return the minimum total removal time that makes the rope colorful. Removal times are paid only for deleted balloons; every retained balloon costs nothing.

### Function Contract
**Inputs**

- `colors`: A lowercase English string of length $N$, where $1 \le N \le 10^5$.
- `needed_time`: An integer array of the same length, where $1 \le \texttt{needed_time[i]} \le 10^4$.

**Return value**

Return the minimum total time required to leave no equal adjacent balloon colors.

### Examples
**Example 1**

- Input: `colors = "abaac", needed_time = [1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input: `colors = "abc", needed_time = [1, 2, 3]`
- Output: `0`

**Example 3**

- Input: `colors = "aabaa", needed_time = [1, 2, 3, 4, 1]`
- Output: `2`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Treat each maximal color run independently**

Consider one maximal consecutive run of the same color. At most one balloon from that run may remain; keeping two would leave equal adjacent colors. Removing the entire run is never cheaper than keeping one balloon because all removal times are positive.

Therefore, every valid optimum removes all but one balloon from each repeated-color run. To minimize the removal cost, retain the balloon with the largest removal time and pay for all other balloons in that run.

**Accumulate the cheaper balloon on every collision**

Scan from left to right while storing the color and removal time of the balloon currently chosen to survive its run. When the next color differs, begin a new run. When it matches, add the smaller of the two removal times to the answer and keep the larger time as the run's surviving candidate.

After processing a whole run, this has paid its total removal time minus its maximum value. Since different maximal runs have different boundary colors, choices inside one run cannot create a new same-color conflict with another run. Summing their independent optima is therefore globally optimal.

#### Complexity detail

The scan examines each balloon once and performs constant work per position, giving $O(N)$ time.

Only the accumulated cost, previous color, and largest retained time for the active run are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Sum each run then subtract its maximum:** explicitly track a run sum and maximum. This is also $O(N)$ time and $O(1)$ extra space.
- **Dynamic programming:** track the minimum cost for which color survives at each prefix. It can express the same choice but uses unnecessary state for this local greedy structure.
- **Repeated deletion simulation:** repeatedly find an equal adjacent pair and delete the cheaper balloon. It is correct, but array deletions and rescans can require $O(N^2)$ time.
- **All colors distinct:** no balloon is removed, so the answer is zero.
- **One balloon:** the rope is already colorful.
- **One long equal-color run:** remove every balloon except the most expensive one.
- **Equal removal times:** either tied balloon may survive; the minimum total is unchanged.
- **Multiple separated runs:** optimize every maximal run independently and add their costs.
- **Largest time in the middle:** the scan must continue carrying that maximum across the rest of the run.
- **Removing a boundary balloon:** maximal runs already have different neighboring colors, so resolving a run never merges it with another run of the same color.

</details>
