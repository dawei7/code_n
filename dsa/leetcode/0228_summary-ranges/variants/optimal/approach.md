## General

**The answer consists of maximal consecutive runs**

Because `nums` is sorted and contains unique values, neighboring array entries
have one of two relationships. If `nums[j + 1] == nums[j] + 1`, they are
consecutive integers and belong in the same range. If not, there is at least
one missing integer between them, so putting both in one inclusive range would
cover a value absent from `nums` and violate the contract.

Therefore the unique smallest exact cover is obtained by splitting the array
at every non-consecutive gap. Each resulting block is a maximal consecutive
run: it cannot extend left or right without encountering the array boundary or
a missing integer.

**Use `i` for the run start and `j` for its expanding end**

At the beginning of each outer-loop iteration, `i` is the first index not yet
represented in the answer. The source sets `j = i`, so the current run starts
as the one-element range containing `nums[i]`.

The inner loop checks two facts before extending:

- `j + 1 < n` guarantees that a next element exists;
- `nums[j + 1] == nums[j] + 1` guarantees that the next value follows with no
  integer gap.

While both hold, incrementing `j` includes that next value. Each new comparison
uses the latest endpoint, so a run can grow across any number of consecutive
values. The loop stops exactly at the last index of the maximal run.

Once `[i, j]` has been formatted and appended, `i = j + 1` moves directly to
the first element after the run. No element is reconsidered as the start of a
second range.

**Format one value differently from a true interval**

The nested helper `f(i, j)` receives endpoint indices, not endpoint values. If
`i == j`, the run contains one array element and must be represented simply as
`str(nums[i])`. If the indices differ, at least two consecutive values belong
to the run, and the helper returns the exact format
`f'{nums[i]}->{nums[j]}'`.

Only the first and last values are needed. Every integer between them is
implicitly covered, and the inner-loop condition has already proved that all
of those integers appear consecutively in `nums`.

For `nums = [0, 1, 2, 4, 5, 7]`, the first run expands from indices 0 through 2
and formats as `"0->2"`. The gap from 2 to 4 ends it. The next run covers
indices 3 and 4 and formats as `"4->5"`. The final index stands alone and
formats as `"7"`.

**Why every input value is covered exactly once**

The outer loop starts at index 0 and, after emitting `[i, j]`, advances to
`j + 1`. Thus the index intervals emitted by successive iterations are
adjacent, non-overlapping, and collectively span indices 0 through `n - 1`.
Every array element is therefore assigned to exactly one output range.

Within one run, each neighboring value differs by exactly one. The inclusive
integer interval from `nums[i]` to `nums[j]` consequently contains precisely
the values stored at array indices `i` through `j`; it introduces no absent
integer. At a boundary between runs, the next value is not the previous value
plus one. Sorted uniqueness then means the difference is greater than one, so
merging the ranges would introduce at least one absent value.

Every emitted range is exact, all elements are covered, and no two adjacent
ranges can legally merge. These facts establish both correctness and
minimality. Output order is sorted automatically because run starts follow the
input's ascending order.

**The helper closes over `nums` safely**

Function `f` reads `nums` from the enclosing method rather than receiving the
list explicitly. It is called only while `i` and `j` are valid indices found by
the loops. It does not retain state between calls or modify the array.

Python integers do not overflow in `nums[j] + 1`. In a fixed-width language,
one may compare the difference carefully near the maximum integer, although a
maximum value can only be last in a valid ascending array.

## Complexity detail

Let $n$ be `len(nums)`. Although the code has nested loops, `j` moves right
through each run and the next outer iteration begins after that run. Every
array element is visited a constant number of times, so total scanning time is
$O(n)$. Formatting output also takes time proportional to the produced text;
with 32-bit input integers, each endpoint has bounded character length, so this
remains $O(n)$.

Variables `i`, `j`, and `n` plus helper call state use $O(1)$ auxiliary space.
The answer can contain up to $n$ strings when every value is isolated, so
including required output gives $O(n)$ space. The manifest's $O(1)$ space is
the conventional bound that excludes returned output.

## Alternatives and edge cases

- **Track endpoint values instead of indices:** Save `start = nums[i]`, advance one pointer to the run end, and format `start` with the final value. It is equivalent; the exact helper uses indices to access both endpoints uniformly.
- **Build ranges incrementally in the answer:** Start a new mutable range at each gap and update its endpoint for consecutive values. This can work but mixes detection with string formatting and may require revising earlier output.
- **Set-based expansion:** Put all values in a set and grow from values lacking predecessors. It loses the useful sorted-input order and uses $O(n)$ extra space for a task solvable by one scan.
- **Empty input:** The outer condition `i < n` is false immediately, so the method returns an empty list.
- **One value:** `j` cannot advance, the helper uses its singleton branch, and one plain number string is returned.
- **All values consecutive:** The inner loop reaches the final index and the method emits exactly one range.
- **No values consecutive:** Every run has `i == j`, producing one singleton string per element.
- **Negative values:** `str` includes the minus sign, and arithmetic consecutiveness still uses a difference of one, so ranges such as `"-3->-1"` are formatted correctly.
- **Crossing zero:** Values `[-1,0,1]` form one consecutive run and become `"-1->1"`.
- **Minimum and maximum 32-bit values:** Python arithmetic and formatting handle both endpoints without overflow.
- **Uniqueness guarantee:** If duplicates were allowed, equality would fail the `+1` test and the same value could appear in separate output ranges, violating exact-cover intent. The algorithm correctly relies on the stated unique-input contract.
- **Input preservation:** Only indices and output strings change; `nums` remains sorted and untouched.
