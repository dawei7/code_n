# Koko Eating Bananas

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 875 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) |

## Problem Description
### Goal
Koko has $n$ piles of bananas, with `piles[i]` bananas in the $i$th pile. The guards are away for exactly `h` hours. Before eating, Koko chooses one integer bananas-per-hour speed `k` that remains fixed throughout that time.

During each hour, she selects one pile and eats `k` bananas from it. If fewer than `k` bananas remain in that pile, she finishes the pile but does not begin another pile during the same hour. Koko wants to eat as slowly as possible while still finishing every pile before the guards return. Find the minimum integer speed `k` that lets her finish within `h` hours.

### Function Contract
**Inputs**

- `piles`: an array of $n$ positive pile sizes, where $1 \leq n \leq 10^4$ and $1 \leq \texttt{piles[i]} \leq 10^9$.
- `h`: the available number of hours, where $n \leq \texttt{h} \leq 10^9$.
- Let $M=\max(\texttt{piles})$.

**Return value**

Return the smallest positive integer `k` for which all piles can be consumed in at most `h` hours.

### Examples
**Example 1**

- Input: `piles = [3,6,7,11], h = 8`
- Output: `4`

**Example 2**

- Input: `piles = [30,11,23,4,20], h = 5`
- Output: `30`

With only one hour per pile, the speed must cover the largest pile.

**Example 3**

- Input: `piles = [30,11,23,4,20], h = 6`
- Output: `23`

One extra hour permits a smaller speed than in Example 2.

### Required Complexity
- **Time:** $O(n\log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn a candidate speed into a monotone feasibility test**

At speed $k$, a pile containing $p$ bananas requires $\lceil p/k\rceil$ hours because an hour cannot be shared between piles. Thus the total required time is

$$
H(k)=\sum_{p\in\texttt{piles}}\left\lceil\frac{p}{k}\right\rceil.
$$

In code, each term can be evaluated with `(pile + k - 1) // k`. Increasing `k` never increases $H(k)$, so infeasible speeds form a prefix of the positive integers and feasible speeds form the suffix that follows it.

**Binary-search the first feasible speed**

Speed `1` is the smallest possible candidate, while $M$ is always sufficient because it finishes every pile in one hour and `h >= n`. Maintain a closed interval containing the minimum feasible speed. For its midpoint, sum the required hours, stopping early if the sum already exceeds `h`. If the midpoint is feasible, keep it as the upper bound; otherwise, discard it and every smaller speed.

The interval invariant always retains the first feasible speed: monotonicity justifies removing the appropriate half, and both initial bounds contain the transition. When the bounds meet, their common value is feasible and every smaller speed has been excluded as infeasible, so it is the required minimum.

#### Complexity detail

Each feasibility test scans at most $n$ piles, and binary search performs $O(\log M)$ tests, giving $O(n\log M)$ time. The search uses only scalar bounds and counters, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Try speeds in increasing order:** This returns the correct minimum but may require $O(nM)$ time when the answer is large.
- **Use the average bananas per hour:** The ceiling cost is paid separately for every pile, so `ceil(sum(piles) / h)` is only a lower bound and can be infeasible.
- **Sort the piles:** Sorting does not make the feasibility sum cheaper and adds unnecessary $O(n\log n)$ work.
- **One hour per pile:** When `h == len(piles)`, the answer is exactly $M$.
- **Enough hours for one banana at a time:** When `h` is at least the total banana count, the minimum speed is `1`.
- **Single pile:** The same ceiling formula applies, and binary search finds `ceil(piles[0] / h)`.
- **Large totals:** Fixed-width implementations should accumulate $H(k)$ in a sufficiently wide integer type or stop once it exceeds `h`.

</details>
