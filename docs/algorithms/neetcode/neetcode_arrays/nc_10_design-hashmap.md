## Problem Description & Examples
### Goal
Design a HashMap without using any built-in hash table libraries.

Implement a `solve(operations)` function that processes operations: `['put', key, value]`, `['get', key]` (returns value or -1 if not found), `['remove', key]`.

### Function Contract
**Inputs**

- `operations`: List[List] - put/get/remove operations

**Return value**

List[int] - results of get operations

### Examples
**Example 1**

- Input: `[["put", 1, 10], ["get", 1], ["get", 2]]`
- Output: `[10, -1]`

**Example 2**

- Input: `operations = [["put", 2, 20], ["put", 2, 30], ["get", 2]]`
- Output: `[30]`

**Example 3**

- Input: `operations = [["put", 1, 5], ["remove", 1], ["get", 1]]`
- Output: `[-1]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
