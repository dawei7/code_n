# Split Strings by Separator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2788 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [split-strings-by-separator](https://leetcode.com/problems/split-strings-by-separator/) |

## Problem Description & Examples
### Goal
Given a list of strings and a specific character separator, decompose each string in the list into smaller substrings based on the occurrences of the separator. The final result should be a flattened list containing all non-empty substrings extracted from the original strings, preserving their relative order.

### Function Contract
**Inputs**

- `words`: A list of strings (`List[str]`) to be processed.
- `separator`: A single character (`str`) used as the delimiter for splitting.

**Return value**

- A list of strings (`List[str]`) containing all non-empty segments resulting from the split operations.

### Examples
**Example 1**

- Input: `words = ["one.two.three","four.five","six"], separator = "."`
- Output: `["one","two","three","four","five","six"]`

**Example 2**

- Input: `words = ["$easy$","$problem$"], separator = "$"`
- Output: `["easy","problem"]`

**Example 3**

- Input: `words = ["|||"], separator = "|"`
- Output: `[]`

---

## Underlying Base Algorithm(s)
The solution utilizes string traversal and the standard library's string splitting mechanism. By iterating through each word in the input list and applying a split operation, we filter out empty strings (which occur when the separator appears at the start, end, or consecutively) to produce the final flattened collection.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the total number of characters across all strings in the input list. Each character is visited once during the split and filtering process.
- **Space Complexity**: `O(N)`, as the output list stores the resulting substrings, which in the worst case (no separators) occupies space proportional to the input size.
