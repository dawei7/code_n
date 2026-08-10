## General

**Normalize every value to its largest reachable form**

The allowed moves are asymmetric. An even value can be divided by two, while an odd value can be doubled. For one original odd value `v`, its only larger reachable value is `2v`; after doubling, it is even and may be divided back. For an original even value, the largest reachable value is the value itself. It can only move downward until becoming odd, after which doubling merely returns to the preceding even value.

The source therefore converts every odd input to `2v` and leaves every even input unchanged. After this normalization, every element starts at the top of its reachable descending chain. All remaining useful transitions are repeated divisions of an even current value by two.

This common direction is crucial. Instead of mixing increases and decreases, the algorithm starts from one valid array and explores candidates by decreasing current maxima.

**Use negative numbers as a max-heap**

Python’s `heapq` is a min-heap. The source stores `-v`, so the smallest negative number represents the largest actual value. Thus `-h[0]` is the current array maximum.

While normalizing, `mi` records the smallest actual value placed in the heap. After `heapify(h)`, the heap contains exactly one current representative for each input element, and `mi` is their minimum. The initial deviation is

`-h[0] - mi`.

The heap gives fast access to the only element that can immediately reduce the current maximum.

**Why only the current maximum is changed**

Deviation is `maximum - minimum`. Starting from every value’s largest reachable representative means no element has an unexplored larger choice. To obtain a smaller range from the current selection, the meaningful next action is to lower a current maximum if it is even.

Lowering a nonmaximum cannot reduce the maximum and can only keep or decrease the minimum, so it cannot improve the current deviation at that moment. The heap simulation therefore divides only the largest current value.

This does not lose configurations. Whenever an element is reduced, the algorithm records the deviation before reducing it. Its old larger value has already participated in the current candidate range. The heap process systematically walks downward through reachable values at the moments they can constrain the maximum, just like the standard smallest-range search across ordered candidate lists.

**Perform one halving transition**

The loop condition `h[0] % 2 == 0` tests whether the current maximum is even. `h[0]` is negative, but an even negative integer still has modulo two equal to zero.

`heappop(h)` removes the negative representation of the maximum. Because that value is even, integer division by two is exact:

`x = heappop(h) // 2`.

If the actual maximum was `M`, the popped value was `-M` and `x` becomes `-M/2`. Pushing `x` therefore inserts the halved actual value.

The new value might establish a new minimum, so `mi = min(mi, -x)` updates the tracked minimum. The maximum after reinsertion is again `-h[0]`; it may be the halved element or a different heap element. The source evaluates the new deviation and keeps the smallest in `ans`.

**Why the process stops at an odd maximum**

An odd current maximum cannot be divided. Doubling it would only increase the maximum and revisit the larger even value from which its chain may have descended. Other elements are no larger than this odd maximum; reducing any of them cannot lower the maximum and may lower the minimum. Therefore no unvisited continuation can improve the best deviation once the maximum itself is odd.

For `[1, 2, 3, 4]`, normalization gives `[2, 2, 6, 4]`. The simulation reduces six to three and then four to two as those values become maxima, evaluating ranges along the way. It encounters a selection equivalent to `[2, 2, 3, 2]` with deviation one.

**Why the recorded minimum is globally optimal**

Each normalized element has a finite descending list of reachable values obtained by halving while even. A valid transformed array chooses one value from each list. Initially the algorithm chooses every list’s largest value. At each step it replaces one occurrence of the current global maximum with the next smaller value from that same list.

Before advancing a list, the algorithm evaluates the range containing its current representative. Any range with a smaller upper endpoint must advance at least one list currently attaining the maximum, so choosing a maximum is a necessary next frontier move. Repeating this explores every frontier at which the smallest possible range can change.

When an odd maximum is reached, its list has no smaller candidate and every future selection must retain an upper endpoint at least that large or lower some other value without changing it. No better range remains. Thus the minimum deviation stored across all evaluated frontiers is the global optimum.

## Complexity detail

Let `n` be the number of elements and `M` the largest normalized value. Each element can be halved at most $O(\log M)$ times before becoming odd. Across all elements, there are at most $O(n\log M)$ heap transitions.

Heap construction takes $O(n)$ time. Each pop and push costs $O(\log n)$, so total running time is $O(n\log M\log n)$ in the worst case.

The heap always contains exactly `n` entries. Apart from it, the algorithm stores scalar values `mi`, `ans`, `v`, and `x`, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Explicit max-heap implementation:** Languages with a native max-heap can store positive values. Python’s negation technique changes representation, not the algorithm.
- **Generate every reachable list and solve smallest range:** This makes the candidate-list interpretation explicit but can store $O(n\log M)$ values instead of the exact heap’s $O(n)$ representatives.
- **Normalize downward and raise minima:** One can start from minimum reachable values and advance upward with a min-heap, but candidate generation and stopping conditions are less direct.
- **All values equal:** The initial deviation is zero, which remains the minimum even if the loop performs later halvings.
- **All values odd:** Normalization doubles all of them, making every heap value even. This creates the option to return each to its original odd value as maxima are processed.
- **Power of two:** It has the longest halving chain down to one and determines the logarithmic transition bound.
- **Odd current maximum:** The loop stops immediately because it cannot be reduced under the allowed rule.
- **New minimum after halving:** Updating `mi` is mandatory; retaining the old minimum would understate the deviation.
- **Duplicate maxima:** Reducing one copy leaves another copy at the old maximum. The next heap iteration can reduce that copy, and both frontier states are evaluated.
- **Negative heap parity:** Python’s modulo operation still reports zero for negative even values, so the loop condition is sound.
- **Integer division:** The popped heap value is divided only when even, so `// 2` has no rounding ambiguity despite being negative.
- **Input preservation:** Odd values are doubled only in the local loop variable `v`. The original `nums` list is not modified.
- **Upper numeric bound:** Doubling an odd value up to $10^9$ produces at most $2\cdot10^9$, which remains safe in Python and within typical 32-bit signed range except near its endpoint; Python integers avoid overflow entirely.
