## General
**English scale words align with base-1000 chunks**

Split the number into base-1000 chunks. Convert each nonzero chunk below 1000, append its scale name (`Thousand`, `Million`, or `Billion`), and combine chunks from largest to smallest.

**Name one chunk with exhaustive local cases**

For a value below 1000, emit a hundreds phrase when needed, then handle a remainder below 20 directly or combine a tens word with an optional ones word.

At scale index `i`, the current chunk is exactly the coefficient of $1000^{i}$. Its local words plus scale name therefore represent that chunk's contribution without affecting any other digits.

**Unique chunk decomposition preserves value and order**

Base-1000 decomposition uniquely expresses the number as a sum of coefficients times $1000^{i}$. The helper covers every coefficient from 1 through 999 through disjoint hundreds, sub-twenty, tens, and ones cases. Appending the corresponding scale word restores its place value, and joining nonzero chunks from largest scale to smallest produces the exact English representation.

## Complexity detail
The algorithm processes one chunk per three decimal digits, giving $O(\log num)$ time and word storage. Under the native 32-bit bound there are at most four chunks.

## Alternatives and edge cases
- **Large lookup table:** is bulky and obscures the repeated structure.
- Zero needs an explicit result; zero-valued internal chunks are skipped without adding a scale word.
