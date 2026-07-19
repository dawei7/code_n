## General
**Match against earlier values.** Scan `arr` once while keeping a set of values already encountered. For a current value `value`, a qualifying earlier partner can have either of two roles: it may equal `2 * value`, or it may be the number whose double is `value`.

The first role is checked directly with `2 * value in seen`. The second is possible only when `value` is even, in which case its exact integer half is `value // 2`. If either partner is present, the current position and the earlier position are distinct by construction, so returning `true` is valid.

Only after both checks fail is `value` inserted into the set. This ordering prevents a single zero from matching itself, while a second zero correctly finds the first. If the scan ends without a match, every pair has been considered when its later member was processed, so no qualifying pair exists.

## Complexity detail
Each of the $n$ values performs a constant expected number of hash-set operations, giving $O(n)$ expected time. The set can hold $n$ distinct values, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Exhaustive pair search:** Testing every pair uses only constant auxiliary space but requires $O(n^2)$ time when no match exists.
- **Sorting with two pointers or binary search:** Sorting supports an $O(n \log n)$ solution, but it is slower than the direct hash-set scan and may alter the input if done in place.
- **One zero:** A single zero cannot use itself as both indices and must not produce a match.
- **Two zeroes:** Two occurrences satisfy `0 == 2 * 0`.
- **Equal nonzero values:** Duplicate values such as `[5, 5]` do not form a double pair.
- **Negative values:** The same factor-of-two relation applies without any special sign handling.
