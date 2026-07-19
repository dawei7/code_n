# Minimum Speed to Arrive on Time

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) |
| Frontend ID | 1870 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You must take $N$ train rides in their given order to reach the office. `dist[i]` is the distance of ride `i`, and every train travels at one shared positive integer speed. The actual travel time of a ride is its distance divided by that speed.

Except for the final ride, the next train can depart only at an integer-hour mark. Finishing an earlier ride at a fractional time therefore adds a wait until the next integer hour; finishing exactly at an integer hour adds no wait. The final arrival is not rounded. Given the available time `hour`, return the smallest speed that arrives no later than the deadline, or `-1` when no valid speed up to the guaranteed bound can do so.

### Function Contract

**Inputs**

- `dist`: an integer list of $N$ positive ride distances, where $1 \le N \le 10^5$ and each distance is at most $10^5$.
- `hour`: the available time, with at most two decimal places.
- Let $U = 10^7$, the guaranteed maximum possible answer.

**Return value**

- Return the minimum positive integer speed that makes the total commute time at most `hour`.
- Return `-1` if no such speed exists.

### Examples

**Example 1**

- Input: `dist = [1,3,2], hour = 6`
- Output: `1`

At speed one, the rides finish at integer-hour marks and total exactly six hours.

**Example 2**

- Input: `dist = [1,3,2], hour = 2.7`
- Output: `3`

The first two departures occur at hours one and two; the last ride finishes after another $2/3$ hour.

**Example 3**

- Input: `dist = [1,3,2], hour = 1.9`
- Output: `-1`

Even at arbitrarily high speed, the two required departure boundaries consume at least two hours before the final ride.

### Required Complexity

- **Time:** $O(N\log U)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Evaluate one candidate speed**

For every ride except the last, add `ceil(dist[i] / speed)`, because the next departure cannot occur before that integer-hour boundary. Compute the ceiling with integer arithmetic as `(dist[i] + speed - 1) // speed`. Add the exact quotient `dist[-1] / speed` for the final ride, then compare the sum with `hour`.

**Use monotonic feasibility**

Increasing the speed never increases any rounded ride duration or the exact final duration. Thus infeasible speeds form a prefix of the positive integers and feasible speeds form a suffix. Binary-search the inclusive range from `1` through $U$, retaining the lower half when its midpoint is feasible and discarding it otherwise.

**Handle impossibility**

The first $N-1$ rides each require at least one integer-hour interval, regardless of speed. If `hour <= N - 1`, positive final travel time makes arrival impossible. After binary search, verify the remaining speed as well; this covers any instance for which even $U$ is insufficient.

#### Complexity detail

Each feasibility check scans the $N$ distances in $O(N)$ time. Binary search performs $O(\log U)$ checks, so total time is $O(N\log U)$. The search bounds and elapsed-time accumulator require $O(1)$ auxiliary space; the generator used to sum rounded rides does not materialize another array.

#### Alternatives and edge cases

- **Linear speed search:** Testing `1, 2, 3, ...` is correct but may require $O(NU)$ time when the minimum speed is large.
- **Binary search over floating-point speed:** The required answer is integral, so integer bounds avoid termination and rounding complications.
- **Round every ride:** Rounding the final ride upward is wrong because there is no subsequent departure to wait for.
- **Deadline at $N-1$:** It is impossible; the final positive-distance ride still needs nonzero time.
- **Single ride:** No departure waiting occurs, so only its exact travel time matters.
- **Exact integer arrival:** A ride ending at an integer hour adds no extra delay.
- **Answer at $U$:** The upper endpoint must remain searchable and can be the minimum valid speed.

</details>
