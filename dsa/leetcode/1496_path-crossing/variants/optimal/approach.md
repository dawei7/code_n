## General
**Represent every location by integer coordinates**

Maintain the current coordinate $(x, y)$, initially $(0, 0)$. A north or south move changes only $y$, while an east or west move changes only $x$. Because every move has unit length and begins at an integer coordinate, the pair after each character identifies the reached location exactly.

The directions themselves are not sufficient history: two equal direction characters may occur in completely different parts of the plane. What matters is whether the resulting coordinate pair has appeared before.

**Include the origin before processing any move**

Initialize a hash set with $(0, 0)$. This records the walk's starting location even though no character produced it. Omitting the origin would miss paths such as `"NS"` or `"NESW"`, whose first repeated point is the start.

For each character, update the appropriate coordinate first. Then test the new pair against the visited set. If it is already present, the definition of a crossing is satisfied and the answer is immediately `true`. Otherwise, insert it and continue.

**Why the first repeated coordinate is decisive**

After processing any prefix of `path`, the set contains exactly the origin and all locations reached by that prefix, provided no crossing has yet occurred. This holds initially. One move computes the next location; membership reports whether it belongs to that complete history, and insertion extends the set with the new location when it does not.

Therefore, a positive membership test can happen only at a genuinely revisited point. Conversely, if the path crosses, consider its earliest repeated location. Every earlier reached coordinate was inserted, so the membership test at that move must detect it. If the scan finishes without such a test, all $N+1$ visited locations are distinct.

## Complexity detail
The scan performs one expected-constant-time hash lookup and at most one insertion for each of the $N$ moves, so expected running time is $O(N)$. At most $N+1$ coordinate pairs are stored, giving $O(N)$ auxiliary space.

The benchmark uses long straight northward paths, for which every coordinate is new. A list-based history must compare each new point with every earlier point and therefore takes $O(N^2)$ time, while the hash-set implementation remains linear.

## Alternatives and edge cases
- **List of visited coordinates:** storing the same history in a list is correct, but each membership test can scan all prior positions, producing $O(N^2)$ time on a non-crossing path.
- **Sort all reached coordinates:** materialize every position, sort the pairs, and check adjacent entries for equality. This is correct in $O(N \log N)$ time and $O(N)$ space but cannot stop at the first crossing.
- **Complex-number coordinates:** encode east/west on the real axis and north/south on the imaginary axis. This keeps the same hash-set algorithm and complexity, though explicit integer pairs make the axes clearer.
- **Return to the origin:** the origin must be present in the set before the first move.
- **Immediate reversal:** `"NS"`, `"SN"`, `"EW"`, and `"WE"` all revisit the start on the second step.
- **Repeated direction without repeated position:** a path such as `"NNNN"` contains repeated characters but never crosses.
- **Touching a non-origin point:** any previously reached coordinate counts, not only a return to $(0, 0)$.
- **Unit grid segments:** because every segment connects adjacent integer coordinates, a geometric intersection or retraced edge necessarily includes a visited endpoint; coordinate tracking captures the crossing.
- **Maximum-length straight path:** all $10^4$ positions are distinct, so the algorithm must scan the entire string and return `false`.
