# Minimum Jumps to Reach Home

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1654 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-home/) |

## Problem Description
### Goal
A bug begins at position 0 on the nonnegative x-axis and wants to reach its home at position `x`. A forward jump always moves exactly `a` positions, while a backward jump always moves exactly `b` positions. The bug may pass beyond its home, but it may never land at a negative position or at any position listed in `forbidden`.

Two backward jumps may not occur consecutively; a forward jump resets that restriction. Return the fewest jumps that can land exactly on `x`, or `-1` when no legal route exists.

### Function Contract
**Inputs**

- `forbidden`: between 1 and 1000 distinct blocked positive positions, each at most 2000; `x` is not blocked.
- `a`: the forward jump length, where $1 \le a \le 2000$.
- `b`: the backward jump length, where $1 \le b \le 2000$.
- `x`: the target position, where $0 \le x \le 2000$.

Let $f=\lvert\texttt{forbidden}\rvert$, $M=\max(x,\max(\texttt{forbidden}))$, and $L=M+a+b$.

**Return value**

Return the minimum number of legal jumps from 0 to `x`, or `-1` if none exists.

### Examples
**Example 1**

- Input: `forbidden = [14, 4, 18, 1, 15], a = 3, b = 15, x = 9`
- Output: `3`

Three forward jumps follow `0 -> 3 -> 6 -> 9`.

**Example 2**

- Input: `forbidden = [8, 3, 16, 6, 12, 20], a = 15, b = 13, x = 11`
- Output: `-1`

**Example 3**

- Input: `forbidden = [1, 6, 2, 14, 5, 17, 4], a = 16, b = 9, x = 7`
- Output: `2`

One forward and one backward jump follow `0 -> 16 -> 7`.

### Required Complexity
- **Time:** $O(f+L)$
- **Space:** $O(f+L)$

<details>
<summary>Approach</summary>

#### General

**Represent the previous direction in the state.** Position alone does not determine the legal next moves: arriving after a backward jump forbids another backward jump, while arriving at the same position after a forward jump permits one. Use states `(position, last_was_backward)` so each state has an unambiguous transition set.

**Search states in jump-count order.** Breadth-first search begins with `(0, false)`. Every state can move forward by `a`; it can move backward by `b` only when its flag is false and the destination is nonnegative. Reject blocked destinations and states already visited. Because every edge represents one jump, the first dequeued state at position `x` has the minimum possible jump count.

**Bound the otherwise infinite axis.** No target or forbidden position exceeds $M$. Searching through $L=M+a+b$ allows every useful overshoot needed to combine one forward and one backward jump near that boundary. Traveling farther into the obstacle-free region cannot create a new alignment that requires more than this extra forward/backward margin; the redundant excursion can be removed from a shortest route. Thus states above $L$ need not enter the queue.

The visited key must include the direction flag. Marking only a position could discard a later arrival that enables a backward move and is therefore behaviorally different.

#### Complexity detail

There are at most two direction states for each integer position from 0 through $L$. Each state is enqueued once and has at most two transitions, so breadth-first search takes $O(L)$ time after building the $O(f)$ blocked set. Total time is $O(f+L)$ and the blocked set, visited set, and queue use $O(f+L)$ space.

#### Alternatives and edge cases

- **Depth-first search with memoization:** It can determine reachability within the same bounded state graph, but extra bookkeeping is needed to recover a minimum edge count; breadth-first search gives it directly.
- **Visited positions without direction:** This incorrectly merges states whose next backward move has different legality.
- **Linear-list membership:** Keeping blocked or visited states in lists preserves correctness but can make membership checks quadratic in the explored range.
- **Unbounded search:** Continuing forward forever when the target is unreachable prevents termination; a justified upper bound is required.
- If `x == 0`, the answer is zero before any jump.
- The bug may jump past `x` and later return by one legal backward jump.
- A forbidden first forward landing can make every route impossible.
- Consecutive backward destinations must never be generated, even when both positions are otherwise legal.
- Different direction states at the same coordinate must both remain discoverable.
- A common divisor of `a` and `b` that does not divide `x` can make the target unreachable even without useful obstacles.

</details>
