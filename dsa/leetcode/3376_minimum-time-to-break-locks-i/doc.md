# Minimum Time to Break Locks I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3376 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Breadth-First Search, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-break-locks-i/) |

## Problem Description

### Goal

Bob must break every dungeon lock. Lock `i` requires the sword to hold at least `strength[i]` energy. The sword begins with zero energy and a growth factor $x=1$; after each minute, its energy increases by the current value of $x$. Bob may choose the order in which locks are attacked.

When enough energy has accumulated, Bob breaks one lock immediately. The sword's energy then resets to zero, while $x$ increases by `k`. Determine the minimum total number of elapsed minutes needed to break all locks. Waiting energy cannot carry across a broken lock, but the larger growth factor applies to every later lock.

### Function Contract

**Inputs**

- `strength`: A list of $n$ positive integers, where `strength[i]` is the energy required by lock `i`.
- `k`: The positive amount added to the sword's growth factor after each broken lock.

The constraints are $1\leq n\leq8$, $1\leq k\leq10$, and $1\leq\texttt{strength[i]}\leq10^6$.

**Return value**

- The minimum total time in minutes required to break all $n$ locks.

### Examples

**Example 1**

- Input: `strength = [3,4,1]`, `k = 1`
- Output: `4`
- Explanation: Break strengths `1`, `4`, and `3` using factors `1`, `2`, and `3`.

**Example 2**

- Input: `strength = [2,5,4]`, `k = 2`
- Output: `5`
- Explanation: One optimal order spends `2`, `2`, and `1` minutes as the factors become `1`, `3`, and `5`.

**Example 3**

- Input: `strength = [6,7]`, `k = 3`
- Output: `8`
- Explanation: Breaking strength `6` first takes six minutes; strength `7` then needs two minutes at factor four.
