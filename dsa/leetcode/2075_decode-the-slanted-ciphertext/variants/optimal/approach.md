## General

**Reconstruct the conceptual matrix dimensions**

The encoded string represents a matrix written row by row. The number of rows is given. Because the encoding is valid, its length is divisible by `rows`, so the number of columns is

`cols = len(encodedText) // rows`.

No physical two-dimensional matrix is necessary. In a row-major flattened string, the character at matrix row `x` and column `y` is stored at index

$$
x\cdot\texttt{cols}+y.
$$

The expression `encodedText[x * cols + y]` therefore retrieves exactly the character that would appear in cell $(x,y)$.

For example, if there are three rows and four columns, row 0 occupies flat indices 0 through 3, row 1 occupies indices 4 through 7, and row 2 occupies indices 8 through 11. Cell $(2,1)$ is consequently at index $2\cdot4+1=9$.

**Read the same diagonals used by the slanted encoding**

The original text was placed along diagonals that move one row down and one column right at every step. Each such diagonal starts in the top row. The starting column identifies which diagonal is being read.

The outer loop tries every top-row starting column `j` from 0 through `cols - 1`. For that diagonal, it initializes `x = 0` and `y = j`. The inner loop appends the current cell and then performs

`x, y = x + 1, y + 1`.

That simultaneous update moves down-right by one cell. The bounds `x < rows and y < cols` ensure that reading stops as soon as the diagonal leaves either the bottom or right side of the matrix.

Starting at column 0 visits $(0,0),(1,1),(2,2)$ and so on while those cells exist. Starting at column 1 visits $(0,1),(1,2),(2,3)$, and the process repeats for every possible start. Concatenating these diagonals in increasing starting-column order reverses the placement rule of the slanted encoding.

It is important that the traversal does not begin diagonals from the left edge below row 0. The source encoding places meaningful characters along diagonals whose origins are on the top row. Cells below the left-to-right diagonal region are not another continuation of the original message. Reading them would introduce characters in an order the encoder never used.

**Build the decoded sequence before removing padding**

Characters are appended to `ans`, a list, rather than repeatedly concatenated to an immutable string. Once all valid diagonal positions have been visited, `''.join(ans)` creates the decoded candidate efficiently.

The rectangular representation may require spaces after the original message so that the encoded data fills its prescribed layout. Those padding spaces appear at the end of the decoded candidate. The final `rstrip()` removes them.

This removal is safe under the problem contract because the original text has no trailing spaces. Therefore, any spaces after its last real character are encoding padding rather than meaningful content. Spaces within the message are not removed: `rstrip()` acts only on the right end. Leading spaces would also remain, because the method does not call `strip()`.

Python's `rstrip()` without an argument removes trailing whitespace characters generally. The encoded alphabet here consists of lowercase letters and spaces, so in the valid input domain this has the intended effect of removing trailing padding spaces.

**Walk through a small shape**

Imagine a three-row, five-column flattened matrix. The decoder considers starting columns 0, 1, 2, 3, and 4:

- start 0 can visit $(0,0),(1,1),(2,2)$;
- start 1 can visit $(0,1),(1,2),(2,3)$;
- start 2 can visit $(0,2),(1,3),(2,4)$;
- start 3 can visit $(0,3),(1,4)$;
- start 4 can visit only $(0,4)$.

The exact characters at those coordinates depend on the encoded text, but the order follows the original diagonal-writing order. Near the right edge, diagonals naturally become shorter because `y < cols` fails sooner. The code does not need a special formula for their lengths; the bounds enforce the shape directly.

**Why the traversal is correct**

Consider any character position in the original text before padding. During encoding, it belongs to one diagonal beginning at some top-row column $j$. Within that diagonal, suppose it is the $x$th step from the top, counting the first cell as step zero. Its matrix coordinate is then $(x,j+x)$.

When the decoder's outer loop reaches that same $j$, the inner loop starts at $(0,j)$ and increments both coordinates together. After $x$ increments, it reaches exactly $(x,j+x)$ and appends that character. It cannot append the character from a different outer iteration because a coordinate $(x,y)$ determines its starting column uniquely as $j=y-x$.

The outer loop processes $j$ in the same order in which encoding starts the diagonals, and the inner loop processes positions along each diagonal from top-left to bottom-right. Every message character is thus appended once and in original order. Any appended characters after the message are padding spaces, which `rstrip()` removes. The returned string is therefore exactly the original text.

The implementation also handles the empty encoded string. Then `cols` is zero, the outer range is empty, `ans` remains empty, and joining and trimming it returns the empty string.

## Complexity detail

Let $L$ be `len(encodedText)`. The matrix has `rows * cols = L` cells.

The nested loops visit only coordinates within that matrix and never visit a coordinate twice. They may visit fewer than all $L$ cells because only diagonals beginning on the top row are relevant, but the number of visits is at most $L$. Joining the list and trimming the result also take at most $O(L)$ time. The total time complexity is therefore $O(L)$.

The list `ans` can contain up to $O(L)$ characters before joining. The produced output string can also have length proportional to $L$. Excluding the required returned string but counting the explicit construction list, the auxiliary space used by this implementation is $O(L)$.

The coordinate variables `x`, `y`, `j`, and `cols` occupy constant space. Avoiding a materialized matrix saves another $O(L)$ storage object, although the output buffer is still linear.

## Alternatives and edge cases

- **Materializing a matrix:** Splitting the flattened text into `rows` row strings can make coordinates visually obvious, but it duplicates or reorganizes $O(L)$ data. Direct row-major indexing obtains the same cells without building the matrix.
- **Repeated string concatenation:** Appending one character at a time to an immutable string may repeatedly copy the accumulated prefix. Collecting characters in a list and joining once gives predictable linear construction.
- **Reading complete matrix rows or columns:** Ordinary row-major or column-major traversal does not undo the slanted placement. Both row and column must increase together along each decoding diagonal.
- **Starting extra diagonals on the left edge:** Those coordinates do not correspond to the encoder's top-row diagonal starts and would add data in the wrong order. Only `j` values in the top row are used.
- **Forgetting the right boundary:** Checking only `x < rows` can make `y` exceed the column count on diagonals near the right edge, producing an invalid flat index or reading unrelated data.
- **Using `strip()` instead of `rstrip()`:** `strip()` also removes leading spaces, which are not identified as right-side padding. The exact solution limits removal to the end.
- **Removing all spaces:** Internal spaces are part of the original text and must remain. Only the consecutive padding at the decoded string's right end is discarded.
- **One row:** Every diagonal has one cell, so the outer loop reads the encoded text from left to right. Trimming padding returns the original message.
- **One column:** Only the diagonal starting at column zero is considered. Valid encoding constraints determine which characters can occur in this shape, and the bounds stop after the available diagonal cells.
- **Empty encoded text:** `cols` becomes zero, no indexing occurs, and the result is the empty string.
- **Divisibility by `rows`:** The solution relies on the valid-encoding guarantee that the flattened length represents a complete rectangular matrix. Integer division then recovers the exact column count.
- **Trailing-space guarantee:** Correctness of `rstrip()` depends on the original text having no trailing spaces. Under that contract, removed rightmost spaces are necessarily padding rather than message content.
