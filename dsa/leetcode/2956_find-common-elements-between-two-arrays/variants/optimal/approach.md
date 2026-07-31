## General

The requested counts concern indices, so repeated occurrences must contribute
separately. Membership itself, however, depends only on whether a value occurs
at least once in the opposite array. Build `values1` and `values2`, the sets of
values appearing in each array. Then scan `nums1` and count every element found
in `values2`; scan `nums2` symmetrically against `values1`.

Each counted position has a value present in the other array, exactly as the
contract requires. Any qualifying position is found during its array's full
scan, including every duplicate occurrence, so neither answer omits or merges
indices. The two counts therefore form the required result in order.

## Complexity detail

Let $N=\lvert\texttt{nums1}\rvert$ and $M=\lvert\texttt{nums2}\rvert$.
Building both sets and scanning both arrays takes $O(N+M)$ expected time under
standard hash-set behavior. The sets store at most $N+M$ distinct values, so
they use $O(N+M)$ space.

## Alternatives and edge cases

- **Nested membership scans:** Searching the opposite array anew for every index is correct but takes $O(NM)$ time in the disjoint worst case.
- **Frequency maps:** Two frequency maps can combine counts by common values, but sets are sufficient because only opposite-array existence matters.
- **Duplicate values:** Every qualifying index counts, so three copies of one shared value contribute three even if the other array contains it once.
- **Disjoint arrays:** When the sets do not intersect, both returned counts are zero.
- **Asymmetric frequencies:** The two answers can differ because each array's qualifying indices are counted independently.
- **Singleton arrays:** Equal single values produce `[1,1]`; distinct values produce `[0,0]`.
