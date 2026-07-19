## General
**Count the fixed alphabet**

Build two frequency arrays of length $26$. The alphabet size is constant, so these counts retain everything needed about the strings while discarding their irrelevant character order.

**Evaluate both strict-order directions**

Choose a boundary after some letter from `a` through `y`. To make every character in `a` at most that boundary and every character in `b` above it, change the suffix characters of `a` plus the prefix characters of `b`. Prefix sums of the two frequency arrays give this cost for every boundary. Swap the roles of the strings to evaluate the second condition. A boundary after `z` is excluded because the higher side must contain a lowercase letter and the relation is strict.

**Evaluate one shared distinct letter**

For the third condition, choose one target letter for both strings. If that letter occurs $f$ times across the combined input, exactly $N-f$ positions must change. Keeping the most frequent combined letter minimizes this cost. The answer is the minimum over these shared-letter choices and both directions at all $25$ valid boundaries.

## Complexity detail
Counting visits each of the $N$ input characters once. Scanning the fixed $26$-letter alphabet takes constant additional work, so total time is $O(N)$. The two frequency arrays always contain $26$ integers and therefore use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Sort both strings:** Sorting supports boundary counts but takes $O(N\log N)$ time and stores reordered characters.
- **Try replacements directly:** Enumerating possible changed strings grows exponentially and ignores that only frequencies affect the conditions.
- **Already strictly ordered:** Return zero without requiring either string to use a single letter.
- **Already one shared letter:** The third condition yields zero even when strict ordering is impossible.
- **Equal boundary letters:** Strictly less forbids the same letter from remaining on both sides of an ordering boundary.
- **One-character strings:** Either ordering direction or the shared-letter condition may be optimal.
- **Boundary at `y`:** The higher side must become all `z`, which remains valid.
