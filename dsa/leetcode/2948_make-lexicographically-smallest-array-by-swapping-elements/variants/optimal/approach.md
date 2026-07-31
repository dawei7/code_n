## General

**Swaps create value components.** Regard values as vertices connected when
their difference is at most `limit`. If two values are joined by a path,
successive legal swaps along that path can move values throughout the
component, even when the path's endpoints differ by more than `limit`.
Because transpositions along the edges of a connected graph generate every
permutation of its vertices, all values in one component can be rearranged
among all indices currently holding component values.

**Sorted gaps identify exactly those components.** Sort pairs of
`(value, original_index)` by value. Consecutive sorted values belong to the
same component when their difference is at most `limit`. A larger gap splits
components: every value on the left is smaller than every value on the right,
so no cross-gap pair can satisfy the limit. Maximal sorted runs separated by
large gaps are therefore precisely the transitive swap components.

**Minimize each component greedily.** For one component, collect and sort its
original indices. Its values are already sorted in the value-ordered run.
Assign the smallest component value to the smallest component index, the next
value to the next index, and so on. At the first component index where any
other reachable assignment differs, that other assignment must use a larger
value, so this assignment is lexicographically minimal. Components cannot
exchange values, making the combination of their minimal assignments globally
minimal.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Sorting value-index pairs and component
indices takes $O(N\log N)$ total time; scanning and assignment take $O(N)$.
The ordered pairs, index lists, and answer use $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Union-find on adjacent sorted values:** Unioning every qualifying adjacent pair produces the same components in $O(N\log N)$ total time.
- **Build every legal graph edge:** Comparing all value pairs can take $O(N^2)$ time and stores far more edges than connectivity requires.
- **Quadratic selection sorting:** Sorting values and component indices without an efficient sort remains correct but takes $O(N^2)$ time.
- **Transitive bridges:** Two values farther apart than `limit` may still share a component through intermediate values.
- **Difference equal to limit:** The swap condition is inclusive, so such values are connected.
- **Duplicate values:** Equal values always belong to the same component.
- **Single element or isolated component:** Its value remains at its original index.

