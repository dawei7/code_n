## General

**Reduce an all-pairs condition to two extreme values**

A subarray is continuous when the absolute difference between every pair of its elements is at most two. Checking all pairs would be unnecessarily expensive. In any collection, the largest possible difference is

$$
\max(\text{window}) - \min(\text{window}).
$$

If this extreme difference is at most two, every other pair lies between those extremes and is also within two. If it is greater than two, the minimum and maximum themselves form a violating pair. The entire validity condition is therefore equivalent to maintaining `maximum - minimum <= 2`.

The exact solution uses a sliding window and a `SortedList`. The sorted multiset contains all values in the current index interval. Its first item `sl[0]` is the minimum, its last item `sl[-1]` is the maximum, and duplicate values are stored with their full multiplicity.

**Grow on the right, repair on the left**

Variable `i` is the left boundary. The `for x in nums` loop supplies each successive right-end value. The algorithm first adds `x` to the sorted multiset. If the new maximum and minimum differ by more than two, it repeatedly removes `nums[i]` and increments `i` until the condition becomes valid again.

The left pointer never moves backward. Once a window ending at the current position is invalid because of its extremes, keeping its old left endpoint cannot become valid merely by adding more elements. Removing the oldest values is the only available way to repair that current ending.

`SortedList.remove(nums[i])` removes one occurrence, not every equal occurrence. This matters because the window may contain duplicates. The data structure must mirror exactly how many positions remain in the interval, not merely which distinct values occur.

**The window is the longest valid suffix ending here**

After the shrinking loop stops, the multiset represents precisely `nums[i:right + 1]` and is valid. Moreover, `i` is the smallest possible left boundary for a valid subarray ending at this right endpoint.

Why? If the newly expanded window was already valid, `i` did not change and it remains the earliest boundary inherited from the previous step. If it was invalid, the loop removed elements from the left one by one and stopped at the first point where the extreme difference became at most two. The immediately earlier boundary was still invalid at the moment it was removed. Thus the surviving interval is the longest valid suffix ending at the current element.

**Count many subarrays at once**

Suppose the valid window spans indices `i` through `right` and has length `right - i + 1`. Every subarray ending at `right` and starting at any index from `i` through `right` is also valid. Removing a prefix cannot introduce a new minimum or maximum outside the old range, so the extreme difference cannot increase.

There are exactly `right - i + 1` such start choices. The code adds `len(sl)`, which equals that same window length because the multiset stores one entry for every position in the current interval.

Subarrays that start before `i` are invalid by the minimal-left-boundary argument. Therefore this addition counts all and only continuous subarrays ending at the current position. Every non-empty subarray has exactly one right endpoint, so summing these contributions counts each valid subarray once.

**A walkthrough**

For `nums = [5, 4, 2, 4]`:

- Add 5. The window `[5]` is valid and contributes one.
- Add 4. Its extremes differ by one, so `[5, 4]` contributes two suffixes.
- Add 2. The difference between 5 and 2 is three. Remove the leftmost 5; `[4, 2]` is valid and contributes two.
- Add 4. The window `[4, 2, 4]` still has extreme difference two and contributes three.

The total is `1 + 2 + 2 + 3 = 8`.

Notice that duplicate 4 values remain distinct multiset entries. That makes `len(sl)` three in the final step, correctly matching three array positions.

**Why the algorithm is correct**

The sorted multiset accurately represents the active interval because each right value is inserted once and every leftward move removes exactly that departing occurrence. After shrinking, the extreme-value equivalence proves the interval is continuous. Minimality of `i` proves no earlier start is valid for this endpoint, while closure under removing a prefix proves every later start is valid. Hence `len(sl)` is exactly the number of valid subarrays ending here. Summation over all endpoints yields the requested total.

**The exact code differs from its manifest**

The Optimal manifest says the implementation uses monotonic deques, runs in `O(n)`, and uses `O(1)` space. The exact solution file does not use deques; it imports and maintains a `SortedList` containing every active-window element. Its real bounds must account for ordered insertion, ordered removal, and potentially a window of length `n`. The explanation follows the code, not the inaccurate summary.

## Complexity detail

Let `n` be `nums.length`. Each element is inserted into `SortedList` once. Because `i` only increases, each element is also removed at most once. Under the standard ordered-multiset cost model, both insertion and removal take `O(log n)` time, while reading the first and last values and getting the length are constant time. The total time is `O(n log n)`.

The inner `while` does not make the algorithm quadratic: its iterations across the entire run are at most `n` because every iteration advances `i` permanently. The logarithmic data-structure operations, rather than repeated pointer movement, determine the bound.

The multiset can hold all `n` values when the entire array's range is at most two. Its auxiliary space is therefore `O(n)`. This directly contradicts the manifest's `O(1)` claim for the exact implementation. The scalar variables use constant space, and the input is not modified.

## Alternatives and edge cases

- **Two monotonic deques:** One decreasing deque can track maxima and one increasing deque can track minima in amortized constant time per element, giving `O(n)` time and `O(n)` worst-case space. This is the strategy described by the manifest, but it is not the exact solution file.
- **Frequency map over the three possible values:** Once a valid window is known, it has at most three distinct integer values, but discovering and repairing the range still requires careful minimum and maximum maintenance. A sorted map can exploit the small distinct range.
- **Recompute minimum and maximum for every window:** This avoids an ordered structure but can rescan long windows repeatedly and degrade to quadratic time.
- **All values equal:** No shrinking occurs. The contributions are `1, 2, ..., n`, correctly counting every subarray.
- **Difference exactly two:** The window remains valid because the condition is inclusive.
- **Difference greater than two after insertion:** The loop may remove several old values; it stops only when both extremes fit the bound.
- **Duplicate values:** `SortedList` preserves multiplicity, and `remove` deletes only one departing occurrence.
- **One-element input:** The single value forms one continuous subarray, so the answer becomes one.
- **Very large element values:** Only comparisons and subtraction matter; the algorithm never allocates an array indexed by value.
- **Large answer:** The count can be `n(n + 1) / 2`. Python integers grow as needed, so no fixed-width overflow occurs.
- **Input order:** Sorting the entire input would destroy contiguity. Only the active window's value multiset is sorted; original positions remain represented by the moving boundaries.
