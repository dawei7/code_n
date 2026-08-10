## General

**Turn each wrapping rule into an ordinary one-dimensional traversal**

The horizontal rule reads each row left to right and, at a row boundary, continues at the first cell of the next row. This is exactly row-major flattening:

`grid[0][0], grid[0][1], ..., grid[0][columns-1], grid[1][0], ...`.

The source builds:

`horizontal = "".join("".join(row) for row in grid)`.

It does not append the first row again, so matching cannot wrap from the final row back to the top. Any ordinary substring of this flattened text corresponds exactly to one legal horizontal substring, including matches that cross row boundaries.

The vertical rule reads top to bottom and, at the bottom of a column, continues at the top of the next column. This is column-major flattening:

`grid[0][0], grid[1][0], ..., grid[rows-1][0], grid[0][1], ...`.

The source builds that ordering with the column loop outside the row loop. Again, the text stops after the last column, so there is no forbidden wrap back to the first column.

The two unusual two-dimensional searches are now two ordinary exact-pattern searches in strings of the same length `N = rows * columns`.

**Build the KMP prefix table once**

Searching naively from every starting position can cost `O(NP)` for pattern length `P`. Knuth-Morris-Pratt search avoids rechecking characters.

The `prefix[i]` value is the length of the longest proper prefix of `pattern[0..i]` that is also a suffix of that same pattern prefix.

While building it, `matched` is the best border length known for the preceding position. If `pattern[index]` does not extend that border, the source falls back to:

`matched = prefix[matched - 1]`.

This tries the next-longest possible border without comparing the already-known matching characters again. If the next characters agree, `matched` increases. The resulting value is saved for the current index.

The prefix table depends only on `pattern`, so the source builds it once and reuses it for both flattened texts.

**Search a text while allowing overlapping matches**

Inside `covered(text)`, `matched` means that the first `matched` pattern characters match a suffix ending immediately before the current search position.

For each text character:

- while there is a mismatch and `matched > 0`, fall back through the prefix table;
- if the current character matches `pattern[matched]`, increment `matched`;
- when `matched == length`, one complete occurrence ends at the current index.

The match start is:

`start = index - length + 1`.

After recording it, the source sets:

`matched = prefix[matched - 1]`.

This fallback is crucial for overlaps. If pattern `"aba"` matches ending at one position, its suffix `"a"` may already be the prefix of another match starting inside the first. Resetting to zero would miss that overlap.

**Mark the union of all matched intervals efficiently**

The final question does not ask how many matches exist. It asks whether each cell belongs to at least one match in each orientation.

For a match covering inclusive text positions `[start,index]`, the source applies a difference-array range addition:

`difference[start] += 1`

`difference[index + 1] -= 1`.

After all matches, a prefix sum `active` tells how many match intervals currently cover each text position. `result[position] = active > 0` marks the union.

This handles overlaps naturally. If two matches cover a position, `active` may be two; the boolean remains true. When one interval ends, the negative difference reduces the active count without erasing coverage from another interval.

The difference array has length `len(text)+1` so `index+1` is always a valid endpoint, even when a match ends at the final character.

**Map a physical cell into both flattened orders**

Cell `(row,column)` has row-major index:

`horizontal_index = row * columns + column`.

It has column-major index:

`vertical_index = column * rows + row`.

These formulas point to the same physical cell in the two different strings. The source counts the cell only when:

`horizontal_cells[horizontal_index]`

and

`vertical_cells[vertical_index]`

are both true.

The horizontal and vertical occurrences do not need to start or end at the same places. A cell qualifies if it belongs to at least one occurrence of each kind.

**Trace a boundary-crossing match**

For a grid with two columns, row-major indices are:

`(0,0)->0, (0,1)->1, (1,0)->2, (1,1)->3`.

A pattern occurrence at flattened interval `[1,2]` uses the last cell of row zero and first cell of row one. That is exactly the allowed horizontal wrapping behavior. An interval cannot continue beyond index `N-1` because ordinary substring search has no circular wrap.

Column-major order provides the analogous behavior at a column bottom.

**Why every qualifying cell is counted exactly once**

Every legal horizontal occurrence is one substring of the row-major text, and every row-major pattern match is a legal horizontal occurrence. KMP finds all of them, and the difference scan marks precisely their union. The same equivalence holds vertically with column-major order.

The final double loop visits each physical grid cell once and consults its exact coverage status in both unions. It increments only the answer count, not a per-match count, so a cell covered by many horizontal and vertical occurrences is still counted once.

This proves both completeness and lack of double-counting.

## Complexity detail

Let `N = rows * columns` and `P = len(pattern)`. Building the KMP prefix table takes `O(P)` time. Constructing each flattened string takes `O(N)` time.

Each call to `covered` runs KMP in `O(N+P)` worst-case reasoning, although the shared prefix table means its search portion is `O(N)`, and then scans a difference array in `O(N)`. Two orientations remain `O(N+P)` total up to constant factors.

The final cell loop takes `O(N)`. Overall time is `O(N+P)`, matching the manifest.

The prefix table uses `O(P)` space. Flattened strings, difference arrays, and boolean coverage arrays use `O(N)` space. Some orientation-specific arrays coexist, so constants are substantial, but asymptotic auxiliary space is `O(N+P)`.

## Alternatives and edge cases

- **Search from every starting cell:** Comparing up to `P` characters at each of `N` starts can cost `O(NP)`. KMP guarantees linear search.
- **Run a two-dimensional matcher:** The wrap definitions are not ordinary rectangular patterns. Flattening precisely follows their one-dimensional traversal and is simpler.
- **Mark every matched cell with an inner loop:** A pattern like repeated `"a"` can have many overlapping matches, making total marking `O(NP)`. Difference ranges mark each occurrence in constant time.
- **Use match counts instead of booleans:** Counts are useful only while accumulating interval coverage. The final condition is presence, so `active > 0` is sufficient.
- **Reset KMP to zero after a match:** This misses overlapping occurrences. Falling back to the last prefix value preserves overlap candidates.
- **Horizontal row boundary:** Row-major adjacency deliberately joins the end of one row to the start of the next.
- **Horizontal bottom boundary:** The flattened string ends at the final cell, so no match wraps back to row zero.
- **Vertical column boundary:** Column-major adjacency deliberately joins the bottom of one column to the top of the next.
- **Vertical last-column boundary:** No characters follow the final column, so circular wrap is impossible.
- **Pattern length one:** Every cell whose character equals the pattern is marked in each flattening; since both represent the same cell value, all matching cells qualify.
- **Pattern length N:** Only a full-text match can occur in each orientation, and all cells in a matching orientation are covered.
- **Overlapping occurrences:** Difference counts may exceed one, but the boolean union remains correct.
- **Same cell mapped differently:** The row-major and column-major formulas must both be used; comparing equal numeric indices would generally refer to different cells.
- **One-row grid:** Horizontal order is the row; vertical order advances one-cell columns, which happens to be the same sequence.
- **One-column grid:** Both traversals likewise coincide.
- **No matches in one orientation:** Its coverage array is all false, so the final answer is zero regardless of the other orientation.
