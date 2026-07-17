# Average Waiting Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1701 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/average-waiting-time/) |

## Problem Description
### Goal

A restaurant has one chef and receives customers in the order listed by `customers`. Each pair contains that customer's arrival time and the time needed to prepare the order. Arrival times are sorted in non-decreasing order, and every customer gives the chef an order upon arriving.

The chef handles only one order at a time and preserves the input order. If the chef is idle when a customer arrives, preparation begins immediately; otherwise that customer waits until all earlier work finishes. A customer's waiting time covers the complete interval from arrival until their own order is finished. Return the average waiting time over all customers. An answer within $10^{-5}$ of the exact value is accepted.

### Function Contract
**Inputs**

- `customers`: a list of $n$ pairs `[arrival, preparation]` in service order
- `arrival` is the customer's arrival time and `preparation` is the duration of that order, with both values between $1$ and $10^4$.
- Arrival times are sorted in non-decreasing order, and $1 \le n \le 10^5$.

**Return value**

The arithmetic mean of `finish - arrival` across all customers, returned as a floating-point value.

### Examples
**Example 1**

- Input: `customers = [[1, 2], [2, 5], [4, 3]]`
- Output: `5.00000`

The orders finish at times `3`, `8`, and `11`, giving waits of `2`, `6`, and `7`; their average is `5`.

**Example 2**

- Input: `customers = [[5, 2], [5, 4], [10, 3], [20, 1]]`
- Output: `3.25000`

The waits are `2`, `6`, `4`, and `1`. The chef becomes idle before the final arrival, so that order starts at time `20` rather than at the previous finish time.

**Example 3**

- Input: `customers = [[1, 1], [2, 2], [3, 3]]`
- Output: `2.33333`

The corresponding waits are `1`, `2`, and `4`, whose average is $7 / 3$.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Carry the chef's next available time**

Maintain `finish`, the completion time of every order processed so far. For a customer arriving at `arrival`, preparation cannot begin before either the arrival or the previous completion. The start time is therefore `max(finish, arrival)`, and adding the current preparation duration gives the new `finish`.

This single value contains all relevant effects of earlier customers. Their individual arrival times no longer matter once their combined workload has determined when the chef becomes available. When there is a gap between customers, the maximum discards the stale earlier finish and correctly restarts the schedule at the new arrival.

**Accumulate complete arrival-to-finish intervals**

After computing a customer's completion time, add `finish - arrival` to a running total. This includes both any delay behind earlier orders and the customer's own preparation duration, exactly matching the definition of waiting time in the contract.

The input order is the mandated service order, so applying this recurrence from left to right uniquely reconstructs the chef's schedule. Each contribution is consequently the true waiting time for its customer. Divide the total by $n$ only after the scan so intermediate calculations remain exact integers.

#### Complexity detail

The algorithm performs constant work for each of the $n$ customers, taking $O(n)$ time. It stores only the current finish time and accumulated wait, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Recompute every prefix schedule:** rebuilding the chef's timeline from the first customer for every requested wait is correct but repeats work and takes $O(n^2)$ time.
- **Explicit waiting queue:** a queue can simulate pending customers, but the fixed service order means the single finish timestamp already represents all outstanding work.
- **Average incrementally:** repeatedly updating a floating-point mean is possible, but summing exact integer waits first is simpler and avoids accumulated rounding error.
- **Idle gap:** when `arrival > finish`, the chef starts at `arrival`; carrying the earlier finish directly would invent waiting time.
- **Simultaneous arrivals:** equal arrival times remain in their input order and accumulate behind one another.
- **Waiting-time meaning:** include the customer's own preparation duration, not only time spent before cooking starts.
- **Single customer:** the average equals that order's preparation time.
- **Large backlog:** integer totals may exceed individual input bounds, so fixed-width implementations need a sufficiently wide accumulator.

</details>
