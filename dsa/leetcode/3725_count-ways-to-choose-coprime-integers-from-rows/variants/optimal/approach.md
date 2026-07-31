## General

Let $V$ be the largest matrix value. For each positive divisor $d \leq V$, first count selections in which every chosen number is divisible by $d$. In one row, the number of eligible choices is the sum of the frequencies at $d,2d,3d,\ldots$. Choices across rows are independent, so multiplying these row counts gives `divisible_ways[d]`.

This count includes every selection whose exact GCD is $d$, $2d$, $3d$, and so on. Recover exact-GCD counts in descending divisor order:

$$
\text{exact}[d]
= \text{divisible\_ways}[d]
- \sum_{k \geq 2,\,kd \leq V}\text{exact}[kd].
$$

When processing $d$ from $V$ down to `1`, every strict multiple already has its exact count, so the subtraction is valid. The required result is `exact[1]`.

Frequency counts preserve positional multiplicity: a value occurring twice in one row contributes two eligible choices to every divisor it satisfies. Applying the modulus after products and subtractions keeps all arithmetic within the requested residue class.

## Complexity detail

Let $m$ be the row count, $n$ the column count, and $V = \max(\texttt{mat[i][j]})$. Building row frequencies costs $O(mn)$. Summing frequencies over multiples for every divisor costs $O(mV\log V)$ by the harmonic series, and descending inversion costs $O(V\log V)$. Total time is $O(mn + mV\log V)$ and auxiliary space is $O(V)$.

## Alternatives and edge cases

- **Enumerate row combinations:** The Cartesian product has $n^m$ selections and is infeasible.
- **GCD-state dynamic programming:** Combining every current GCD with every row value is correct but costs $O(mnV)$ without exploiting the small divisor lattice.
- **Deduplicate a row:** This loses ways because equal-valued cells are distinct positional choices.
- **A row with no multiple of `d`:** Its factor is zero, so no selection is counted in `divisible_ways[d]`.
- **Value `1`:** Any selection containing `1` necessarily has overall GCD `1` and is included naturally.
- **Modulo subtraction:** Normalize each exact count modulo $10^9+7$ after removing strict-multiple counts.
