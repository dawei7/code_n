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

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Delay each refueling decision until it is necessary**

Treat `startFuel` as the farthest position currently reachable. Scan stations in position order and place the fuel from every reachable station into a max-heap. The heap represents stops the car could have made while passing those positions; choosing one later is a bookkeeping device that produces the same final fuel as choosing it at the station.

If the current reach is still below `target`, one additional stop is necessary. Remove the largest available fuel amount from the heap, extend the reach by that amount, and count the stop. Newly reachable stations then become eligible. If the heap is empty while the target remains out of reach, no past station can supply more fuel and the trip is impossible.

**The largest reachable fuel is the safe greedy choice**

At any point where another stop is required, every station in the heap has already been reachable under the current choices. All candidate stops cost exactly one toward the objective. Selecting the largest fuel amount gives at least as much reach as selecting any other candidate for that same stop count, so it cannot exclude a station or destination that an alternative choice would reach.

By applying this exchange at every required stop, the greedy process maintains the greatest achievable reach for its number of stops. The first stop count that reaches `target` is therefore minimum.

#### Complexity detail

Each of the $n$ stations is inserted into the heap once and removed at most once. Heap operations cost $O(\log n)$, so total time is $O(n\log n)$. The heap can contain $O(n)$ fuel values, giving $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Dynamic programming by stop count:** Tracking the farthest distance reachable with each number of stops is correct but takes $O(n^2)$ time and $O(n)$ space.
- **Always stop at every reachable station:** It guarantees at least as much fuel but can use far more stops than necessary.
- **Choose the nearest station first:** Position alone does not capture usefulness; a farther reachable station may offer much more fuel.
- **Initial fuel reaches `target`:** Return `0` without using any station.
- **First station unreachable:** No later station can be reached either, so return `-1`.
- **Arrive with zero fuel:** Equality between reach and a station or `target` is sufficient.
- **Unused passed stations:** Their fuel remains eligible in the heap until selected or the journey ends.
- **Large distances and fuel values:** Reach totals may exceed 32-bit range, so fixed-width implementations should use a sufficiently wide integer type.

</details>
