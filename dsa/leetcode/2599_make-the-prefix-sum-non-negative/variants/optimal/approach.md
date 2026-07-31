## General

**Treat moved elements as temporarily deferred.** Scan the array in its original order and maintain the sum of elements that would remain in the current prefix. Store every negative value seen in a min-heap.

If the retained sum becomes negative, at least one seen element must be moved behind the current prefix. Deferring the smallest value—that is, the most negative one—raises the retained sum by the greatest possible amount. Remove that value from the heap, subtract it from the retained sum, and count one operation.

After every iteration, the retained elements form a non-negative-prefix subsequence of everything processed. Whenever an operation is forced, no solution can use fewer deferrals up to that position. Among all choices with that count, removing the most negative value leaves the greatest possible retained sum, so it cannot make any future prefix harder to satisfy. This exchange argument proves the greedy choices preserve a globally minimum operation count. The deferred negatives can be appended after the retained sequence; the guaranteed feasible total sum keeps the completed final prefix non-negative.

## Complexity detail

Let $n$ be the length of `nums`. Each negative value is inserted into the heap once and removed at most once. Heap operations cost $O(\log n)$, giving $O(n \log n)$ time overall. The heap can hold $O(n)$ values, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Repeated minimum scan:** Keep all seen negative values in a list and linearly find the most negative one after each deficit. The greedy result remains correct, but worst-case time becomes $O(n^2)$.
- **Move the current negative:** This can use too many operations because an earlier, more negative value may restore much more prefix sum with the same one move.
- **Already valid order:** If the running sum never becomes negative, the heap may contain values but the answer remains zero.
- **Negative first element:** It must be deferred immediately because no earlier positive value can support it.
- **Integer width:** Prefix sums can exceed 32-bit range even though individual elements fit; fixed-width implementations should accumulate in 64 bits.
