## General

**Keep parallel data attached.** A name has meaning only with the height at the same index. Combine each height and name into one pair before reordering so sorting can never separate a person from their measurement.

**Sort by the ordering key.** Sort the pairs in descending order of height, then read the name component from left to right. Because all heights are distinct, every pair has one unambiguous position; duplicate name strings do not create a tie because they still belong to different heights.

The sorted height sequence is strictly descending by construction. Each input pair appears exactly once in that sequence, so the extracted list contains every original person exactly once and in the required order.

## Complexity detail

Creating and sorting $n$ pairs costs $O(n\log n)$ time, and extracting their names costs $O(n)$. The paired records and returned list occupy $O(n)$ space.

## Alternatives and edge cases

- **Height-to-name map:** Distinct heights permit a dictionary followed by sorted keys, with the same $O(n\log n)$ time and $O(n)$ space.
- **Repeated tallest selection:** Searching all remaining people for each output position is correct but costs $O(n^2)$ time.
- **Single person:** The only name is returned unchanged.
- **Duplicate names:** Equal strings represent separate people and must remain associated with their distinct heights.
- **Already descending:** Sorting preserves the existing required order.
- **Reverse order:** Initially ascending heights must reverse the paired names completely.
