## General
**Maximize the values that can remain unchanged.** Any continuous result is a
set of $N$ consecutive integers. If its minimum is $x$, an existing distinct
value can stay only when it lies in $[x,x+N-1]$. Duplicate occurrences cannot
both remain because the final values must be unique. Therefore, after sorting
the distinct input values, the problem becomes finding the largest number that
fit in any interval of width $N-1$.

**Sweep all candidate intervals with one window.** Maintain indices `left` and
`right` into the sorted distinct values. For each `left`, advance `right` while
the value there is less than `values[left] + N`. The window then contains
exactly the distinct values that can remain unchanged when its first value is
the final minimum. Its replacement count is
`N - (right - left)`. Take the minimum across all left endpoints, and never
move `right` backward.

For any final continuous interval, its unchanged input values form one such
window, so no solution can keep more elements than the largest window.
Conversely, every window can be completed by replacing all other positions
with the missing integers from its length-$N$ interval. Thus subtracting the
largest feasible distinct count from $N$ gives exactly the optimum.

## Complexity detail
Here $N$ is the length of `nums`. Deduplication and sorting take
$O(N\log N)$ time. Each window pointer advances at most once across the
distinct values, adding $O(N)$ time. The distinct-value collection uses
$O(N)$ space.

## Alternatives and edge cases
- **Restart a scan for every minimum:** Testing every sorted value and walking
  forward from it is correct but takes $O(N^2)$ time on dense inputs.
- **Binary search each right boundary:** Searching for `value + N` from every
  left endpoint takes $O(N\log N)$ after sorting, matching the overall bound
  but doing more repeated work than the sliding window.
- Duplicate occurrences beyond the first always require replacement, even
  when their shared value lies inside the chosen interval.
- A one-element array is already continuous.
- Values may be as large as $10^9$; the method depends on their order and
  differences, not on allocating an array across the value domain.
