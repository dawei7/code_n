## General

**Expansion stops at the first greater value on each side.** Fix index `i`. Any adjacent smaller value may be included while `nums[i]` remains the subarray maximum. The first greater value to the left cannot be crossed because including it would make `nums[i]` cease to be maximum. The same is true on the right.

Therefore, if `left[i]` is the nearest greater index to the left, or negative one when absent, and `right[i]` is the nearest greater index to the right, or `n` when absent, the largest valid subarray is

`nums[left[i] + 1 : right[i]]`.

Its length is `right[i] - left[i] - 1`.

**Find left blockers with a decreasing stack.** The first pass scans from left to right. The stack stores indices whose values are in strictly decreasing order from bottom to top after processing.

For current value `x`, the source pops while `nums[stk[-1]] <= x`. Any popped value cannot be the nearest greater blocker for the current position because it is not greater. It also cannot be a useful blocker for a future position that sees `x` first: current `x` is at least as large and closer to that future position.

After the pops, the top stack value, if one exists, is greater than `x`. Because closer non-greater indices have been removed and stack indices follow scan order, it is the nearest greater value on the left. The source stores that index in `left[i]`.

If the stack is empty, no greater left value exists and the initialized sentinel negative one remains. Current index `i` is then pushed as a possible blocker for later values.

**Find right blockers symmetrically.** The stack is cleared, and the second pass scans indices from right to left. It again pops values no greater than the current one. The remaining top, if present, is the nearest greater index on the right and is stored in `right[i]`. An empty stack leaves sentinel `n`.

The input values are distinct, so `<=` behaves the same as `<` for actual different positions. The non-strict comparison also makes the intended “only a strictly greater value blocks” rule explicit and would pop equal values if the guarantee were relaxed.

**Why the open interval is maximal.** Every index strictly between `left[i]` and `right[i]` has value smaller than `nums[i]`. If a greater value existed inside, the nearest greater blocker on that side would have been closer. Thus `nums[i]` is the maximum throughout that entire interval.

Extending one position farther left would include `left[i]` when it exists, whose value is greater. Extending one position farther right would include `right[i]` when it exists. Therefore, no larger valid subarray containing index `i` exists.

The returned list comprehension applies this length formula to every pair of boundaries.

**Amortized stack behavior.** A while loop appears inside each scan, but an index can be pushed once and popped once per pass. A single large value may pop many indices immediately, but those indices never re-enter that pass. Total stack work is linear rather than quadratic.

**A small example.** For `[1, 5, 4, 3, 6]`, value five at index one has no greater value to its left, so its left sentinel is negative one. Its nearest greater right value is six at index four. The valid open interval is indices zero through three, length four. Value four at index two is blocked by five on the left and six on the right, yielding indices two through three, length two.

**Why storing indices matters.** The final answer needs distance between blockers, not merely their values. Indices also let the source retrieve values through `nums[stk[-1]]` while maintaining one compact stack.

**No input mutation.** Both passes only read `nums`. All boundaries and results are allocated separately.

## Complexity detail

Each of the $n$ indices is pushed once and popped at most once in the left pass, so that pass is $O(n)$. The same argument applies to the right pass. Building the result is another $O(n)$. Total time is $O(n)$.

Arrays `left` and `right` each store $n$ integers. The stack can contain $n$ indices, and the returned answer contains $n$ required values. Auxiliary space excluding output is $O(n)$; including output remains $O(n)$.

A direct outward scan for every index could take $O(n^2)$ on a sorted array. The monotonic stacks share blocker-discovery work across positions and reach the optimal linear time.

## Alternatives and edge cases

- **Contribution-style single stack:** Pop indices when a greater current value arrives and assign one boundary then; a second cleanup or sentinel can finish the other side. It can reduce code duplication but is easier to get wrong.
- **Segment tree with searches:** Range maxima plus boundary binary searches can find blockers in $O(n\log n)$ time and $O(n)$ space, slower than the stack.
- **Brute-force expansion:** Expand left and right independently for every index. It is simple but quadratic in monotone arrays.
- **Global maximum:** Both stacks are empty at its boundary checks, so its answer spans the entire array.
- **Smallest value:** Its nearest neighbors may immediately block it, often giving length one.
- **Strictly increasing array:** Every value's right side is unblocked until a greater immediate successor, while no greater left value exists; answers become one through $n$.
- **Strictly decreasing array:** The symmetric pattern expands each value to the right.
- **Single element:** Sentinels negative one and one yield length one.
- **Distinctness:** It guarantees a unique maximum in every considered subarray. If duplicates were allowed and equality still counted as maximum, equal values should not be blockers; the source's pop condition already treats them as non-blocking.
- **Boundary sentinels:** Negative one and `n` eliminate special formulas at array edges.
- **Indices rather than values:** Distances require exact blocker positions, so storing only values would be insufficient.
