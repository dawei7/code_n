## General
Only the parity of each increment count matters. Maintain one bit for every row and every column. For operation `[r, c]`, toggle the bit for row `r` and the bit for column `c`; toggling is equivalent to adding one modulo two.

**Deriving a cell's parity**

Cell `(r, c)` receives every increment applied to row `r` and every increment applied to column `c`. Its final parity is therefore the exclusive-or of those two parity bits. The cell is odd exactly when one bit is odd and the other is even. The double increment at an operation's intersection is handled automatically because two toggles cancel modulo two.

**Counting without constructing the matrix**

Let $R$ be the number of rows with odd parity and $C$ the number of columns with odd parity. An odd row paired with an even column contributes $R(n-C)$ odd cells. An even row paired with an odd column contributes $(m-R)C$ more. These groups are disjoint and cover every odd cell, so return $R(n-C)+(m-R)C$.

## Complexity detail
Toggling the $k$ operations takes $O(k)$ time, and counting the row and column bits takes $O(m+n)$ time. The two parity arrays occupy $O(m+n)$ auxiliary space.

## Alternatives and edge cases
- **Direct matrix simulation:** Incrementing every affected cell follows the statement literally but costs $O(k(m+n)+mn)$ time and $O(mn)$ space.
- **Sets of odd rows and columns:** Adding or removing each index from a set also tracks parity and uses space proportional to the currently odd indices.
- **Repeated operation:** Applying the same pair twice restores both associated parity bits and has no net parity effect.
- **Single cell:** Every operation increments its row and column, so the cell always receives an even total.
- **All row and column bits equal:** When both sides have the same parity everywhere, no cell is odd.
