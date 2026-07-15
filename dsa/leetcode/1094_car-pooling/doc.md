# Car Pooling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1094 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/car-pooling/) |

## Problem Description

### Goal

A car begins with `capacity` empty seats and travels only east, so it cannot turn around and revisit a location to the west. Locations are measured in kilometers east of the car's starting point.

Each entry `trips[i] = [numPassengers_i, from_i, to_i]` describes a group that enters at `from_i` and leaves at `to_i`. Determine whether the car can pick up and drop off every group without the number of passengers on board ever exceeding `capacity`.

### Function Contract

**Inputs**

- `trips`: a list of $n$ triples `[numPassengers, from, to]`, where $1 \leq n \leq 1000$, $1 \leq \texttt{numPassengers} \leq 100$, and $0 \leq \texttt{from} < \texttt{to} \leq 1000$.
- `capacity`: the number of seats, with $1 \leq \texttt{capacity} \leq 10^5$.

**Return value**

Return `True` if every trip can be served without exceeding `capacity`; otherwise return `False`.

### Examples

**Example 1**

- Input: `trips = [[2, 1, 5], [3, 3, 7]], capacity = 4`
- Output: `False`

At location 3, both groups are aboard and require five seats.

**Example 2**

- Input: `trips = [[2, 1, 5], [3, 3, 7]], capacity = 5`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Record changes instead of every occupied segment.** For each trip, add its passenger count at `from` and subtract the same count at `to`. The locations are restricted to $[0,1000]$, so these changes fit in a fixed array. A prefix sum from west to east then gives the number of passengers in the car after all events at each location.

**Drop-offs and pickups share one net event.** A group traveling to location `x` is no longer aboard when another group starts at `x`. Adding both the negative drop-off change and positive pickup change at the same index produces the correct net load; no arbitrary event ordering is needed.

Before the first event, the load is zero. At every later location, the prefix sum includes exactly the trips whose pickup has occurred and whose drop-off lies farther east. It therefore equals the actual load on the next eastbound segment. If any prefix exceeds `capacity`, that segment is impossible; if none does, every group can be served.

#### Complexity detail

Writing the two changes for each of the $n$ trips takes $O(n)$ time. Scanning the 1001 possible locations is $O(1001)=O(1)$ under the fixed contract, so total time is $O(n)$. The 1001-entry difference array is fixed-size auxiliary storage and therefore $O(1)$.

#### Alternatives and edge cases

- **Sorted event map:** Store pickup and drop-off deltas by location and sort the occupied locations. This handles an unbounded coordinate range but costs $O(n \log n)$ time in the worst case.
- **Min-heap of active trips:** Sort by pickup and remove completed trips by drop-off. It is useful when coordinates are not bounded, but requires $O(n \log n)$ time and $O(n)$ space.
- **Rescan all trips at every pickup:** Directly summing active groups is correct but can take $O(n^2)$ time.
- **Drop-off equals another pickup:** Passengers ending at that location free their seats before travel continues, which the net difference handles automatically.
- **Exact capacity:** A load equal to `capacity` is valid; only a strictly larger load fails.
- **Immediate overload:** The scan may return `False` as soon as any prefix sum exceeds the available seats.

</details>
