## General

**Collapse repeated steps with modular arithmetic.** A row of $C$ columns
returns to the same alignment after every $C$ one-position shifts. Therefore
`k` steps have the same effect as a shift of
$s=\texttt{k}\bmod C$ positions.

For an even row shifted left, the final value at column $j$ is the original
value at column $(j+s)\bmod C$. Equality with the original row requires

$$
\texttt{row[j]}=\texttt{row[(j+s)\bmod C]}
$$

for every $j$. An odd row shifted right instead compares with
$(j-s)\bmod C$. These two conditions are equivalent: one cyclic permutation
is the inverse of the other, and a sequence fixed by a permutation is also
fixed by its inverse. The same positive-offset comparison can consequently be
used for every row.

**Check without modifying the matrix.** Visit every cell and compare it with
the entry $s$ columns ahead in the same row, wrapping by modulo $C$. Any
mismatch proves that the corresponding shifted row differs, so return
`False`. If every comparison succeeds, all even and odd rows are invariant
under their required shifts and the final matrix is identical to the original.

## Complexity detail

The check visits all $RC$ matrix entries once, taking $O(RC)$ time. It stores
only the column count, effective shift, and loop positions, so auxiliary space
is $O(1)$.

## Alternatives and edge cases

- **Construct each shifted row:** Slicing or copying makes the comparison direct but uses $O(RC)$ extra space.
- **Simulate all k steps:** Rebuilding rows after every one-position shift is correct but takes $O(kRC)$ time.
- **Use separate direction formulas:** Checking positive offsets for even rows and negative offsets for odd rows is equivalent but adds an unnecessary branch.
- **Shift divisible by C:** The effective shift is zero, so every matrix is similar.
- **Single column:** Every cyclic shift leaves each row unchanged.
- **Periodic rows:** A nonconstant row may still be invariant when its period divides the effective shift.
- **Early mismatch:** One differing entry is enough to return `False`.

