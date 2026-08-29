## General

**Restating “special” as two counts**

A position `(i, j)` is special only when three facts hold:

- the cell itself contains one;
- row `i` contains no other one;
- column `j` contains no other one.

Because the matrix is binary, those facts have a compact numerical form. If `mat[i][j] == 1`, then the row condition is equivalent to the total number of ones in row `i` being exactly one, and the column condition is equivalent to the total number of ones in column `j` being exactly one.

The solution precomputes those totals in `rows` and `cols`. This avoids rescanning an entire row and column separately for every candidate one.

**First pass: collect reusable summaries**

`rows` has one entry for every matrix row and starts with zeros. `cols` has one entry for every matrix column and also starts with zeros.

The nested loops use `enumerate` twice. The outer loop yields the row index `i` and the row list itself. The inner loop yields column index `j` and cell value `x`. At each cell, the code executes:

`rows[i] += x`

`cols[j] += x`

Since every `x` is either zero or one, adding `x` directly counts ones. A zero changes neither total; a one increments both the total for its row and the total for its column. An explicit `if x == 1` would produce the same summaries, but binary arithmetic makes the two unconditional additions concise.

After this first complete traversal, `rows[i]` equals the sum of all cells in row `i`, which is exactly its number of ones. Similarly, `cols[j]` equals the number of ones in column `j`.

For the matrix `[[1,0,0],[0,0,1],[1,0,0]]`, the row totals are `[1,1,1]` and the column totals are `[2,0,1]`. This immediately shows why the one at `(0,0)` is not special: its row contains one one, but its column contains two. The one at `(1,2)` has both totals equal to one and is special.

**Second pass: test every position in constant time**

The second pair of nested loops visits every matrix cell again. It evaluates:

`x == 1 and rows[i] == 1 and cols[j] == 1`.

This Boolean expression is true exactly for a special position. It first ensures the current cell is the one represented by the unique row and column counts. This first condition is logically useful even though a row and column total of one strongly constrain their intersection; stating it directly follows the definition and prevents counting a zero at the crossing of an unrelated one in the row and an unrelated one in the column.

The code adds the Boolean result directly to `ans`. In Python, `True` has integer value one and `False` has integer value zero. Therefore, a special cell increments `ans` by one, while every other cell leaves it unchanged.

This use of Boolean arithmetic is not counting “truth values” as a separate concept. It is a concise conditional increment:

- when all three comparisons are true, add one;
- otherwise, add zero.

**Why every counted cell is special**

Suppose a cell contributes one to `ans`. The expression proves `x == 1`. It also proves `rows[i] == 1`. Since the current cell itself supplies that one, all other cells in row `i` must be zero. Likewise, `cols[j] == 1` and the current one imply every other cell in column `j` is zero. The cell therefore meets every part of the definition.

**Why every special cell is counted**

Now suppose `(i,j)` is special. Its value is one. By definition, every other value in row `i` is zero, so the first pass computes `rows[i] == 1`. Every other value in column `j` is also zero, so it computes `cols[j] == 1`. When the second pass reaches this cell, all three comparisons are true and it contributes exactly one.

The second pass visits each coordinate once, so the same special position cannot be counted twice. Together, these two directions prove that `ans` equals the number of special positions.

**Why precomputation changes the efficiency**

A direct candidate-by-candidate method could find a one and then scan its whole row and whole column looking for another one. In a matrix containing many ones, it would repeat the same row and column work many times.

The count arrays share that work. Each cell contributes once to its row summary and once to its column summary. Afterward, deciding whether a cell is special uses three constant-time lookups and comparisons. The algorithm trades $O(R+C)$ storage for a linear-in-the-matrix running time.

**The binary-matrix guarantee**

Adding `x` counts ones only because each cell is guaranteed to be zero or one. If arbitrary integers were allowed, a row such as `[2, -1]` could sum to one without containing exactly one value equal to one, and the method would no longer express the definition. Under the stated binary contract, sum and count of ones are identical.

The matrix is also guaranteed non-empty, so `len(mat[0])` is safe. All rows have the common matrix width, allowing a single `cols` array to serve every row.

## Complexity detail

Let $R$ be the number of rows and $C$ the number of columns.

The first traversal visits all $RC$ cells and performs constant work at each. The second traversal visits all $RC$ cells again and also performs constant work per cell. The total is $2RC$ cell visits, which simplifies to $O(RC)$ time.

The `rows` array has length $R$, and `cols` has length $C$. All other state—`ans`, indices, row references, and the current value—uses constant space. The auxiliary space complexity is therefore $O(R+C)$.

The input matrix is not modified, and the scalar integer returned as output needs $O(1)$ space. The two traversals do not create copies of rows; `enumerate` yields references and indices lazily.

## Alternatives and edge cases

- **Scan a row and column for every one:** This uses $O(1)$ extra space but can take $O(RC(R+C))$ time in the worst case because the same lines are checked repeatedly.
- **Store coordinates of all ones:** One could record each one and then examine only those candidates after building row and column counts. That may reduce the second scan for sparse matrices, but it adds up to $O(RC)$ coordinate storage; the checked-in solution simply performs a predictable second pass.
- **Use sets of occupied rows and columns:** A set records presence but not whether a row or column contains exactly one one. Counts are required to distinguish one occurrence from several.
- **Mutate the matrix to store counts:** Reusing the first row and column can reduce auxiliary storage, but it complicates marker collisions and alters the input. Separate count arrays are clearer and match the checked-in source.
- **All-zero matrix:** Every row and column count is zero. The `x == 1` test is always false, so the answer is zero.
- **Single one in the entire matrix:** Its row and column totals are both one, so it is the sole special position.
- **One row:** A one is special only if that row contains exactly one one. Each column contains at most its single cell, so the row total is the deciding restriction.
- **One column:** Symmetrically, a one is special only if the column contains exactly one one.
- **Identity matrix:** Every row and every column contains one one, so every diagonal one is counted.
- **Two ones sharing a row:** That row’s count is two, so neither can be special even if their respective column counts are one.
- **Two ones sharing a column:** The column count of two rejects both positions.
- **Boolean addition in Python:** The final expression adds one for true and zero for false. A port to a language that does not treat Booleans numerically should use an explicit conditional increment.
- **Non-binary values:** The direct-sum counting technique depends on the zero-or-one guarantee. For arbitrary cell values, increment counters only when a cell equals one.
- **Rectangular rather than square input:** `rows` and `cols` have independent lengths, so the solution handles any valid $R\times C$ shape.
