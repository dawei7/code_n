## General

The problem asks for any valid grid, not for a grid with the fewest obstacles or the largest number of free cells. That freedom makes a direct construction possible. Instead of opening many cells and then trying to count or eliminate extra paths, the source deliberately opens the cells of one very simple route and blocks everything else.

The chosen route has two straight parts:

1. travel right across the entire top row, from `(0,0)` to `(0,n-1)`;
2. travel down the entire final column, from `(0,n-1)` to `(m-1,n-1)`.

These two parts meet at the top-right cell. Their union always connects the required start and destination.

**Building the obstacle grid first**

The source begins with

```python
g = [["#"] * n for _ in range(m)]
```

This creates `m` separate rows, each containing `n` obstacle characters. The nested list comprehension is significant: every iteration creates a new row list, so modifying one row does not accidentally modify every row.

Starting from an all-obstacle grid makes the construction easy to reason about. Every free cell must be opened intentionally, and there cannot be an unnoticed alternative corridor through the interior.

**Opening the horizontal part**

The assignment

```python
g[0] = ["."] * n
```

replaces the first row with `n` free cells. This opens every position

$$
(0,0),(0,1),\ldots,(0,n-1).
$$

The start cell is therefore free, and moving right along the top boundary is always possible.

**Opening the vertical part**

The loop

```python
for i in range(m):
    g[i][-1] = "."
```

opens the final cell of every row. In Python, index `-1` means the last column, so these cells are

$$
(0,n-1),(1,n-1),\ldots,(m-1,n-1).
$$

The top-right cell was already free because it belongs to the first row; assigning `"."` again is harmless. The bottom-right destination is also opened.

All cells outside the top row and final column remain obstacles. For ordinary dimensions `m>1` and `n>1`, the grid therefore has the form

```text
.......
######.
######.
######.
```

where the exact number of rows and columns depends on `m` and `n`.

**Why a valid path exists**

Begin at `(0,0)`. Every cell to its right in row zero is free, so the path can move right `n-1` times to `(0,n-1)`. Every cell below that point in the last column is free, so the path can then move down `m-1` times to `(m-1,n-1)`.

All moves are legal right-or-down moves, and every visited cell contains `"."`. Thus the construction has at least one valid path.

**Why there cannot be a second path**

From any top-row cell `(0,j)` with `j<n-1`, moving down would enter `(1,j)` when that row exists. That cell is outside the final column, so it is an obstacle. Therefore a valid path cannot leave the top row early.

The path is forced to continue right until it reaches `(0,n-1)`. At the top-right cell, moving right would leave the grid. If the destination has not already been reached, the only legal continuation is down.

Once the path is in the final column, another right move would also leave the grid, while every downward cell in that column is free. The path must continue down to the destination.

There is consequently no position at which a valid path can choose between two free outgoing directions. Its entire sequence is forced:

$$
R^{\,n-1}D^{\,m-1},
$$

meaning `n-1` right moves followed by `m-1` down moves. Existence plus the absence of any branch proves that the number of valid paths is exactly one.

**Converting rows to the required type**

The working grid uses mutable character lists because individual cells are easy to assign in that representation. The contract requires a list of strings, so the return expression

```python
return ["".join(row) for row in g]
```

joins each row's characters into one string. It preserves every `"."` and `"#"` and produces exactly `m` strings of length `n`.

The result does not need to match the sample output. Multiple grids can have exactly one valid path, and the contract explicitly accepts any one of them.

**Degenerate dimensions remain natural**

If `m=1`, the top row is the entire grid. It is all free, and the only possible valid path moves right to the destination. There is no lower row into which the path could branch.

If `n=1`, the final column is the entire grid. The loop opens every cell, and the only possible path moves down. The replacement of the first row and the last-column assignments still use valid indices.

If `m=n=1`, the start and destination are the same single free cell. The length-zero path consisting of that cell is the unique valid path.

## Complexity detail

There are `mn` grid cells. Creating the initial nested list writes every cell once, which costs `O(mn)` time. Replacing the first row costs `O(n)`, opening the final column costs `O(m)`, and joining all rows into strings costs another `O(mn)`. The total time complexity is therefore `O(mn)`.

This running time is asymptotically unavoidable for an explicit `m`-by-`n` result: the function must return `mn` characters, so merely producing the output takes `\Omega(mn)` time.

The returned strings contain `mn` characters, giving `O(mn)` output space. The exact source also constructs the mutable grid `g` before creating the string list, so its auxiliary working representation is `O(mn)` as well. During the return expression, the old rows and newly joined strings can coexist temporarily, but their combined size remains `O(mn)`.

No recursion, path enumeration, or dynamic-programming table is used. The method writes a known unique corridor directly.

## Alternatives and edge cases

- **Free only the left column and bottom row:** This symmetric construction also forces one down-then-right route and has the same complexity. The source specifically chooses the top row and final column.

- **A staircase corridor:** Opening a single alternating right/down chain can also work, but neighboring turns must be chosen carefully because extra adjacent free cells can create shortcuts or branches. The boundary corridor is simpler to verify.

- **Make every cell free:** An all-free grid has one path only when `m=1` or `n=1`. With at least two rows and columns, right and down moves can be interleaved in multiple orders.

- **Count paths after guessing obstacles:** Dynamic programming can verify whether a proposed grid has one path, but verification is unnecessary when the construction makes every move forced by design.

- **Backtracking over obstacle patterns:** Searching the `2^{mn}` possible grids is far beyond what is needed. The problem asks for any valid construction, so a deterministic formula is enough.

- **One row:** Every cell becomes free through the top-row assignment, and exactly one all-right path exists.

- **One column:** Every cell becomes free through the last-column loop, and exactly one all-down path exists.

- **One cell:** The single cell is both endpoints and is free. No movement choice exists.

- **Independent row lists:** Using `[["#"] * n] * m` would alias the same row object `m` times; changing the last cell of one row would change them all. The source's comprehension creates separate rows and avoids that Python-specific trap.

- **Negative indexing:** `g[i][-1]` is safe because `n` is positive. It always refers to column `n-1`.

- **Output formatting:** Returning nested character lists would violate the required list-of-strings interface. Joining every row is part of the construction, not merely cosmetic formatting.

- **Optimality meaning:** Here “optimal” refers to asymptotic construction cost and simplicity, not to minimizing obstacles. The contract imposes no obstacle-count objective.
