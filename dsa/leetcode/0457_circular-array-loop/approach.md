## General

Every array index has exactly one destination, so the array defines a directed functional graph: each vertex has one outgoing edge. Following jumps from any start must eventually revisit an index. However, not every repeated route is valid. All jumps in the cycle must have one sign, and a one-index self-loop must be rejected.

The exact solution applies Floyd's slow-and-fast-pointer cycle detection from each start, while sign checks prevent the pointers from crossing into the opposite direction. It also writes zero into processed starting positions so later outer iterations skip them.

**Compute circular destinations**

For index `i`, `next(i)` returns

$$
(i + (\texttt{nums}[i]\bmod n) + n)\bmod n.
$$

Modulo wraps forward jumps beyond the last index back to the front and wraps backward jumps before zero back to the end. In Python, `nums[i] % n` is already nonnegative, so the extra `+ n` is redundant but harmless. Reducing the jump before addition also handles magnitudes larger than the array length.

Input values initially are nonzero. The algorithm later uses zero as an internal “already processed” marker; for such a slot, `next(i)` becomes `i`, but sign-product checks prevent that marker from joining a valid search.

**Floyd detection under one fixed direction**

For an unmarked start `i`, initialize `slow = i` and `fast = next(i)`. On each loop iteration, slow is prepared to advance one edge and fast two edges.

The loop continues only while

`nums[slow] * nums[fast] > 0`

and

`nums[slow] * nums[next(fast)] > 0`.

A positive product means the two jumps have the same nonzero sign. The first check confirms that slow and fast remain in one direction; the second confirms that fast's next landing also has that direction before fast takes its second step. If either product is nonpositive, the route changes sign or reaches a zero marker, so it cannot be the required uniform-direction cycle for this start.

When the checks pass and `slow == fast`, Floyd's method has found a repeated position. The code then tests `slow != next(slow)`. If the next jump returns to the same position, the cycle length is one and is forbidden. Otherwise the meeting lies on a cycle of length greater than one, and all traversed cycle jumps have the verified common sign, so the method returns `True`.

If no meeting occurs yet, slow advances once and fast advances twice. In any finite functional graph, pointers restricted to a genuine cycle eventually meet because fast gains one cycle position on slow per iteration.

**Trace the valid first example**

For `[2,-1,1,2,2]`, start at index `0`. Its route is `0 -> 2 -> 3 -> 0`. Values at those indices are `2`, `1`, and `2`, all positive. Slow moves one edge at a time while fast moves two; they eventually meet inside this three-index cycle. Since the meeting index does not point to itself, the method returns `True`.

**Why mixed signs are rejected**

The graph may contain a repeated route whose edges alternate direction, but the problem explicitly disallows it. A product check fails as soon as one pointer reaches a value whose sign differs from the route's current sign. For `[1,-1,...]`, the route `0 -> 1 -> 0` repeats, yet the values `1` and `-1` have opposite signs, so it is not accepted.

**Why a self-loop is rejected separately**

A jump can be a nonzero multiple of `n`, making its circular destination equal to its source. Floyd's pointers then meet immediately, but the required cycle length is greater than one. Comparing `slow` with `next(slow)` identifies exactly this case and breaks instead of returning true.

**What the cleanup loop actually does**

After a start fails to produce a valid cycle, the code enters a cleanup loop intended to mark the same-direction route with zeros. Marking an entire failed route would be safe: if that route reached a valid same-sign multi-node cycle, Floyd would already have returned true; otherwise none of its nodes needs to be explored again.

The exact statement order, however, is:

```text
nums[j] = 0
j = next(j)
```

Because `next(j)` reads the now-zeroed `nums[j]`, it returns `j` itself. The next loop condition sees a zero product and stops. Consequently, this exact source marks only the current outer-loop starting index, not the complete explored route.

This detail does not create a false cycle. A zero marker can only stop future sign-consistent traversals, and the marked start was already shown not to lead to an acceptable cycle from its direction. It does, however, remove the intended amortization: later starts may traverse much of the same failed path again.

To perform the intended full cleanup, the destination must be cached before mutation: compute `nxt = next(j)`, then set `nums[j] = 0`, then assign `j = nxt`.

## Complexity detail

The manifest states $O(n)$ time and $O(1)$ auxiliary space, which are the standard bounds for Floyd detection combined with complete path marking. With the corrected cleanup order, every failed-path index is zeroed once, so later searches skip it; all pointer work amortizes to $O(n)$.

For the exact source as written, only one start is zeroed per outer iteration. A long same-direction path that eventually reaches an opposite-sign edge or an invalid self-loop can be traversed again from many successive starts. The actual worst-case time is therefore $O(n^2)$, although many inputs finish sooner and any discovered valid cycle returns early.

Auxiliary space is $O(1)$: the algorithm stores only indices, scalar values, and the nested function. It achieves this by mutating `nums` with zero markers. Recursion and per-index visited arrays are not used.

## Alternatives and edge cases

- **Corrected in-place cleanup:** Cache `next(j)` before writing zero. This preserves the same logic and restores the intended $O(n)$ amortized time with $O(1)$ auxiliary space.
- **Per-start visited set:** Record indices along each walk and detect repeats directly. It is simpler to visualize but can use $O(n)$ extra space and repeat work unless global state is also maintained.
- **Three-state visitation array:** Mark nodes unseen, active in the current walk, or fully processed. This gives $O(n)$ time and clear cycle ownership, but uses $O(n)$ space.
- **Ignore direction:** Ordinary functional-graph cycle detection would wrongly accept routes containing both positive and negative jumps.
- **One-element array:** Every jump returns to the sole index, producing only a forbidden length-one cycle; the result is false.
- **Jump divisible by `n`:** Its destination is the same index even though the stored jump is nonzero, so the explicit self-loop test is necessary.
- **Mixed-sign repeated route:** Repetition alone is insufficient; sign-product guards reject it.
- **All-positive or all-negative valid cycle:** Direction checks remain positive products in either case because two negatives multiply to a positive number.
- **Zero values:** Original inputs cannot contain zero. Zeros are reserved for internal marking and cause future traversals to stop.
- **Input mutation:** Failed starts are replaced with zero. Callers that need the original jumps must pass a copy.
- **Negative modulo:** Python already produces a nonnegative remainder for positive `n`; other languages may need the double-modulo normalization shown by the formula.
