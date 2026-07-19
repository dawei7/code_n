## General
**Each color state excludes one previous color**

Track the cheapest valid prefix ending in each of the three colors. To paint the next house red, add its red cost to the smaller prior blue/green total, and analogously for the other colors.

After processing house `i`, each state is the minimum cost of every valid coloring through `i` whose final color is that state's color.

**Three optimal prefixes are sufficient for the next decision**

Any valid coloring ending in red must previously end in blue or green; there is no other legal predecessor. Adding the red cost to the cheaper of those two optimal prefixes therefore produces the cheapest red-ending prefix. The same exhaustive transition holds for the other colors. Induction keeps all three states optimal, and the cheapest final state is the global optimum.

## Complexity detail
Three constant-time transitions are performed per house for $O(n)$ time. Three scalar totals use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate colorings:** explores exponentially many assignments.
- **Recompute every prefix:** remains correct but can cost $O(n^2)$.
- An empty input costs zero; a single house uses its cheapest color.
