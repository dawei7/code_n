# Minimum Skips to Arrive at Meeting On Time

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/) |
| Frontend ID | 1883 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You have `hoursBefore` hours to reach a meeting by traveling $N$ roads in their given order. Road $i$ has length `dist[i]` kilometers, and you travel every road at the constant rate `speed` kilometers per hour.

After finishing any road except the last, you normally must wait until the next integer-hour mark before starting the following road. Finishing exactly on an integer hour requires no extra wait. You may skip selected rests, which preserves the exact accumulated time and can also change the hour marks reached after later roads. Return the fewest rests that must be skipped to arrive no later than the deadline, or `-1` when even uninterrupted travel is too slow.

### Function Contract

**Inputs**

- `dist`: a length-$N$ array of positive road distances in travel order, where $1 \le N \le 1000$ and $1 \le \texttt{dist[i]} \le 10^5$.
- `speed`: the fixed positive travel speed, with $1 \le \texttt{speed} \le 10^6$.
- `hoursBefore`: the positive integer-hour deadline, with $1 \le \texttt{hoursBefore} \le 10^7$.

**Return value**

- Return the minimum number of rests to skip so that arrival time is at most `hoursBefore`, or `-1` if this is impossible.

### Examples

**Example 1**

- Input: `dist = [1,3,2], speed = 4, hoursBefore = 2`
- Output: `1`

Skipping the first rest lets the first two roads finish exactly at hour `1`; the final road then ends at hour `1.5`.

**Example 2**

- Input: `dist = [7,3,5,5], speed = 2, hoursBefore = 10`
- Output: `2`

Skipping the rests after the first and third roads produces an arrival exactly at hour `10`.

**Example 3**

- Input: `dist = [7,3,5,5], speed = 1, hoursBefore = 10`
- Output: `-1`

The roads themselves require `20` hours, so removing rests cannot meet the deadline.
