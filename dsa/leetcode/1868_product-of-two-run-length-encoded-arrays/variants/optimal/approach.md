## General

**Intersect runs instead of expanding them.** At any expanded position, the product is determined by the currently active run from `encoded1` and the currently active run from `encoded2`. If those runs have remaining frequencies `f1` and `f2`, their values overlap for exactly `min(f1, f2)` positions. That entire block has one product value and can be emitted at once.

The solution iterates each first encoding run `[vi, fi]`. `fi` is unpacked into a local integer, so reducing it does not modify `encoded1`. Pointer `j` identifies the current second-array run.

**Consume the current overlap.** While local `fi` is positive:

- `f = min(fi, encoded2[j][1])` is the number of expanded positions shared by the two current runs.
- `v = vi * encoded2[j][0]` is the product at every one of those positions.

The method then subtracts `f` from both remaining frequencies. At least one becomes zero because `f` is their minimum, so every iteration finishes at least one run and makes progress.

**Merge adjacent equal products immediately.** Minimal run-length encoding forbids consecutive output runs with the same value. If `ans` already ends with product `v`, the new block belongs to that same run and the code adds `f` to its frequency. Otherwise, it appends `[v, f]`.

This merge is needed even when input run boundaries differ. For example, one source pair may produce six and the next pair may also produce six through different factors. Expanded output still contains one uninterrupted run of sixes, so preserving the intermediate boundary would not be minimal.

**Advance the second encoding only when exhausted.** The exact source decrements `encoded2[j][1]` in place. When that frequency reaches zero, `j += 1` moves to the next second run. If it remains positive, the next first run continues overlapping the same second value.

Because expanded lengths are guaranteed equal, the first encoding finishes exactly when all required positions from the second encoding have been consumed. No length mismatch branch is needed.

**Trace a crossing boundary.** Suppose the current first run has frequency five and the current second run has frequency two. The overlap block consumes two positions, exhausts the second run, and leaves local first frequency three. Pointer `j` advances, and the while loop multiplies the same first value with the next second value for the remaining three positions.

If instead the first run is shorter, local `fi` becomes zero and the outer loop advances while the second run retains its reduced frequency.

**Trace the fully merged sample.** First runs one-times-three and two-times-three align with second runs six-times-three and three-times-three. Both overlap products are six. The first appends `[6, 3]`; the second sees the same final product and extends it to `[6, 6]`.

**Two-pointer invariant.** Before each overlap, all earlier expanded positions have been multiplied and represented minimally in `ans`. `vi, fi` and `encoded2[j]` describe the next unprocessed blocks in the two arrays. Consuming their minimum remaining length computes exactly the next block of elementwise products. Immediate equality merging preserves minimal encoding. By induction, the returned list encodes the complete product and contains no adjacent equal runs.

**Exact mutation behavior.** `encoded2[j][1] -= f` changes the caller’s inner lists. By completion, consumed second-run frequencies are zero. `encoded1` is not mutated because `fi` is a local integer copied during tuple unpacking. This asymmetry is important if inputs are reused after the call.

## Complexity detail

Let `M` and `N` be the numbers of runs in the two encodings. Every overlap iteration exhausts at least one current run. Thus there are at most `M + N - 1` overlaps, giving `O(M + N)` time.

The output has at most `O(M + N)` runs and is required return storage. Beyond it, the method keeps a pointer and scalar values, using `O(1)` auxiliary space. Including output, space is `O(M + N)`.

## Alternatives and edge cases

- **Expand both arrays:** It is conceptually simple but can require memory and time proportional to enormous expanded length.
- **Copy second frequencies first:** This preserves `encoded2` while retaining the same algorithm and asymptotic bounds.
- **One run versus many:** The while loop naturally intersects the single long run with each shorter opposing run.
- **Both runs end together:** Both remaining frequencies reach zero; the outer loop and `j` advance consistently.
- **Equal adjacent products from different factors:** Immediate merging is required for minimum-length encoding.
- **Single expanded position:** One overlap emits one run with frequency one.
- **Unequal run counts:** Complexity depends on total run boundaries, not on counts being equal.
- **Equal expanded lengths:** This guarantee prevents `j` from running past the second encoding before the first finishes.
- **Positive frequencies:** Every overlap length is positive, ensuring loop progress.
- **Large products:** Values reach at most the product of source bounds and fit safely in Python integers.
- **Input mutation:** Every consumed `encoded2` frequency is reduced in place, usually to zero.
- **First input preservation:** Unpacked `fi` changes locally and leaves `encoded1` intact.
