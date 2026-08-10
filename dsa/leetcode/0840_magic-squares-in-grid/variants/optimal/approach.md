## General

**Treat every cell as a possible top-left corner**

A candidate magic square always has exactly three rows and three columns. The outer expression calls `check(i,j)` for every grid coordinate, interpreting it as a possible top-left corner.

The first check rejects positions where `i+3 > m` or `j+3 > n`. Those candidates would extend below or to the right of the grid.

Calling `check` even near boundaries keeps the outer iteration simple. Out-of-bounds candidates return zero before any cell access.

**Validate the allowed values and distinctness**

Inside a valid 3-by-3 window, the nested loops inspect all nine cells.

If a value is below 1 or above 9, the candidate immediately fails. Otherwise, it is inserted into set `s`.

After scanning, `len(s) == 9` means all nine values are distinct. Combined with every value lying in the nine-element domain `1..9`, this proves the window contains each number from 1 through 9 exactly once.

The code does not need a separate sorted comparison against `[1,2,\ldots,9]`. Nine distinct selections from a domain containing exactly nine possibilities must be the complete domain.

**Accumulate every required line sum**

Arrays `row` and `col` contain three zeroes each. For grid cell `(x,y)`:

- `row[x-i]` receives its value;
- `col[y-j]` receives its value.

Subtracting the window's top-left coordinate converts global grid indices into local indices 0, 1, and 2.

Variable `a` sums the main diagonal, where local row equals local column. Variable `b` sums the other diagonal, where local row equals `2 - local column`.

The center cell belongs to both diagonals, as it should.

**Use one diagonal as the common target sum**

After all nine cells are processed, the code first requires `a == b`. It then verifies every row sum and every column sum equals `a`.

If these tests pass:

- all three rows equal `a`;
- all three columns equal `a`;
- both diagonals equal `a`.

These are exactly the eight line-sum requirements of a 3-by-3 magic square.

Because the values are exactly 1 through 9, their total is 45. Three equal row sums must each be 15, so `a` will necessarily be 15. The code does not hard-code 15; comparing all lines to one reference sum is sufficient and directly expresses equality.

**Return one or zero from each candidate**

`check` returns integer 1 for a magic square and 0 otherwise. The outer `sum` adds these results, producing the total count.

Overlapping 3-by-3 windows are separate subgrids and are correctly evaluated independently.

**Trace a valid Lo Shu square**

For

`[[4,3,8],[9,5,1],[2,7,6]]`:

- the nine values are distinct and within 1 through 9;
- row sums are 15, 15, and 15;
- column sums are 15, 15, and 15;
- diagonal sums are `4+5+6=15` and `8+5+2=15`.

Every check passes and the candidate contributes one.

Changing one value may preserve some line sums, but it will fail either the range/distinctness condition or at least one required line comparison.

**Why the validation is exact**

Every returned-one window has the precise required dimensions, contains nine distinct allowed values, and has equal row, column, and diagonal sums, so it is a magic square.

Conversely, every magic-square window lies at some enumerated top-left coordinate. Its values pass range and distinctness, and all its required lines have one common sum, so `check` returns one. Summing all corners counts every valid subgrid exactly once.

## Complexity detail

Let the grid have `r` rows and `c` columns. The outer iteration calls `check` `rc` times. Each call performs either a constant-time boundary rejection or examines exactly nine cells and fixed-size arrays. Nine is constant, so total time is `O(rc)`.

The set holds at most nine values, and row and column arrays each hold three integers. All other state is scalar. Auxiliary space is `O(1)`.

The generator used by `sum` is lazy and does not store all candidate results.

## Alternatives and edge cases

- **Enumerate only valid top-left ranges:** Loop through `range(r-2)` and `range(c-2)`. This avoids boundary calls but has the same complexity.

- **Exploit special Lo Shu properties:** Every 3-by-3 normal magic square has center 5 and other structural constraints. Those checks can reject faster, but explicit definition validation is easier to prove.

- **Check only line sums:** Equal lines are not enough; values must also be distinct and in 1 through 9.

- **Check only distinctness:** A permutation of 1 through 9 is not necessarily magic; all eight line sums still need verification.

- **Grid smaller than 3-by-3:** Every candidate fails the boundary check, so the answer is zero.

- **Value zero or above nine:** The candidate returns zero immediately.

- **Duplicate allowed value:** Set size is below nine, so the candidate is rejected.

- **Equal rows but unequal columns:** The column comparison rejects it.

- **Equal rows and columns but unequal diagonal:** The diagonal checks reject it.

- **Overlapping candidates:** Each top-left coordinate identifies a different subgrid and may contribute independently.

- **Maximum 10-by-10 grid:** Constant work per coordinate remains small.

- **Input immutability:** The function only reads grid values and creates temporary fixed-size structures.
