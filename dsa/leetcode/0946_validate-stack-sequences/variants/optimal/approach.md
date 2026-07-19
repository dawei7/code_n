## General
**Simulate only the decisions that can help.** Keep an explicit stack and an index `next_pop` into `popped`. Process each value in `pushed` from left to right and append it to the stack. After every push, repeatedly pop while the stack is nonempty and `stack[-1] == popped[next_pop]`, advancing `next_pop` each time.

**Why immediate pops lose no valid sequence.** If the stack top equals the next required popped value, that value must leave before any later popped value. Delaying it and pushing more values would only place additional items above it, all of which would have to be removed first and would contradict the required order. Popping the match immediately is therefore forced in every valid execution. If the top does not match, no pop is legal for the proposed sequence, so the only possible progress is to consume another prescribed push.

Once all pushes have been processed, the sequence is valid exactly when `next_pop == n`. If an expected value remains unmatched, some different value blocks it on the stack, and no operations remain that could repair the order.

## Complexity detail
Each of the $n$ values is pushed once and popped at most once, so the total simulation work is $O(n)$. The explicit stack can hold all $n$ values, giving $O(n)$ space.

## Alternatives and edge cases
- **Reuse the input array as stack storage:** Maintain a write pointer into `pushed` and overwrite positions as the simulated stack. This preserves $O(n)$ time and reduces auxiliary space to $O(1)$, but mutates the input.
- **Backtrack over push/pop choices:** Explore both operations whenever they are legal. This can verify the sequence but repeats equivalent states and may take exponential time.
- **Remove the next pushed value from the front:** A direct simulation that repeatedly shifts a list is correct, but front removal can make the implementation $O(n^2)$.
- **One value:** The only permutation matches one push followed by one pop.
- **Immediate-pop order:** When `popped` equals `pushed`, each value can be popped as soon as it is pushed.
- **Reverse order:** Push every value first, then pop the entire stack; this is always valid.
- **Blocked earlier value:** Once a later-pushed value sits above the next required value and is not itself next in `popped`, the proposed sequence cannot be repaired by another pop.
