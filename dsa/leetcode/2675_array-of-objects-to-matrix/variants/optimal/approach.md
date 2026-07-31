## General

Recursively flatten each top-level item into a map from complete leaf path to primitive value. When visiting an object or array, extend the current path with each property key or array index; when visiting a primitive or `null`, store it at that path. Empty containers have no entries and therefore add no leaf path.

Collect every flattened map's keys into a set, convert the set to an array, and sort it lexicographically to obtain the header. For each flattened row, traverse that same header and use an own-property check to distinguish a present value such as `null`, `false`, `0`, or `""` from an absent path. Emit the stored value when present and `""` otherwise.

The recursive traversal records every primitive at exactly its full path. The union therefore contains exactly the required columns, and sorting establishes the required order. Looking up each header path in each row places every leaf in its unique column while filling precisely the missing cells.

## Complexity detail

Flattening visits $S$ properties and array elements. Sorting the $k$ paths costs $O(k \log k)$ comparisons, and materializing $r$ rows of $k$ cells costs $O(rk)$, for $O(S + k \log k + rk)$ total time. The flattened maps and output matrix use $O(S + rk)$ space; recursion additionally uses depth proportional to the deepest input nesting.

## Alternatives and edge cases

- **Resolve every cell from the original object:** Re-parsing a dotted path or scanning a row for each matrix cell repeats nested work and can be asymptotically slower than flattening once.
- **Build columns in encounter order:** A set alone deduplicates paths but does not satisfy the required lexicographic ordering without the final sort.
- `null` is a leaf value, while an empty object or array contributes no column.
- Empty strings, zero, and `false` are present values and must not be replaced through truthiness checks.
- Array indices are string path components and follow the same period-separated notation as object keys.
