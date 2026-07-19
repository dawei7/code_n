## General
**View adjacent comparisons on a circle**

Compare every element with its successor, using the first element as the successor of the last. Call an index a descent when `nums[i] > nums[(i + 1) % n]`. Equal adjacent values are not descents because the original order is non-decreasing rather than strictly increasing.

**Allow only the single rotation boundary**

Within each unchanged portion of a sorted array, values cannot decrease. A rotation can introduce only one circular descent: the boundary where the sorted array's largest trailing region is followed by its smallest leading region. More than one descent therefore proves that no single rotation created the input.

**Use the descent as a sufficient cut**

If exactly one descent exists, cutting immediately after it produces a sequence with no internal decrease and therefore a non-decreasing original array. If there is no descent, all circular neighbors are equal or the one-element array is already valid. Thus at most one circular descent is both necessary and sufficient.

## Complexity detail
The algorithm performs one circular comparison per element and can stop after the second descent, taking $O(n)$ time. It stores only the descent count and current index, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Try every rotation:** Sorting a copy and comparing all $n$ rotations is straightforward but requires $O(n^2)$ comparison work after sorting.
- **Find the minimum first:** Choosing one minimum as a presumed cut can fail with duplicates when the same minimum appears in several positions; the circular descent criterion avoids that ambiguity.
- **Zero-position rotation:** An already non-decreasing array must return `True`.
- **Duplicates:** Equal neighbors never count as a descent.
- **All equal:** There are zero descents, so the array is valid.
- **One element:** Its circular comparison is equal and the array is valid.
- **Two elements:** Either ordering is a rotation of the sorted pair.
- **Wraparound comparison:** Omitting the last-to-first pair can accept arrays with two effective rotation boundaries.
