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
