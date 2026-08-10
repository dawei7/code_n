## General

**Count choices by divisibility before asking for an exact GCD**

Choosing one cell from every row can create up to `n^m` combinations, far too many to enumerate. The values, however, are at most 150. The solution groups selections according to divisibility conditions on their eventual greatest common divisor.

Let `V` be the maximum value in the matrix. For each divisor `d` from one through `V`, define `divisible_ways[d]` as:

the number of ways to choose one cell from every processed row such that every chosen value is divisible by `d`.

After all rows are processed, “every chosen value is divisible by `d`” is equivalent to “the GCD of the chosen values is a multiple of `d`.” This count is easier to build because choices from different rows multiply.

**Count divisible positions within one row**

For a current row, the array `frequency` records how many cells contain each value. It counts positions, not merely distinct values. This is essential: if a row contains `[2, 2]`, choosing the first two and choosing the second two are different ways even though both contribute the same numeric value.

For a fixed divisor `d`, the number of eligible cells in this row is

$$
C_{\text{row}}(d)
=
\sum_{\substack{v\le V\\d\mid v}}\operatorname{frequency}[v].
$$

The exact source computes this by iterating

`d, 2d, 3d, ...`

through `V` and summing the corresponding frequencies. Every value visited is divisible by `d`, and every positive multiple within the value range is visited once.

**Multiply independent row choices**

`divisible_ways` starts filled with one. For each row and divisor, the code performs

`divisible_ways[divisor] *= divisible_count`

modulo $10^9+7$.

This multiplication follows the product rule. If the first processed rows offer `A` valid position choices whose values are all divisible by `d`, and the next row offers `B` divisible cells, combining each earlier choice with each eligible cell creates `A * B` choices. Exactly one cell is selected from each row.

After every row,

$$
\texttt{divisible\_ways}[d]
=
\prod_{\text{row}} C_{\text{row}}(d)
\pmod{10^9+7}.
$$

If any row contains no value divisible by `d`, its factor is zero and the complete count becomes zero, correctly showing that no selection can have a GCD divisible by `d`.

For `d = 1`, every positive matrix value is divisible by one, so `divisible_ways[1]` is the total number of position-based selections. The desired answer is a subset of that total: only selections whose exact GCD is one.

**Recover exact GCD counts from multiple-of-divisor counts**

Let `exact_gcd[g]` be the number of selections whose GCD is exactly `g`. Every selection counted by `divisible_ways[d]` has some exact GCD that is a positive multiple of `d`. These exact-GCD groups are disjoint, so

$$
\texttt{divisible\_ways}[d]
=
\texttt{exact\_gcd}[d]
+\texttt{exact\_gcd}[2d]
+\texttt{exact\_gcd}[3d]
+\cdots.
$$

Rearranging gives

$$
\texttt{exact\_gcd}[d]
=
\texttt{divisible\_ways}[d]
-
\sum_{k\ge2,\ kd\le V}\texttt{exact\_gcd}[kd].
$$

The solution evaluates divisors from `V` down to one. When it reaches `d`, every proper multiple `2d, 3d, ...` is larger and has already had its exact count computed. It copies `divisible_ways[d]`, subtracts all those exact-multiple groups, and reduces the result modulo the required modulus.

This is divisor-lattice inclusion–exclusion. It resembles Möbius inversion, but the descending subtraction implements the inversion directly and requires no separately precomputed Möbius function.

**Why subtracting modulo values remains valid**

Counts may become negative temporarily during repeated subtraction. The statement

`exact_gcd[divisor] %= modulo`

maps the integer to its equivalent residue from zero through `modulo - 1`. Addition, multiplication, and subtraction all respect congruence, so performing the whole computation modulo $10^9+7$ gives the required reduced answer.

Although `exact_gcd[multiple]` values are themselves stored modulo the modulus rather than as huge exact integers, subtracting those residues yields the same final residue as subtracting the full counts.

