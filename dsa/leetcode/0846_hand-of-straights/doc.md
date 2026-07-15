# Hand of Straights

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 846 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/hand-of-straights/) |

## Problem Description
### Goal
Alice has a collection of cards, each labeled with an integer. She wants to rearrange every card into groups containing exactly `groupSize` cards. Within each group, the card values must be consecutive integers; repeated values are allowed only when separate physical cards supply them to one or more groups.

Given the values in `hand` and the required group size, determine whether all cards can be partitioned into such consecutive groups. Every card must belong to exactly one group, so an unused card or a group with fewer than `groupSize` cards makes the arrangement invalid.

### Function Contract
**Inputs**

- `hand`: an integer array of length $n$, where $1 \leq n \leq 10^4$ and $0 \leq \texttt{hand[i]} \leq 10^9$.
- `group_size`: the app-local name for LeetCode's `groupSize`, with $1 \leq \texttt{group\_size} \leq n$.

**Return value**

Return `true` if all cards can be rearranged into groups of `group_size` consecutive values; otherwise return `false`.

### Examples
**Example 1**

- Input: `hand = [1,2,3,6,2,3,4,7,8], group_size = 3`
- Output: `true`

One valid partition is `[1,2,3]`, `[2,3,4]`, and `[6,7,8]`.

**Example 2**

- Input: `hand = [1,2,3,4,5], group_size = 4`
- Output: `false`

Five cards cannot all be placed into groups of four.

**Example 3**

- Input: `hand = [1,2,2,3,3,4], group_size = 3`
- Output: `true`

The cards form `[1,2,3]` and `[2,3,4]`.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The smallest remaining card fixes a group start**

Count the available copies of every value and process distinct values in ascending order. If the smallest value still present is $x$, it cannot be placed after a smaller card: no smaller remaining value exists to begin that group. Therefore every remaining copy of $x$ must start a group containing $x,x+1,\ldots,x+\texttt{group\_size}-1$.

Let `copies = counts[start]`. For each value in that consecutive interval, require at least `copies` available cards and subtract that many. If any count is smaller, those unavoidable groups cannot be completed, so no partition exists. Otherwise, all copies of the current start are consumed and the scan continues to the next sorted value with a positive count.

This greedy choice is forced rather than merely convenient. Any valid arrangement must place the smallest remaining cards at the beginnings of their groups, and consuming their required successors leaves exactly the residual instance that later starts must solve. Repeating the argument either constructs a partition of every card or identifies the first impossible successor.

Before processing counts, reject when `len(hand) % group_size != 0`, because complete equal-sized groups cannot cover a non-divisible number of cards.

#### Complexity detail

Building the frequency map takes $O(n)$ time, and sorting at most $n$ distinct values takes $O(n\log n)$. Across all successful starts, each loop operation removes at least one card, so the consecutive-range work totals $O(n)$. The overall time is $O(n\log n)$ and the counts plus sorted keys use $O(n)$ space.

#### Alternatives and edge cases

- **Min-heap of distinct values:** Repeatedly taking the smallest live value also implements the forced greedy choice in $O(n\log n)$ time, but stale heap entries and synchronized counts add bookkeeping.
- **Repeated minimum search:** Calling `min(counts)` after deleting every exhausted key is correct, but rescans the remaining keys and can take $O(n^2)$ time.
- **Sorted card list with open groups:** Tracking how many groups expect each next value can remain $O(n\log n)$, though its state is less direct than subtracting forced batches.
- **Non-divisible hand size:** If $n$ is not a multiple of `group_size`, a complete partition is impossible immediately.
- **Group size one:** Every card forms its own valid group, including duplicate and widely separated values.
- **Duplicate cards:** Multiple copies of a start force the same number of parallel consecutive groups.
- **Large gaps:** A gap is harmless only after all groups below it have already closed; otherwise the first missing successor causes failure.
- **Zero-valued cards:** Zero is an ordinary possible start because card values are nonnegative.

</details>
