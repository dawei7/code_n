## Description

You have `n` bulbs in a row numbered from `1` to `n`. Initially, all the bulbs are turned off. We turn on **exactly one** bulb every day until all bulbs are on after `n` days.

You are given an array `bulbs` of length `n` where $\text{bulbs}[i] = x$ means that on the $(i+1)^th$ day, we will turn on the bulb at position `x` where `i` is **0-indexed** and `x` is **1-indexed.**

Given an integer `k`, return *the **minimum day number** such that there exists two **turned on** bulbs that have **exactly** `k` bulbs between them that are **all turned off**. If there isn't such day, return `-1`.*
### Function Contract

$solve(bulbs: \text{list}[int], k: int) -> int$

**Inputs**

- `bulbs`: a permutation of the one-based bulb positions. At zero-based index `i`, $\text{bulbs}[i]$ is the position switched on during day $i + 1$.
- `k`: the exact number of bulbs that must remain off strictly between two bulbs that are on.

**Return value**

Return the earliest one-based day when such a pair of lit endpoints exists. Return `-1` when no day satisfies the condition.

### Examples

#### Example 1

- **Input:** $bulbs = [1,3,2], k = 1$
- **Output:** `2`
- **Explanation:**
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
#### Example 2

- **Input:** $bulbs = [1,2,3], k = 1$
- **Output:** `-1`
### Constraints

- $n = \text{bulbs.length}$

- $1 \le n \le 2 * 10^{4}$

- $1 \le \text{bulbs}[i] \le n$

- `bulbs` is a permutation of numbers from `1` to `n`.

- $0 \le k \le 2 * 10^{4}$