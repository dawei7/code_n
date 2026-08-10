## General

**Simulate the only useful greedy behavior**

Values must be pushed in exactly the order given by `pushed`. The only choice is when to pop.

Whenever the stack top equals the next required value in `popped`, delaying that pop cannot help. A later push would cover the matching value, making it temporarily inaccessible, while no different value is allowed to pop first.

The algorithm therefore pushes each incoming value and then pops as many currently required values as possible.

List `stk` is the simulated stack. Pointer `i` counts how many requested pop values have already been produced, so `popped[i]` is the next target.

**What happens after each push**

For every `x` in `pushed`, the code first executes `stk.append(x)`. The new value becomes the top.

The inner loop runs while:

- the stack is nonempty;
- `stk[-1] == popped[i]`.

When both are true, popping is legal and required by the target order. The code removes the top and increments `i`.

The loop repeats because one pop may reveal another value that is immediately the next target. For example, after pushing `1, 2, 3, 4`, target four can pop. If target three comes next, removing four exposes three, so it should pop before another push.

Using an `if` instead of a `while` would miss such chains of forced pops.

**Why immediate popping is safe**

Suppose the current top is the next required target. Any valid operation sequence must eventually pop this occurrence before it can emit the following target.

There are only two possible actions:

- pop it now;
- push more values above it and pop those later before returning to it.

The second option cannot produce a different target first because the requested sequence says this top value must be next. Any newly pushed value would have to remain above it, so delaying creates no new valid choice.

Therefore, if some valid schedule exists, there is also a valid schedule that performs this pop immediately. The greedy step cannot destroy feasibility.

**Why continuing to push is the only option on a mismatch**

If the stack is empty, nothing can pop. If its top differs from `popped[i]`, popping that top would violate the requested output order.

The only potentially useful action is to push the next value from `pushed`. This may place the required target on top, or it may build the necessary stack arrangement for later pops.

Thus at every moment the simulation either makes a forced pop or the only legal progress-making push.

**A successful trace**

For `pushed = [1, 2, 3, 4, 5]` and `popped = [4, 5, 3, 2, 1]`:

- Push one, two, and three; none matches target four.
- Push four, then pop it. Pointer `i` now targets five.
- Push five and pop it.
- Removing five reveals three, which matches the next target, so pop three.
- The loop then pops two and one in order.

All five targets are matched, so the result is true.

For target `[4, 3, 5, 1, 2]`, four and three can pop, then five can pop. The remaining stack has two above one. Target one cannot be popped before two, and there are no more pushes that can change their relative stack order, so the result is false.

**Why the final pointer is decisive**

If `i == len(popped)`, every requested value was produced in order. The operations performed by the simulation are themselves a witness that the sequences are valid.

If `i` is smaller after every pushed value has been processed, the next requested target is not available at the top. No push remains, and popping a different top would be wrong. Completion is impossible.

The expression `popped[i]` remains safe. Pointer `i` can reach the length only after all `n` values have popped, which leaves `stk` empty. The short-circuit condition checks `stk` first, so the target is not accessed again.

**Role of distinctness**

All values are distinct and `popped` is a permutation of `pushed`. A value therefore identifies one exact stack item. The algorithm does not need occurrence counters or checks for missing values; it only validates whether the required order is compatible with last-in, first-out behavior.

## Complexity detail

Let `n` be the common sequence length.

Every value is appended exactly once and removed at most once. Although the while loop is nested syntactically inside the for loop, its total number of successful iterations over the whole method is at most `n`. Time is `O(n)`.

The simulated stack can contain all `n` values when no early target is reachable, so auxiliary space is `O(n)`.

## Alternatives and edge cases

- **Recursive search:** Branch between pushing and popping at every step. It explores many schedules even though a matching top can always be popped greedily.
- **Reuse `pushed` as stack storage:** A write pointer can simulate the stack in place with `O(1)` auxiliary space, but it mutates the input and is less explicit.
- **Pop only once per push:** This is incorrect because one push may unlock a chain of several target pops.
- **Identical orders:** Each value is popped immediately after being pushed, and the method returns true.
- **Reverse orders:** All values are pushed first and then popped from the top, also returning true.
- **Buried target:** If the next target lies below a different top after all pushes, the sequence is impossible.
- **One element:** It is pushed and immediately popped, so the result is true.
- **Empty stack guard:** It must be checked before reading `stk[-1]`.
- **Pointer boundary:** Stack emptiness protects the access after all targets have matched.
- **Permutation guarantee:** The method need not separately reject length mismatches or foreign values because the contract excludes them.
