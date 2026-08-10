## General

For one position `i`, the next greater value may lie later in the ordinary array or may appear after wrapping from the final position back to index zero. Conceptually concatenating `nums` with itself turns that circular search into an ordinary rightward search. The source simulates this doubled array with modular indices instead of allocating a second copy.

`ans` begins as `[-1] * n`. The sentinel is already correct for any value that never finds a strictly greater element. `stk` is a monotonic stack of values seen to the right in the conceptual doubled traversal.

The loop counts backward from `2 * n - 1` through zero, exactly `2n` iterations. Each raw loop index is replaced by `i %= n`, mapping the second conceptual copy and the first copy onto the real array positions.

The first `n` reverse iterations process conceptual positions `n` through `2n - 1`. They prepare suffix information that represents values encountered after wrapping. The final `n` iterations process the actual positions `0` through `n - 1` and overwrite `ans[i]` with answers that now consider a complete circular lap.

**Remove values that cannot answer the current position.** Before answering for `nums[i]`, the loop pops while

`stk[-1] <= nums[i]`.

A smaller value is not greater, so it cannot answer. An equal value also cannot answer because the requirement is strictly greater. Moreover, once current `nums[i]` is available farther left, a popped no-larger value is dominated for future positions: whenever it could be greater than a future value, current `nums[i]` is at least as large and appears earlier in that future position's traversal order.

After popping, if the stack is nonempty, its top is the first surviving value to the right that is strictly greater than `nums[i]`. The code assigns it to `ans[i]`. If the stack is empty, no qualifying value is known in the complete relevant suffix, and the prefilled `-1` remains.

Finally, `nums[i]` is pushed so it can serve as a candidate for positions farther left.

**Why the stack top is the first greater value, not merely the smallest greater value.** The stack compresses the right-side sequence by removing dominated values while preserving the order of candidates. A closer greater value is pushed above farther candidates and remains there unless an even closer value dominates it for future work. After all values no greater than the current one are popped, the nearest remaining qualifying candidate is on top.

Suppose `nums = [1, 2, 1]`. During the conceptual second copy, the stack learns the suffix pattern. In the final pass, the last real `1` can see wrapped value `2` and receives two. The middle value `2` pops every value no greater than two and finds no larger candidate, retaining `-1`. The first `1` finds the immediate `2`. The result is `[2, -1, 2]`.

**Why two copies are enough.** Starting just after any position and moving circularly visits at most the other `n - 1` positions before returning to itself. A doubled linear representation contains that entire sequence to the right of the first-copy position. Anything beyond two copies would repeat values already examined and could not introduce a new greater value.

Processing a position twice does not allow it to answer itself. When the second occurrence of the same array value is processed in the final pass, the `<=` loop pops an equal copy from the stack. Since equal is not strictly greater, this is exactly what should happen.

Correctness follows from the standard reverse monotonic-stack invariant applied to the conceptual doubled array. Before each conceptual position is processed, the stack represents undominated candidates to its right in traversal order. Popping no-greater candidates cannot remove the required answer, and the remaining top is the first strictly greater value. The final-copy assignments correspond to each real position with all circular successors available, so they are the required answers.

The stack stores values rather than indices because the output asks only for values. Duplicates are handled by the `<=` pop rule. An index stack would also work and can be useful when the output needs positions or distances.

## Complexity detail

The loop performs `2n` iterations. Every pushed occurrence can be popped at most once. Although one iteration may pop many values, total pushes and pops are linear in the doubled traversal, so time is $O(n)$.

The answer requires $O(n)$ space. The monotonic stack holds at most $O(n)$ relevant values under the circular processing and duplicate elimination, so auxiliary space is $O(n)$. No doubled input array is allocated.

## Alternatives and edge cases

- **Brute-force circular scan:** For each position, inspect up to `n - 1` successors with modulo indexing. This costs $O(n^2)$ time.
- **Explicit doubled array:** Concatenate `nums + nums` and run a normal next-greater algorithm. It is correct but uses another $O(n)$ array that modular indexing avoids.
- **Forward unresolved-index stack:** Traverse two copies left to right and resolve indices when a greater value arrives. It also runs in $O(n)$ but requires care not to push first-copy indices repeatedly.
- **All values equal:** Every equal candidate is popped, so all answers remain `-1`.
- **Strictly decreasing ordinary order:** Several positions find answers only after wrapping; the maximum value still has no greater answer.
- **Single element:** Both conceptual occurrences are equal and pop each other, leaving the only answer `-1`.
- **Duplicate values:** Equality does not satisfy “greater,” so the pop condition must be `<=` rather than `<`.
- **Negative values:** Ordering comparisons work unchanged, and `-1` is an output sentinel rather than a candidate value. A legitimate next greater value can itself be `-1`, but the returned numeric result is still correct.
- **Answer overwritten twice:** The preliminary second-copy assignment may be incomplete. The final first-copy pass intentionally overwrites it after all wrapped candidates are available.
