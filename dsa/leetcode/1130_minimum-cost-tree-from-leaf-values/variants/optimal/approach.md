## General
**View construction as eliminating leaves.** Whenever two neighboring components are joined, the smaller component maximum contributes its product with a neighboring value that survives above it. For a leaf value `mid`, using anything larger than the smaller of its nearest surviving greater-or-equal neighbors cannot improve the total. Thus, once both such boundaries are known, greedily pairing `mid` with the smaller boundary is safe; the larger value remains available for later joins.

**Expose those boundaries with a decreasing stack.** Start with an infinite sentinel. For each `value`, pop while `stack[-1] <= value`. Every popped `mid` has `value` as its first greater-or-equal value on the right and the new stack top as its nearest greater value on the left. Add `mid * min(stack[-1], value)`, which is the cheapest unavoidable partner for `mid`, then continue until the stack is decreasing and push `value`.

**Finish the decreasing suffix.** Values left after the scan have no greater-or-equal value to their right. Pop them from right to left and multiply each by its left neighbor. In a decreasing sequence that neighbor is the smaller available surviving partner. Every value except the global maximum is eliminated exactly once, producing exactly the $n-1$ internal-node products of a full binary tree. The exchange argument above shows no alternative tree can give an eliminated value a cheaper valid partner, so the sum is minimum.

## Complexity detail
Each of the $n$ values is pushed once and popped once, so all stack operations take $O(n)$ time. The monotonic stack can contain $n$ values plus its sentinel, giving $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Interval dynamic programming:** Try every root split for every contiguous leaf interval using precomputed interval maxima; this is straightforward and correct but costs $O(n^3)$ time and $O(n^2)$ space.
- **Repeatedly remove the global smallest leaf:** Pairing the current minimum with its smaller neighbor is another greedy formulation, but finding and deleting minima naively costs $O(n^2)$.
- **Two leaves:** There is only one valid tree, so the answer is their product.
- **Equal values:** The `<=` pop condition may eliminate either equal copy first without changing the product or optimum.
- **Strictly decreasing input:** No value pops during the scan; the cleanup pairs adjacent surviving values from right to left.
