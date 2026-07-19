# Remove Stones to Minimize the Total

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1962 |
| Difficulty | Medium |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-stones-to-minimize-the-total/) |

## Problem Description
### Goal
An array `piles` records the number of stones in each pile. Perform exactly
`k` operations. In one operation, choose any pile of current size $p$ and
remove $\lfloor p/2\rfloor$ stones, leaving
$p-\lfloor p/2\rfloor$ stones.

The same pile may be selected more than once. Choose the piles so that the sum
of all remaining stones after the `k` operations is as small as possible, and
return that minimum total.

### Function Contract
**Inputs**

- `piles`: a list of $N$ positive pile sizes, where $1\le N\le10^5$ and each
  size is at most $10^4$.
- `k`: the exact number of operations $K$, where $1\le K\le10^5$.

**Return value**

- The minimum possible total number of stones after exactly $K$ operations.

### Examples
**Example 1**

- Input: `piles = [5, 4, 9], k = 2`
- Output: `12`

**Example 2**

- Input: `piles = [4, 3, 6, 7], k = 3`
- Output: `12`

**Example 3**

- Input: `piles = [9], k = 2`
- Output: `3`

### Required Complexity
- **Time:** $O(N+K\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Take the largest available reduction**

Operating on a pile of size $p$ removes $\lfloor p/2\rfloor$ stones. This
quantity is nondecreasing with $p$, so a currently largest pile offers a
largest immediate reduction. Store all pile sizes in a max-priority queue,
extract the largest, replace it with
`largest - largest // 2`, and repeat exactly $K$ times.

**Why the greedy choices remain optimal**

Each pile exposes a sequence of possible removal gains as it is repeatedly
chosen. That sequence never increases because the pile only becomes smaller.
At any step, the first unclaimed gain from each pile is available, while later
gains from that pile cannot be taken before it.

The priority queue always takes the largest available gain. If an optimal
schedule instead takes a smaller available gain first, exchanging that
operation with the greedy choice cannot reduce the stones removed, and the
remaining gain sequences are still feasible afterward. Repeating the exchange
aligns an optimum with every greedy operation. Maximizing removed stones
minimizes the remaining total.

#### Complexity detail

Building the heap from $N$ piles takes $O(N)$ time. Each of the $K$ operations
performs one removal and insertion in $O(\log N)$ time, giving
$O(N+K\log N)$ total time. The heap stores $N$ integers and uses $O(N)$ space.

#### Alternatives and edge cases

- **Scan for the largest pile each time:** This makes the same greedy choices
  but spends $O(N)$ per operation, for $O(KN)$ time.
- **Sort after every operation:** Reordering the complete array repeatedly is
  correct but costs $O(KN\log N)$ time.
- An odd pile keeps the extra stone because the operation removes the floor of
  half; for example, `9` becomes `5`.
- A pile of size one remains one when selected, but the operation still counts
  toward the required total.
- Tied largest piles are interchangeable because they offer equal reductions.

</details>
