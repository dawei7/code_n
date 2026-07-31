## General

For any chosen elements, changing them all to a median minimizes the sum of
absolute differences. After sorting, an optimal chosen set can be taken as a
contiguous window: replacing a selected value while skipping a closer value
cannot increase the window size or reduce feasibility.

Build prefix sums of the sorted values. For window `[left, right]`, use its
middle element as the median. Prefix sums give in constant time the cost to
raise the left half to the median and lower the right half to it. Extend
`right`; while the cost exceeds `k`, advance `left`. Once feasible, record the
window length.

For a fixed right endpoint, removing the smallest remaining value cannot
increase median-conversion cost, so feasibility is monotone as `left` advances.
The maintained window is therefore the longest feasible window ending at each
right endpoint. Considering every endpoint finds the maximum attainable
frequency.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Sorting takes $O(N\log N)$ time. Both
window boundaries advance at most $N$ times and every cost query is $O(1)$, so
the scan is $O(N)$. The sorted values and prefix sums use $O(N)$ space.

## Alternatives and edge cases

- **Enumerate every sorted window:** Prefix sums make each cost test constant-time, but checking all $O(N^2)$ windows is still quadratic.
- **Binary search the answer:** Testing whether any window of a chosen length is feasible also works in $O(N\log N)$ after sorting, but the sliding window avoids another logarithmic search.
- **Zero budget:** Only values already equal can contribute together, so the answer is the original maximum frequency.
- **Even window:** Any value between its two middle elements minimizes absolute-deviation cost; using the lower median yields the same minimum.
- **Both increments and decrements:** The target is a median, unlike variants that permit only increases and therefore target a window maximum.
- **Large budget:** If the cost for the whole sorted array is at most `k`, the maximum score is $N$.
