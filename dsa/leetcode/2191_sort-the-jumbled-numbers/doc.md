# Sort the Jumbled Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2191 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sort-the-jumbled-numbers](https://leetcode.com/problems/sort-the-jumbled-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sort-the-jumbled-numbers/).

### Goal
Map every decimal digit through a supplied digit substitution, interpret each mapped digit sequence as a number, and stably sort the original values by those mapped numbers.

### Function Contract
**Inputs**

- `mapping`: a permutation-like length-10 array where digit `d` becomes `mapping[d]`.
- `nums`: nonnegative integers to sort.

**Return value**

The original integers ordered by mapped value; equal mapped values retain their input order.

### Examples
**Example 1**

- Input: `mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]`, `nums = [991, 338, 38]`
- Output: `[338, 38, 991]`

**Example 2**

- Input: `mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, `nums = [789, 456, 123]`
- Output: `[123, 456, 789]`

**Example 3**

- Input: `mapping = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`, `nums = [0, 1, 10]`
- Output: `[1, 0, 10]`

---

## Solution
### Approach
Compute a mapped numeric key for each value by replacing its digits in place order; handle zero as the one-digit representation `0`. Stable-sort pairs of `(mapped_key, original_index, original_value)` or rely on a stable sorting implementation keyed only by the mapped value.

### Complexity Analysis
- **Time Complexity**: `O(D + n log n)`, where `D` is the total number of input digits
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
