## General
**Expose the best price on each side**

Maintain sell orders in a min-heap by price and buy orders in a max-heap, represented in Python by negated prices. The heap roots are exactly the orders that the contract requires a new opposite order to consider first.

**Consume quantities without losing a partial order**

While prices cross, remove the best opposite order and trade the smaller of its amount and the arriving amount. If the removed order retains some quantity, push that remainder back with the same price. Continue until the arriving amount is exhausted or the best opposite price no longer permits a match.

**Store only the unmatched remainder**

If some of the arriving amount remains after matching, push it into its own side's heap. Thus, after every input order, the heaps contain exactly the unmatched backlog. Moreover, if both heaps are nonempty, their best prices do not cross; otherwise the processing loop would have matched them.

Each match follows the mandated price priority, preserves any unfilled quantity, and strictly reduces at least one order to zero. Induction over the input stream therefore proves the heaps represent the correct backlog, so summing their amounts gives the required result.

## Complexity detail
Each of the $n$ arriving orders is inserted at most once. A heap entry may be popped and reinserted after a partial match, but every match completely removes either the arriving order or one existing entry; total heap operations remain $O(n)$. Each operation costs $O(\log n)$, giving $O(n\log n)$ time. The two heaps store at most $n$ entries and use $O(n)$ space.

## Alternatives and edge cases
- **Unsorted backlog lists:** Scanning for the lowest sell or highest buy is correct but can require $O(n^2)$ total time.
- **Balanced ordered maps:** Price-to-amount maps also support best-price access in $O(\log n)$ time and can aggregate equal prices, but Python has no built-in balanced tree.
- **Exact fill:** When both quantities reach zero, push neither order back.
- **Partial fill of a backlog order:** Reinsert its remaining amount at the same price.
- **One order crosses several prices:** Continue matching until its amount is zero or the next best price is incompatible.
- **Equal prices:** Buy and sell prices may match because both price comparisons are inclusive.
- **Large amounts:** Keep full integer quantities during simulation and apply the modulus only to the final backlog total.
