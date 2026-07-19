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
