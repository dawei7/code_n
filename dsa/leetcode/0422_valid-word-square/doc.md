# Valid Word Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 422 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-word-square/) |

## Problem Description
### Goal
Given an ordered list of nonempty words that may have different lengths, arrange them as rows of a character grid. The list forms a valid word square when reading row `r` produces the same available characters as reading column `r`.

Return `True` only when symmetry holds at every existing coordinate: whenever row `r` has a character at column `c`, row `c` must exist, contain column `r`, and store the same character there. The condition must also work in the opposite direction, so ragged missing positions cannot be ignored. Return `False` for any value mismatch or one-sided coordinate.

### Function Contract
**Inputs**

- `words`: an ordered list of nonempty strings

**Return value**

- Return `True` exactly when every character at row `r`, column `c` has an equal character at row `c`, column `r`, with both coordinates present.

### Examples
**Example 1**

- Input: `words = ["abcd", "bnrt", "crmy", "dtye"]`
- Output: `True`

**Example 2**

- Input: `words = ["abcd", "bnrt", "crm", "dt"]`
- Output: `True`

**Example 3**

- Input: `words = ["ball", "area", "read", "lady"]`
- Output: `False`
