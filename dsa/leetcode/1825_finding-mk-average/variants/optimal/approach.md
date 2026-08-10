## General

**Keep only the active window and split it by rank.** An MKAverage depends exclusively on the last `m` stream values. Among those values, the smallest `k` and largest `k` must be discarded, while the remaining `m - 2k` values must be summed and averaged. Re-sorting all `m` values for every query would repeat almost all previous work. This implementation instead maintains the window continuously in three ordered multisets:

- `lo` contains the smallest values, with a target size of `k`.
- `mid` contains the values that contribute to the average.
- `hi` contains the largest values, with a target size of `k`.

All three are `SortedList` objects, so equal values are preserved as separate occurrences and the smallest or largest element can be accessed by position. The ordering invariant is that every value in `lo` is no greater than every value in `mid`, and every value in `mid` is no greater than every value in `hi`. Boundaries may contain equal values; rank removal does not require equal copies to have distinct identities.

The deque `q` stores the active values in arrival order. It answers a different question from the sorted lists: when the window grows beyond `m`, `q.popleft()` identifies exactly which oldest stream occurrence must expire. Finally, `s` stores the sum of all values currently represented by `mid`. Because only this middle partition contributes to the MKAverage, a query can use `s` immediately rather than summing the partition again.

**Insert into a partition whose range can contain the value.** The new number is first placed according to the current boundaries.

- If `lo` is empty or `num <= lo[-1]`, it belongs on the low side and is added to `lo`.
- Otherwise, if `hi` is empty or `num >= hi[0]`, it belongs on the high side and is added to `hi`.
- Otherwise, it lies between the two boundaries, so it is added to `mid` and also added to `s`.

This is only an initial placement. A bucket may temporarily have the wrong size, and later rebalancing repairs that. What matters now is that inserting on the proper side does not violate the sorted relationship between buckets.

The new value is also appended to `q`. If this makes the deque longer than `m`, the oldest value `x` is removed. The code searches `lo` first, then `hi`, and otherwise removes it from `mid`. Removing from `mid` also subtracts `x` from `s`.

**Why duplicate values do not make removal ambiguous.** The deque identifies an old occurrence by value, but the sorted containers do not attach arrival IDs to equal copies. If the same value appears in more than one boundary bucket, the code may remove an equal copy from `lo` even if one imagines that the expiring occurrence was in `mid`. This is harmless. Equal copies are interchangeable for rank and sum purposes. The combined multiset still loses exactly one occurrence of `x`, and rebalancing subsequently restores the required bucket sizes. If a middle copy is moved across the boundary as a result, `s` is adjusted during that move, yielding the same middle sum that occurrence-level tracking would produce.

**Shrink oversized boundary buckets.** The first two balancing loops enforce the upper size limits.

- While `lo` has more than `k` values, `lo.pop()` removes its largest value. That value is the low-side element closest to the middle, so it is inserted into `mid` and added to `s`.
- While `hi` has more than `k` values, `hi.pop(0)` removes its smallest value. That is the high-side element closest to the middle, so it too enters `mid` and is added to `s`.

Choosing these boundary elements is essential. Moving the smallest value out of `lo`, for example, could leave a larger low value below a smaller middle value and destroy the rank partition.

**Fill undersized boundary buckets from the middle.** Expiring an old value can leave `lo` or `hi` short. The next loops repair those deficits when `mid` is nonempty.

- While `lo` contains fewer than `k` values, `mid.pop(0)` takes the smallest middle value and moves it into `lo`. The value is subtracted from `s` because it is no longer averaged.
- While `hi` contains fewer than `k` values, `mid.pop()` takes the largest middle value and moves it into `hi`, again subtracting it from `s`.

After enough stream elements exist, these steps make `lo` and `hi` contain exactly `k` values each. Before that point, the middle can be empty and one or both sides can be smaller than `k`; that is fine because queries must return `-1` until the window reaches size `m`.

**Why size balancing also preserves value ordering.** Insertion uses the current low maximum and high minimum to choose a compatible bucket. Overflow moves only the element nearest the middle. Underflow is filled only by the nearest middle element. Deletion cannot introduce a new out-of-order value; it merely creates a hole. Therefore no explicit swap loop between `lo` and `hi` is needed. The placement and boundary moves maintain the ordering invariant together.

