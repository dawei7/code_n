
## General

Sorted order allows the two arrays to be merged conceptually without storing their intersection. Keep one pointer at the smallest unexamined value in each array.

If the pointed values match, that value is common. Everything skipped earlier was smaller and could not match the other array, so this first equality is necessarily the minimum common value and can be returned immediately.

When the values differ, advance the pointer holding the smaller one. That smaller value cannot occur at or beyond the other pointer because the other array is non-decreasing and already points to a larger value. Advancing it therefore discards no possible match. Repeating this rule either finds the minimum common value or exhausts one array, after which no common value remains.

## Complexity detail

Let $n=\lvert\texttt{nums1}\rvert$ and $m=\lvert\texttt{nums2}\rvert$. Each pointer advances at most through its own array, so the algorithm takes $O(n+m)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Hash set:** Storing one array and scanning the other also takes expected $O(n+m)$ time, but requires $O(\min(n,m))$ additional space and does not exploit both sorted orders.
- **Binary search:** Searching every value of the shorter array in the longer one takes $O(\min(n,m)\log\max(n,m))$ time and $O(1)$ space.
- **Nested comparison:** Comparing every pair is correct but can take $O(nm)$ time when the arrays are disjoint.
- **Duplicate values:** Advancing one pointer at a time remains correct; equality is detected as soon as both pointers reach the duplicated value.
- **No intersection:** If either pointer reaches the end before an equality, the correct sentinel is `-1`.
- **Common boundary value:** A match may occur at the first entries or only at the final entries; the same pointer invariant covers both.
