# Exam Room

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 855 |
| Difficulty | Medium |
| Topics | Design, Heap (Priority Queue), Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/exam-room/) |

## Problem Description
### Goal
An exam room has $n$ seats in one row, labeled from $0$ through $n-1$. When a student enters, they choose an empty seat that maximizes the distance to the closest seated student. If several seats provide the same maximum distance, the student must take the lowest-numbered one. An empty room always assigns seat `0`.

Design `ExamRoom` to preserve this rule across arrivals and departures. `seat()` places the next student and returns the chosen label. `leave(p)` removes the student at seat `p`; each departure is guaranteed to name an occupied seat.

### Function Contract
**Inputs**

- `n`: the number of seats, where $1 \leq n \leq 10^9$.
- `operations`: an app-local trace of $q$ calls, where $1 \leq q \leq 10^4$. Each entry is `["seat"]` or `["leave", p]`. A `seat` call occurs only while a seat is available.

**Return value**

Return one result per operation: the assigned seat for `seat`, and `null` for `leave`.

The native LeetCode artifact instead implements constructor `ExamRoom(n)` and the methods `seat()` and `leave(p)` directly.

### Examples
**Example 1**

- Input: `n = 10, operations = [["seat"],["seat"],["seat"],["seat"],["leave",4],["seat"]]`
- Output: `[0,9,4,2,null,5]`

**Example 2**

- Input: `n = 1, operations = [["seat"],["leave",0],["seat"]]`
- Output: `[0,null,0]`

**Example 3**

- Input: `n = 4, operations = [["seat"],["seat"],["seat"],["seat"]]`
- Output: `[0,3,1,2]`

### Required Complexity
- **Time:** $O(q\log q)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Represent available choices as gaps between occupied seats**

Use a free interval `(left, right)` for every pair of consecutive occupied boundaries. Virtual boundaries `-1` and `n` represent the room edges. The best seat for an interval is `0` when `left == -1`, `n - 1` when `right == n`, and `(left + right) // 2` otherwise.

Its distance is the full edge gap for a virtual boundary and half the gap for an interior interval. Store intervals in a priority heap ordered first by decreasing distance and then by increasing candidate seat, exactly matching the placement and tie rules.

**Split on arrival and merge on departure**

When `seat()` removes the best valid interval `(left, right)`, let its candidate be `p`. Replace the interval with `(left, p)` and `(p, right)`. Even intervals containing no empty seat remain in endpoint maps, because they identify neighboring occupied seats for a future departure.

For `leave(p)`, the map ending at `p` gives the left neighbor boundary and the map starting at `p` gives the right neighbor boundary. Remove those two intervals and insert their merged interval.

**Discard stale heap entries lazily**

A merge can invalidate an interval that remains buried in the heap. Keep an active interval set; `seat()` pops until it finds a pair still active. Each stale entry was created by an earlier update and is discarded at most once, so lazy removal preserves the amortized bound.

The active intervals always partition the row between consecutive occupied seats and virtual boundaries. Their candidates are exactly the locally best available seats. Selecting the globally highest-priority candidate therefore implements the required maximum distance and lowest-label tie break after every valid trace prefix.

#### Complexity detail

Each operation creates or invalidates only a constant number of intervals. Heap pushes and valid pops cost $O(\log q)$; stale entries are popped once over the entire trace, so processing $q$ calls takes $O(q\log q)$ amortized time. The heap, active set, endpoint maps, and output use $O(q)$ space.

#### Alternatives and edge cases

- **Sorted occupied list:** Scan every gap for `seat` and insert or remove in sorted order; it is simple and correct but can take $O(q^2)$ total time.
- **Balanced interval tree:** An ordered set augmented with the best gap supports logarithmic operations, but Python's standard library does not provide one directly.
- **Eager heap deletion:** Locating and removing arbitrary heap entries is linear; lazy invalidation avoids that cost.
- **Empty room:** The initial virtual interval chooses seat `0`.
- **One-seat room:** After its only student leaves, merging the two virtual-boundary intervals restores seat `0`.
- **Equal distances:** The heap's candidate-seat key selects the smaller label.
- **Boundary gaps:** Their full length matters because only one occupied endpoint constrains the student.
- **Adjacent occupied seats:** Their interval has no free candidate but must remain in endpoint maps for merging.
- **Leaving a boundary seat:** A virtual endpoint is merged just like an occupied neighbor.
- **Repeated reuse:** Departures and later arrivals may recreate an old interval; active-pair validation distinguishes its current validity.

</details>
