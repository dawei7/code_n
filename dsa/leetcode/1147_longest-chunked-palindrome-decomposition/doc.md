# Longest Chunked Palindrome Decomposition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1147 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming, Greedy, Rolling Hash, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-chunked-palindrome-decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/).

### Goal
Split `text` into the maximum number of non-empty chunks such that the first chunk equals the last chunk, the second equals the second-to-last, and so on.

### Function Contract
**Inputs**

- `text`: Input string.

**Return value**

Maximum number of chunks in a valid chunked palindrome decomposition.

### Examples
**Example 1**

- Input: `text = "ghiabcdefhelloadamhelloabcdefghi"`
- Output: `7`

**Example 2**

- Input: `text = "merchant"`
- Output: `1`

**Example 3**

- Input: `text = "antaprezatepzapreanta"`
- Output: `11`

---

## Solution
### Approach
Greedily match the smallest possible equal prefix and suffix. Build a left chunk from the front and a right chunk from the back. Whenever they become equal, those two chunks can be fixed as an outer pair, and the search restarts inside the remaining middle substring.

Choosing the shortest matching outer chunks leaves the largest possible middle region, which maximizes the number of chunks.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` with direct string accumulation/comparison in the worst case; rolling hash can reduce comparison overhead.
- **Space Complexity**: `O(n)` for intermediate chunk strings or recursion state.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
