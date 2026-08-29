## General

The stream keeps growing, but the answer depends only on its `k` largest values. Everything below those top `k` values can be forgotten: a value already outside the top group cannot become the `k`th largest merely because more values are added.

The solution stores exactly this useful group in a min-heap.

**Why a min-heap is the right orientation**

A min-heap exposes its smallest stored value at index zero.

If the heap contains the `k` largest values seen so far, the smallest among those `k` is precisely the `k`th largest value of the complete stream. Thus:

`self.min_q[0]`

is the requested answer.

A max-heap would expose the overall largest value, which is not the boundary of the retained top-`k` group.

**The heap invariant**

After processing `t` stream values, `min_q` contains the largest `min(k, t)` values among them, including duplicate occurrences, and its root is the smallest retained value.

When at least `k` values have been processed, its size is exactly `k` and the root is the current `k`th largest.

This invariant covers both constructor values and later calls because the constructor deliberately feeds each initial value through the same `add` operation.

**Processing one value**

`heappush(self.min_q, val)` first inserts the new value while restoring heap order.

If the heap now has more than `k` entries, `heappop` removes its smallest value.

There are two conceptual cases:

- If `val` is too small to belong to the top `k`, it becomes the heap minimum and is immediately removed.
- If `val` belongs in the top `k`, then the previously smallest retained value is removed instead.

Either way, the heap ends with exactly the largest `k` values among everything processed, once the stream contains at least `k` elements.

The code always pushes before deciding what to discard. An optimized variant could skip a small value when a full heap already exists, but push-then-pop is simpler and preserves the same invariant.

**Why discarded values never matter later**

Suppose value `x` is removed because at least `k` processed values are greater than or equal to it. Future operations only add more values; they never remove historical stream values. Those `k` witnesses remain in the stream forever.

Therefore, `x` can never rise into the top `k` later. Forgetting it is safe.

**Constructor behavior**

The constructor stores `k`, initializes an empty heap, and calls `self.add(x)` for every `x` in `nums`.

This reuses one proven update rule rather than having separate heap-building logic. During early calls when fewer than `k` values have been seen, no pop occurs, so all values are retained.

The problem guarantees `k <= len(nums) + 1`. If the initial stream has fewer than `k` values, the next required `add` call brings the total to at least `k` before its returned root is interpreted as the `k`th largest.

Return values produced by `add` during construction are ignored.

**Duplicate values**

The stream is a multiset, not a set. Equal values occupy separate heap entries.

For example, the fourth largest value of `[7, 7, 7, 8]` is `7`. Retaining duplicates separately gives the correct rank. Deduplicating would change the problem.

**A trace**

Let `k = 3` and initial values be `[4, 5, 8, 2]`.

- Add `4`: heap contains `[4]`.
- Add `5`: heap contains two values.
- Add `8`: heap contains the top three `[4, 5, 8]`, with root `4`.
- Add `2`: temporary size becomes four; `2` is popped, leaving the same top three.

Now add `3`. It is pushed and then popped because it is below `4`, so the answer remains `4`.

Add `5`. After insertion, the smallest retained value `4` is popped. The heap now represents `[5, 5, 8]`, and its root `5` is the new third largest.

**Why the invariant proves correctness**

Assume the heap contains the largest `min(k,t)` of the first `t` values. After adding the next value, the temporary heap contains those retained values plus the newcomer.

Any previously discarded value is no larger than the retained boundary and cannot beat a retained candidate. If there are more than `k` temporary entries, removing the smallest leaves exactly the largest `k` among all `t+1` values. If there are at most `k`, retaining everything is correct.

By induction, the invariant always holds. Once the stream contains `k` values, the heap's minimum is exactly rank `k` from the top, so every returned value is correct.

## Complexity detail

Let `m` be the number of initial values and `s` the number of later `add` calls.

The heap size never exceeds `k+1` temporarily. Each push and possible pop takes `O(\log k)` time. Constructor initialization through `m` calls takes `O(m\log k)`, and each public `add` takes `O(\log k)`.

Across initialization and all additions, time is

$$
O((m+s)\log k).
$$

The heap retains at most `k` integers, so auxiliary persistent space is

$$
O(k).
$$

No complete history of the stream is stored.

## Alternatives and edge cases

- **Sorted full stream:** Binary-search an insertion position and insert into a list. Rank lookup is easy, but insertion shifts elements and storage grows with every value.

- **Balanced ordered multiset:** It can support updates and rank queries but is more complex and not built into standard Python.

- **Skip small values when full:** If `val <= min_q[0]` and the heap has `k` entries, return the root without pushing. This improves constants but is not necessary for the bound.

- **`k = 1`:** The heap stores only the maximum value seen, and its minimum is also that maximum.

- **Initial list empty:** The constraint then forces `k = 1`. The first public addition creates a nonempty heap before returning its root.

- **Fewer than `k` constructor values:** They are all retained. The next valid addition makes the `k`th rank exist.

- **Negative values:** Heap ordering handles them normally.

- **Duplicates:** Each occurrence counts toward rank and must remain a separate entry.

- **Very small incoming value:** It is pushed and immediately popped, leaving the answer unchanged.

- **Very large incoming value:** It remains while the old heap minimum is removed, potentially raising the answer.

- **Heap array is not globally sorted:** Only the min-heap property and root are required; internal order does not affect correctness.
