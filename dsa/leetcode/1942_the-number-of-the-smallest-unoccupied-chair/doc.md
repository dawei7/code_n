# The Number of the Smallest Unoccupied Chair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1942 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/) |

## Problem Description
### Goal
There are $N$ friends, numbered from $0$ through $N-1$, attending a party
with an unlimited supply of chairs numbered $0,1,2,\ldots$. Whenever a friend
arrives, that friend occupies the currently unoccupied chair with the smallest
number.

Each friend has a distinct arrival time and a later leaving time. A chair
becomes available at the exact moment its occupant leaves, so a friend arriving
at that same time may immediately take it. Given every friend's interval and
the index `targetFriend`, return the chair assigned to that particular friend.

### Function Contract
**Inputs**

- `times`: an array of $N$ pairs where `times[i] = [arrival, leaving]`
  describes friend `i`; $2 \le N \le 10^4$,
  $1 \le \textit{arrival} < \textit{leaving} \le 10^5$, and all arrival
  times are distinct.
- `targetFriend`: an integer in the range $0$ through $N-1$.

**Return value**

- The number of the chair that `targetFriend` occupies upon arriving.

### Examples
**Example 1**

- Input: `times = [[1, 4], [2, 3], [4, 6]], targetFriend = 1`
- Output: `1`
- Explanation: Friend 0 takes chair 0, so friend 1 takes chair 1.

**Example 2**

- Input: `times = [[3, 10], [1, 5], [2, 6]], targetFriend = 0`
- Output: `2`
- Explanation: Chairs 0 and 1 are occupied when friend 0 arrives.

**Example 3**

- Input: `times = [[1, 2], [2, 3]], targetFriend = 1`
- Output: `0`
- Explanation: Chair 0 is released exactly when friend 1 arrives.

### Required Complexity
- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Process friends in chronological order**

Attach each friend's original index to that friend's interval, then sort the
records by arrival time. This produces the exact order in which chair choices
must be made while preserving the identity of `targetFriend`.

Maintain an occupied min-heap of pairs `(leaving, chair)`. Before handling an
arrival at time $t$, remove every occupied entry whose leaving time is at most
$t$ and insert its chair into an available-chair min-heap. Using “at most” is
essential: it makes a chair reusable when a departure and arrival occur at the
same moment.

**Assign the smallest possible chair**

If the available heap is nonempty, remove its smallest chair. Otherwise, use
the next chair number that has never been assigned and advance that number.
Return immediately when the arriving friend is `targetFriend`; later events
cannot change the chair already assigned.

Every chair in the available heap has been released, and every smaller chair
absent from that heap is still occupied. When no released chair exists, the
never-used chair is the smallest number beyond all chairs allocated so far.
Thus each assignment is precisely the smallest unoccupied chair required by
the rules, including the target's assignment.

#### Complexity detail

Sorting $N$ arrival records costs $O(N\log N)$. Each processed friend enters
and leaves the occupied heap at most once and each chair enters and leaves the
available heap at most once; every heap operation costs $O(\log N)$. The total
time is therefore $O(N\log N)$. The sorted records and two heaps together use
$O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Ordered event simulation:** Sort separate arrival and departure events and
  maintain an ordered set of free chairs. This can meet the same asymptotic
  bound, but departures must be ordered before arrivals at equal timestamps.
- **Linear chair search:** Track occupancy in an array and scan from chair 0
  for every arrival. It is straightforward but can require $O(N^2)$ time when
  many friends overlap.
- A chair whose friend leaves at time $t$ is available to a friend arriving at
  time $t$.
- Several friends may share a leaving time, so all qualifying occupied-heap
  entries must be released before assigning a chair.
- Original friend indices do not describe arrival order; sorting must retain
  each index to recognize `targetFriend`.
- When every earlier friend is still present, the target receives the next
  previously unused chair.
- When the target arrives first, the answer is chair 0.

</details>
