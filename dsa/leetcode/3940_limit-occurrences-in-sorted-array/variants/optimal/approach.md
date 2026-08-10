## General

Because `nums` is sorted, every occurrence of one value appears in one contiguous run. The source can decide whether to retain an element by tracking its one-based occurrence number within the current run:

- keep occurrences 1 through `k`;
- skip occurrence `k + 1` and every later occurrence of that same value.

At the same time, a write pointer compacts retained values into the front of `nums`. The method finally returns a slice containing only that compacted prefix.

**The first element is always retained**

The constraints guarantee that `nums` is nonempty and `k >= 1`. Therefore the first occurrence of the first value must be kept.

The chained assignment

`cnt = l = 1`

encodes two initial facts:

- `cnt = 1` because `nums[0]` is the first occurrence in its run;
- `l = 1` because index zero is already the compacted output and index one is the next destination for a retained value.

The scan pointer `r` begins at one, so every later input position is considered exactly once.

**Use sorted order to count a run**

At position `r`, comparing `nums[r]` with `nums[r - 1]` tells whether the current value continues the same run.

If they differ, sorted order guarantees that a new distinct value has begun and the old value will never appear again. The current value is its first occurrence, so `cnt` resets to one.

If they are equal, this is the next occurrence of the same value, so `cnt` increases by one.

No dictionary is required. In an unsorted array, equal values could reappear after other values and would need global frequency tracking. Here contiguity makes one scalar run count sufficient.

**Compact only retained occurrences**

When `cnt <= k`, the current occurrence belongs in the result. The source writes it to the next compacted position:

`nums[l] = nums[r]`,

then increments `l`.

When `cnt > k`, it does nothing. The write pointer stays still, so the next retained value will overwrite the earliest output position that has not yet been filled.

For example, with `nums = [1, 1, 1, 2, 2, 3]` and `k = 2`:

- the first two ones occupy output indices zero and one;
- the third one is skipped, leaving `l = 2`;
- the first two twos are written to indices two and three;
- the three is written to index four.

The meaningful prefix becomes `[1, 1, 2, 2, 3]`.

**Why in-place writes do not corrupt the scan**

At every iteration, `l <= r` because the output cannot contain more values than the input positions processed. The assignment therefore writes at the current position or somewhere earlier; it never overwrites a future unread element.

The run comparison uses `nums[r - 1]`. Could compaction have changed that value? If an earlier write reached index `r - 1`, it happened while processing that same original position and wrote `nums[r - 1]` to itself. If skipped values made `l` smaller, writes land strictly before `r - 1`. Thus the adjacent input values needed for run counting remain intact.

This is an important detail because the algorithm reads and writes the same list without keeping an untouched copy.

**Why the compacted prefix is exact**

Maintain the following meaning before processing position `r`:

- `nums[:l]` contains exactly the retained occurrences from original positions before `r`, in their original order;
- `cnt` records the occurrence number of the preceding original element within its run.

The comparison updates `cnt` to the correct occurrence number for `nums[r]`. If that number is at most `k`, appending it at `l` extends the compacted prefix with exactly the next required value. If it exceeds `k`, skipping it is required and leaves the prefix correct.

By induction, after the last position, `nums[:l]` contains each run's first `min(frequency, k)` elements and nothing else. Since these are taken in scan order, relative order is preserved.

The return expression `nums[:l]` creates the result list from that prefix. The original list object still has its original length and may contain stale values after index `l - 1`; callers must use the returned list rather than interpret the old suffix.

**The source differs from the manifest's summarized test**

The manifest summary mentions retaining a value when it differs from the element kept `k` positions earlier. That is another standard in-place solution, but it is not the condition in this source. The checked implementation explicitly counts consecutive occurrences using `cnt`. Both methods rely on sorted order and have the same asymptotic bounds, but this explanation follows the actual counter-based code.

## Complexity detail

Let $N$ be the input length. The loop examines each position from one through $N-1$ once, doing constant work. The time complexity is $O(N)$.

The compaction itself uses only `n`, `cnt`, `l`, and `r`, so its auxiliary working space is $O(1)$. Python's `nums[:l]` allocates the returned list and copies $l$ references, requiring $O(l)$ output space and time. The contract explicitly excludes return/resizing storage from the follow-up's auxiliary-space accounting, which is why the manifest reports $O(1)$ space.

If output allocation is counted, peak additional space is $O(N)$ in the worst case. The loop remains an in-place compaction of the supplied list's prefix.

## Alternatives and edge cases

- **Compare with the compacted value `k` positions back:** Retain `value` when fewer than `k` outputs exist or `value != nums[l - k]`. This is the manifest's summarized method and also uses $O(1)$ working space, but it is not the source's run counter.
- **Use a frequency dictionary:** It works even for unsorted input but spends $O(D)$ space for $D$ distinct values. Sorted contiguity makes it unnecessary.
- **Build a separate output with append:** This is simple and linear but uses output-sized storage beyond the in-place prefix. The source writes retained values directly into `nums`.
- **Delete excess entries while scanning:** Repeated deletion from the middle of a Python list shifts later values and can produce quadratic time.
- **`k = 1`:** `cnt <= k` keeps only the first element of every run, producing one copy of each distinct value.
- **`k` at least every run frequency:** No element is skipped. Every write is effectively to its own position and the returned slice equals the input values.
- **All values equal:** The first `k` occurrences are retained and every later occurrence is skipped.
- **All values distinct:** `cnt` resets to one at every position, so all values are retained.
- **A run begins after skipped values:** `l` may be behind `r`; the first new value is written into the earliest gap, maintaining order.
- **Nonempty input assumption:** Initializing `cnt` and `l` to one relies on index zero being present. The stated constraints guarantee this.
- **Positive `k` assumption:** The first element is retained unconditionally, which is correct only because `k >= 1`.
- **Returned slice versus original object:** The returned list has the requested length. The supplied `nums` is compacted in its prefix but is not resized by the source.
