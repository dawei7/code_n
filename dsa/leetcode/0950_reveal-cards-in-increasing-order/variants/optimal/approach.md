## General
**Determine which positions are revealed first.** The reveal process depends only on positions, not card values. Put the indices `0` through `n - 1` into a queue. Removing its front models revealing that position; moving the next front index to the back models rotating the next card.

**Assign values in increasing reveal order.** Sort the unique card values. For each value from smallest to largest, remove the next revealed index from the queue and store the value at that position in the answer. If indices remain, rotate the queue once before assigning the following value.

**Reverse the simulation without reversing its rules.** The index queue produces exactly the order in which positions will be exposed by the required process. The algorithm places the first sorted value at the first exposed position, the second value at the second exposed position, and so on. Therefore replaying the process on the constructed deck reveals the sorted values in strictly increasing order. Every input card is assigned once, so the result is a permutation of the original deck.

## Complexity detail
Sorting $n$ values costs $O(n\log n)$ time. Each index enters the queue once and participates in a constant number of queue operations, adding $O(n)$ time. The answer and index queue each use $O(n)$ space.

## Alternatives and edge cases
- **Reverse construction:** Process values from largest to smallest, repeatedly moving the current bottom card to the top before placing the next value. A deque supports this equivalent method in $O(n\log n)$ total time including sorting.
- **Selection sort before simulation:** Choosing each next-smallest value by scanning the remaining deck preserves correctness but raises sorting work to $O(n^2)$.
- **List front removal:** Using `pop(0)` for the index queue shifts later elements and can make the simulation itself $O(n^2)$.
- **One card:** Its only possible ordering is already valid.
- **Input order:** The supplied order carries no constraint because the deck may be rearranged arbitrarily.
- **Unique values:** The contract's uniqueness guarantee makes increasing reveal order strict and the resulting arrangement deterministic.
