## General

**Understand when equal values can share one operation**

An operation selects a subarray and turns every occurrence of that subarray's minimum value into zero.

Two occurrences of positive value `v` can be cleared together only if every element between them is at least `v` at the time of that operation. If a smaller positive value lies between them, then:

- while it remains positive, `v` is not the minimum of the spanning subarray;
- after the smaller value is cleared, it becomes zero, and zero is then the minimum of any spanning subarray, so the two `v` occurrences are separated.

An existing zero is already such a permanent separator.

Therefore, for each positive value level, every separate contiguous component that survives above smaller values needs one operation. The monotonic stack counts exactly these value-level components.

**Maintain open nested value levels**

`stk` is strictly increasing from bottom to top. Each stored value represents a positive level whose current component has begun somewhere in the processed prefix and has not yet been closed by a smaller value.

Larger levels are nested inside components of smaller levels. For example, while scanning `[1,2]`, level one remains open and level two starts inside it, producing stack `[1,2]`.

The source delays counting an open component until it closes or until the scan ends.

**Close levels greater than the current value**

For current `x`:

`while stk and stk[-1] > x`

pops every open level larger than `x` and increments `ans` once per pop.

Why must such a level close? The current smaller value `x` prevents an earlier occurrence of the larger level from sharing one minimum operation with any later occurrence across this position. Its current component has ended, and at least one operation is necessary for that component.

Popping several levels handles nested components that all terminate at this smaller boundary.

**Treat zero as a complete separator**

If `x=0`, the while loop pops every positive stack value because all are greater than zero. The source then skips pushing because its condition begins with `if x`.

Zero needs no operation. It also prevents any positive component on its left from joining one on its right, exactly matching the full stack reset.

**Reuse an equal open level**

After popping, the stack is empty or its top is at most `x`.

If top equals `x`, the current occurrence belongs to the same still-open level component. Every intervening obstacle smaller than `x` would already have popped that level, so equality at the top certifies it can share the eventual operation. The source does not push or count again.

For `[1,2,1]`, processing the final one first closes level two. Level one remains on top, so both one occurrences belong to one component and require one shared operation.

**Start a new higher level**

If `x>0` and the stack is empty or its top differs from `x`, then after the pop loop top must be strictly smaller than `x`. The current value begins a new nested component, so the source pushes it.

No operation is counted yet. That component will be counted exactly once when a future smaller value pops it or when it remains open at the end.

**Count levels that remain open after the scan**

At the array end, every stack entry represents one component that never encountered a smaller right boundary. Each still needs one operation, so:

`ans += len(stk)`.

Every pushed component is counted exactly once: either during one pop or in this final addition. The source could equivalently increment the answer on each push, as the editorial version does; delayed counting yields the same total.

**Why this count is a lower bound**

Each push identifies a new positive value component separated from any prior same-value component by a smaller value or zero. One operation cannot clear two such components together:

- before the separating smaller value is removed, the larger value is not the spanning minimum;
- afterward, the resulting zero is the spanning minimum.

Thus every pushed component requires its own operation. The stack's total count is unavoidable.

**Why the lower bound is achievable**

The components form a nested hierarchy. For an open lower level, choose the subarray spanning its component while that value is the minimum; one operation clears all occurrences of that level in the component. This creates zero-separated subregions containing only higher levels. Apply the same process recursively inside each subregion.

Equivalently, process component nodes in increasing-level, outer-before-inner order. Every counted component can be cleared in one operation, and clearing a lower level creates exactly the separations that the stack used to distinguish higher components.

Therefore, one operation per pushed component is sufficient. Combined with the lower bound, the stack count is minimum.

**Trace the alternating example**

For `[1,2,1,2,1,2]`:

- push one, then push two;
- the next one pops and counts the first level-two component, while level one stays open;
- each later one similarly closes the preceding level-two component;
- the last two remains open.

At the end, the stack contains levels one and two. Two level-two components were already counted, and these two open components add two more, totaling four: one operation for all ones and one for each of the three separated twos.

## Complexity detail

Each positive value is pushed at most once for the component it starts. Every stack entry is popped at most once. Although one iteration may pop many entries, total pops across the scan are `O(n)`.

The scan therefore takes `O(n)` amortized time.

In the worst case of strictly increasing positive values, the stack stores all `n` values, so auxiliary space is `O(n)`. Scalars use constant additional space.

The answer is at most `n` because each counted component originates from a push associated with an input position.

## Alternatives and edge cases

- **Increment answer on push:** Equivalent to the protected delayed-pop counting because every pushed entry is eventually popped or remains at the end.
- **Simulate minimum operations directly:** Repeatedly finding minima and zeroing ranges can become quadratic. The stack counts the component hierarchy in one pass.
- **Use a set of distinct values:** The same value may require multiple operations when smaller values or zeros separate its components.
- **Keep a non-monotonic stack:** Larger levels must close when a smaller boundary arrives; strict increasing order exposes exactly those levels at the top.
- **All zeros:** Nothing is pushed or popped, so the answer is zero.
- **One positive value:** It is pushed and counted at the end, giving one.
- **All equal positive values:** The first is pushed and later equal values reuse the same level, so one operation clears all.
- **Strictly increasing values:** Every value starts a nested level; all remain open and the answer is `n`.
- **Strictly decreasing values:** Each new value pops and counts the previous level, then starts its own; total is also `n`.
- **Zero between equal positives:** Zero pops the left component, so the right occurrence starts another and needs a separate operation.
- **Smaller positive between equal larger values:** The larger level is popped at the smaller value and cannot be shared across it.
- **Larger values between equals:** They are popped when the equal lower value returns, while the lower level stays open and is shared.
- **Minimum includes zero:** Selecting a subarray containing zero cannot clear positive values, which is why zeros are permanent separators.
- **Final stack addition:** Omitting it would forget every component that reaches the array's right boundary.
