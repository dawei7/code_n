## General
**Maximum cells belong to every operation**

Each operation adds exactly one to its prefix rectangle. A cell receives the largest possible total only when it lies inside every operation; missing any rectangle leaves it at least one increment behind cells in the common intersection.

**Intersect prefix rectangles by their minimum dimensions**

All rectangles share the origin, so their intersection has height equal to the smallest `a` and width equal to the smallest `b`. Every cell in that rectangle receives all `k` increments, and every cell outside misses at least one.

**Handle no operations as the whole matrix**

When `ops` is empty, every cell remains zero and ties for the maximum. Initialize the intersection dimensions to `m` and `n`, update them for each operation, and return their product.

**Why the product is exact**

The maintained height and width are the coordinate-wise minimum across all processed rectangles, so their product counts precisely the cells contained in every one. Those cells receive the full number of increments. Any cell outside the intersection violates at least one minimum boundary and receives fewer increments, proving that no other cell ties them unless there are no operations, when the initialized whole matrix is correct.

## Complexity detail
For `k` operations, scan each pair once and maintain two minima, taking $O(k)$ time and $O(1)$ extra space. Matrix dimensions do not affect the work.

## Alternatives and edge cases
- **Simulate the matrix:** is correct but may require $O(mn)$ space and $O(sum(a b))$ update time.
- **Two-dimensional difference array:** reduces rectangle updates but still allocates and scans the full matrix unnecessarily.
- **No operations:** all `m n` cells share the maximum zero value.
- **One operation:** its `a b` cells are maximal.
- **Operation covering the whole matrix:** does not shrink the common intersection.
- **Repeated operations:** contribute multiple increments but leave the intersection dimensions unchanged.
- **Different limiting operations:** one may supply the minimum height and another the minimum width.
