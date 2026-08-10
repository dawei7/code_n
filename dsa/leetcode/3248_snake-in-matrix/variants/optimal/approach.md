## General

Cell identifiers use row-major order. A cell at row $r$ and column $c$ has identifier

$$
r\cdot n+c.
$$

The snake starts at identifier zero, which corresponds to coordinates `(0,0)`. The solution tracks its row in `x` and column in `y` while executing every command, then applies the row-major formula once at the end.

Each legal command changes exactly one coordinate by one:

- `UP` changes the row by minus one.
- `DOWN` changes the row by plus one.
- `LEFT` changes the column by minus one.
- `RIGHT` changes the column by plus one.

The source uses structural pattern matching on `c[0]`, the first character of the command. The four command names begin with unique letters `U`, `D`, `L`, and `R`, so inspecting the first character is sufficient to identify the full direction. It avoids repeating or comparing the remaining letters.

After every processed prefix of `commands`, the invariant is that `(x,y)` equals the snake's actual grid coordinates after that prefix. Initially both are zero, matching the starting cell. Each match case applies exactly the coordinate displacement defined by its command, so the invariant remains true by induction.

The statement guarantees that the snake never leaves the grid. Therefore the code does not check `0 <= x < n` or `0 <= y < n` after each move. Under legal input, the final coordinates and every intermediate coordinate are valid. Avoiding redundant checks keeps the loop focused on movement.

At the end, `x * n + y` converts the final coordinates to the required cell position. Multiplying the row by $n$ skips all cells in preceding rows; adding the column chooses the offset within the current row.

For a two-by-two grid, begin at `(0,0)`. `RIGHT` produces `(0,1)`. `DOWN` produces `(1,1)`. Encoding gives `1 * 2 + 1 = 3`, matching the example.

For a three-by-three grid with `["DOWN","RIGHT","UP"]`, the positions are `(0,0)`, `(1,0)`, `(1,1)`, and `(0,1)`. The final identifier is `0 * 3 + 1 = 1`.

**Relationship to direct identifier changes.** Moving left or right changes the identifier by minus or plus one. Moving up or down changes it by minus or plus $n$. The solution could therefore maintain only one integer position. Its manifest summary describes that direct displacement view. The exact source instead stores row and column separately and encodes them at the end. Both are equivalent because

$$
(r\pm1)n+c=(rn+c)\pm n
$$

and

$$
rn+(c\pm1)=(rn+c)\pm1.
$$

Tracking coordinates is especially readable because it mirrors the geometric commands and makes the final row-major mapping explicit.

**Why command order still matters even though displacements add.** For the guaranteed-valid path, the final coordinates equal the starting coordinates plus the sum of all direction changes, so reordering commands would produce the same final arithmetic location. However, a reordered sequence might temporarily leave the grid and would no longer satisfy the input guarantee. The algorithm correctly executes the supplied order and relies on validity of that actual order.

No grid is allocated because cell contents are irrelevant. The matrix exists only as a coordinate system and identifier mapping. Building an $n\times n$ array would add unnecessary time and space.

## Complexity detail

Let $c$ be the number of commands. The loop examines each command once and performs one constant-time coordinate update, giving $O(c)$ time. Accessing `c[0]` is constant time.

Only two coordinate integers and the current command reference are stored, so auxiliary space is $O(1)$. The input command list is not copied or modified, and no representation of the grid is created.

The maximum identifier is $n^2-1$, which is tiny under $n\le10$ and is safely represented by Python integers.

## Alternatives and edge cases

- **Track the identifier directly:** Add minus $n$, plus $n$, minus one, or plus one for up, down, left, and right. This uses one scalar and exactly matches the manifest summary, with the same $O(c)$ time and $O(1)$ space.
- **Direction dictionary:** Map each complete command to a coordinate pair or identifier delta. This can make the transition table data-driven, though four match cases are already clear.
- **Simulate an actual matrix:** Allocating cell values or marking visited locations is unnecessary because only the final position matters.
- **Count commands by direction:** Summing the number of ups, downs, lefts, and rights also yields the final coordinates under legal input. Sequential processing is simpler and remains linear.
- **Returning to the start:** Opposite commands cancel. If final `x` and `y` are both zero, the returned identifier is zero regardless of the path taken.
- **Moves along a boundary:** They are handled like any other moves. The guarantee excludes only commands that would cross the boundary.
- **One command:** The corresponding single coordinate update is encoded directly.
- **Repeated commands:** Each occurrence represents another unit move and is processed independently.
- **First-character dispatch:** It is safe only because the four legal command strings have distinct initial letters. If new commands with shared initials were added, full-string matching would be necessary.
- **Illegal command:** No match case would run, effectively treating it as no movement. The contract guarantees this situation never occurs; the source does not validate or raise an error.
- **Illegal out-of-bounds path:** The exact code would allow negative or oversized coordinates and return an invalid identifier. Correctness is scoped to the explicit boundary guarantee.
