# Index Pairs of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1065 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Trie, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [index-pairs-of-a-string](https://leetcode.com/problems/index-pairs-of-a-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/index-pairs-of-a-string/).

### Goal
Find every pair of indices `[i, j]` such that `text[i:j + 1]` is exactly one of the given words. Return the pairs sorted by starting index and then ending index.

### Function Contract
**Inputs**

- `text`: Search string.
- `words`: List of words to match as substrings.

**Return value**

Sorted list of index pairs `[start, end]`.

### Examples
**Example 1**

- Input: `text = "thestoryofleetcodeandme", words = ["story", "fleet", "leetcode"]`
- Output: `[[3, 7], [9, 13], [10, 17]]`

**Example 2**

- Input: `text = "ababa", words = ["aba", "ab"]`
- Output: `[[0, 1], [0, 2], [2, 3], [2, 4]]`

**Example 3**

- Input: `text = "abc", words = ["d"]`
- Output: `[]`

---

## Solution
### Approach
Build a trie from `words`. For each start position in `text`, walk forward through the trie while characters continue to match. Whenever a terminal trie node is reached, record the current `[start, end]` pair.

Since starts are processed from left to right and ends grow left to right for each start, the generated pairs are already in the required order.

### Complexity Analysis
- **Time Complexity**: `O(n * L + total_word_length)` in the worst case, where `L` is the maximum word length.
- **Space Complexity**: `O(total_word_length)` for the trie.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
