## General
**Reverse the operations:** Searching forward offers two choices at every step and can explore many unnecessary values. Starting from `target` makes the inverse move forced. An even value could have resulted from doubling, so halve it. An odd value greater than `startValue` cannot be the result of doubling; increment it first, which reverses a preceding subtract-one operation.

**Greedily remove the largest possible scale:** While the current reversed value exceeds `startValue`, perform the forced parity move and count it. Halving an even value is always preferable to incrementing or simulating extra forward decrements because any forward path that reaches that even value without a final doubling must spend at least as many operations adjusting a larger predecessor. For an odd value, incrementing is the only way to make a later inverse halving possible.

Once the reversed value is at most `startValue`, no inverse halving is useful: the forward calculator must subtract exactly `startValue - current` times. Adding that difference to the reversed-operation count completes an optimal path.

## Complexity detail
Every one or two reversed iterations reduce the current value by roughly half. The loop therefore performs $O(\log T)$ operations and uses only counters plus the current value, for $O(1)$ space.

## Alternatives and edge cases
- **Forward breadth-first search:** BFS finds the minimum path, but the reachable numeric state space grows with `target` and can require $O(T)$ time and space.
- **Forward greedy doubling:** Always doubling while below the target can overshoot in a way that requires more decrements than subtracting before an earlier doubling.
- **Target not above the start:** When `target <= startValue`, only subtraction can reduce the display, so the answer is their difference.
- **Odd reversed value:** Increment before halving; integer division directly would reverse no legal forward operation.
- **Equal values:** No operation is needed when `startValue == target`.
