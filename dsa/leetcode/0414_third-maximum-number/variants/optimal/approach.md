## General
**Track three ordered distinct maxima**

Maintain `first`, `second`, and `third`, initially absent. Ignore a value equal to any occupied slot because duplicates do not change distinct rank.

**Insert a new value at its rank**

If the value exceeds `first`, shift the previous first and second values down and install it. Otherwise compare with `second`, then `third`, shifting only the lower ranks affected by the insertion.

**Choose the required fallback**

After one scan, an occupied `third` is exactly the third-largest distinct value. If it is absent, there were only one or two distinct values, and `first` is the required maximum.

**Why the three slots remain correct**

Initially they represent the maxima of an empty prefix. Ignoring duplicates preserves that property. Inserting a new distinct value into the first position it exceeds and shifting lower ranks is the standard ordered insertion step, so induction keeps the slots equal to the three greatest distinct values of every processed prefix.

## Complexity detail
Each of the `n` values undergoes a constant number of comparisons and assignments, giving $O(n)$ time. Three optional numeric slots use $O(1)$ space.

## Alternatives and edge cases
- **Set plus descending sort:** is concise but takes $O(n \log n)$ time and $O(n)$ space.
- **Keep a set capped at three values:** insert each distinct value and remove the minimum when necessary; it also has linear time and constant-size storage.
- **Explicit insertion-sort of all distinct values:** can take $O(n^2)$ time.
- Duplicate maxima count only once.
- Negative values retain their ordinary numeric ordering.
- Fewer than three distinct values trigger the maximum fallback.
- Sentinel numeric values are unsafe because the full integer range is valid; use absence markers.
