## General
**Split pairs by where their indices lie**

Merge sort recursively counts pairs entirely inside the left half and entirely inside the right half. The only missing pairs have their first index in the left half and second index in the right half.

**Count cross pairs before merging**

Once both halves are sorted, scan left values in ascending order and maintain a pointer into the right half. While `left_value > 2 * right_value`, advance the pointer. Because later left values are no smaller, the pointer never moves backward. Its offset from the right-half start is the number of valid partners for that left value.

**Merge to preserve the recursive condition**

After cross counting, merge the two sorted halves into a shared buffer and copy the result back. The parent call then receives sorted children and can use the same monotonic-pointer argument.

**Why every pair is counted once**

Every index pair has a unique lowest recursive split that places its indices in opposite halves. It is counted as a cross pair at exactly that split; pairs remaining in one half are delegated to one child. The sorted two-pointer scan includes precisely those right values satisfying the strict inequality, so neither omissions nor duplicates occur.

## Complexity detail
Each recursion level performs linear cross counting and merging across all subarrays. There are $O(\log n)$ levels, giving $O(n \log n)$ time. The merge buffer uses $O(n)$ space and the recursion stack uses $O(\log n)$ additional space.

## Alternatives and edge cases
- **Nested pair scan:** directly tests every $i < j$ and is correct, but takes $O(n^2)$ time.
- **Fenwick tree with coordinate compression:** processes values while querying doubled thresholds in $O(n \log n)$ time.
- **Balanced ordered multiset:** can count prior values above each threshold, but requires rank queries and careful duplicate handling.
- **Negative values:** may form reverse pairs with other negative values; do not assume only positives matter.
- **Strict inequality:** equality with exactly twice the right value does not count.
- **Large magnitudes:** languages with fixed-width integers must widen before multiplying by two.
- **Empty or one-element array:** contains no index pair.
