## General

**Use a variable-length consecutive window**

The chosen robots must be consecutive, so every candidate is a window `[l, r]`. Its length is:

$$
k=r-l+1,
$$

and its cost is:

$$
\max(\texttt{chargeTimes}[l..r])
+k\sum_{i=l}^{r}\texttt{runningCosts}[i].
$$

The algorithm moves `r` from left to right. It maintains the running-cost sum and maximum charge time for the current window, then advances `l` only while the budget is exceeded.

**Maintain the running-cost sum**

`s` is the sum of `runningCosts[l..r]`. When a new right endpoint arrives, its cost `c` is added. When the window shrinks from the left, `runningCosts[l]` is subtracted before `l` advances.

All running costs are positive. Therefore, removing a left endpoint never increases this sum or the window length, so shrinking moves the total-cost expression toward feasibility.

**Maintain the maximum charge with a decreasing deque**

Deque `q` stores indices in increasing position order, but their charge values are strictly decreasing from front to back.

Before appending new index `r` with charge `t`, the code removes back indices whose charge is less than or equal to `t`. Those indices can never become the maximum while `r` remains in the window: `r` is newer, stays at least as long, and has an equal or larger charge.

After appending `r`, `q[0]` is the index of the current maximum charge.

When `l` leaves the window, the code removes the deque front only if that stored maximum index equals `l`. Other expired dominated indices were already removed from the back or will never sit before a valid front under the maintained index order.

**Shrink until the cost fits**

The exact budget check is:

```python
(r - l + 1) * s + chargeTimes[q[0]] > budget
```

While this is true, the current window is invalid. The method removes its leftmost robot and repeats. It stops when the window is valid or becomes empty.

If a single robot itself exceeds budget, its index is removed from `q`, its running cost is subtracted, and `l` moves to `r + 1`. The deque becomes empty, the guarded while condition stops, and the current feasible length is zero.

**Why discarding left endpoints is safe**

Fix right endpoint `r`. If window `[l,r]` exceeds budget, no larger window ending at `r` and starting before `l` can be feasible. Such a window has at least as many robots, a no-smaller running-cost sum, and a no-smaller maximum charge.

Therefore, advancing `l` does not discard a candidate that could improve the answer for this or any later processing stage. The smallest remaining `l` after shrinking gives the longest feasible window ending at `r`.

`ans` records the maximum of these per-right-endpoint lengths, covering every possible optimum.

**Trace the first three robots**

For charge times `[3,6,1]` and running costs `[2,1,3]`, the running sum is six and length is three. The decreasing deque's front points to charge six. Cost is:

$$
6+3\cdot6=24,
$$

which fits budget 25, so answer reaches three.

Adding the next robot raises the running sum and length enough to exceed budget. The while loop moves `l` and updates both the sum and deque until the remaining consecutive window is legal.

**Why the deque invariant is correct**

Indices are appended in increasing order. Removing smaller-or-equal charges from the back preserves decreasing charge values. Every removed index has a later dominating index, so it cannot be needed as a future maximum before it expires.

The front is therefore always the maximum charge among active window indices. Removing it exactly when it crosses `l` keeps all stored indices inside the window.

**Why the full algorithm is correct**

For every `r`, maintained `s` and deque front give the exact cost of `[l,r]`. The shrink loop removes only starts that cannot form a feasible window ending at `r` until the longest feasible ending window remains. Updating the global maximum considers that best length for every possible right endpoint.

Every consecutive candidate has some right endpoint, so the global optimum is considered. The returned maximum is exact.

## Complexity detail

Each robot index is appended to the deque once. It is removed at most once, either from the back when dominated or from the front when leaving the window. The left pointer advances at most $n$ times across the entire scan. Total time is $O(n)$.

The deque can contain $O(n)$ indices in a strictly decreasing charge sequence. All other state is scalar, so auxiliary space is $O(n)$.

Products and sums can be large; Python integers handle them. Fixed-width implementations need 64-bit arithmetic because budget reaches $10^{15}$.

## Alternatives and edge cases

- **Binary search window length:** For each candidate length, use sliding sums and maxima to test feasibility. It can work in $O(n\log n)$ but is slower than the direct variable window.
- **Heap for maximum charge:** Lazy deletion can maintain maxima in $O(\log n)$ operations, while the monotonic deque gives amortized $O(1)$.
- **No single robot fits:** Every window shrinks to empty and the answer remains zero.
- **Exactly budget:** The while condition uses `>`, so equal cost is correctly accepted.
- **Equal charge times:** Older equal charges are removed because the newer one dominates and expires later.
- **Maximum at the left boundary:** It is popped exactly when `l` passes it, exposing the next maximum.
- **All windows fit:** `l` stays zero and the answer grows to `n`.
- **Positive costs:** They supply the monotonicity that makes shrinking safe.
- **Empty current window:** The `q and ...` guard avoids reading a missing maximum.