**Walk through the two-row example**

For `mat = [[1, 2], [3, 4]]`:

- For divisor one, both cells in both rows qualify, so `divisible_ways[1] = 2 * 2 = 4`.
- For divisor two, the first row has one eligible cell, two, and the second row has one, four, so `divisible_ways[2] = 1`.
- Larger possible divisors do not create another all-row selection with a common divisor.

Descending inversion identifies one selection with exact GCD two: choosing two and four. Subtracting it from the four selections whose GCD is divisible by one leaves three with exact GCD one.

For `[[2, 2], [2, 2]]`, each row has two positions divisible by two, so four selections have GCD divisible by two. All four total selections are also in `divisible_ways[1]`. Inversion subtracts the exact-GCD-two group from the divisor-one total and returns zero. Duplicate positions are counted correctly throughout.

**Why the final entry is the requested answer**

The row multiplication counts every position-based selection under each divisibility condition. The descending inversion partitions those counts by exact GCD without overlap. Therefore `exact_gcd[1]` counts exactly the selections whose greatest common divisor equals one, which is precisely the requested coprime count.

## Complexity detail

Let `m` be the number of rows, `n` the number of columns, and `V = max(mat)`. Building one row's frequency array and filling it from the row costs $O(V+n)$ time. For that row, the total number of visited multiples across all divisors is

$$
\sum_{d=1}^{V}\left\lfloor\frac{V}{d}\right\rfloor
=O(V\log V).
$$

Across all rows, frequency counting costs $O(mn)$ and divisible-cell summation costs $O(mV\log V)$. The descending exact-GCD inversion performs the same harmonic pattern once more in $O(V\log V)$ time, which is absorbed by the row term for `m >= 1`. The total time complexity is $O(mn + mV\log V)$.

`frequency`, `divisible_ways`, and `exact_gcd` each have `V + 1` entries. Only one row-frequency array exists at a time. The auxiliary space complexity is $O(V)$, excluding the input matrix.

## Alternatives and edge cases

- **Enumerate one choice per row:** This requires $n^m$ combinations in a rectangular matrix and becomes impossible long before the maximum dimensions.
- **Dynamic programming over current GCD:** Updating a `V`-sized GCD distribution for every cell in every row can work in roughly $O(mnV)$ time. Divisibility products and inversion exploit the small value range more efficiently.
- **Deduplicate equal values inside a row:** That would undercount because choices are cell positions. The frequency must contribute the multiplicity of each value.
- **Use sets of divisible values:** A set answers which values qualify but not how many positions hold them. Frequencies preserve the required positional count.
- **Return `divisible_ways[1]` directly:** Every positive number is divisible by one, so that entry counts all selections, not just selections with exact GCD one. Proper-multiple GCD groups must be subtracted.
- **Subtract only prime multiples:** Exact GCD could be `4d`, `6d`, or another composite multiple. The recurrence subtracts every proper multiple exactly once through its already-computed exact group.
- **Process divisors upward:** Then exact counts for proper multiples would not yet be known. Descending order is what makes the recurrence directly evaluable.
- **A row containing the value one:** Selecting that cell guarantees the overall GCD is one, but other choices from that row may still lead to other GCDs. The general count handles both without a special branch.
- **A divisor absent from one row:** Its per-row eligible count is zero, making the product zero. No cross-row selection can then have every value divisible by it.
- **All cells share a common factor greater than one:** Every selection belongs to an exact-GCD group above one, and inversion leaves `exact_gcd[1] = 0`.
- **Single row:** A selection's GCD is simply its chosen value. The answer is the number of cells equal to one, including duplicates, which the formula recovers.
- **Modulo subtraction:** Intermediate negative integers are expected. Applying the modulus after all subtractions for a divisor restores the correct nonnegative residue.
- **Maximum derived from the matrix:** Divisors greater than `V` cannot divide any positive selected value, so no array entries or loops are needed beyond `V`.
