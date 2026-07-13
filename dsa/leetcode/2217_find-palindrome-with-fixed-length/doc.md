# Find Palindrome With Fixed Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2217 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-palindrome-with-fixed-length](https://leetcode.com/problems/find-palindrome-with-fixed-length/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-palindrome-with-fixed-length/).

### Goal
For each query, return the queried positive palindrome in increasing order among all palindromes with exactly `intLength` digits. Return `-1` when that many palindromes do not exist.

### Function Contract
**Inputs**

- `queries`: one-based ranks of requested palindromes.
- `intLength`: the required decimal digit length.

**Return value**

The palindrome for every query, or `-1` for an out-of-range rank.

### Examples
**Example 1**

- Input: `queries = [1, 2, 3, 4, 5, 90]`, `intLength = 3`
- Output: `[101, 111, 121, 131, 141, 999]`

**Example 2**

- Input: `queries = [2, 4, 6]`, `intLength = 4`
- Output: `[1111, 1331, 1551]`

**Example 3**

- Input: `queries = [1, 10]`, `intLength = 1`
- Output: `[1, -1]`

---

## Solution
### Approach
A palindrome is determined by its first `ceil(intLength / 2)` digits. The smallest valid prefix is the corresponding power of ten. For query `q`, add `q - 1` to that prefix; if it exceeds the prefix range, return `-1`. Otherwise mirror the prefix, omitting its final digit from the reflected half when the requested length is odd.

### Complexity Analysis
- **Time Complexity**: `O(q * intLength)`
- **Space Complexity**: `O(q)` for the output

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
