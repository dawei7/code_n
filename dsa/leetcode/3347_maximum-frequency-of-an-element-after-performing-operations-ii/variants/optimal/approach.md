## General

For an original value `v`, one operation can transform it into any integer in `[v - k, v + k]`. Regard that range as an inclusive interval. For a prospective target `x`, let $R(x)$ count intervals that contain `x`, and let $C(x)$ count elements already equal to `x`.

All $C(x)$ existing copies may remain unchanged. Of the other $R(x)-C(x)$ reachable values, at most `numOperations` can be changed to `x`. The attainable frequency at `x` is therefore

$$
C(x)+\min(\texttt{numOperations},R(x)-C(x)).
$$

Build sparse difference events: add one at `v - k` and subtract one at `v + k + 1`. Insert each original value as a zero-delta event as well. Sweeping the sorted coordinates maintains $R(x)$, and the frequency map supplies $C(x)$.

These coordinates cover every optimum. Coverage is constant between consecutive events, so for a target absent from `nums`, evaluating the segment's left boundary gives the same score as every other integer in that segment. An original value must also be evaluated because its unchanged copies add a bonus without spending operations.

The contract demands exactly `numOperations` selected indices. If fewer than that many changes help the chosen target, select additional unused indices and add zero; this satisfies the operation count without reducing the frequency.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The event map contains $O(n)$ coordinates even when values and `k` approach $10^9$. Constructing it takes $O(n)$ time, sorting the coordinates takes $O(n\log n)$ time, and sweeping takes $O(n)$ time. Auxiliary space is $O(n)$.

The benchmark size is $n$. Its widely spaced values still create $O(n)$ sparse coordinates. The calibrated slower method checks the same candidate targets but rescans all $n$ values for each one, taking $O(n^2)$ time.

## Alternatives and edge cases

- **Dense coordinate difference array:** This can exploit the smaller bounds of related variants, but coordinates near $10^9$ make its memory use invalid here.
- **Sort plus binary searches:** Reachability around each original target can be counted with two searches, but targets absent from the input need additional candidate handling.
- **Quadratic candidate scan:** Testing every boundary against every element is correct but performs $O(n^2)$ work.
- **Absent target:** Two far-apart values can share a reachable integer even when neither original value can be the target.
- **Inclusive endpoints:** Intervals that meet at exactly one integer overlap; removal events belong at `v + k + 1`.
- **Existing duplicates:** Values already equal to the target do not consume operations.
- **Zero `k`:** Every selected index can only receive zero, so original frequencies are unchanged.
- **Exact operation count:** Surplus operations may add zero to distinct unused indices.
