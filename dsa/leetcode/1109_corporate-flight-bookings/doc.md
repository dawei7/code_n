# Corporate Flight Bookings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1109 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/corporate-flight-bookings/) |

## Problem Description

### Goal

There are `n` flights labeled consecutively from `1` through `n`. You receive `bookings`, where each entry `[first, last, seats]` records that `seats` seats were reserved on every flight from `first` through `last`, inclusive.

Several bookings may overlap, so a flight's final reservation count is the sum of every booking range that contains its label. Return an array `answer` of length `n` in flight-label order: `answer[i]` is the total number of seats reserved for flight `i + 1`.

### Function Contract

**Inputs**

- `bookings`: $B$ rows `[first, last, seats]`, with `1 <= first <= last <= n` and a positive `seats` value.
- `n`: the number of flights, labeled from `1` through `n`.

**Return value**

- An integer array of length $n$ whose zero-based position `i` contains the total reserved seats for flight `i + 1`.

### Examples

**Example 1**

- Input: `bookings = [[1,2,10],[2,3,20],[2,5,25]]`, `n = 5`
- Output: `[10,55,45,25,25]`

The first booking adds 10 to flights 1 and 2, the second adds 20 to flights 2 and 3, and the third adds 25 to flights 2 through 5. Adding those contributions by flight gives the output.

**Example 2**

- Input: `bookings = [[1,2,10],[2,2,15]]`, `n = 2`
- Output: `[10,25]`

### Required Complexity

- **Time:** $O(B+n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Represent each inclusive range by two boundary changes:** Allocate a difference array with one extra sentinel position. For a booking `[first, last, seats]`, execute `diff[first - 1] += seats` to begin its contribution at the zero-based position for `first`, then execute `diff[last] -= seats` to end that contribution immediately after flight `last`. The sentinel makes the second update valid even when `last = n`.

**Recover flight totals with a prefix sum:** Scan positions `0` through `n - 1`, updating `current += diff[i]`. The running value contains every booking that has started but not yet ended, exactly the bookings whose inclusive range contains flight `i + 1`. Append that value to the answer.

For any booking, the prefix sum includes its `seats` contribution beginning at `first - 1`. The negative boundary is not encountered until index `last`, so the contribution remains present through output index `last - 1`, corresponding to flight `last`, and disappears afterward. Summing these independent boundary pairs therefore gives precisely the total contribution of all bookings at every flight.

#### Complexity detail

Each of the $B$ bookings performs two constant-time boundary updates, and one prefix scan visits the $n$ flights. Time is $O(B+n)$. The difference array and returned answer each have length proportional to $n$, so auxiliary storage is $O(n)$; if the output array itself is reused for differences, extra space beyond the required result can be $O(1)$.

#### Alternatives and edge cases

- **Update every covered flight:** Loop from `first - 1` through `last - 1` for each booking. It is straightforward and correct but costs $O(Bn)$ when many bookings cover most flights.
- **Event map plus ordered sweep:** Store boundary changes only at touched labels and process them in order. It can help for sparse labels in a different output contract, but this problem must still produce all $n$ flight totals.
- **Segment tree with lazy propagation:** Supports interleaved range updates and queries, but all updates arrive before one final full output, so the difference array is simpler and asymptotically faster.
- **Single-flight booking:** When `first = last`, the positive and negative boundaries are adjacent and affect exactly one answer position.
- **Full-range booking:** When `[first, last] = [1, n]`, its contribution begins at index zero and ends at the sentinel, so every flight receives it.
- **Overlapping ranges:** Boundary changes add together; the prefix sum naturally carries their combined seat counts through the overlap.
- **Adjacent ranges:** Ending one contribution at the same difference index where another begins preserves both ranges' inclusive endpoints correctly.

</details>
