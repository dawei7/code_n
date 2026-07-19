## General
**Treat the words as a ragged character grid**

For each existing character `words[row][column]`, its reflected coordinate is `words[column][row]`. A word square is valid only if the reflected row exists, that row is long enough to contain the reflected column, and the two characters match.

**Reject missing reflected cells as well as mismatches**

Checking characters alone is insufficient for ragged rows. If `column >= len(words)` or `row >= len(words[column])`, one side of the proposed symmetric pair exists without the other, so the shape itself violates the square property. Otherwise compare the two characters directly.

**Why checking every existing cell is sufficient**

The scan rejects every existing coordinate whose reflection is absent or unequal. If it finishes, each cell has an equal reflected cell. Applying the same reflection twice returns to the original coordinate, so there cannot be an unchecked extra cell on the column side; every row and column sequence is identical.

## Complexity detail
Let `C` be the total number of characters across all words. Each existing character is inspected once, so time is $O(C)$. Only loop indices are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Materialize all columns:** build each column string and compare it with the corresponding row in $O(C)$ time but $O(C)$ additional space.
- **Rescan a counterpart row for every cell:** retrieves the same characters correctly but takes $O(n^3)$ time for an `n`-by-`n` square.
- **Ragged valid square:** shorter trailing rows are allowed when every reflected coordinate still exists.
- **Missing reflected row:** a word longer than the number of words makes any character beyond the final row invalid.
- **One word of length one:** its sole diagonal character always forms a valid square.
