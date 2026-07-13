# Evaluate the Bracket Pairs of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1807 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [evaluate-the-bracket-pairs-of-a-string](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/).

### Goal
Replace every bracketed key in a string with its value from a knowledge list. Unknown keys become a question mark.

### Function Contract
**Inputs**

- `s`: a string containing lowercase text and parenthesized keys.
- `knowledge`: key-value pairs.

**Return value**

Return the evaluated string after replacing every `(key)` occurrence.

### Examples
**Example 1**

- Input: `s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]`
- Output: `"bobistwoyearsold"`

**Example 2**

- Input: `s = "hi(name)", knowledge = [["a","b"]]`
- Output: `"hi?"`

**Example 3**

- Input: `s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]`
- Output: `"yesyesyesaaa"`

---

## Solution
### Approach
Store the knowledge pairs in a hash map. Scan the string; when an opening parenthesis appears, collect characters until the closing parenthesis, look up the key, and append either the mapped value or `"?"`. Ordinary characters are appended directly.

### Complexity Analysis
- **Time Complexity**: `O(len(s) + total knowledge characters)`
- **Space Complexity**: `O(total knowledge characters)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
