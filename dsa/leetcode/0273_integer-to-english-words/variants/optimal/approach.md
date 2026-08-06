## General
**English scale words align with base-1000 chunks**

Split the number into base-1000 chunks. Convert each nonzero chunk below 1000, append its scale name (`Thousand`, `Million`, or `Billion`), and combine chunks from largest to smallest.

**Name one chunk with exhaustive local cases**

For a value below 1000, emit a hundreds phrase when needed, then handle a remainder below 20 directly or combine a tens word with an optional ones word.

At scale index `i`, the current chunk is exactly the coefficient of $1000^{i}$. Its local words plus scale name therefore represent that chunk's contribution without affecting any other digits.

**Unique chunk decomposition preserves value and order**

Base-1000 decomposition uniquely expresses the number as a sum of coefficients times $1000^{i}$. The helper covers every coefficient from 1 through 999 through disjoint hundreds, sub-twenty, tens, and ones cases. Appending the corresponding scale word restores its place value, and joining nonzero chunks from largest scale to smallest produces the exact English representation.

## Complexity detail

For positive `num`, the loop processes one chunk per three decimal digits, and `chunk_words` does constant work on a
value below 1,000. The time is therefore $O(\log \texttt{num})$. The chunk-word groups and final returned words occupy
$O(\log \texttt{num})$ space. Under the native 32-bit bound, at most four chunks are processed; zero returns in
$O(1)$ time and space.

## Alternatives and edge cases

- **Large lookup table:** is bulky and obscures the repeated structure.
- **Repeated subtraction by each scale:** remains correct but performs unnecessary work proportional to the chunk coefficients.
- **Zero:** it needs the explicit word `Zero` because the chunk loop would otherwise emit nothing.
- **Zero-valued internal chunk:** it contributes neither local words nor a scale word, preventing phrases such as `Zero Thousand`.
