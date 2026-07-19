# String Compression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 443 |
| Difficulty | Medium |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/string-compression/) |

## Problem Description
### Goal
Given a mutable character array, divide it into maximal consecutive runs of equal characters. Encode each run by writing its character once, followed by the decimal digits of its length only when that length is greater than one.

Write the encoding into the beginning of the same array using constant extra space, and return the compressed prefix length. Counts of ten or more occupy several character positions, one per decimal digit. Only the first returned-length positions define the result; leftover array contents beyond them are irrelevant. Runs are based on adjacency, so separated occurrences of the same character are encoded independently.

### Function Contract
**Inputs**

- `chars`: a mutable list of single-character strings

**Return value**

- The native method returns the compressed length and leaves the compressed characters in the first positions of `chars`. The app-local `solve` returns `{"length": k, "prefix": chars[:k]}` so both parts of that outcome are verifiable.

### Examples
**Example 1**

- Input: `chars = ["a", "a", "b", "b", "c", "c", "c"]`
- Output: `{"length": 6, "prefix": ["a", "2", "b", "2", "c", "3"]}`

**Example 2**

- Input: `chars = ["a"]`
- Output: `{"length": 1, "prefix": ["a"]}`

**Example 3**

- Input: `chars = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]`
- Output: `{"length": 3, "prefix": ["a", "1", "2"]}`
