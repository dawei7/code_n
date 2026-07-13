# Find K-Length Substrings With No Repeated Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1100 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-k-length-substrings-with-no-repeated-characters](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/).

### Goal
Count substrings of length `k` whose characters are all distinct.

### Function Contract
**Inputs**

- `s`: Input string.
- `k`: Required substring length.

**Return value**

Number of length-`k` substrings with no repeated characters.

### Examples
**Example 1**

- Input: `s = "havefunonleetcode", k = 5`
- Output: `6`

**Example 2**

- Input: `s = "home", k = 5`
- Output: `0`

**Example 3**

- Input: `s = "abcabc", k = 3`
- Output: `4`

---

## Solution
### Approach
Use a sliding window with character counts. Expand the right side one character at a time and shrink the left side whenever the window exceeds length `k`. When the window length is exactly `k`, it is valid if the number of distinct characters is also `k`.

For lowercase English letters, this can be implemented with a small fixed-size count array; otherwise a hash map works.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `s`.
- **Space Complexity**: `O(min(k, alphabet_size))`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
