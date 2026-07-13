# Longest Palindrome by Concatenating Two Letter Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2131 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-palindrome-by-concatenating-two-letter-words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/).

### Goal
Choose and arrange some two-letter words so their concatenation is a palindrome, using each occurrence at most once. Return the greatest possible palindrome length.

### Function Contract
**Inputs**

- `words`: a list of lowercase strings, each exactly two characters long.

**Return value**

The maximum achievable palindrome length in characters.

### Examples
**Example 1**

- Input: `words = ["lc", "cl", "gg"]`
- Output: `6`

**Example 2**

- Input: `words = ["ab", "ty", "yt", "lc", "cl", "ab"]`
- Output: `8`

**Example 3**

- Input: `words = ["cc", "ll", "xx"]`
- Output: `2`

---

## Solution
### Approach
Count each word. Pair every non-palindromic word with its reverse, adding four characters per pair. For words with equal letters, use as many pairs of identical words as possible and place at most one unpaired word in the center.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(u)`, where `u` is the number of distinct words

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
