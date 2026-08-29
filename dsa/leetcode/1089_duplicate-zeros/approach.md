## General

**Why ordinary left-to-right writing destroys unread data**

Duplicating a zero shifts every later logical element one position farther right. If the algorithm writes those shifted values from left to right inside the same fixed array, a newly written duplicate can overwrite an original value before that value has been read. An extra output array would avoid the problem, but the contract requires an in-place modification with constant auxiliary space.

The safe direction for the actual copy is therefore right to left. Before that copy can begin, the algorithm must determine which original element is the last one that contributes to the fixed-length result. Some original suffix elements are pushed beyond the array and must never be copied.

**Measure the virtual expanded length**

The first loop uses two conceptual positions. `i` is an index in the original array, initially before the first element at `-1`. The value `k` is how many positions the examined source prefix would occupy after zero duplication.

Each iteration advances `i` to the next source element. A nonzero occupies one destination position, so it adds one to `k`. A zero occupies two positions, so the conditional expression adds two. The loop continues while the virtual length is smaller than the real length `n`.

When it stops, `i` points to the last source element that contributes at least one copy to the result. Because an iteration adds only one or two, `k` can finish in only two states:

- `k == n` means the source prefix fits the destination exactly.
- `k == n + 1` means the last processed item was a zero whose first copy fits but whose duplicate would fall one position beyond the boundary.

It cannot overshoot by more than one, and a nonzero cannot cause the overshoot because it increases `k` by only one.

For `[1,0,2,3,0,4,5,0]`, virtual positions grow by one for nonzeros and two for zeros. The scan stops once the prefix through `4` accounts for all eight output slots. Original values `5` and the final zero are outside the source prefix that survives after shifting.

**Handle a half-fitting boundary zero**

The second state is the subtle edge case. If `k == n + 1`, the zero at source index `i` has room for only one copy at the final destination index `j = n - 1`. The code writes that zero directly to `arr[j]`. It then decrements both `i` and `j`, excluding the already handled source zero and filled destination slot from the backward copy.

Without this adjustment, the general zero-copy logic would try to write two zeros even though only one destination slot remains. It could use an invalid or unrelated index and misalign the rest of the array.

**Copy the surviving prefix backward**

After any boundary adjustment, `i` identifies the rightmost unprocessed source value and `j` identifies the rightmost unfilled destination position. The loop condition `while ~j` is compact Python: `~j` equals `-j - 1`. It is nonzero while `j` is zero or positive, and it becomes zero exactly when `j == -1`. Thus the condition is equivalent to `while j >= 0`.

For a nonzero source value, one destination slot is needed, so `arr[j] = arr[i]` copies it once. For a zero, two consecutive slots are needed. The chained assignment `arr[j] = arr[j - 1] = arr[i]` writes zero to both, and the extra `j -= 1` accounts for the additional slot. The common final update then moves both source and destination indices one step left.

At the start of every backward iteration, the destination suffix strictly to the right of `j` is already final, while all still-needed original values lie at or to the left of `i`. Writing at the far-right unfilled position cannot destroy any unread source value that will be needed later. After copying one source element, the same statement holds for the shorter prefix. When `j` becomes negative, every array position is final.

The function returns nothing. All observable work is the mutation of `arr`, exactly as the contract requires.

## Complexity detail

Let $n$ be the fixed array length. The virtual-length scan advances `i` at most $n$ times. The backward copy decreases `j` on every iteration and sometimes twice for a zero, so it performs at most $n$ destination writes up to constant factors. The two sequential passes therefore take $O(n)$ time.

The algorithm stores only `n`, two source or destination indices, and the virtual length. It allocates no list proportional to the input and performs all writes inside `arr`, so auxiliary space is $O(1)$.

The array itself remains length $n$. Values logically shifted past index $n-1$ are never materialized, which is precisely why the first pass finds the surviving source boundary before copying.

## Alternatives and edge cases

- **Extra output array:** Simulate duplication from left to right into a new list and copy its first $n$ values back. This is easy to reason about but uses $O(n)$ extra space and misses the in-place objective.
- **Repeated insertion and deletion:** Insert a zero next to every zero and trim the end. Python list insertion shifts many elements, so the worst-case time becomes $O(n^2)$ even if the final length is restored.
- **Count duplicable zeros explicitly:** The editorial formulation counts how many duplicates fit and then uses an offset during a backward pass. It is equivalent to tracking the virtual destination length used here.
- **No zeros:** The first scan advances one virtual position per source element, and the backward loop copies every value onto itself. The array remains unchanged.
- **All zeros:** Only the prefix needed to fill $n$ virtual slots is considered. Backward writes still leave every array position zero.
- **Length one with zero:** The forward scan overshoots to two, the boundary case writes the sole zero, and both indices move before the general loop.
- **Length one with nonzero:** The virtual length reaches one exactly, and the backward pass copies that single value.
- **Boundary zero with only one slot:** This is exactly the `k == n + 1` case. Only one zero is written because its duplicate would be truncated.
- **Zero with two available slots:** The general backward branch writes two copies, and at that point `j` is at least one, so `j - 1` is a valid destination.
- **Values after the surviving prefix:** They are intentionally discarded because duplication of earlier zeros shifts them beyond the fixed array boundary.
- **Input mutation:** Callers must inspect the original list after the method returns. Assigning the return value is incorrect because the method deliberately returns `None`.
- **Compact loop condition:** `while ~j` is valid Python but less readable than `while j >= 0`. Both have identical behavior for the integer index used here.
