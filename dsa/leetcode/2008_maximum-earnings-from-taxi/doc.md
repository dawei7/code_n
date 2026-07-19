# Maximum Earnings From Taxi

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2008 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-earnings-from-taxi/) |

## Problem Description

### Goal

A one-way road contains points labeled from $1$ through $n$ in the direction
your taxi travels. You begin at point $1$, intend to reach point $n$, and
cannot reverse direction.

Each passenger request is `[start, end, tip]`. Accepting it occupies the taxi
from `start` through `end` and earns `end - start + tip` dollars. At most one
passenger may ride at a time, although dropping one passenger and collecting
another at the same point is allowed. Choose a compatible sequence of requests
that maximizes total earnings.

### Function Contract

Let $R$ be the number of passenger requests.

**Inputs**

- `n`: the final road point, where $1\le n\le10^5$.
- `rides`: a list of $R$ triples `[start, end, tip]`, where
  $1\le R\le3\cdot10^4$, $1\le\texttt{start}<\texttt{end}\le n$, and
  $1\le\texttt{tip}\le10^5$.

**Return value**

Return the maximum total dollars obtainable from a non-overlapping sequence of
rides.

### Examples

**Example 1**

- Input: `n = 5, rides = [[2, 5, 4], [1, 5, 1]]`
- Output: `7`
- Explanation: Taking the first request earns `5 - 2 + 4 = 7`.

**Example 2**

- Input: `n = 20, rides = [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]`
- Output: `20`
- Explanation: Rides `3 -> 10`, `10 -> 12`, and `13 -> 18` earn $9$, $5$,
  and $6$.

**Example 3**

- Input: `n = 6, rides = [[1, 2, 1], [2, 4, 2], [4, 6, 1]]`
- Output: `9`
- Explanation: The rides touch only at endpoints, so all three may be taken.

### Required Complexity

- **Time:** $O(N+R)$
- **Space:** $O(N+R)$

<details>
<summary>Approach</summary>

#### General

**Turn each endpoint into a dynamic-programming state.** Group requests by
their ending point. Let `best[x]` be the greatest earnings possible after
reaching road point `x`. Moving without a passenger preserves the previous
value, so begin each state with `best[x] = best[x - 1]`.

**Evaluate every ride exactly when it becomes available.** For a request
`[start, x, tip]` ending at `x`, the best compatible history is already stored
at `best[start]`. Taking that ride produces
`best[start] + x - start + tip`. Maximize `best[x]` over the carry-forward
choice and every request ending there.

All transitions come from points no later than the current endpoint. By
induction, `best[start]` already represents the optimal compatible sequence
before a considered ride begins. The transition appends that ride without
overlap, including the permitted case where one ride ends exactly at
`start`. Conversely, every valid optimal sequence either takes no ride ending
at `x` or has some final ride ending there, so one of the evaluated choices
reconstructs its value. Thus `best[n]` is optimal.

#### Complexity detail

Here $N=n$ is the number of road positions and $R$ is the number of requests.
Creating the endpoint groups takes $O(N+R)$ space. The scan visits $N$ points
and processes each ride once, taking $O(N+R)$ time. The dynamic-programming
array and grouped rides use $O(N+R)$ space.

#### Alternatives and edge cases

- **Sort rides plus binary search:** Weighted interval scheduling over rides
  sorted by endpoint takes $O(R\log R)$ time and $O(R)$ space, which can avoid
  scanning unused road points but does not meet the requested linear bound.
- **Compare every pair of rides:** A direct compatibility transition over all
  earlier requests takes $O(R^2)$ time.
- Rides may share an endpoint; a drop-off and pickup at the same point are
  compatible.
- Skipping road segments earns nothing but may be necessary before a later,
  more profitable request.
- Earnings can exceed 32-bit integer range across many rides, so the result
  must retain the platform's wide integer value.

</details>
