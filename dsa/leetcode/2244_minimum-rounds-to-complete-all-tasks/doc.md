# Minimum Rounds to Complete All Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2244 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-rounds-to-complete-all-tasks](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/).

### Goal
Complete all tasks in rounds, where each round must contain exactly two or three tasks of one difficulty. Find the minimum number of rounds, or report impossibility.

### Function Contract
**Inputs**

- `tasks`: task difficulty values.

**Return value**

The minimum rounds needed, or `-1` if any difficulty cannot be grouped.

### Examples
**Example 1**

- Input: `tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]`
- Output: `4`

**Example 2**

- Input: `tasks = [2, 3, 3]`
- Output: `-1`

**Example 3**

- Input: `tasks = [1, 1, 1, 1]`
- Output: `2`

---

## Solution
### Approach
Count tasks by difficulty. A frequency of one makes completion impossible. Every frequency of at least two is optimally grouped using as many triples as possible, with a remainder of one converted from `3 + 1` into `2 + 2`. The resulting round count is `ceil(frequency / 3)`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(u)`, where `u` is the number of difficulties

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
