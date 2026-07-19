## General
**Order only the distinct values**

Create a set from `arr` to discard duplicates, then sort those distinct values ascending. Enumerating the sorted sequence from 1 defines the unique smallest legal rank for every value. Store this mapping in a hash table.

Scan the original array and replace each element by its mapped rank. Because the mapping is built from sorted distinct values, equal inputs use the same entry, every strict increase advances to a larger rank, and no integer rank is skipped. Those properties are exactly the ranking rules and establish minimality.

## Complexity detail
Building the set and transforming the result take expected $O(n)$ time. Sorting at most $n$ distinct values costs $O(n\log n)$, which dominates. The distinct set, rank map, sorted values, and output use $O(n)$ space.

## Alternatives and edge cases
- **Binary search per element:** Sort the distinct values and locate every input rank with binary search, preserving $O(n\log n)$ time but avoiding a separate rank map.
- **Count smaller distinct values:** Scanning all distinct values for every element is direct but can take $O(n^2)$ time.
- **Empty array:** Return an empty array without calling `min` or indexing a sorted value.
- **All equal:** Every element receives rank 1.
- **Negative values:** Numeric ordering, not magnitude, determines ranks.
- **Gaps in values:** Ranks remain consecutive because absent integers do not consume ranks.
