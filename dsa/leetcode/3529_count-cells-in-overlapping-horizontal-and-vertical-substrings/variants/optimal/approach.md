## General

The horizontal rules are exactly row-major flattening: concatenate the rows. The vertical rules are column-major flattening: concatenate each column from top to bottom. An occurrence may cross a row or column boundary because those boundaries are adjacent in the corresponding flattened string, while neither flattened string wraps at its final character.

Build the KMP prefix table for `pattern` once and scan each flattened string. When a match ends at position $e$, it covers the interval from $e-P+1$ through $e$, where $P$ is the pattern length. Mark that interval with `+1` at its start and `-1` just after its end. A prefix sum over the difference array then tells whether every flattened position belongs to at least one match. This interval method handles arbitrarily many overlapping matches without revisiting all $P$ characters for each occurrence.

Finally, map cell `(row, column)` to row-major position `row * columns + column` and column-major position `column * rows + row`. Count it exactly when both coverage arrays mark their corresponding positions.

## Complexity detail

Let $N = mn$ be the number of cells and $P = \lvert\texttt{pattern}\rvert$. The KMP table costs $O(P)$ time, and both scans, both coverage prefix sums, and the final cell pass each cost $O(N)$. Total time is $O(N+P)$. The flattened strings, difference arrays, coverage arrays, and prefix table require $O(N+P)$ space.

## Alternatives and edge cases

- **Check every start directly:** Comparing up to $P$ characters at every position can take $O(NP)$ time.
- **Mark every matched character individually:** Even with fast pattern matching, many overlapping occurrences can make interval marking quadratic; difference arrays keep it linear.
- **Search each row or column separately:** This incorrectly rejects valid occurrences that continue into the next row or column.
- **Index mapping:** Column-major position is `column * rows + row`, not the row-major index used by the horizontal scan.
- **Pattern of length one:** A matching character is covered in both orientations at the same cell, so every grid occurrence of that character qualifies.
- **Full-length pattern:** It has only one possible start in each flattened order and never wraps from the end back to the beginning.
