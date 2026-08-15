# The Latest Time to Catch a Bus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2332 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-latest-time-to-catch-a-bus/) |

## Problem Description

### Goal

The unique values in `buses` are bus departure times, and the unique values in
`passengers` are existing passenger arrival times. Each bus holds at most
`capacity` people. At a departure, all waiting passengers board if they fit;
otherwise, those with the earliest arrival times take the available seats.

Choose an arrival time for yourself. You may board a bus departing at time
`x` when you arrive at time `y` with $y \le x$ and a seat remains when your
turn is reached. Your time cannot equal any existing passenger's arrival time.
Neither input array is guaranteed to be sorted. Return the latest arrival time
that still lets you board some bus.

### Function Contract

Let $b=\lvert\texttt{buses}\rvert$ and
$p=\lvert\texttt{passengers}\rvert$.

**Inputs**

- `buses`: Between 1 and $10^5$ unique departure times in
  $[2,10^9]$.
- `passengers`: Between 1 and $10^5$ unique existing arrival times in
  $[2,10^9]$.
- `capacity`: The common bus capacity, with
  $1 \le \texttt{capacity} \le 10^5$.

**Return value**

The greatest unoccupied arrival time at which you can board a bus under the
earliest-arrival-first rule.

### Examples

#### Example 1

- **Input:** `buses = [10,20]`, `passengers = [2,17,18,19]`, `capacity = 2`
- **Output:** `16`
- **Explanation:** Arriving at 16 puts you ahead of the passengers at 17 and 18
  for the final bus; 17 is unavailable.

#### Example 2

- **Input:** `buses = [20,30,10]`,
  `passengers = [19,13,26,4,25,11,21]`, `capacity = 2`
- **Output:** `20`
- **Explanation:** After the earlier buses leave, arrival time 20 secures a place
  on the bus at 30 ahead of the passenger at 21.

#### Example 3

- **Input:** `buses = [10]`, `passengers = [10]`, `capacity = 1`
- **Output:** `9`
- **Explanation:** The full bus requires arriving before its passenger, and 9 is
  the latest unoccupied choice.
