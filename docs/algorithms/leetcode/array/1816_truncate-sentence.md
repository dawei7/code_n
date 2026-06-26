# Truncate Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1816 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [truncate-sentence](https://leetcode.com/problems/truncate-sentence/) |

## Problem Description & Examples
### Goal
Return only the first `k` words of a sentence.

### Function Contract
**Inputs**

- `s`: a sentence with words separated by single spaces.
- `k`: the number of words to keep.

**Return value**

Return the sentence prefix containing exactly the first `k` words.

### Examples
**Example 1**

- Input: `s = "Hello how are you Contestant", k = 4`
- Output: `"Hello how are you"`

**Example 2**

- Input: `s = "What is the solution to this problem", k = 4`
- Output: `"What is the solution"`

**Example 3**

- Input: `s = "chopper is not a tanuki", k = 5`
- Output: `"chopper is not a tanuki"`

---

## Underlying Base Algorithm(s)
Split the sentence into words and join the first `k`. Alternatively, scan characters until the `k`th word ends and return that prefix.

---

## Complexity Analysis
- **Time Complexity**: `O(len(s))`
- **Space Complexity**: `O(len(s))` with split, or `O(1)` extra when scanning
