## General
**Count how many values arrive at each position.** Allocate a frequency array covering all original values and another $n$ positions beyond the maximum. After counting `nums`, scan value positions from left to right. At a position with frequency zero or one, nothing must move. If `frequency[value]` is greater than one, keep one item there and treat all remaining copies as excess.

**Carry duplicates one unit at a time in aggregate.** Add the excess to `frequency[value + 1]` and add the same amount to the move count. This represents incrementing each excess copy once. A carried copy may meet other values at the next position and be carried again during the following iteration, with every additional unit of distance charged exactly once.

At most one item can finish at `value`, so every excess item currently there must cross from `value` to `value + 1`; that unit of cost is unavoidable in any valid result. Keeping one item and moving all excess copies to the earliest possible next position never pushes an item farther than necessary. Applying this argument from left to right proves that every charged move is necessary and that the final distinct placement has minimum total cost.

## Complexity detail
Counting the $n$ inputs costs $O(n)$, and the frequency scan covers $M$ value positions, for $O(n+M)$ time. The frequency array contains $M$ counters, giving $O(M)$ space.

## Alternatives and edge cases
- **Sort and raise greedily:** Sort the values, then replace each value conceptually by the greater of itself and one more than the preceding assigned value. This uses $O(n\log n)$ time and is often simpler when the numeric range is large.
- **Next-free union-find:** Map an occupied value to the next candidate position and compress paths after each placement. It avoids a range-sized array but has more bookkeeping and expected near-linear behavior.
- **Increment until a set slot is free:** For each number, repeatedly add one while the value is already used. This is correct, but many equal inputs cause $O(n^2)$ membership iterations.
- **Already unique:** Every frequency is at most one, so no item is carried and the answer is zero.
- **All values equal:** The copies occupy consecutive final positions; their move counts are $0,1,\ldots,n-1$.
- **Collisions created by carrying:** Excess from a smaller value may meet an original larger value. Adding frequencies before processing the next position handles that collision without a special case.
- **Upper input value:** The extra $n$ positions ensure enough room even when many copies begin at `100000`.
