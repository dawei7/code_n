# Random Pick with Blacklist

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 710 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Binary Search, Sorting, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/random-pick-with-blacklist/) |

## Problem Description
### Goal
Given an integer domain `[0, n)` and a list of distinct blacklisted values inside that domain, design a picker whose `pick()` method returns an integer that is not in the blacklist.

Every allowed integer must be returned with equal probability on each call. After preprocessing, repeated picks should run in constant expected time, and the design must not allocate an array or set proportional to `n`, which may be much larger than the blacklist. A pick does not remove its result, so the same allowed value may be returned again later.

### Function Contract
**Inputs**

- `n`: the exclusive upper bound of the integer domain
- `blacklist`: distinct forbidden values in `[0, n)`
- `draws`: app-local deterministic raw bucket indices in `[0, n - len(blacklist))`; the native method generates these uniformly at random

**Return value**

- The allowed value produced by remapping each raw draw

### Examples
**Example 1**

- Input: `n = 7, blacklist = [2,3,5], draws = [0,1,2,3,2]`
- Output: `[0,1,4,6,4]`

**Example 2**

- Input: `n = 4, blacklist = [0,1], draws = [0,1]`
- Output: `[2,3]`

**Example 3**

- Input: `n = 1, blacklist = [], draws = [0,0]`
- Output: `[0,0]`

### Required Complexity

- **Time:** $O(b + p)$
- **Space:** $O(b)$

<details>
<summary>Approach</summary>

#### General

**Shrink random choice to the allowed count**

Let `bound = n - b`, where `b` is the blacklist size. A random choice from `[0, bound)` has exactly as many outcomes as the allowed domain, but some of those low outcomes may themselves be blacklisted.

**Reserve high allowed replacements**

Values in `[bound, n)` are never generated directly. Put every blacklisted value in a set, then walk upward from `bound`, skipping blacklisted high values. Assign each blacklisted low value a distinct remaining high value.

**Pick through one hash lookup**

Generate a raw value below `bound`. Return its mapped replacement when present and the raw value otherwise. App-local `draws` expose these raw choices deterministically so correctness cases and benchmarks are reproducible.

**Why the output is uniform and legal**

Unblacklisted low values map to themselves. Every blacklisted low value maps one-to-one onto an unblacklisted high value, and the counts of those two sets are equal. The mapping is therefore a bijection from the `bound` equally likely raw outcomes to all allowed values, preserving uniform probability while excluding every blacklisted number.

#### Complexity detail

Building the blacklist set and at most one remap entry per blacklisted value takes expected $O(b)$ time and $O(b)$ space. Each of `p` picks uses one random draw and one expected constant-time hash lookup, so total time is $O(b + p)$.

#### Alternatives and edge cases

- **Materialize every allowed value:** random indexing is simple afterward, but initialization and memory take $O(n)$, which violates the large-domain requirement.
- **Rejection sampling:** repeatedly draw from `[0, n)` until the value is allowed; it is unbiased but can become arbitrarily slow when most values are blacklisted.
- **Sorted blacklist plus rank adjustment:** binary-search how many blocked values precede a candidate; it can achieve $O(\log b)$ per pick without a remap.
- An empty blacklist makes every raw draw map to itself.
- Blacklisted values at or above `bound` need no map entry because raw draws never select them directly.
- The remap must skip high values that are also blacklisted.
- Duplicate blacklist entries are excluded by the problem contract.

</details>
