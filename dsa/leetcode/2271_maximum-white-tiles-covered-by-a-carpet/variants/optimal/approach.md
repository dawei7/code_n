## General

**An optimal carpet can align with a white boundary**

If a carpet placement covers at least one white tile but neither end is aligned
with a useful interval boundary, slide it without losing covered white
positions until one end reaches such a boundary. It is therefore sufficient
to consider carpets whose right endpoint equals the right endpoint of some
white interval.

Sort the non-overlapping intervals by their left endpoints. Sweep a right
pointer through them and add each complete interval length to a running
coverage total. For interval `[start, end]`, a carpet ending at `end` begins at

`carpet_start = end - carpetLen + 1`.

Advance a left pointer while its interval ends before `carpet_start`,
subtracting each interval that has left the window. At most one surviving
leftmost interval is only partially covered. Its uncovered prefix has length
`max(0, carpet_start - tiles[left][0])`; subtract that prefix from the running
total to obtain the exact white coverage of the current carpet.

**Why the window remains exact**

After expired intervals are removed, every interval strictly between the two
pointers lies wholly inside the carpet. The right interval ends at the
carpet's right endpoint and is also fully included. Because intervals are
ordered and disjoint, only the leftmost remaining interval can cross the
carpet's left boundary, and subtracting its uncovered prefix corrects the
total exactly.

The sweep evaluates a boundary-aligned representative of every potentially
optimal placement. Taking the largest corrected total therefore returns the
global optimum. If the result reaches `carpetLen`, no larger answer is
possible because the carpet contains only that many integer positions.

## Complexity detail

Let $n=\lvert\texttt{tiles}\rvert$. Sorting takes $O(n\log n)$ time. Each
interval enters the window once and leaves it at most once, so the sweep is
$O(n)$. The total time is $O(n\log n)$. Python's in-place sort may use $O(n)$
auxiliary storage.

## Alternatives and edge cases

- **Test every interval against every carpet start:** Aligning a carpet at each interval and rescanning all intervals is correct but takes $O(n^2)$ time.
- **Prefix sums plus binary search:** Sorted interval lengths and endpoint searches also give $O(n\log n)$ time, but the two-pointer window avoids a search for every start.
- **One long interval:** The answer is the smaller of its length and `carpetLen`.
- **Carpet longer than the white span:** It can cover every white tile, including gaps at no benefit or penalty.
- **Partial endpoint interval:** Count only the inclusive overlap with the carpet.
- **Large gaps:** They consume carpet length but contribute zero coverage.
- **Unsorted input:** Sort before applying the monotone window.
- **Inclusive coordinates:** An interval `[left, right]` contains `right - left + 1` tiles.
- **Full carpet:** Once coverage equals `carpetLen`, return immediately because every carpet position is white.
