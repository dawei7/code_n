## General

Ordinary binary search begins with known array boundaries. Here the array length is hidden, and values can be accessed only through `reader.get(index)`. An out-of-range request returns the sentinel `2^31 - 1`, which is larger than every legal array value and target.

The solution has two phases:

1. exponentially expand a right boundary until its value is at least the target;
2. perform lower-bound binary search inside the discovered interval.

**Why exponential expansion is needed**

Starting with `r = 1`, the loop asks whether `reader.get(r) < target`.

If it is smaller, strict increasing order proves that every index up through `r` is also too small. The target, if present, must lie farther right. The statement `r <<= 1` doubles the index, producing `2, 4, 8, 16`, and so on.

Doubling rather than advancing one position at a time is what preserves logarithmic complexity when the target lies far into the hidden array.

**Why the expansion always stops**

There are two ways to stop.

First, an in-bounds value at `r` may be at least the target. The target cannot lie to the right of the first such lower-bound candidate without also passing this position in sorted order.

Second, `r` may move outside the secret array. The reader then returns `2^31 - 1`. Because that sentinel is greater than the legal target range, the loop condition becomes false.

Thus even when the target is greater than every real array value, the artificial sentinel supplies a safe upper boundary.

**Recovering the left boundary**

After expansion stops, the code sets `l = r >> 1`, which halves `r`.

If expansion ran at least once, this is the previous tested power of two. That previous position had a value smaller than the target; it is a safe left boundary for searching the next interval.

If expansion never ran, `r` remains one and `l` becomes zero. This includes targets at index zero, at index one, smaller than the first value, or between the first two values.

The desired lower-bound position is therefore within the inclusive interval `[l, r]`.

**The lower-bound invariant**

The second loop searches for the smallest index in `[l, r]` whose reader value is at least `target`.

Its invariant is:

> The lower-bound index exists within the current inclusive interval.

Existence is guaranteed because `reader.get(r) >= target` when expansion ends.

At each iteration, `mid = (l + r) >> 1`.

If `reader.get(mid) >= target`, `mid` itself could be the first adequate position, so it must be retained. Every index to its right can be discarded by setting `r = mid`.

If `reader.get(mid) < target`, sorted order proves that `mid` and every earlier index are too small. The update `l = mid + 1` discards them.

Both updates strictly shorten the interval while preserving the lower-bound index.

**Why the loop uses `l < r`**

The interval is never allowed to become empty. When `l == r`, exactly one candidate remains, and the invariant says it is the smallest position whose reader value is at least the target.

Using `r = mid` in the first branch is safe because floor midpoint is strictly less than `r` whenever `l < r`. The interval always makes progress.

**Final equality check**

Lower-bound search finds the first value not smaller than the target. That value could be:

- exactly the target;
- a larger in-bounds value, meaning the target lies in a sorted gap;
- the out-of-bounds sentinel, meaning the target exceeds all real values.

Therefore, the method returns `l` only if `reader.get(l) == target`; otherwise it returns `-1`.

The array's elements are unique, so a successful index is the only possible answer. The lower-bound method would still return the first occurrence if duplicates existed.

**A successful trace**

For hidden array `[-1, 0, 3, 5, 9, 12]` and target `9`:

- `r = 1` reads `0 < 9`, so double to `2`.
- Index `2` reads `3 < 9`, so double to `4`.
- Index `4` reads `9`, so expansion stops and `l = 2`.
- Lower-bound search within `[2, 4]` narrows to index `4`.
- The final equality check succeeds and returns `4`.

**An absent target**

For target `2`, expansion stops when a boundary reads at least two. Lower-bound search returns the index of `3`, the first greater value. Since `3 != 2`, the result is `-1`.

**Why the complete algorithm is correct**

Expansion ends with a right boundary whose value is at least the target and a left boundary that does not exclude the first adequate index. Binary search preserves and isolates the smallest index with value at least the target.

If its value equals the target, sorted order confirms the correct location. If it is larger, no earlier value can equal the target because it is the lower bound, and no later value can equal it because later values are even larger. The sentinel case follows the same reasoning.

## Complexity detail

Let `p` be the target's index when present, or the insertion position where it would occur. Expansion takes `O(\log(p+1))` reader calls because `r` doubles.

The resulting interval width is proportional to the reached power of two, and binary search takes another `O(\log(p+1))` calls. Overall time is

$$
O(\log(p+1)),
$$

which is `O(\log n)` under the hidden array's length `n`.

The method stores only `l`, `r`, and `mid`. Auxiliary space is

$$
O(1).
$$

Reader calls do not materialize the hidden array.

## Alternatives and edge cases

- **Linear boundary discovery:** Advancing `r` one step at a time can take `O(n)` calls and violates the requested logarithmic runtime.

- **Exact-match binary search after expansion:** A standard inclusive binary search also works. The lower-bound form cleanly handles real values and the sentinel with one final equality check.

- **Target at index zero:** If expansion does not run, `l` becomes zero and binary search retains it when appropriate.

- **One-element hidden array:** Out-of-range reads at index one provide the upper sentinel boundary; the final check returns zero or `-1`.

- **Target smaller than the first value:** Lower bound becomes index zero, whose value fails equality, so `-1` is returned.

- **Target larger than every value:** Doubling eventually goes out of bounds; the sentinel stops expansion and the final comparison fails.

- **Target equals the sentinel:** The source's legal target range excludes this. Without that guarantee, an out-of-bound response could be mistaken for a real match.

- **Strictly increasing guarantee:** It justifies discarding entire halves and makes a successful index unique.

- **Bit shifts:** `r <<= 1` doubles and `r >> 1` halves a positive power of two. Ordinary multiplication and integer division would be equivalent.

- **Repeated reader call at the end:** The final call is necessary because lower-bound search proves only “at least target,” not equality.
