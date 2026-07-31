## General

Each original value $x$ may become any integer in the interval $[x-k, x+k]$. A collection of values can all become equal exactly when their intervals share at least one common point. For equal-radius intervals, that happens precisely when the largest original value minus the smallest original value is at most $2k$.

Sort `nums`. Any set satisfying this endpoint condition can be extended to include every sorted value between its minimum and maximum, so an optimal set appears as a contiguous sorted window. Maintain such a window with pointers `left` and `right`. Advance `right` through the sorted values; while `nums[right] - nums[left] > 2 * k`, move `left` forward until the window is feasible again. Record the greatest window length seen.

**Why the longest valid window is the maximum beauty**

Every maintained window has endpoint difference at most $2k$. Its intervals therefore overlap: choosing any integer between `nums[right] - k` and `nums[left] + k` gives a target reachable by every window element. The window length is consequently achievable as beauty.

Conversely, consider any subsequence that can be made equal to one target. Every selected value lies within $k$ of that target, so its maximum and minimum differ by at most $2k$. After sorting, all values between those endpoints are compatible as well, and the selected values fit inside a valid contiguous window. The sliding window examines the maximal feasible window ending at every `right`, so its best length is at least the size of any achievable subsequence and cannot exceed an achievable beauty. The two quantities are equal.

## Complexity detail

Sorting $n$ values costs $O(n\log n)$ time. Each pointer then advances at most $n$ times, so the window scan is $O(n)$ and the total remains $O(n\log n)$. Python's in-place list sort may use $O(n)$ auxiliary memory in the worst case; the pointers themselves use $O(1)$ space.

## Alternatives and edge cases

- **Binary search per left endpoint:** After sorting, binary-search the furthest value within `nums[left] + 2 * k`; this is also $O(n\log n)$ but repeats logarithmic searches that the two pointers avoid.
- **Quadratic expansion:** Trying every sorted pair or target window is straightforward and correct but can take $O(n^2)$ time.
- **Difference-array counting:** The bounded value domain permits a sweep over coordinates, but its cost depends on the maximum value range and needs extra counting storage.
- **Zero `k`:** A valid window contains only equal values, reducing the result to the highest frequency.
- **Inclusive interval boundary:** Values differing by exactly $2k$ can meet at the touching endpoint and must stay together.
- **Single element:** Its interval always contains a target, so the answer is one.
- **Duplicate values:** Sorting keeps them adjacent, and the window naturally counts every copy.
- **Input mutation:** The reference sorts `nums` in place; this is permitted because the contract asks only for the resulting beauty.
