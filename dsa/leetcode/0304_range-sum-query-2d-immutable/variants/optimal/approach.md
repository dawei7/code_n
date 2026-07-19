## General
**Give every grid boundary a two-dimensional prefix value**

Build a matrix `prefix` with one extra top row and left column of zeroes. Entry `prefix[r][c]` stores the sum of the original rectangle from $(0,0)$ through $(r-1,c-1)$.

For a new cell, combine the prefix above it and the prefix to its left, subtract their overlap, then add the cell:
`prefix[r + 1][c + 1] = value + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]`.

**Inclusion–exclusion isolates any requested rectangle**

For inclusive corners `(row1,col1)` and `(row2,col2)`, begin with the prefix through the lower-right boundary. Subtract the region above the query and the region left of it. Their upper-left overlap was subtracted twice, so add that overlap back once.

The formula is:
`prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] - prefix[row2 + 1][col1] + prefix[row1][col1]`.

The zero border makes queries touching the top or left image edge use the identical formula.

**Every cell receives coefficient one exactly when it is inside**

Consider a matrix cell relative to the requested rectangle. A cell inside lies in the large lower-right prefix but in neither removed strip, so its coefficient is one. A cell solely above or left is canceled by the corresponding subtraction. A cell in the upper-left overlap appears in the large prefix, both subtractions, and the added overlap, giving coefficient $1 - 1 - 1 + 1 = 0$. Thus precisely the requested cells remain.

## Complexity detail
Constructing all $(m + 1)(n + 1)$ prefix entries takes $O(mn)$ time and space. Each of the `q` queries performs four reads and constant arithmetic, so total time is $O(mn + q)$. Returned sums are output storage.

## Alternatives and edge cases
- **Scan each rectangle directly:** is correct but can cost $O(mn)$ per query and $O(qmn)$ overall.
- **One-dimensional prefix sums per row:** reduce each query to $O(number of rows)$, but the full 2D prefix achieves constant query time.
- Single-cell, single-row, single-column, and full-matrix rectangles all use the same inclusion–exclusion formula. Negative entries require no special case.
