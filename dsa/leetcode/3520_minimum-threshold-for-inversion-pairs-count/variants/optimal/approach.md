## General

For a fixed threshold $x$, let $C(x)$ be the number of qualifying inversion pairs. Increasing $x$ can only add pairs, so the predicate $C(x)\ge k$ is monotone and the minimum valid threshold can be found by binary search.

To evaluate $C(x)$, scan `nums` from left to right. When the current value is $v=\texttt{nums[j]}$, every earlier index already stored in the data structure automatically satisfies $i<j$. The remaining requirements are

$$
v < \texttt{nums[i]} \le v+x.
$$

Coordinate-compress the distinct array values and store the frequencies of values already seen in a Fenwick tree. Two prefix sums then count the earlier values in that half-open interval: subtract the number at most $v$ from the number at most $v+x$. This excludes equal values, as required by the strict inversion inequality. Add the current value only after querying, so an index is never paired with itself or a later position.

The largest possible difference $R$ admits every inversion pair. Evaluating $C(R)$ first therefore detects the impossible case. Otherwise, binary-search thresholds from 1 through $R$. At each step, keep the lower half exactly when its midpoint already admits at least `k` pairs. Monotonicity guarantees that the converged value is the smallest valid threshold.

## Complexity detail

Let $n$ be the array length, let $m\le n$ be the number of distinct values, and let $R=\max(\texttt{nums})-\min(\texttt{nums})$. Sorting the compressed values costs $O(n\log n)$. Each counting pass performs $n$ Fenwick queries and updates in $O(n\log m)$ time, and binary search performs $O(\log R)$ passes. The total time is $O(n\log n\log R)$, with the initial sort absorbed by that bound when a valid search is needed.

The compressed values and Fenwick tree use $O(n)$ space. Each counting pass rebuilds one tree of that size; it does not retain trees from earlier thresholds.

## Alternatives and edge cases

- **Merge-sort counting:** A modified merge step can also count pairs whose ordered values differ by at most the threshold in $O(n\log n)$ per predicate, but the Fenwick formulation makes the value interval explicit.
- **Segment tree:** Range-sum queries over compressed values give the same asymptotic bounds with a larger implementation and constant-factor overhead.
- **Enumerate all inversion differences:** Materializing up to $n(n-1)/2$ differences and selecting the `k`th uses quadratic time and space.
- **No inversions:** If the count at the full value span is below `k`, no threshold can succeed and the answer is `-1`.
- **Equal values:** They do not satisfy `nums[i] > nums[j]`; the lower prefix subtraction deliberately removes them.
- **Repeated differences:** Every index pair is counted separately, so duplicates may cause the count to jump by more than one at a threshold.
- **Early count saturation:** A predicate may stop once it reaches `k`, because the binary search needs only the truth of $C(x)\ge k$.
- **Large value span:** Binary search uses only $O(\log R)$ iterations even when values are near $10^9$.
