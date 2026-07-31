## General

**Validity becomes a prefix-balance condition**

Interpret `(` as $+1$ and `)` as $-1$. A complete string is valid exactly when
its running balance never becomes negative and its final balance is zero.
Consequently, a path state needs to remember its current cell and unmatched
opening count, not the full string that led there.

Several paths can reach the same cell with the same balance. Their futures are
identical, so keep that balance only once in a set. For cell $(r,c)$, union the
reachable balances from the cell above and the cell to the left, then add the
current cell's $+1$ or $-1$ contribution.

**Discard states that can no longer succeed**

A negative balance has already used an unmatched closing parenthesis and can
never become a valid prefix. Also let

$$
R=(m-1-r)+(n-1-c)
$$

be the number of cells remaining after the current cell. If the new balance
exceeds $R$, even making every remaining character `)` cannot close all
openings. Retain only balances between zero and $R$.

The path length $m+n-1$ must be even, the first cell must be `(`, and the last
must be `)`. These necessary checks reject impossible grids immediately.

**Why the final state is decisive**

Inductively, the balance set at each cell contains exactly the nonnegative,
still-closable balances of monotone paths ending there. The union considers
both legal predecessor directions, applying the cell contribution extends
each of those paths, and the discarded balances cannot belong to any valid
completion. Therefore no viable path is lost and no unreachable balance is
introduced. At the bottom-right cell, balance zero is present exactly when a
path has nonnegative prefixes and equal opening and closing counts, which is
precisely a valid parentheses string.

## Complexity detail

Let the grid have $m$ rows and $n$ columns. A path balance is at most
$m+n-1$, so each of the $mn$ cells can process $O(m+n)$ states. The worst-case
running time is $O(mn(m+n))$. Keeping only the previous-row state for each
column uses $O(n(m+n))$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every monotone path:** Checking each completed path is correct but the number of paths is exponential in the grid dimensions.
- **Three-dimensional boolean table:** Storing reachability for every cell and balance gives the same $O(mn(m+n))$ time with $O(mn(m+n))$ space instead of rolling columns.
- **Odd path length:** A valid parentheses string has even length, so return `false`.
- **Closing start:** A path beginning with `)` has a negative first prefix and is impossible.
- **Opening end:** The final balance cannot be zero when the last character adds an opening.
- **Premature negative balance:** Discard it immediately; later openings cannot repair an invalid prefix.
- **Too many openings left:** If the balance exceeds the number of remaining cells, it cannot be closed.
- **Single cell:** Its one-character path has odd length and cannot be valid.
