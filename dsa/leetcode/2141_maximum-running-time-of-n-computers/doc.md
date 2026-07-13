# Maximum Running Time of N Computers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2141 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-running-time-of-n-computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-running-time-of-n-computers/).

### Goal
Run `n` computers simultaneously for as long as possible using replaceable batteries. Each battery powers one computer at a time, and batteries may be moved instantly at integer times, but they cannot be recharged.

### Function Contract
**Inputs**

- `n`: the number of computers that must remain on together.
- `batteries`: available battery capacities in minutes.

**Return value**

The greatest whole number of minutes all `n` computers can run simultaneously.

### Examples
**Example 1**

- Input: `n = 2`, `batteries = [3, 3, 3]`
- Output: `4`

**Example 2**

- Input: `n = 2`, `batteries = [1, 1, 1, 1]`
- Output: `2`

**Example 3**

- Input: `n = 2`, `batteries = [10, 10]`
- Output: `10`

---

## Solution
### Approach
Binary-search a candidate runtime `t`. A battery can contribute at most `t` minutes toward this target, so feasibility is exactly `sum(min(capacity, t)) >= n * t`. This predicate is monotonic: if `t` is feasible, every shorter runtime is feasible too.

### Complexity Analysis
- **Time Complexity**: `O(m log(sum(batteries) / n))`, where `m` is the number of batteries
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
