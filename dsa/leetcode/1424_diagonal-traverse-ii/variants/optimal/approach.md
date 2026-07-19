## General
**Bucket by coordinate sum.** Scan rows from top to bottom and values within each row from left to right. Place `nums[row][column]` into the bucket at index `row + column`. Grow the bucket list whenever a new largest diagonal index appears.

**Restore direction within each diagonal.** Because rows are scanned in increasing order, values enter each bucket from the smallest row index to the largest. The required order inside a diagonal is the reverse, so after collection, visit the buckets by increasing index and append each bucket in reverse insertion order.

**Why the buckets preserve exact order.** Every coordinate belongs to exactly one sum bucket, and bucket indices directly encode the required global diagonal ordering without a sort. Reversing a bucket changes its top-to-bottom insertion order into the required bottom-to-top traversal. Thus every value appears once in exactly its specified position.

## Complexity detail
Each of the $N$ values is appended once and read once. The largest possible diagonal index is $O(N)$ because rows are nonempty and the total row and column extent is bounded by the number of values. Time is therefore $O(N)$, and the buckets plus output use $O(N)$ space.

## Alternatives and edge cases
- **Sort coordinate triples:** Store `(row + column, -row, value)` for every element and sort. It is correct but takes $O(N\log N)$ time.
- **Rescan rows for every diagonal:** Check possible coordinates one diagonal at a time. This repeats row work and can become superlinear.
- **Queue traversal:** Seed the first element of each row at the appropriate time and use a queue. It can achieve $O(N)$ but is more intricate for jagged rows.
- **Single row:** Increasing diagonal sums preserve ordinary left-to-right order.
- **One value per row:** Each value occupies a new diagonal and remains in row order.
- **Long later row:** Bucket indices may extend far beyond earlier row lengths, so grow storage dynamically.
- **Duplicate values:** Ordering depends only on coordinates, not value identity.
