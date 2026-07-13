# Single-Row Keyboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1165 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [single-row-keyboard](https://leetcode.com/problems/single-row-keyboard/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/single-row-keyboard/).

### Goal
Given a one-row keyboard layout and a word, compute the total finger movement needed to type the word. The finger starts at index `0`, and moving between two letters costs the absolute difference of their indices.

### Function Contract
**Inputs**

- `keyboard`: Permutation of the 26 lowercase letters.
- `word`: Word to type.

**Return value**

Total movement cost.

### Examples
**Example 1**

- Input: `keyboard = "abcdefghijklmnopqrstuvwxyz"`, `word = "cba"`
- Output: `4`

**Example 2**

- Input: `keyboard = "pqrstuvwxyzabcdefghijklmno"`, `word = "leetcode"`
- Output: `73`

**Example 3**

- Input: `keyboard = "abcdefghijklmnopqrstuvwxyz"`, `word = "abc"`
- Output: `2`

---

## Solution
### Approach
Build a map from each character to its keyboard index. Starting at position `0`, scan the word and add the distance from the current position to the next character's position.

### Complexity Analysis
- **Time Complexity**: `O(26 + m)`, where `m` is the length of `word`.
- **Space Complexity**: `O(1)`, because the alphabet size is fixed.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