**Calculate in constant query work.** If `len(q) < m`, the definition says there are not yet enough elements, so `calculateMKAverage` returns `-1`. Once the deque has `m` elements, the middle contains exactly `m - 2k` values and `s` is their exact sum. The result is

`s // (m - 2 * k)`.

All stream values are positive, so Python’s integer floor division is exactly the requested average rounded down. The constraint `2k < m` guarantees a positive denominator.

**Why the maintained answer is correct.** Consider the active window as one sorted multiset. Its first `k` ranks are precisely `lo`, its last `k` ranks are precisely `hi`, and all ranks between them are `mid`. This follows from the bucket sizes and cross-bucket ordering. Those are exactly the values the definition says to discard and retain. Every addition inserts one new occurrence, every expiration deletes one old occurrence, and every cross-bucket move updates `s` exactly when a value enters or leaves `mid`. Thus `s` always equals the sum of the retained ranks, making the returned quotient the required MKAverage.

For the sample with `m = 3` and `k = 1`, the first complete window is `[3, 1, 10]`. The partitions become `lo = [1]`, `mid = [3]`, and `hi = [10]`, so `s = 3`. After enough fives arrive, expiration removes the older values, the three equal fives occupy the three rank regions, and the middle sum becomes five. Equal boundary values cause no difficulty because one copy is still discarded at each end and one copy remains in the middle.

## Complexity detail

Let `m` be the window size and let `q` be the number of calls to `addElement`. Each sorted partition holds at most `m` active occurrences in total. A `SortedList` search, insertion, membership test, removal, or boundary pop takes logarithmic time in the active size under the ordered-container interface used here. Each added value is inserted once, at most one expired value is removed, and only a constant number of boundary values can move during that call: insertion or deletion changes a bucket size by only one. Therefore `addElement` takes `O(log m)` time, and `q` additions take `O(q log m)` time. `calculateMKAverage` performs only a length check, subtraction, multiplication, and floor division, so it takes `O(1)` time.

The deque and the three sorted lists together store exactly the active occurrences, never more than `m` after an addition finishes. The remaining fields are scalars, so the maintained data structure uses `O(m)` space. This exact implementation does not allocate a value-frequency array of size `U`; its costs are governed by the window size and ordered-container operations. Any broader `O(U + q log U)` accounting assumes a different value-domain structure or uses `U` as a loose bound, rather than describing the storage actually present in this code.

## Alternatives and edge cases

- **Sort on every calculation:** Copying and sorting the last `m` values is simple, but each query costs `O(m log m)` instead of reusing the maintained rank partition.
- **Fenwick tree over the bounded value domain:** Frequency and sum trees can locate rank cutoffs and compute retained sums in `O(log U)` time, where `U` is the maximum value. This is efficient but requires coordinate or domain indexing and more intricate rank-sum logic.
- **Two heaps alone:** Heaps expose extremes but do not support arbitrary expired-value deletion cleanly without lazy-deletion maps and careful duplicate accounting. Three ordered multisets express the needed ranks more directly.
- **Fewer than `m` values:** The partitions may not yet have both boundary groups at full size, but `calculateMKAverage` deliberately returns `-1` and never divides an incomplete middle.
- **Exactly `m` values:** No expiration occurs until the next insertion; the first complete window is already fully partitioned and queryable.
- **More than `m` values:** Exactly one oldest value is removed per insertion, so `q` and all three sorted lists represent only the latest window.
- **Many duplicate boundary values:** Equal occurrences can be stored in different buckets. Removing any one equal copy is equivalent, and the subsequent size repair keeps the middle sum correct.
- **A removed middle value:** The code subtracts it from `s` immediately, then may move a boundary value into the middle and add that replacement.
- **A removed low or high value:** No immediate sum change is needed because boundary values were excluded; if a middle value fills the gap, that move subtracts the value from `s`.
- **Integer rounding:** Positive inputs and a positive denominator make `//` the required mathematical floor.
- **Repeated queries without additions:** They do not mutate any structure, so every such call returns the same value in constant time.
- **Library requirement:** The solution relies on `SortedList` supporting duplicates and ordered index operations; replacing it with a plain Python list would make middle insertions and removals linear.
