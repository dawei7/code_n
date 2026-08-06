## General
**One forbidden color makes two minima sufficient**

For each completed row, remember the smallest total, its color, and the second-smallest total. A new color adds its cost to the smallest prior total unless that total used the same color; then it uses the second smallest.

After each house, the DP value for every color is the cheapest valid prefix ending in that color. The two retained minima are exactly the best and second-best values of that row.

**Excluding the current color selects the right predecessor**

A prefix ending in color `c` may extend every previous color except `c`. If the cheapest prior state uses another color, it is plainly the best allowed predecessor. If it uses `c`, removing that single forbidden state makes the second-cheapest prior state optimal. Each transition is therefore exact, and induction makes the minimum of the last row globally optimal.

## Complexity detail

For each of the $n$ rows, finding the smallest total and its color, finding the second-smallest total, and building the
next DP row each take $O(k)$ time. The total is therefore $O(nk)$. Only one $k$-value DP row and constant scalar state
are retained, so the auxiliary space is $O(k)$.

## Alternatives and edge cases

- **Compare every prior color:** takes $O(nk^2)$.
- **Tied prior minima:** excluding one minimum color leaves the other equal minimum as `second_minimum`, so no valid tie is lost.
- **No houses:** the defensive app-local guard returns zero, although the native contract requires at least one house.
- **One house:** the zero-initialized prior row makes the result the cheapest color cost. The contract always provides at least two colors.
