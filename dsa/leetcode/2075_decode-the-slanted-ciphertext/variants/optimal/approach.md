## General
**Recover the matrix width**

The encoded string contains every matrix cell in row-major order, including padding spaces. Dividing its length by `rows` therefore gives the exact column count $C$. A cell at matrix coordinates `(row, column)` occupies index `row * columns + column` in `encodedText`.

**Follow each original diagonal**

The encoder began one diagonal at each top-row column from left to right. For a starting column `start_column`, visit `(0, start_column)`, `(1, start_column + 1)`, and so on while both coordinates remain inside the matrix. Appending these characters for every top-row start exactly reverses the encoder's placement order: every reachable cipher cell is read once, and their diagonal order is the original character order.

**Remove only padding at the end**

Spaces encountered between non-space characters belong to the original text and must remain. Padding can appear after the last original character in the recovered sequence, while the contract guarantees that the original itself has no trailing spaces. Applying a right-side trim once after joining the characters therefore removes precisely the ambiguous padding without disturbing meaningful internal or leading spaces.

## Complexity detail
Across all diagonals, at most the $L$ matrix cells are visited once. Index calculation and each append take constant time, so traversal and the final join require $O(L)$ time. The accumulated decoded characters and returned string use $O(L)$ space.

## Alternatives and edge cases
- **Materialize the matrix:** Splitting `encodedText` into rows makes the diagonal geometry explicit, but it stores another $O(L)$ representation without improving the asymptotic running time.
- **Repeated string concatenation:** Adding one character to an immutable result string on every visit can repeatedly copy the growing prefix and degrade to $O(L^2)$ time; collect characters and join once.
- **Empty encoded text:** Then $C=0$, no diagonal starts exist, and the decoded result is the empty string.
- **One row:** Every diagonal contains one cell, so the traversal returns `encodedText` unchanged except for any valid terminal padding.
- **Space preservation:** Use a right-side trim only. A general trim would incorrectly remove a meaningful leading space, and removing all spaces would destroy words.
