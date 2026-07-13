# Groups of Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2157 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [groups-of-strings](https://leetcode.com/problems/groups-of-strings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/groups-of-strings/).

### Goal
Group words by connectivity under single-letter transformations. Two words are directly connected when one can be obtained from the other by adding, deleting, or replacing one letter; transformation order does not matter because each word contains distinct letters. Return the number of connected groups and the size of the largest group.

### Function Contract
**Inputs**

- `words`: lowercase words with no repeated letter within a word.

**Return value**

`[group_count, largest_group_size]`.

### Examples
**Example 1**

- Input: `words = ["a", "b", "ab", "cde"]`
- Output: `[2, 3]`

**Example 2**

- Input: `words = ["a", "ab", "abc"]`
- Output: `[1, 3]`

**Example 3**

- Input: `words = ["ab", "cd"]`
- Output: `[2, 1]`

---

## Solution
### Approach
Encode each word as a 26-bit mask and create a disjoint-set node for each mask. Union masks that differ by adding or deleting one set bit. To capture replacement efficiently, remove each present letter and map the resulting 25-bit-or-smaller mask to the first word that produced it; words sharing such a deletion form are one replacement apart and should be unioned. Finally count roots and their component sizes.

### Complexity Analysis
- **Time Complexity**: `O(26n * alpha(n))`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
