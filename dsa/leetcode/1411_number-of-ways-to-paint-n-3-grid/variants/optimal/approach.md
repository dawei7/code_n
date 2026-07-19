## General
**Collapse twelve row colorings into two shapes.** Within one row, adjacent cells must differ. Its three colors therefore form one of two structural types:

- `ABA`: the first and third cells share a color. There are $3 \cdot 2 = 6$ such rows.
- `ABC`: all three cells use different colors. There are $3 \cdot 2 \cdot 1 = 6$ such rows.

Rows of the same type have identical transition counts, so their concrete colors do not need to remain separate. Let $a$ and $b$ be the numbers of paintings ending in an `ABA` and `ABC` row, respectively. For the first row, $a=b=6$.

**Count compatible next rows.** From any particular `ABA` row, three `ABA` rows and two `ABC` rows avoid its colors vertically. From any particular `ABC` row, two compatible rows have each type. Consequently the next totals are

$$
a' = 3a + 2b
$$

and

$$
b' = 2a + 2b.
$$

Apply these simultaneous transitions for each remaining row, reducing both counts modulo $10^9 + 7$. The answer is $(a+b) \bmod (10^9+7)$.

The two states partition every horizontally valid row, and each coefficient counts exactly the vertically compatible choices of the destination type. Thus every valid painting extends through exactly one transition, while every counted transition preserves both horizontal and vertical restrictions. Induction over the rows proves that $a+b$ counts all and only valid full-grid paintings.

## Complexity detail
The algorithm performs constant work for each of the $n$ rows, so it takes $O(n)$ time. It retains only the two current state totals and therefore uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Twelve explicit row states:** Enumerate every horizontally valid color triple and transition between compatible pairs. This is still $O(n)$ because the width is fixed, but it uses more states and hides the two-type symmetry.
- **Matrix exponentiation:** Raise the fixed two-by-two transition matrix to the $(n-1)$st power in $O(\log n)$ time. It is asymptotically faster but more machinery than the constraints require.
- **Enumerate complete grids:** Trying all color assignments grows exponentially with $n$ and is infeasible.
- **Single row:** No transition is applied, and the two six-pattern groups give $12$ paintings.
- **Simultaneous update:** Compute both next totals from the old pair before replacing either state.
- **Modulo arithmetic:** Reduce during every transition, not only after constructing the enormous exact count.
