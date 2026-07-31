## General

**Separate arrays by their final value.** Let $Z[i][j]$ count stable arrays using exactly $i$ zeroes and $j$ ones that end in `0`, and let $O[i][j]$ count those that end in `1`. The boundary states are $Z[i][0]=1$ for $1\le i\le\texttt{limit}$ and $O[0][j]=1$ for $1\le j\le\texttt{limit}$; longer one-value arrays are forbidden.

**Append a value, then remove one invalid class.** Appending `0` to every stable array counted by `Z[i - 1][j] + O[i - 1][j]` produces every candidate ending in `0`. When $i>\texttt{limit}$, the candidates whose trailing zero run now has length `limit + 1` are in bijection with arrays counted by `O[i - limit - 1][j]`: take such an array and append exactly `limit + 1` zeroes. Therefore

$$
Z[i][j]=Z[i-1][j]+O[i-1][j]-O[i-\texttt{limit}-1][j],
$$

where the subtraction term is used only when $i>\texttt{limit}$. By symmetry,

$$
O[i][j]=Z[i][j-1]+O[i][j-1]-Z[i][j-\texttt{limit}-1]
$$

when $j>\texttt{limit}$, and the subtraction is omitted otherwise. Normalize every value modulo $10^9+7$.

These transitions are correct by induction on $i+j$. Each extension starts from a shorter stable array, and the single subtracted class is exactly the class that violates the trailing-run bound. Conversely, removing the final bit from any stable non-boundary array reaches one of the predecessor states, so no valid array is missed. The two final-bit classes are disjoint, making `Z[zero][one] + O[zero][one]` the required total.

## Complexity detail

Let $z=\texttt{zero}$ and $o=\texttt{one}$. There are $(z+1)(o+1)$ pairs of states, and each of the two transitions takes constant time after the prefix-window subtraction is derived. The algorithm therefore uses $O(zo)$ time and $O(zo)$ auxiliary space.

## Alternatives and edge cases

- **Track the trailing run length:** A memoized or tabulated state `(used_zero, used_one, last, run)` is direct but has $O(zo\cdot\texttt{limit})$ time and space.
- **Sum every possible final run:** Compute each ending state by summing all opposite-ending states reached after placing 1 through `limit` equal bits. This is correct but repeats a length-`limit` window sum and takes $O(zo\cdot\texttt{limit})$ time.
- **Count run compositions:** Choose the number of alternating runs and count bounded positive compositions of the zeroes and ones. Inclusion-exclusion makes this viable, but the boundary bookkeeping is more intricate than the two-state recurrence.
- **Limit equal to 1:** Every valid array must alternate, so a count imbalance greater than one makes the answer zero.
- **Limit at least both counts:** No run can exceed the limit, so all $\binom{z+o}{z}$ binary arrangements are valid.
- **Modular subtraction:** Normalize after subtracting the newly invalid window so negative intermediate values do not leak into languages without Python-style modulo behavior.
