## General

Each row is shifted cyclically $k$ times by one position, which is equivalent to one cyclic shift by $k$ positions. The source checks whether every original element matches the element that the shift maps to its position, without constructing a shifted matrix.

Let $n$ be the number of columns. Modular indexing wraps positions around the row.

**Odd-indexed rows**

Odd rows shift right. The source checks

`mat[i][j] == mat[i][(j + k) % n]`.

One may expect a right-shift comparison with `j - k` instead. For the question “does the row remain unchanged?”, the two directions are equivalent. A row invariant under rotation by $k$ is also invariant under the inverse rotation by $-k$, because both moves traverse the same cycles of column positions in reverse order.

Thus checking equality along the $+k$ permutation correctly decides invariance under the stated right shift.

**Even-indexed rows**

Even rows shift left. The source checks

`mat[i][j] == mat[i][(j - k + n) % n]`.

Again this follows the inverse direction of the physical move, but invariance under a cyclic permutation equals invariance under its inverse. Adding $n$ before modulo keeps the expression visibly nonnegative, though Python's modulo would also handle a negative value.

**Why every cell comparison is sufficient**

A shifted matrix equals the original exactly when every row equals its shifted version at every column. The loops visit every cell. If a mismatch exists, the method returns `False` immediately.

If all comparisons succeed, values are constant along every cycle formed by advancing $k$ columns modulo $n$. Applying the corresponding left or right rotation only permutes equal values within those cycles, so every row and therefore the matrix remains identical.

**Period interpretation**

The column permutation decomposes a row into $\gcd(n,k)$ cycles. A row is invariant when all entries within each cycle are equal. The source verifies this condition cell by cell rather than explicitly computing cycles.

For row `[1,2,1,2]` with $k=2$, positions $0$ and $2$ form one equal-valued cycle, while positions $1$ and $3$ form another. The row remains unchanged.

For $k$ divisible by $n$, every shifted index equals $j$, so every matrix is similar. The modulo expressions handle this automatically even though the source does not explicitly reduce `k` first.

## Complexity detail

Let $R$ be row count and $C$ column count. In the worst case, both nested loops inspect all $RC$ cells, so time complexity is $O(RC)$.

Only indices, current row references, and current values are used. No shifted rows or matrix are allocated, giving $O(1)$ auxiliary space.

Early return can reduce work when a mismatch appears, but it does not change the worst-case bound.

## Alternatives and edge cases

- **Construct the shifted matrix:** It is straightforward but uses $O(RC)$ extra space and writes values that comparison can address directly.
- **Slice each row:** Python slicing can express rotations but allocates new row lists, increasing auxiliary space.
- **Reduce `k %= n` first:** This improves readability and avoids repeated large-modulus operands, but the exact expressions already produce correct indices.
- **One column:** Every cyclic shift maps the only position to itself, so the result is always true.
- **All row values equal:** Any shift leaves that row unchanged.
- **Repeated pattern:** A row may remain invariant even when $k$ is not a multiple of $n$ if its values repeat with the required period.
- **Even versus odd direction:** Directions differ physically, but equality under a rotation is equivalent to equality under its inverse.
- **Rectangular guarantee:** The source takes column count from the first row and assumes every row has that length, as the matrix contract provides.
- **Large $k$:** Modulo indexing automatically reduces it by the row width.
- **Input preservation:** The method performs comparisons only and does not mutate `mat`.
- **Why inverse invariance holds:** If applying rotation $P$ leaves a row $r$ unchanged, then applying $P^{-1}$ to both sides of $P(r)=r$ gives $r=P^{-1}(r)$. The converse follows symmetrically.
- **Cycle length:** Each positional cycle has length $C/\gcd(C,k)$. Checking one equality per edge around these cycles proves all values in a cycle match.
- **Different rows are independent:** A shift never moves a value between rows, so failure or success can be decided row by row and combined with logical AND.
- **Early return location:** The first mismatch proves the final matrix differs at that cell; inspecting later cells cannot restore whole-matrix equality.
- **Parity check:** Row zero is even and uses the second branch. The explicit `i % 2` tests follow zero-based indexing from the contract.
- **No repeated simulation:** Performing $k$ one-position shifts would cost $O(kRC)$ and mutate data. Modular indexing collapses all steps into one comparison per cell.
- **Modulo with `j-k+n`:** Adding only one $n$ is still safe in Python even when $k>n$, because Python's modulo returns a nonnegative residue for negative dividends.
- **Zero-based row parity:** The first row shifts left, exactly as the even-index rule requires.
