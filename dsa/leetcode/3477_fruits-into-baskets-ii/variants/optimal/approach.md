## General

**Simulate the rule in its stated order.** The choice for a fruit is not an optimization over capacities: it must use the leftmost currently available basket that is large enough. Therefore process `fruits` from left to right and scan `baskets` from index 0 for every fruit. The first qualifying entry is exactly the contract-mandated destination, so stop that scan immediately.

All legal fruit quantities are at least 1. After assigning a basket, replace its capacity with `0`; this value can never qualify for any later fruit and therefore represents “used” without a separate array. If the inner scan reaches its end, Python's loop `else` records one more unplaced fruit.

The simulation maintains the exact state required for the next step. Before each fruit, the positive basket entries are precisely the unused baskets with their original capacities, and every zero is a basket already used once. Selecting the first positive capacity at least as large as the fruit is consequently the leftmost available qualifying basket. Marking it zero preserves the state for the next fruit, while completing the scan without a match proves that the current fruit must remain unplaced.

## Complexity detail

There are $n$ fruit types and $n$ baskets. In the worst case, every fruit scans all baskets, so the time complexity is $O(n^2)$. The accepted implementation modifies `baskets` in place and otherwise stores only counters and loop variables, giving $O(1)$ auxiliary space.

The input bound $n\le100$ intentionally makes direct simulation practical. A segment tree can reduce the search to $O(\log n)$ per fruit, but its additional machinery is unnecessary for this bounded version.

## Alternatives and edge cases

- **Separate used array:** Preserving `baskets` and tracking availability in $O(n)$ extra space is equivalent, but the positive-value constraint makes the zero marker simpler.
- **Segment tree:** Storing interval maxima can locate the leftmost sufficient capacity in $O(\log n)$ per fruit, at the cost of $O(n)$ extra space and more complex updates.
- **Best-fit basket:** Choosing the smallest sufficient capacity violates the leftmost rule and can change later placements.
- **Sort fruits or baskets:** Sorting destroys the required processing and positional order.
- **Exact capacity:** A basket qualifies when its capacity is equal to the fruit quantity because the condition is greater than or equal.
- **Used basket:** Setting a used capacity to zero prevents reuse; one basket cannot hold two fruit types.
- **No qualifying basket:** The fruit remains unplaced, but processing continues with the next fruit and the basket state is unchanged.
- **All fruits unplaced:** The result is $n$ when every capacity is too small.
- **All fruits placed:** The result is zero, not the number of successful placements.
- **Input mutation:** The canonical implementation consumes the supplied `baskets` list; callers that need the original capacities must pass a copy.
