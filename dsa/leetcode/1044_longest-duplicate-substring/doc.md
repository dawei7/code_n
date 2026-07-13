# Longest Duplicate Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1044 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Binary Search, Sliding Window, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-duplicate-substring](https://leetcode.com/problems/longest-duplicate-substring/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-duplicate-substring/).

### Goal
Return any longest substring that appears at least twice in `s`. The occurrences may overlap.

### Function Contract
**Inputs**

- `s`: Lowercase English string.

**Return value**

One longest duplicated substring, or an empty string if no duplicate substring exists.

### Examples
**Example 1**

- Input: `s = "banana"`
- Output: `"ana"`

**Example 2**

- Input: `s = "abcd"`
- Output: `""`

**Example 3**

- Input: `s = "aaaaa"`
- Output: `"aaaa"`

---

## Solution
### Approach
Binary search the answer length. For a candidate length `L`, use a rolling hash over all length-`L` windows and record hashes already seen. When a hash repeats, compare or otherwise verify the substrings to avoid treating collisions as proof.

If a duplicate of length `L` exists, try a longer length; otherwise try shorter. Keep the best substring found during successful checks.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` expected with rolling hashes, where `n` is the length of `s`.
- **Space Complexity**: `O(n)` for the hashes seen during one check.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
