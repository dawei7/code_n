## General

**Why direct incrementing is the bottleneck**

A normal array stack can push and pop in constant time, but incrementing the bottom $k$ elements directly would touch up to $k$ positions. Repeating that operation many times can be expensive. The exact design uses lazy propagation: it records that a whole bottom prefix should receive an increment, then distributes that increment downward only as elements are popped.

The object stores three pieces of state:

- `stk` is a fixed array of length `maxSize` containing the base pushed values.
- `add` is a same-sized array containing deferred prefix increments.
- `i` is the number of current elements and also the next free index. The current top, when nonempty, is at `i - 1`.

Preallocating both arrays makes capacity checks and indexed access constant time.

**The meaning of a lazy marker**

A value `add[p] = v` means that increment $v$ applies to every stack element currently at indices zero through $p$. It is stored only at the top boundary of that affected prefix rather than copied into every position.

For example, with three elements, `increment(2, 100)` adds 100 only to `add[1]`. That marker represents the update to indices zero and one. Index two is above the boundary and must not receive it.

Several operations may accumulate at one boundary. Using `+=` rather than assignment ensures their effects combine.

**Push**

`push(x)` first checks `self.i < len(self.stk)`. If capacity remains, it writes `x` at the next free slot and increases `i`. If the stack is full, it does nothing, exactly as required.

No lazy increment is copied onto a newly pushed element. Earlier increments applied only to elements that were present among the bottom prefix when those operations occurred. A new top element must not inherit them.

The reused `add` position is safe because every popped slot is reset to zero before it can later be pushed into again.

**Increment**

The number of affected elements is `min(k, self.i)`: either the requested bottom $k$ or the entire current stack when it is shorter. The highest affected index is therefore

`min(k, self.i) - 1`.

If the stack is empty, this expression is $-1$, and the guard `if i >= 0` correctly performs no update. Otherwise, adding `val` to `self.add[i]` creates one marker for the complete affected prefix. No stack element is scanned, so increment is constant time.

**Pop and downward propagation**

If `self.i <= 0`, the stack is empty and `pop` returns $-1$. Otherwise it first decrements `i`, turning it from the element count into the index of the top being removed.

At this moment, every lazy increment that applies to the top element has accumulated at `add[self.i]`. Its actual value is therefore

`self.stk[self.i] + self.add[self.i]`.

The marker at this top boundary also applies to every element below it. Removing the top must not erase their increment. If another element remains, the statement

`self.add[self.i - 1] += self.add[self.i]`

moves the deferred amount one boundary downward. It will eventually reach each lower element when that element becomes the top.

Finally, `self.add[self.i] = 0` clears the removed slot so a future push into the same array position begins without stale updates.

**Tracing the two increments from the example**

Suppose the stack holds base values `[1, 2, 3]`. After `increment(5, 100)`, all three elements are affected, so `add[2]` becomes 100. After `increment(2, 100)`, `add[1]` also becomes 100.

Popping index two returns $3+100=103$. Its marker moves to index one, where the existing 100 becomes 200. Popping index one returns $2+200=202$ and moves 200 to index zero. The final pop returns $1+200=201$. The visible results are exactly what eager modification would produce, yet each operation touched only constant many array positions.

**The invariant behind correctness**

For every deferred increment operation, its value is stored at the highest still-present element in the prefix it originally affected. When that boundary element is popped, the marker moves to the next element below, which is still part of the same original prefix. Therefore the update remains available to all and only the elements it should affect.

A top pop collects every marker that has reached its index, so its returned base value includes exactly all increments issued while it was in the affected bottom range. Propagation preserves those same updates for lower survivors. Push neither loses old markers nor gives them to new elements. By induction over the operation sequence, the structure behaves exactly like an eagerly updated bounded stack.

## Complexity detail

The constructor allocates two arrays of length `maxSize`, taking $O(\texttt{maxSize})$ time and space. Each later `push` performs a comparison, assignment, and counter update. `increment` computes one index and changes one marker. `pop` reads, propagates, clears, and adjusts a constant number of slots. Thus every stack operation is $O(1)$ time.

The two fixed arrays use $2\cdot\texttt{maxSize}$ cells, which is $O(\texttt{maxSize})$ space and matches the manifest. No operation allocates storage proportional to $k$ or the current stack size.

## Alternatives and edge cases

- **Eager array updates:** Add `val` directly to the first `min(k, size)` elements. It is easier to visualize but makes `increment` cost $O(k)$.
- **Dynamic Python list:** Append and pop base values while retaining a parallel lazy array. It avoids unused base slots but still needs capacity tracking and the same marker invariant.
- **Segment tree with lazy propagation:** Supports richer range updates and queries, but is unnecessary complexity when every update always begins at the bottom.
- **Full stack:** `push` is ignored and changes neither stored values nor lazy markers.
- **Empty stack pop:** The method returns $-1$ before changing `i` or accessing arrays.
- **Empty stack increment:** The computed boundary is $-1$, so the guard makes it a no-op.
- **`k` exceeds current size:** The marker is placed at the current top, correctly affecting every present element.
- **`k = 1`:** Only `add[0]` changes, so only the bottom element eventually receives the increment.
- **Several overlapping increments:** Markers accumulate at their boundaries and combine during downward propagation.
- **Push after an increment:** The new element lies above the old affected prefix and correctly receives none of that earlier increment.
- **Pop then reuse a slot:** Clearing `add` at the removed index prevents a later pushed value from inheriting stale state.
- **Nonnegative `val`:** The stated constraint uses nonnegative increments, but the lazy arithmetic would also work for negative values.
- **Index interpretation:** `i` is a size and next-free index, not the top index; decrementing before a successful pop is therefore essential.
