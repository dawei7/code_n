# Maximum Number of Removable Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1898 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-removable-characters](https://leetcode.com/problems/maximum-number-of-removable-characters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-removable-characters/).

### Goal
Characters can be removed from `s` in the order listed by `removable`. Find the maximum number of removals after which `p` is still a subsequence of the remaining string.

### Function Contract
**Inputs**

- `s`: the original string.
- `p`: the subsequence that must remain.
- `removable`: indices in the order they may be removed.

**Return value**

Return the largest removable prefix length that keeps `p` as a subsequence.

### Examples
**Example 1**

- Input: `s = "abcacb", p = "ab", removable = [3,1,0]`
- Output: `2`

**Example 2**

- Input: `s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]`
- Output: `1`

**Example 3**

- Input: `s = "abcab", p = "abc", removable = [0,1,2,3,4]`
- Output: `0`

---

## Solution
### Approach
Binary search the number of removals. For a candidate `mid`, mark the first `mid` removable indices as deleted, then scan `s` to check whether `p` is still a subsequence. The predicate is monotonic: if `p` survives after `mid` removals, it survives after fewer removals.

### Complexity Analysis
- **Time Complexity**: `O((len(s) + len(removable)) log len(removable))`
- **Space Complexity**: `O(len(s))`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
