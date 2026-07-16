# Minimum Number of Days to Make m Bouquets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1482 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) |

## Problem Description
### Goal

A garden contains $N$ flowers in a fixed left-to-right order. The flower at index `i` blooms on day `bloomDay[i]`; from that day onward it is available for use. Each flower may belong to exactly one bouquet.

Make `m` bouquets, each from `k` adjacent flowers. The flowers of one bouquet must occupy consecutive garden positions, and bouquets cannot reuse flowers. Return the minimum day by which such a selection is possible. If the garden can never supply all `m` bouquets, return `-1`.

### Function Contract
**Inputs**

Let $N$ be the length of `bloomDay`, and define the inclusive bloom-day range

$$
D = \max(\texttt{bloomDay}) - \min(\texttt{bloomDay}) + 1.
$$

- `bloomDay`: an integer array of length $N$, with $1 \le N \le 10^5$.
- Every entry satisfies $1 \le \texttt{bloomDay[i]} \le 10^9$.
- `m`: the required number of bouquets, with $1 \le m \le 10^6$.
- `k`: the number of adjacent flowers per bouquet, with $1 \le k \le N$.
- In the app-local `solve` contract, the corresponding parameter name is `bloom_day`.

**Return value**

Return the smallest day on which at least `m` pairwise disjoint groups of `k` adjacent bloomed flowers can be formed, or `-1` when this is impossible.

### Examples
**Example 1**

- Input: `bloomDay = [1,10,3,10,2], m = 3, k = 1`
- Output: `3`
- Explanation: By day three, the flowers at positions zero, two, and four have bloomed, providing three one-flower bouquets.

**Example 2**

- Input: `bloomDay = [1,10,3,10,2], m = 3, k = 2`
- Output: `-1`
- Explanation: Three bouquets would require six distinct flowers, but the garden contains only five.

**Example 3**

- Input: `bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3`
- Output: `12`
- Explanation: On day seven, the unbloomed middle flower separates the garden into runs of lengths four and two, enough for only one bouquet. On day twelve, all seven positions are available and two disjoint groups of three can be selected.

### Required Complexity
- **Time:** $O(N \log D)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Rejecting an impossible flower requirement**

Every bouquet consumes exactly `k` different flowers, so `m * k` positions are necessary regardless of bloom days. If `m * k > N`, no day can make the request feasible and the answer is immediately `-1`. This check also prevents performing a binary search for a solution that cannot exist.

**Defining a monotone feasibility predicate**

For a proposed day `day`, mark a flower available precisely when `bloom_day[i] <= day`. If the required bouquets can be made on that day, they remain possible on every later day because flowers never become unavailable. Thus `can_make(day)` changes at most once, from false to true, across increasing days.

This false-then-true structure is what permits binary search for the first feasible day rather than simulating every day in the potentially billion-wide range.

**Counting disjoint adjacent bouquets**

Scan the garden from left to right while maintaining `adjacent`, the length of the current run of available flowers not yet assigned to a bouquet. An unavailable flower resets the run to zero because a bouquet cannot cross that position. Whenever `adjacent == k`, form one bouquet and reset `adjacent` to zero so none of those flowers can be reused.

This greedy grouping maximizes the number of bouquets within every available run. A run of length $r$ can contain exactly $\lfloor r/k \rfloor$ disjoint bouquets, and taking each group as soon as it reaches length `k` realizes that bound. The scan may return true as soon as it has formed `m` bouquets.

**Finding the first feasible day**

After the impossibility check, `min(bloom_day)` is a valid lower search bound and `max(bloom_day)` is guaranteed feasible because all flowers have bloomed and $m k \le N$. At each step, test the midpoint. If it is feasible, keep it as a candidate by moving the right bound to `mid`; otherwise discard it and every earlier day by moving the left bound to `mid + 1`.

The bounds converge on one day. All smaller days have been proven infeasible, while the converged day is feasible, so it is exactly the minimum waiting time required.

#### Complexity detail

The impossibility check and bound calculation take $O(N)$ time. Each feasibility test scans at most $N$ flowers using constant state. Binary search performs $O(\log D)$ tests over the inclusive day range, giving $O(N \log D)$ time overall. The scan and search retain only scalar counters and bounds, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Linear day simulation:** Test every integer day from the minimum bloom day upward. It is correct but can take $O(ND)$ time, which is prohibitive when bloom days differ by as much as $10^9$.
- **Linear scan over distinct bloom days:** Sort the $U$ distinct candidate days and test them one by one. This avoids empty numeric gaps but still takes $O(NU + U \log U)$ time in the worst case because it repeats the garden scan for every candidate.
- **Search only distinct bloom days:** Sort the unique values in `bloomDay` and binary-search that list. Feasibility changes only on bloom days, but building the candidates costs $O(N \log N)$ time and $O(N)$ space.
- **Activate flowers with a disjoint-set structure:** Process positions in bloom-day order, merge neighboring active segments, and track how many groups of size `k` they contribute. This can solve the problem in $O(N \log N)$ time but is substantially more intricate.
- **Ignoring adjacency:** Counting all flowers with `bloomDay[i] <= day` is insufficient because late flowers can split the available positions into short runs.
- **Reusing flowers:** Overlapping groups are invalid; resetting the run after forming a bouquet ensures each position is consumed at most once.
- **Exactly enough positions:** When $m k = N$, every flower must be available, so the answer is the maximum bloom day.
- **One flower per bouquet:** For `k = 1`, the answer is the day of the `m`-th flower to bloom.
- **One bouquet:** The task becomes finding the earliest day with a consecutive available run of length `k`.
- **Equal bloom days:** Several flowers may activate together; the first feasible day can equal that shared value.
- **Large products:** In fixed-width languages, evaluate $m k$ in a wide integer type before comparing it with $N$.

</details>
