## General

**Use sorted order to recognize a new distinct value immediately**

Because `nums` is sorted in non-decreasing order, all copies of the same value form one contiguous run. While scanning from left to right, a value is new exactly when it differs from the most recently retained distinct value. No set is needed: the compacted prefix itself remembers that last value.

The task does not require shrinking the Python list. It requires returning a length `k` and placing the distinct values in `nums[:k]`. Everything at index `k` or later is outside the judged answer and may contain stale data.

**Give `k` two related meanings**

The source initializes `k = 0`. Throughout the loop:

- `k` is the number of unique values already written; and
- `k` is the index where the next new value must be written.

Those meanings agree because a prefix with `k` elements occupies indices `0` through `k - 1`, making index `k` the next free position.

The central invariant is:

> Before processing the next scanned value `x`, `nums[:k]` contains every distinct value from the already scanned input prefix exactly once, in original sorted order.

The invariant holds initially because both the scanned prefix and `nums[:0]` are empty.

**Handle the first value without an invalid index**

The acceptance condition is

```python
if k == 0 or x != nums[k - 1]:
```

When no value has been retained, `k - 1` would be `-1`, which in Python refers to the array's last element rather than representing “no previous value.” The explicit `k == 0` condition ensures that the first scanned value is always kept for the correct reason.

Python short-circuits `or`. When `k == 0` is true, it does not evaluate `x != nums[k - 1]`, so the algorithm never consults a supposed last retained value before one exists. This also lets the exact source return zero safely for an empty list, even though the stated constraints make the list non-empty.

**Write only the first occurrence of each sorted run**

If `x` differs from `nums[k - 1]`, it is not part of the run represented by the last retained value. Sortedness guarantees it cannot equal any earlier retained value either: returning to an older smaller value would violate non-decreasing order. Therefore `x` is a genuinely new distinct value.

The code writes it and advances the boundary:

```python
nums[k] = x
k += 1
```

If `x` equals the last retained value, the source does nothing. That copy belongs to the same contiguous run, and one representative is already in the answer prefix.

**Why reading and writing the same list is safe**

`for x in nums` reads elements by increasing source position while the body writes into earlier compacted positions. At a source index `i`, the number of retained values satisfies `k <= i + 1`; before a new write, its destination satisfies `k <= i`. Thus the algorithm never overwrites an unvisited future element.

The loop variable `x` already holds the current value before `nums[k] = x` executes. Writing the same position or an earlier one cannot change `x`, and it cannot disturb values that the iterator has yet to read. This leftward-only compaction is what makes the in-place scan reliable.

**Trace `[0,0,1,1,1,2,2,3,3,4]`**

The first `0` is written at index zero and makes `k = 1`. The next `0` equals `nums[0]` and is skipped. The first `1` differs from the last retained `0`, so it is written at index one and makes `k = 2`; later `1` values are skipped. The same action writes `2`, `3`, and `4` at indices two, three, and four.

The method returns `5`, and the judged prefix is `[0,1,2,3,4]`. Positions five onward still contain whatever values resulted from the original list and the compaction. They do not need to be cleared or replaced with literal underscores; underscores in the example only mean “ignored.”

**Why the final prefix is exactly correct**

If a scanned value equals the last retained value, sortedness proves it is a duplicate within the same run, so skipping it loses no distinct value. If it differs, sortedness proves it begins a new run, so retaining it adds exactly one necessary representative. In either case, the invariant remains true. After every input value has been scanned, `nums[:k]` contains one representative of every run, which is exactly one copy of every distinct value, in sorted relative order. Returning `k` gives its length.

## Complexity detail

Let $n$ be `len(nums)` and $k$ the final number of distinct values.

- **Time complexity: $O(n)$.** The loop reads each of the $n$ values once. Each iteration performs constant-time comparisons and at most one assignment.
- **Auxiliary space: $O(1)$.** Only `k` and the loop value `x` are stored independently of input size. The required prefix is written inside the supplied array, and no set or replacement list is allocated.

At least $\Omega(n)$ reads are necessary in the worst case because the final element could be either a duplicate or a new distinct value, so the linear scan is asymptotically optimal.

## Alternatives and edge cases

- **Read index plus write index:** Iterate explicit indices from one onward and compare `nums[i]` with `nums[i - 1]`. It has the same bounds and is the form used in many editorials.
- **Set followed by sorting:** It uses $O(k)$ extra space, may require sorting, and ignores the stronger in-place opportunity provided by already sorted input.
- **Delete duplicates from the list:** Repeated physical deletion shifts later elements and can make the method $O(n^2)$ in an array-backed list.
- **Empty list outside the stated constraints:** The exact source returns `0` because the loop never runs.
- **One value:** It is written to index zero and the method returns one.
- **All values equal:** Only the first is kept; `k` remains one.
- **All values distinct:** Every value is written, often back to its current position, and `k = n`.
- **Negative values:** No sentinel is used, so the full permitted numeric range works normally.
- **Tail contents:** Values at and after index `k` are unspecified and must not be interpreted as part of the answer.
- **Sortedness is essential:** On an unsorted sequence such as `[1,2,1]`, the last `1` would be retained again; the algorithm removes duplicate runs, relying on the contract to make each value one run.
- **Relative order:** Values are scanned and written left to right, so the retained sequence keeps its original order automatically.
