# Design Compressed String Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 604 |
| Difficulty | Easy |
| Topics | Array, String, Design, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/design-compressed-string-iterator/) |

## Problem Description
### Goal
Design an iterator for a compressed string made of consecutive letter-and-count runs, where a positive count may contain multiple digits. The iterator must expose `next()`, which returns the next character of the expanded sequence, and `hasNext()`, which reports whether another character remains without consuming it.

Process calls in order while keeping the string compressed rather than materializing the potentially much larger expansion. Once all runs are exhausted, `hasNext()` returns `False` and every later `next()` call returns one space character. Repeated calls must preserve the remaining count within the current run before advancing to the next encoded letter.

### Function Contract
**Inputs**

- `compressedString: str`: consecutive letter-and-positive-count runs, with counts possibly containing several digits
- `operations: list[list[str]]`: app-local calls, each either `["next"]` or `["hasNext"]`

**Return value**

- A list containing each operation result in order
- `next()` returns the next expanded character, or one space character after exhaustion
- `hasNext()` reports whether another character remains without consuming it

### Examples
**Example 1**

- Input: `compressedString = "L1e2t1C1o1d1e1"`
- Output of repeated `next()` calls: the characters in `"LeetCode"`

**Example 2**

- Input: `compressedString = "a12"`
- Output: twelve `"a"` characters before exhaustion

**Example 3**

- Input: call `hasNext()` several times before `next()`
- Output: each availability check is `True`, and the next character is still unconsumed
