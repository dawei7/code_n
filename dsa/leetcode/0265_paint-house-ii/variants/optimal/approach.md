## General
**One forbidden color makes two minima sufficient**

For each completed row, remember the smallest total, its color, and the second-smallest total. A new color adds its cost to the smallest prior total unless that total used the same color; then it uses the second smallest.

After each house, the DP value for every color is the cheapest valid prefix ending in that color. The two retained minima are exactly the best and second-best values of that row.

**Excluding the current color selects the right predecessor**

A prefix ending in color `c` may extend every previous color except `c`. If the cheapest prior state uses another color, it is plainly the best allowed predecessor. If it uses `c`, removing that single forbidden state makes the second-cheapest prior state optimal. Each transition is therefore exact, and induction makes the minimum of the last row globally optimal.

## Complexity detail
Each of `n` rows performs constant work for each of `k` colors, giving $O(nk)$ time. The current DP row uses $O(k)$ space.

## Alternatives and edge cases
- **Compare every prior color:** takes $O(nk^2)$.
- No houses cost zero; one house chooses its cheapest color. Native constraints provide enough colors for multiple houses.
