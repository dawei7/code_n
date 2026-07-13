# Count Vowels Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1220 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-vowels-permutation](https://leetcode.com/problems/count-vowels-permutation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-vowels-permutation/).

### Goal
Count strings of length `n` made only from vowels where each character must follow the allowed transition rules. Return the count modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `n: int` - Required string length.

**Return value**

`int` - Number of valid vowel strings modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `5`

**Example 2**

- Input: `n = 2`
- Output: `10`

**Example 3**

- Input: `n = 5`
- Output: `68`

---

## Solution
### Approach
Track how many valid strings of the current length end in each vowel. For every new position, compute the next five counts from the previous counts according to the transition graph, applying the modulo after each step. The answer is the sum of the five counts after `n` positions.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)` because only five rolling counts are needed.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
