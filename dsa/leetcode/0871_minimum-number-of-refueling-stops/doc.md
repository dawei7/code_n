# Minimum Number of Refueling Stops

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 871 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-refueling-stops/) |

## Problem Description
### Goal
A car begins at position `0` and must travel east to `target`. It has an unlimited-capacity tank initially containing `startFuel` liters and consumes exactly one liter per mile. Each station is described by `[position, fuel]`, where positions are strictly increasing and the station holds the stated amount of fuel.

Upon reaching a station, the car may stop and transfer all of that station's fuel into its tank. Find the minimum number of refueling stops needed to reach `target`, or return `-1` if the trip is impossible. Reaching a station or the destination with exactly zero fuel is allowed.

### Function Contract
**Inputs**

- `target`: the destination distance, where $1 \leq \texttt{target} \leq 10^9$.
- `startFuel`: the initial liters in the tank, where $1 \leq \texttt{startFuel} \leq 10^9$.
- `stations`: an array of $n$ pairs `[position, fuel]` in strictly increasing position order, where $0 \leq n \leq 500$, $1 \leq \texttt{position} < \texttt{target}$, and $1 \leq \texttt{fuel} \leq 10^9$.

**Return value**

Return the minimum number of stations at which the car must refuel to reach `target`, or `-1` if no selection of stations succeeds.

### Examples
**Example 1**

- Input: `target = 1, startFuel = 1, stations = []`
- Output: `0`

The initial fuel reaches the destination exactly.

**Example 2**

- Input: `target = 100, startFuel = 1, stations = [[10,100]]`
- Output: `-1`

The car cannot reach the first station.

**Example 3**

- Input: `target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]`
- Output: `2`

Refueling at positions `10` and `60` supplies enough fuel to arrive.
