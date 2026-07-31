## General

**Express every final entry through its row and column choices**

Only the parity of the number of flips matters. Let $r_i$ say whether row $i$
is flipped an odd number of times and let $c_j$ do the same for column $j$.
Entry $(i,j)$ finishes as

$$
\texttt{grid[i][j]}\mathbin{\mathrm{xor}}r_i\mathbin{\mathrm{xor}}c_j.
$$

For every entry to become zero, its original value must equal
$r_i\mathbin{\mathrm{xor}}c_j$.

Compare each row with the first row. If row $i$ uses the same row-flip parity
as row $0$, their values must agree in every column. If their row-flip
parities differ, their values must disagree in every column. Consequently,
every row must be either identical to the first row or its bitwise complement.

This condition is also sufficient. Choose each row's flip parity according to
whether it equals or complements the first row. After those row flips, all
rows are identical. Then flip precisely the columns containing `1` in that
common row, making every entry zero.

Scan each row once. Its first entry determines whether the row is expected to
match or complement the first row; every remaining entry must maintain that
same relationship. Return false at the first inconsistency, and true if all
rows pass.

## Complexity detail

Let $m$ and $n$ be the row and column counts. The scan examines every matrix
entry once, taking $O(mn)$ time. It compares in place and uses $O(1)$ auxiliary
space.

## Alternatives and edge cases

- **Compare every pair of rows:** Verifying that all row pairs are equal or
  complementary is correct but redundant and takes $O(m^2n)$ time.
- **Simulate flip combinations:** Enumerating row or column subsets takes
  exponential time even though only relative row patterns matter.
- **Materialize normalized rows:** Flipping copies of rows before comparison
  takes the same $O(mn)$ time but uses $O(mn)$ extra space.
- A one-cell matrix is always removable, whether its entry is `0` or `1`.
- Every one-column matrix is removable because each row may be flipped
  independently.
- A mismatch in even one column makes a row neither equal nor complementary
  and therefore makes the whole matrix impossible.
