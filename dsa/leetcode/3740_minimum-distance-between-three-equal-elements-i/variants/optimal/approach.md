## General

Order any good tuple's indices as $a<b<c$. Its distance simplifies to

$$
(b-a)+(c-b)+(c-a)=2(c-a).
$$

Thus, for three occurrences of one value, only the first and last selected indices determine the distance. If another occurrence of that value lies between two selected occurrences, replacing an outer choice with the nearer interior occurrence cannot increase the span. A minimum-distance triple must therefore consist of three consecutive occurrences of its value.

Scan the array from left to right and retain the latest two indices for every value. When that value appears again at index `i`, those stored positions and `i` form the newest consecutive occurrence triple. Its distance is twice the difference between `i` and the older stored index. Evaluate it, discard that older index, and retain the two newest positions for future triples. Every possible minimum candidate is examined exactly when its third occurrence arrives.

## Complexity detail

Each of the $n$ indices is processed once with constant-time state updates, so the running time is $O(n)$. The per-value occurrence state uses $O(n)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Enumerate all triples:** Testing every three-index combination follows the definition directly but takes $O(n^3)$ time.
- **Store every occurrence list:** Grouping all indices and then scanning each list is also $O(n)$ time, but keeping only two recent positions uses less retained state.
- **Fewer than three occurrences:** Such a value cannot form a good tuple and contributes no candidate.
- **Exactly three adjacent equal values:** Their indices differ by one, producing the smallest possible distance `4`.
- **More than three occurrences:** Consecutive triples overlap, and each must be considered because a later span may be smaller.
- **Tuple ordering:** Reordering the same three indices does not change the three pairwise absolute differences.
