## General

**Process the smallest remaining value first**

The changed array contains only nonnegative values. After sorting, the smallest unused value `x` cannot be the double of a smaller positive unused original value, because no smaller unused value exists. It must serve as an original value and be paired with `2x`.

This removes the ambiguity between treating a number as an original or as someone else's double.

The source sorts `changed` in place and builds `Counter(changed)` to track how many unused occurrences of each value remain.

**Skip occurrences already consumed as doubles**

The loop still iterates through every entry of the sorted list, including entries whose counter was reduced earlier when they served as a double.

If `cnt[x] == 0`, that occurrence is already fully accounted for, so the loop continues. Otherwise, one occurrence of `x` is selected as an original and its count is decremented.

**Require and consume its double**

The double is computed as `x << 1`, a left shift by one bit that equals `2 * x` for nonnegative integers.

If `cnt[2x] <= 0` after consuming the original occurrence, no unused double exists. The array cannot be partitioned into original-double pairs, so the method returns an empty list.

If it exists, the source decrements that count and appends `x` to `ans`.

The order of decrementing matters for zero. When `x=0`, its double is also zero. Consuming the original first means the second count check correctly requires another zero. An odd number of zeroes eventually fails.

**Trace a valid array**

For sorted `[1,2,3,4,6,8]`, one pairs with two, three with six, and four with eight. When the loop later reaches two, six, or eight, their counts are already zero and they are skipped.

The result is `[1,3,4]`. Doubling and appending those values reproduces the changed multiset.

**Why the greedy choice is safe**

Let `x` be the smallest unused value. If $x>0$, it cannot be the double of an unused original $x/2$, since that smaller value would have appeared earlier and, if present, would already have consumed this occurrence as its double. Therefore any valid remaining pairing must use `x` as an original with `2x`.

For zero, both members are zero, and pairing them two at a time is forced.

Thus each greedy pair is necessary in every valid decomposition. If its double is missing, no alternative pairing can rescue the multiset.

**Counter invariant during the scan**

Before each sorted occurrence is examined, `cnt` describes exactly the multiset not yet assigned to a completed pair. A zero count means the loop occurrence belongs to an earlier pair. A positive count means it is the smallest still-unassigned value, so consuming it and one double preserves the invariant for the next iteration.

**Why successful completion is sufficient**

Every appended `x` consumes one distinct occurrence of `x` and one distinct occurrence of `2x`. Counters prevent reuse.

If the loop completes, all selected pairs are legal and every original input occurrence has either initiated a pair or been skipped because it was consumed by one. The collected originals therefore generate exactly the changed multiset.

An odd-length array is not checked explicitly, but it cannot be fully paired. The process eventually finds some occurrence without a required partner and returns empty.

**Input mutation and output order**

`changed.sort()` permanently rearranges the caller's list. The answer is produced in nondecreasing order because originals are appended during the sorted scan, although the contract permits any order.

## Complexity detail

Let $N$ be the changed-array length. Sorting takes $O(N\log N)$ time. Counter construction and the greedy scan take expected $O(N)$ time, so total is $O(N\log N)$.

The counter and answer can each contain $O(N)$ entries, and Python sorting may use $O(N)$ temporary memory. Auxiliary space is $O(N)$, including the produced answer as the manifest does.

## Alternatives and edge cases

- **Counting-array scan:** Values are bounded by $10^5$, so frequencies can be processed from zero upward in $O(N+V)$ time and $O(V)$ space.
- **Unsorted counter iteration:** Unsafe because deciding whether a value is original or a double requires magnitude order.
- **Backtracking pair choices:** Exponential ambiguity is unnecessary once the smallest remaining value is chosen.
- **Odd changed length:** Cannot be split into pairs and eventually returns empty.
- **Zero values:** Must occur an even number of times; consuming the original before checking its identical double enforces this.
- **Missing double:** Causes immediate failure because the smallest remaining value has no alternative role.
- **Duplicate originals:** Each occurrence consumes a distinct doubled occurrence through counter multiplicity.
- **Large values:** Their doubles may exceed the input value bound but absent counter entries safely read as zero.
- **Already valid sorted input:** Works identically; sorting preserves its order.
- **Answer order:** The exact method returns sorted originals, which is allowed.
- **Bit shift:** `x << 1` is exactly twice `x` for these nonnegative integers.
- **Input side effect:** The exact source sorts `changed` in place.
- **Environment import:** The solution assumes `Counter` is available.
