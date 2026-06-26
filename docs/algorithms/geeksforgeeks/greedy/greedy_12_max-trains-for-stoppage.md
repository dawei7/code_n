# Maximum Trains for Stoppage

| | |
|---|---|
| **ID** | `greedy_12` |
| **Category** | greedy |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **GeeksForGeeks Equivalent** | [Maximum trains for which stoppage can be provided](https://www.geeksforgeeks.org/maximum-trains-stoppage-can-provided/) |

## Problem statement

You are given `N` trains with their `[arrival_time, departure_time, platform_number]`.
A station has `P` platforms. A platform can only host one train at a time. Two trains on the same platform are non-conflicting if departure\_time[train_1] \le arrival\_time[train_2].
Find the maximum number of trains that can successfully stop at the station without conflicting. (If a train encounters a conflict on its designated platform, it bypasses the station completely).

**Input:** Number of platforms `P`, and a list of `N` trains where each is `(arrival, departure, platform)`.
**Output:** An integer representing the maximum number of trains that can stop.

## When to use it

- When you encounter an Activity Selection problem that has been partitioned into multiple independent "buckets" or "channels".

## Approach

**1. The "Independent Buckets" Insight:**
This problem sounds like "Minimum Meeting Rooms" at first glance. However, there is a massive catch! The trains are *hardcoded* to specific platforms. Train A is assigned to Platform 1. We CANNOT move Train A to Platform 2 just because Platform 1 is busy!
Because the platforms are mutually exclusive and trains cannot be reassigned, this isn't one giant problem. It is `P` completely independent, smaller problems!

**2. Activity Selection per Platform:**
For any single platform, the problem is literally: "Given X trains with start and finish times, select the maximum number of non-overlapping trains."
This is the exact definition of the **Activity Selection (`greedy_01`)** algorithm!

**3. The Algorithm:**
1. Create a 2D list `platforms_list` of size `P+1` (using 1-based indexing for convenience).
2. Iterate through the `N` trains and append the tuple `(arrival, departure)` into the specific sub-list `platforms_list[train.platform]`.
3. Initialize a global `count = 0`.
4. Loop through every single platform from 1 to `P`.
5. For each platform's sub-list, sort it by **departure time** (finish time).
6. Run the standard Activity Selection greedy logic: Pick the first train. Then iterate through the rest. If the next train's arrival time \ge the last picked train's departure time, pick it and update the tracker! Add to `count`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_12: Max Trains for Stoppage.

A single platform can hold one train at a time. Given arrival
and departure times for n trains, find the maximum number that
can be served without overlap. Greedy: sort by departure, accept
a train iff its arrival is after the last accepted departure.
O(n log n) for the sort.
"""


def solve(arrivals, departures, n):
    if n == 0:
        return 0
    order = sorted(range(n), key=lambda i: (departures[i], arrivals[i]))
    count = 0
    last_departure = -1
    for i in order:
        if arrivals[i] >= last_departure:
            count += 1
            last_departure = departures[i]
    return count
```

</details>

## Walk-through

`P = 2`. Trains: `T1(10:00, 10:30, p=1)`, `T2(10:10, 10:20, p=1)`, `T3(10:25, 10:40, p=1)`, `T4(11:00, 11:30, p=2)`.
Convert times to integers for simplicity: `T1(1000, 1030, 1)`, `T2(1010, 1020, 1)`, `T3(1025, 1040, 1)`, `T4(1100, 1130, 2)`.

1. **Bucket the trains:**
   - `Platform 1`: `[(1000, 1030), (1010, 1020), (1025, 1040)]`.
   - `Platform 2`: `[(1100, 1130)]`.

2. **Process Platform 1:**
   - Sort by departure: `[(1010, 1020), (1000, 1030), (1025, 1040)]`.
   - Pick first: `(1010, 1020)`. `count = 1`. `last_dep = 1020`.
   - Check `(1000, 1030)`: `1000 >= 1020` NO.
   - Check `(1025, 1040)`: `1025 >= 1020` YES. `count = 2`. `last_dep = 1040`.
   - Platform 1 yields `2` trains.

3. **Process Platform 2:**
   - Sort by departure: `[(1100, 1130)]`.
   - Pick first. `count = 1`.
   - Platform 2 yields `1` train.

Result: `total_trains = 2 + 1 = 3`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N + P)$ |
| **Average** | $O(N \log N)$ | $O(N + P)$ |
| **Worst** | $O(N \log N)$ | $O(N + P)$ |

Bucketing the trains takes $O(N)$.
Sorting the sub-lists: In the worst-case, all N trains are assigned to a single platform. Sorting that platform takes $O(N \log N)$.
Processing the sub-lists takes $O(N)$ across all platforms.
Therefore, the time complexity is strictly bounded by the sorting step: $O(N \log N)$.
Space complexity is $O(N + P)$ to maintain the 2D bucketing array holding the N train tuples.

## Variants & optimizations

- **Minimum Platforms Required:** A much harder variation where trains do NOT have pre-assigned platforms, and you must calculate the minimum number of dynamic platforms required so that 0 trains are rejected. This is solved by separating all arrival and departure times into two sorted arrays, and using Two Pointers to track the maximum concurrent overlap (often called the Meeting Rooms II problem).

## Real-world applications

- **Airport Runway Scheduling:** Runways (platforms) are assigned to specific flight classes (e.g. heavy wide-body jets vs light prop planes). Air traffic controllers must maximize throughput on each physical runway independently.

## Related algorithms in cOde(n)

- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — The literal exact algorithm running inside the inner loop of this problem.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
