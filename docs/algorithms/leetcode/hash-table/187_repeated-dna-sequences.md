# Repeated DNA Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `string_06` |
| Frontend ID | 187 |
| Difficulty | Medium |
| Topics | Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function |
| Official Link | [repeated-dna-sequences](https://leetcode.com/problems/repeated-dna-sequences/) |

## Problem Description & Examples
### Goal
Find the first index where pattern occurs in text using
the Rabin-Karp rolling-hash algorithm. Uses a base-256
polynomial hash mod a large prime; on a hash match we
verify by direct comparison to avoid false positives.
Requirement: O(n + m) average; worst-case O(n*m) on
spurious hash collisions (vanishingly rare in practice).
Source: https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

### Function Contract
**Inputs**

- `text`: the string to search in.
- `pattern`: the string to search for.

**Return value**

the first index of pattern in text, or -1 if not found.

### Examples
**Example 1**

- Input: `text = 'hello', pattern = 'll'`
- Output: `2`

**Example 2**

- Input: `text = 'aaaa', pattern = 'aa'`
- Output: `0`

**Example 3**

- Input: `text = 'abcde', pattern = 'xyz'`
- Output: `-1`

---

## Underlying Base Algorithm(s)
strings

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `TODO`
