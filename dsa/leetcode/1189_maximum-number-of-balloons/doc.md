# Maximum Number of Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1189 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-balloons](https://leetcode.com/problems/maximum-number-of-balloons/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-balloons/).

### Goal
Return how many instances of the word `"balloon"` can be formed from the characters of `text`, using each character at most once.

### Function Contract
**Inputs**

- `text`: Lowercase input string.

**Return value**

Maximum number of complete `"balloon"` words.

### Examples
**Example 1**

- Input: `text = "nlaebolko"`
- Output: `1`

**Example 2**

- Input: `text = "loonbalxballpoon"`
- Output: `2`

**Example 3**

- Input: `text = "leetcode"`
- Output: `0`

---

## Solution
### Approach
Count characters in `text`. The word `"balloon"` needs `b`, `a`, and `n` once, and `l` and `o` twice. The limiting ratio among those requirements is the answer.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`, since only lowercase letter counts are needed.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
