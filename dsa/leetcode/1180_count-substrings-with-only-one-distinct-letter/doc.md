# Count Substrings with Only One Distinct Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1180 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-substrings-with-only-one-distinct-letter](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/).

### Goal
Count all substrings that contain only one distinct character.

### Function Contract
**Inputs**

- `s`: Input string.

**Return value**

Number of single-character-type substrings.

### Examples
**Example 1**

- Input: `s = "aaaba"`
- Output: `8`

**Example 2**

- Input: `s = "aaaaaaaaaa"`
- Output: `55`

**Example 3**

- Input: `s = "abc"`
- Output: `3`

---

## Solution
### Approach
Split the string into maximal runs of equal characters. A run of length `L` contributes `L * (L + 1) / 2` substrings, because any start and end inside that run is valid.

Sum that contribution for every run.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
