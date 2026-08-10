## General

**Why an ordinary stack is not enough**

A normal stack can return or remove its top in constant time because the top is
stored at a known end of the underlying list. Its minimum is different: without
extra information, `getMin()` would have to inspect every active value. That
would take linear time and violate the requirement that every operation be
$O(1)$.

The key observation is that stack history is nested. While a value remains in
the stack, nothing below it changes. Therefore, for every depth, the minimum of
the prefix ending at that depth can be computed once during `push` and kept
until the matching `pop`.

The selected class represents this history with two synchronized lists:

- `stk1[i]` is the actual value pushed at depth `i`;
- `stk2[i + 1]` is the minimum of all actual values from depth zero through
  depth `i`.

`stk2` has one extra entry at its bottom: positive infinity. That sentinel is
the minimum of an empty conceptual prefix and lets the first `push` use exactly
the same formula as every later push.

**Push a value and its prefix minimum together**

For `push(val)`, the source first appends `val` to `stk1`. It then computes
`min(val, stk2[-1])` and appends that result to `stk2`.

Suppose the old stack minimum was $m$. After pushing $v$, every earlier value
is unchanged, so the new minimum can only be one of two values: the old minimum
$m$, or the newly introduced value $v$. Hence the new minimum is
$\min(v,m)$. No scan is necessary.

For the first push, the old tracker top is infinity. Every allowed integer is
smaller than infinity, so the appended tracker value is the first actual value.
The sentinel removes the need for a special empty-stack branch.

Equal minima are deliberately repeated. If the current minimum is `-2` and
another `-2` is pushed, the tracker receives another `-2`. This is useful:
each actual stack entry has exactly one matching tracker entry, so a pop can
remove one item from each list without counting duplicates or comparing values.

**Keep both lists synchronized on removal**

`pop()` calls `pop()` once on `stk1` and once on `stk2`. Before the operation,
an actual stack of size $k$ has a tracker of size $k+1$, including the
sentinel. After removing one entry from each, their size difference remains
one.

The tracker value exposed afterward was created when the new top was pushed.
It is therefore exactly the minimum of all entries that still remain. This
holds whether the removed value was larger than the minimum, was the only
occurrence of the minimum, or was one of several equal minima.

The problem guarantees that `pop()` is called only on a nonempty stack. As a
result, the actual list never underflows, and the sentinel is never removed.

**Answer both queries from the final entries**

`top()` returns `stk1[-1]`, the most recently pushed value that has not been
popped.

`getMin()` returns `stk2[-1]`. On every nonempty logical stack, that position
contains the prefix minimum associated with the current depth, never the
sentinel. The method only reads it; retrieving the minimum does not remove
anything.

These operations are constant time because Python lists support indexing and
append/pop at the end without walking through earlier elements. Append is
amortized $O(1)$: a rare internal resize costs more, but across a sequence of
appends the average cost per call is constant.

**Trace the supplied operation sequence**

Start with `stk1 = []` and `stk2 = [inf]`.

- Pushing `-2` gives actual values `[-2]` and minima `[inf, -2]`.
- Pushing `0` gives `[-2, 0]` and `[inf, -2, -2]`; zero does not change the
  minimum.
- Pushing `-3` gives `[-2, 0, -3]` and `[inf, -2, -2, -3]`; the new value
  becomes the minimum.
- `getMin()` reads `-3`.
- `pop()` removes `-3` from both histories, exposing `0` as the actual top and
  `-2` as the restored minimum.

The trace also shows why recomputation is unnecessary. The old minimum was not
destroyed when `-3` arrived; its historical tracker entry remained one level
below and became visible again after the pop.

**Why the invariant proves every result**

After construction, the actual stack is empty and the tracker contains only
the sentinel. Assume that for a stack of size $k$, each tracker entry records
the minimum through its corresponding depth. A push appends the minimum of the
new value and the previously correct minimum, so the property extends to depth
$k+1$. A pop removes the last depth from both histories, leaving all earlier
correct entries untouched.

By induction, the relationship holds after every valid operation. `top()` and
`getMin()` read exactly the entries that this relationship identifies, so both
queries are correct.

**Exact-source dependency**

The selected file initializes `self.stk2 = [inf]`, but it does not import or
define `inf`. In a standalone Python execution, construction raises
`NameError`. The intended representation works if the environment supplies
`inf`, or if the source uses `float("inf")` or imports `inf` from `math`. This
is a runtime dependency in the stored source, not a flaw in the prefix-minimum
algorithm.

## Complexity detail

Let $n$ be the number of values currently in the logical stack, and let $q$ be
the total number of calls.

Each `push`, `pop`, `top`, and `getMin` performs a constant number of end-list
operations, comparisons, or index reads. Each call is $O(1)$ amortized time;
the non-growing query and pop operations are worst-case constant time.

`stk1` stores $n$ values. `stk2` stores $n$ corresponding prefix minima plus
one sentinel. Thus the total auxiliary storage is $2n+1$, which is $O(n)$.
Across at most $q$ pushes without matching pops, this is also $O(q)$. The
manifest's $O(1)$ per-operation time and $O(n)$ space bounds match the intended
implementation.

## Alternatives and edge cases

- **One stack of pairs:** Store `(value, minimum_so_far)` at every depth. It expresses the same invariant with one container and the same $O(n)$ storage.
- **Two stacks with change points:** Keep all values in one stack and push onto a minimum stack only when a value is at most the current minimum. Equal minima must also be tracked, or counted, so popping one duplicate does not lose the remaining minimum.
- **Difference encoding:** Store differences relative to the current minimum and restore the previous minimum algebraically when a negative marker is popped. It uses one list but requires more careful arithmetic.
- **Scan during `getMin`:** Uses no minimum history, but a query becomes $O(n)$ and violates the contract.
- **Heap or balanced tree:** Maintaining deletions consistently costs at least logarithmic time and is unnecessary for stack-ordered removal.
- **Repeated minimum:** The tracker intentionally stores repeated prefix minima, so removing one occurrence leaves the next correct tracker entry.
- **First push:** The infinity sentinel makes the ordinary minimum formula valid, provided `inf` is defined.
- **Pop to empty:** The actual list becomes empty while the tracker returns to `[inf]`; the contract prevents `top()` or `getMin()` at that moment.
- **Full integer range:** Comparing an allowed integer with mathematical infinity is safe in Python.
- **Undefined sentinel name:** Standalone use must define `inf`; otherwise even construction fails before any stack operation.
