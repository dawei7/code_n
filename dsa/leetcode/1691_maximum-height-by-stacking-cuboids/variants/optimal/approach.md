## General
**Give every rotation one canonical representation**

Sort the three dimensions inside every cuboid into ascending order. Use the first two entries as its horizontal sides and the largest entry as its vertical height. This loses no optimal stack: if one cuboid's dimensions can be paired with another's so every upper dimension is no larger, then their sorted dimension triples have the same coordinatewise relationship. Sorting both triples pairs the smallest with the smallest, the middle with the middle, and the largest with the largest.

The canonical orientation also chooses the largest possible height for every selected cuboid. Because all three sorted coordinates participate in the same containment test, making the largest coordinate vertical does not invalidate a compatible relation that another orientation could achieve.

**Turn the stack into a weighted ordered chain**

Sort the normalized triples lexicographically. If cuboid `top` can be placed on cuboid `bottom`, every coordinate of `top` is at most the corresponding coordinate of `bottom`, so `top` cannot appear after `bottom` in this order. Equal triples remain separate input cuboids and can all be used; their arbitrary relative order is sufficient.

Let `best[bottom]` be the greatest height of a valid stack whose bottom cuboid is `bottom`. Initially that stack contains only the bottom, contributing its largest normalized dimension. For each earlier `top`, test all three coordinate inequalities. When they hold, append `bottom` below the best stack ending at `top` and update with

$$
\texttt{best[bottom]} = \max\bigl(\texttt{best[bottom]},\; \texttt{best[top]} + \texttt{normalized[bottom][2]}\bigr).
$$

Every update preserves coordinatewise compatibility. Conversely, remove the bottom cuboid from any optimal stack ending there: the remaining stack ends at some earlier compatible cuboid whose optimal height has already been recorded. The transition therefore considers its exact predecessor, so induction over the sorted order proves that every `best` value is optimal. The maximum entry allows the chosen subset to end at any cuboid.

## Complexity detail
Normalizing all triples takes $O(n)$ time, sorting them takes $O(n \log n)$ time, and checking every ordered pair takes $O(n^2)$ time. The DP array and normalized list require $O(n)$ auxiliary space because each cuboid has exactly three dimensions.

## Alternatives and edge cases
- **Enumerate rotations as separate boxes:** three choices of vertical dimension per cuboid can also model orientations, but the state must prevent reusing the same physical cuboid; canonical normalization avoids that bookkeeping.
- **Repeated edge relaxation:** treating compatible pairs as a DAG and repeatedly relaxing every edge eventually finds the same longest weighted chain, but an unstructured $n$-round method takes $O(n^3)$ time.
- **Greedy by largest height:** selecting the tallest available cuboid can block several shorter compatible cuboids whose combined height is greater.
- **Compare only base dimensions:** the contract also requires the upper vertical dimension to be no greater, so all three normalized coordinates must pass.
- **Identical cuboids:** distinct equal triples may all be stacked because equality is allowed in every dimension.
- **Incomparable triples:** when one cuboid is larger in one coordinate but smaller in another, neither orientation permits the canonical coordinatewise relation and they cannot be adjacent.
- **One cuboid:** rotate its largest dimension vertically; the answer is that dimension.
