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

### Required Complexity

- **Time:** $O(C)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Treat the words as a ragged character grid**

For each existing character `words[row][column]`, its reflected coordinate is `words[column][row]`. A word square is valid only if the reflected row exists, that row is long enough to contain the reflected column, and the two characters match.

**Reject missing reflected cells as well as mismatches**

Checking characters alone is insufficient for ragged rows. If `column >= len(words)` or `row >= len(words[column])`, one side of the proposed symmetric pair exists without the other, so the shape itself violates the square property. Otherwise compare the two characters directly.

**Why checking every existing cell is sufficient**

The scan rejects every existing coordinate whose reflection is absent or unequal. If it finishes, each cell has an equal reflected cell. Applying the same reflection twice returns to the original coordinate, so there cannot be an unchecked extra cell on the column side; every row and column sequence is identical.

#### Complexity detail

Let `C` be the total number of characters across all words. Each existing character is inspected once, so time is $O(C)$. Only loop indices are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Materialize all columns:** build each column string and compare it with the corresponding row in $O(C)$ time but $O(C)$ additional space.
- **Rescan a counterpart row for every cell:** retrieves the same characters correctly but takes $O(n^3)$ time for an `n`-by-`n` square.
- **Ragged valid square:** shorter trailing rows are allowed when every reflected coordinate still exists.
- **Missing reflected row:** a word longer than the number of words makes any character beyond the final row invalid.
- **One word of length one:** its sole diagonal character always forms a valid square.

</details>
